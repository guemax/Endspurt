# Mitwirken

Wir freuen uns über Ihr Interesse daran, *Endspurt* verbessern zu
wollen.  Sie können zum Beispiel einen [Fehler melden](https://github.com/guemax/endspurt/issues/new) oder
sich eine neue [Funktion wünschen](https://github.com/guemax/endspurt/issues/new).

Desweiteren können Sie ebenfalls mit eigenem Programmcode an dem Projekt beitragen.
Bitte folgen Sie hierfür der untenstehenden Anleitung, um direkt durchzustarten.

## Einrichten der Entwicklungsumgebung

Wenn Sie die Webseite mit Hilfe eines Developmentservers auf Ihrem eigenen
Rechner ausprobieren wollen, folgen Sie bitte folgenden Anweisungen:

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

### 3. Durchführen der Tests:

```shell
# Sollte im Zweig 'main' immer problemlos klappen,
# andere Zweige können, während der Entwicklungsphase,
# hier einen oder mehrere Fehler produzieren.
python3 manage.py test
```

### 4. Anwenden der Datenbankmigrationen

```shell
python3 manage.py migrate
```

### 5. Erstellen eines Admin-Accounts

```shell
python3 manage.py createsuperuser
```

### 6. Starten des Developmentservers:

```shell
python3 manage.py runserver
```

## Entwicklungsprozess

Alles beginnt mit einer Idee: Sei es ein Fehler, der behoben werden muss, sei es,
dass eine Funktionalität implementiert werden soll, oder sei es, dass Sie im Quelltext
eine Stelle gefunden haben, die sich effizienter oder schöner schreiben lässt.

Forken und Klonen Sie das Projekt, und fügen Sie Ihre Änderungen einem Git Commit hinzu.

Es empfiehlt sich, frühzeitig einen Pull Request (ggf. als Draft) zu erstellen und so Feedback und Tips für die Umsetzung zu erhalten.
