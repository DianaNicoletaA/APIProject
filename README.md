# ProiectGitHubAPI

Acesta este un framework de testare automată pentru API-ul GitHub. Framework-ul este scris în Python și folosește `pytest` pentru testarea automată și generarea de rapoarte HTML.

## Instalare 

1. **Clonează acest repository pe calculatorul local:**
git clone https://github.com/DianaNicoletaA/ProiectGitHubAPI.git

2. **Navighează în directorul proiectului:**
cd ProiectGitHubAPI

3. **Instalează dependințele proiectului folosind pip:**
pip install -r requirements.txt

## Configurarea Accesului la API-ul GitHub

Pentru a accesa și testa API-ul GitHub, veți avea nevoie de un token de acces personal și de numele de utilizator al contului dvs. GitHub. Aceste detalii trebuie introduse în `api_helper.py`.

## Structura Proiectului

- `test_runner.py`: Script pentru rularea tuturor testelor și generarea rapoartelor.
- `tests/`: Directorul care conține toate fișierele de testare individuale.
- `api/`: Directorul care conține helperii și funcționalitățile pentru interacțiunea cu API-ul.
- `reports/`: Directorul în care sunt generate rapoartele HTML.

În plus, proiectul conține și următoarele funcționalități suplimentare:

- `list_repos.py`: Un script care listează repository-urile generate după ce ai rulat testele. Acest script îți permite să afișezi lista completă a repository-urilor create în cadrul testelor.

- `delete_repos.py`: Un script care șterge repository-urile generate în timpul testelor. Acest script este util pentru curățarea mediului după efectuarea testelor și eliminarea resurselor neutilizate.

Asigură-te că ești atent la utilizarea acestor funcționalități, în special când vine vorba de ștergerea repository-urilor, pentru a evita pierderea datelor importante.



## Rulare Teste

- **Pentru a rula toate testele și a genera rapoartele HTML în directorul "reports":**
pytest --html=reports/report.html


- **Pentru a rula un test specific:**

De exemplu, pentru a rula testul `test_create_issue.py`:
pytest tests/test_create_issue.py

## Structura Proiectului

- `test_runner.py`: Script pentru rularea tuturor testelor și generarea rapoartelor.
- `tests/`: Directorul care conține toate fișierele de testare individuale.
- `api/`: Directorul care conține helperii și funcționalitățile pentru interacțiunea cu API-ul.
- `reports/`: Directorul în care sunt generate rapoartele HTML.

## Dezinstalare

Dezinstalează dependințele Python:
pip uninstall -r requirements.txt
Aceasta va dezinstala toate pachetele listate în `requirements.txt`.




