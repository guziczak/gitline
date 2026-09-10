![Gitline — jednoplikowy klient Git dla Windows][hero]

<p align="center">
<b>Jeden plik <code>gitline.py</code>. Zero instalatora, zero <code>pip</code>, zero uprawnień administratora.</b><br>
Pierwsze uruchomienie samo przygotowuje prywatne środowisko, a jeśli trzeba — także własną, zweryfikowaną kopię Gita.
</p>

<br>

## Spis treści

1. [Czym jest Gitline](#czym-jest-gitline)
2. [Szybki start](#szybki-start)
3. [Zwiedzanie interfejsu](#zwiedzanie-interfejsu)
4. [Najważniejsze możliwości](#najważniejsze-możliwości)
5. [Skróty klawiszowe](#skróty-klawiszowe)
6. [Co powstaje obok skryptu](#co-powstaje-obok-skryptu)
7. [Polecenia deweloperskie](#polecenia-deweloperskie)
8. [Architektura](#architektura)
9. [Bezpieczeństwo](#bezpieczeństwo)
10. [Licencje](#licencje)

<br>

## Czym jest Gitline

Gitline to desktopowy klient Git napisany w Pythonie i Qt, którego cała dystrybucja mieści się w **jednym pliku źródłowym**. Przekazujesz komuś `gitline.py`, ta osoba uruchamia go zainstalowanym Pythonem — i to wszystko. Skrypt sam:

- tworzy prywatne środowisko wirtualne obok siebie i instaluje w nim zapięte hashami biblioteki (PySide6, keyring),
- na Windows x64 pobiera zweryfikowaną sumą kontrolną kopię MinGit, jeśli w systemie nie ma Gita,
- wyświetla złoty, renderowany programowo loader 3D, a potem przekazuje go głównemu oknu bez mrugnięcia ekranu.

Nie modyfikuje systemu: nie dotyka `PATH`, globalnej konfiguracji Gita ani cudzych ustawień. Każda kopia pliku ma własne środowisko i własny `gitline.json`.

<br>

## Szybki start

**Wymagania:** Windows, 64‑bitowy CPython 3.10 – 3.14 oraz internet przy pierwszym uruchomieniu.

```powershell
python gitline.py                    # pierwszy start przygotuje wszystko sam
python gitline.py C:\projekty\app    # od razu otwórz wskazane repozytorium
python gitline.py --help             # pomoc bez instalowania czegokolwiek
```

Przed instalacją bibliotek pojawia się okno wyboru źródła pakietów: **publiczne PyPI** albo **firmowe Artifactory** (hasło jest użyte wyłącznie do tej jednej instalacji i nigdzie nie jest zapisywane). To samo okno pokazuje postęp i zamyka się dopiero wtedy, gdy loader 3D narysuje pierwszą klatkę.

> Pierwsze uruchomienie trwa kilka minut. Każde kolejne startuje natychmiast, bo środowisko `.gitline-venv-3.xx` jest już gotowe.

<br>

## Zwiedzanie interfejsu

### Zmiany — zaznaczasz, czytasz diff, commitujesz

Lista plików z checkboxami, filtr, licznik zaznaczenia i diff z numerami linii po obu stronach. Nowe pliki są zaznaczane automatycznie, a wybór jest pamiętany dla repozytorium. Tytuł i opis commita, `Ctrl+Enter` i gotowe.

![Widok Zmiany][main_changes]

### Historia — z podglądem plików i patcha każdego commita

Ostatnie 150 commitów bieżącej gałęzi z wyszukiwarką. Commity, których jeszcze nie ma na serwerze, mają odznakę **Lokalny**; opublikowane — znacznik. Każdy commit pokazuje listę zmienionych plików z bilansem `+ / −` oraz patch wybranego pliku.

![Widok Historia][main_history]

### Strona startowa i ostatnie repozytoria

| Przegląd projektów | Szybki przełącznik `Ctrl+R` |
| :---: | :---: |
| ![Strona startowa][home] | ![Ostatnie repozytoria][repo_popup] |

### Operacje na historii — z podglądem i kopią bezpieczeństwa

Zmiana opisu, squash, cofnięcie i revert działają tylko na commitach, na których to jest bezpieczne, i zawsze mówią wprost, co się stanie. Poprzednia historia zostaje zachowana jako lokalna kopia.

| Zmień opis commita | Squash · 2 commity → 1 |
| :---: | :---: |
| ![Zmiana opisu commita][reword] | ![Squash][squash] |

| Informacje o commicie | Wysyłanie z kontrolą celu |
| :---: | :---: |
| ![Informacje o commicie][commit_details] | ![Wyślij commity][push] |

### Klonowanie i konta

Konta GitHub, GitLab i firmowych serwerów łączysz raz — tokeny trafiają do systemowego magazynu poświadczeń, a projekty z kont pojawiają się w oknie klonowania same.

| Klonuj repozytorium | Wszystkie konta w jednym miejscu |
| :---: | :---: |
| ![Klonowanie][clone] | ![Konta][accounts] |

### Drobiazgi, które robią różnicę

| Szybkie polecenia `Ctrl+K` | Technologie i licencje |
| :---: | :---: |
| ![Szybkie polecenia][palette] | ![Technologie i licencje][technologies] |

| Ekran startowy | O aplikacji |
| :---: | :---: |
| ![Ekran startowy][splash] | ![O aplikacji][about] |

<br>

## Najważniejsze możliwości

| Obszar | Co dostajesz |
| :--- | :--- |
| **Codzienna praca** | zaznaczanie plików do commita, filtr, diff z numerami linii i zawijaniem, wyszukiwanie w diffie, commit z tytułem i opisem |
| **Gałęzie i serwer** | przełączanie i tworzenie gałęzi, `Fetch` / `Pull` / `Push` z licznikiem ahead/behind, podgląd celu przed wysłaniem, zmiana serwera zdalnego |
| **Historia** | zmiana opisu, squash wielu commitów, cofnięcie ostatniego commita, revert z odzyskiwaniem, plan force‑push z jawnym potwierdzeniem |
| **Schowek** | odłożenie i przywrócenie zmian (stash) bez opuszczania okna |
| **Konta** | GitHub, GitLab i własne serwery HTTPS; automatyczny dobór konta dla repozytorium, ręczny wybór pamiętany per repozytorium, katalog projektów do sklonowania |
| **Komfort** | bezramkowe okno w ciemnym motywie, paleta poleceń, ostatnie repozytoria, przypinanie do paska zadań, tryb kończenia pracy czekający na trwające operacje |
| **Przejrzystość** | okno *Technologie i licencje* z pełną listą składników, ich wersjami i tekstami licencji |

<br>

## Skróty klawiszowe

| Skrót | Działanie |
| :--- | :--- |
| `Ctrl + O` | Otwórz repozytorium z dysku |
| `Ctrl + Shift + O` | Klonuj repozytorium |
| `Ctrl + N` | Utwórz nowe repozytorium |
| `Ctrl + R` | Ostatnie repozytoria |
| `Ctrl + K` | Szybkie polecenia |
| `Ctrl + Enter` | Utwórz commit |
| `Ctrl + F` | Szukaj w diffie |
| `F5` | Odśwież stan repozytorium |

<br>

## Co powstaje obok skryptu

```text
📁 twój-folder/
├── gitline.py               ← jedyny plik, który udostępniasz
├── gitline.json             ← ustawienia tej kopii (bez tokenów)
├── .gitline-venv-3.12/      ← prywatne środowisko dla używanej wersji Pythona
└── .gitline/                ← dzienniki, prywatny MinGit (jeśli pobrany), ikony skrótów
```

Tokeny kont **nigdy** nie lądują w tych plikach — mieszkają w systemowym magazynie poświadczeń (Windows Credential Manager przez `keyring`). Zwykłe uruchomienia ignorują odziedziczone zmienne środowiskowe innych kopii i nie importują cudzych ustawień.

<br>

## Polecenia deweloperskie

Wszystko poniżej jest zaimplementowane w tym samym pliku.

| Polecenie | Co robi |
| :--- | :--- |
| `--setup` | Wybór źródła pakietów i skrótów, przygotowanie środowiska |
| `--self-test` | Testy na prawdziwym Gicie w tymczasowych repozytoriach, izolowane konta, regresje GUI |
| `--check` | Kontrola składni (także zgodności z 3.10), kompletności locka i **wszystkie** testy regresji |
| `--diagnose` | Sprawdzenie Gita, GCM i magazynu poświadczeń bez odczytu tokenów |
| `--smoke-test` | Uruchomienie interfejsu z izolowanymi danymi aplikacji |
| `--screenshot PLIK` | Zapis podglądu interfejsu do pliku i wyjście |
| `--report PLIK.json` | Maszynowy raport z testów |

Tryby testowe nigdy nie czytają prawdziwego katalogu kont ani preferencji — pracują w tymczasowym profilu, który po zakończeniu jest usuwany.

<br>

## Architektura

```text
bootstrap  →  czysty backend Git i modele  →  konta i credential helper  →  widoki Qt i koordynator operacji  →  diagnostyka
```

- **Qt tylko rysuje i dispatchuje.** Zaakceptowana operacja dostaje własny kontekst repozytorium i konta i wykonuje się poza wątkiem GUI.
- **Backend Git to wyłącznie biblioteka standardowa.** Każde wywołanie to lista argumentów (nigdy `shell=True`), z oczyszczonym środowiskiem i limitem czasu; duże wyjścia trafiają do plików tymczasowych, więc olbrzymi diff nie zjada pamięci.
- **Credential helper jest osobnym procesem** tego samego pliku, podpinanym do Gita per polecenie (`-c credential.helper=…`), bez zapisów do globalnej konfiguracji.
- **Import nie ma efektów ubocznych.** Import pliku nie instaluje zależności ani nie odpala testów — robi to wyłącznie jawny tryb uruchomienia.

<br>

## Bezpieczeństwo

- Zależności są **przypięte hashami SHA‑256** (`--hash=sha256:…`); pip nie zainstaluje niczego, czego nie ma w locku wbudowanym w plik.
- Pobierany MinGit ma **znaną sumę kontrolną**, limit rozmiaru i wymóg HTTPS; archiwum jest sprawdzane pod kątem zip‑slip i dowiązań symbolicznych przed rozpakowaniem.
- Git działa z `GIT_TERMINAL_PROMPT=0` i `GCM_INTERACTIVE=never` — żadnych ukrytych okien z prośbą o hasło.
- Helper poświadczeń nigdy nie serializuje nieoczekiwanych wyjątków (mogłyby zawierać sekret) i nigdy nie „odblokowuje” kolejnego helpera, gdy przypisane konto jest niedostępne.
- Tokeny nie trafiają do dzienników operacji ani ustawień; komunikaty błędów są filtrowane z danych wrażliwych.

<br>

## Licencje

| Składnik | Licencja |
| :--- | :--- |
| Qt / PySide6 / Shiboken — © The Qt Company Ltd. i współtwórcy | [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.html) · [Qt for Python — licencje](https://doc.qt.io/qtforpython-6/licenses.html) · [zobowiązania LGPL](https://www.qt.io/development/open-source-lgpl-obligations) |
| keyring — © współtwórcy | [MIT](https://github.com/jaraco/keyring/blob/main/LICENSE) |
| Git — osobny plik wykonywalny | [GPLv2](https://git-scm.com/about/free-and-open-source) |

Aplikacja ładuje dynamicznie moduły Qt Core, Gui i Widgets na warunkach LGPLv3. Dystrybucja komercyjna musi zachować noty licencyjne, zapewnić dostęp do źródeł bibliotek i umożliwić użytkownikom ich podmianę. Pojedynczy plik źródłowy nie znosi tych zobowiązań — teksty licencji zależności pozostają zainstalowane w wymienialnym środowisku uruchomieniowym, a ich pełną listę pokazuje okno *Technologie i licencje*.

<br>

<p align="center"><sub>Gitline 0.2.0 · zrzuty ekranu pochodzą z rzeczywistego, uruchomionego interfejsu tej wersji</sub></p>


[hero]: docs/screenshots/hero.png
[main_changes]: docs/screenshots/main_changes.png
[main_history]: docs/screenshots/main_history.png
[home]: docs/screenshots/home.png
[repo_popup]: docs/screenshots/repo_popup.png
[reword]: docs/screenshots/reword.png
[squash]: docs/screenshots/squash.png
[commit_details]: docs/screenshots/commit_details.png
[push]: docs/screenshots/push.png
[clone]: docs/screenshots/clone.png
[accounts]: docs/screenshots/accounts.png
[palette]: docs/screenshots/palette.png
[technologies]: docs/screenshots/technologies.png
[splash]: docs/screenshots/splash.png
[about]: docs/screenshots/about.png
