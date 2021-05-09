# dyktando-ortograficzne
## Informacje ogólne
  Folder `dyktandoapp` z plikami z folderu `Client` powinien znajdować się po stronie klienta (domyślnie w katalogu `/home/nazwa_uzytk`).
Zawartość folderu `Server` domyślanie powinny znajdować się na serwerze w `/home/nazwa_uzytk`.

ŚCIEŻKI DOSTĘPU MOŻNA ZMIENIAĆ W PLIKU settings.py

## Konfiguracja
  Przed rozpoczęciem korzystania z systemu sprawdzania dyktand należy określić adresy IP, nazwy użytkowników oraz hasła w pliku konfiguracyjnym `settings.py`.
Plik `settings.py` należy zamienić po stronie klineta i serwera (mają być identyczne). 

## Uruchomienie aplikacji
  Aplikację uruchamiamy po stronie klienta za pomocą pliku `main.py`.
Polecenie w bash: `python3 main.py`

## Potrzebne pakiety (doinstalowanie)
Przy wykorzystaniu `pip3 install nazwa_pakietu`
### Strona klienta:
* Kivy
* paramiko
* scp
### Strona serwera:
* paramiko
* enchant
* pexpect
* scp
* dominate
