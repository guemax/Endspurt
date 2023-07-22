# Mitwirken

Auf dieser Seite finden Sie eine Anleitung darüber, wie Sie durch
eigenen Programmcode an *Endspurt* beitragen können. Sie können
stattdessen auch einen [Fehler
melden](https://github.com/guemax/Endspurt/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=)
oder sich eine neue [Funktion
wünschen](https://github.com/guemax/Endspurt/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.md&title=).

## Herunterladen des Quelltextes

Damit Sie *Endspurt* weiterentwickeln können, laden Sie sich zuerst
den Quelltext herunter:

```shell
git clone https://github.com/guemax/Endspurt.git  # Mit Git
gh repo clone guemax/Endspurt                     # Oder der GitHub CLI
```

## Einrichten der Entwicklungsumgebung

Nun richten Sie die Entwicklungsumgebung ein:

### 1. Aufsetzen einer virtuellen Umgebung für Python:

```shell
python3 -m venv venv      # Erstellen
source venv/bin/activate  # Aktivieren
deactivate                # Deaktivieren
```

### 2. Installieren der Abhängigkeiten:

```shell
# Virtuelle Umgebung sollte zuvor aktiviert worden sein!
pip3 install -r requirements.txt
npm install
```

### 3. Erstellen eines Admin-Accounts

```shell
python3 manage.py createsuperuser
```

### 4. Anwenden der Datenbankmigrationen

```shell
python3 manage.py migrate
```

### 5. Starten des Developmentservers:

```shell
python3 manage.py runserver
```

Nun können Sie Änderungen vornehmen, diese durch Commits registrieren
und mittels eines Pull Requests einreichen.

Falls Sie bisher wenig mit Git und/oder GitHub gearbeitet haben, hilft
Ihnen vielleicht einer der folgenden Links weiter:

 - [Einführung zu Git](https://git-scm.com/book/en/v2)
 - [Über Pull
   Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
