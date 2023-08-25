# ProiectGitHubAPI

Acesta este un framework de testare automata pentru API-ul GitHub. Framework-ul este scris in Python și folosește `pytest` pentru testarea automata si generarea de rapoarte HTML.

## Instalare 

1. **Cloneaza acest repository pe calculatorul local:**
git clone https://github.com/DianaNicoletaA/ProiectGitHubAPI.git

2. **Navigheaza in directorul proiectului:**
cd ProiectGitHubAPI

3. **Instaleaza dependintele proiectului folosind pip:**
pip install -r requirements.txt

## Configurarea Accesului la API-ul GitHub

Pentru a accesa si testa API-ul GitHub, veti avea nevoie de un token de acces personal și de numele de utilizator al contului dvs. GitHub. Aceste detalii trebuie introduse in `api_helper.py`.

## Structura Proiectului

- `test_runner.py`: Script pentru rularea tuturor testelor și generarea rapoartelor.
- `tests/`: Directorul care conține toate fișierele de testare individuale.
- `api/`: Directorul care conține helperii și funcționalitațile pentru interacțiunea cu API-ul.
- `reports/`: Directorul in care sunt generate rapoartele HTML.

In plus, proiectul contine si urmatoarele functionalitati suplimentare:

- `list_repos.py`: Un script care listeaza repository-urile generate dupa ce ai rulat testele. Acest script iti permite sa afisezi lista completa a repository-urilor create in cadrul testelor.

- `delete_repos.py`: Un script care sterge repository-urile generate in timpul testelor. Acest script este util pentru curatarea mediului dupa efectuarea testelor si eliminarea resurselor neutilizate.

Asigura-te ca esti atent la utilizarea acestor functionalitati, in special cand vine vorba de ștergerea repository-urilor, pentru a evita pierderea datelor importante.



## Rulare Teste

- **Pentru a rula toate testele si a genera rapoartele HTML in directorul "reports":**
pytest --html=reports/report.html


- **Pentru a rula un test specific:**

De exemplu, pentru a rula testul `test_create_issue.py`:
pytest tests/test_create_issue.py

## Structura Proiectului

- `pytest.py`: Script pentru rularea tuturor testelor si generarea rapoartelor.
- `tests/`: Directorul care contine toate fisierele de testare individuale.
- `api/`: Directorul care contine helperii și functionalitatile pentru interactiunea cu API-ul.
- `reports/`: Directorul in care sunt generate rapoartele HTML.

## Dezinstalare

Dezinstaleaza dependintele Python:
pip uninstall -r requirements.txt
Aceasta va dezinstala toate pachetele listate in `requirements.txt`.




