"""Run gitline.py's regression tests one by one and keep going after a failure.

`python gitline.py --check` is the gate, and it stops at the first failing
test. When it fails, this driver loads the same file as a module, repeats the
isolation that run_application() sets up for test modes and calls every test
in the same order, so one CI run names every failure.

Usage: python selftests.py GITLINE_PY [TEST_NAME ...]
Exit code: number of failed tests (capped at 100).
"""
import importlib.util
import os
import re
import sys
import tempfile
import time
import traceback
from pathlib import Path


def annotate(level, title, message):
    """GitHub Actions annotation; prints nothing outside a workflow."""
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        return
    def data(text): return text.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
    title = data(title).replace(':', '%3A').replace(',', '%2C')
    print(f'::{level} title={title}::{data(message[:3500])}', flush=True)


def main():
    script = Path(sys.argv[1]).resolve()
    selected = sys.argv[2:]
    source = script.read_text(encoding='utf-8')
    runner = source[source.index('\ndef run_application():'):]
    names = re.findall(r"report\['checks'\]\['\w+'\] = (\w+)\(\)", runner)
    if selected:
        names = [name for name in names if name in selected] or selected

    # The script decides its test-profile mode from argv while it is imported.
    sys.argv = [str(script), '--check']
    os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
    if os.name == 'nt':
        os.environ.setdefault('QT_QPA_FONTDIR', str(Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'))
    spec = importlib.util.spec_from_file_location('gitline_under_test', script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    tempfile.tempdir = str(Path(tempfile.gettempdir()).resolve())
    data = tempfile.TemporaryDirectory(prefix='gitline-check-')
    module.APP_DATA = Path(data.name)
    os.environ['GITLINE_DATA_DIR'] = str(module.APP_DATA)

    failures = []
    for name in names:
        started = time.monotonic()
        try:
            result = getattr(module, name)()
        except BaseException as error:  # A SystemExit raised by a test is a failure too.
            seconds = time.monotonic() - started
            frames = traceback.extract_tb(error.__traceback__)
            trail = ' <- '.join(f'{frame.name}:{frame.lineno}' for frame in reversed(frames[-7:]))
            summary = f'{type(error).__name__}: {error}'
            print(f'FAIL {name} ({seconds:.1f}s): {summary}\n     at {trail}', flush=True)
            traceback.print_exc()
            failures.append((name, summary, trail))
        else:
            if isinstance(result, dict):
                result = f"{result.get('passed', '?')} checks"
            print(f'ok   {name} ({time.monotonic() - started:.1f}s): {str(result)[:110]}', flush=True)
    try:
        data.cleanup()
    except OSError:
        pass

    print(f'\n{len(names) - len(failures)} passed, {len(failures)} failed on {sys.platform} / Python {sys.version.split()[0]}', flush=True)
    if failures:
        overview = '\n'.join(f'{name}: {summary[:160]}' for name, summary, trail in failures)
        annotate('error', f'{len(failures)} self-tests failed on {sys.platform}', overview)
        # GitHub keeps ten annotations of each level per step.
        for index, (name, summary, trail) in enumerate(failures):
            level = 'error' if index < 9 else 'warning' if index < 19 else 'notice'
            annotate(level, name, f'{summary}\nat {trail}')
    return min(len(failures), 100)


if __name__ == '__main__':
    raise SystemExit(main())
