# ProiectGitHubAPI

Acesta este un framework de testare automată pentru API-ul GitHub. Framework-ul este scris în Python și folosește `pytest` pentru testarea automată și generarea de rapoarte HTML.

## Instalare 

1. Clonează acest repository pe calculatorul local:
```bash
git clone https://github.com/DianaNicoletaA/ProiectGitHubAPI.git

cd ProiectGitHubAPI
Instalează dependințele proiectului folosind pip:

pip install -r requirements.txt
Configurare
Pentru a accesa și testa API-ul GitHub, veți avea nevoie de un token de acces personal și de numele de utilizator al contului dvs. GitHub. Aceste detalii trebuie introduse în api_helper.py.

Rulare Teste
Pentru a rula toate testele și genera rapoartele HTML în directorul "reports", folosește comanda:


pytest --html=reports/report.html
Pentru a rula un test specific, utilizează comanda pytest cu calea către testul respectiv. De exemplu, pentru a rula testul test_create_issue.py:


pytest tests/test_create_issue.py
Structura Proiectului
test_runner.py: Script pentru rularea tuturor testelor și generarea rapoartelor.
tests/: Directorul care conține toate fișierele de testare individuale.
reports/: Directorul în care sunt generate rapoartele HTML.
Dezinstalare
Dezinstalează dependențele Python:

pip uninstall -r requirements.txt
Aceasta va dezinstala toate pachetele listate în requirements.txt.