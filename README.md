# <img src="files/icon/icon.png" width=24 /> Endspurt

*Endspurt* ist ein fortgeschrittenes Evaluationsprogramm zur Erfassung
sowie Auswertung der Ergebnisse eines Sportfestes.

Es wurde mit Python und Django erstellt und erlaubt das parallele
Eintragen von Wertungen durch mehrere Helfer, indem diese die
Ergebnisse auf der Django Adminseite registrieren.  Diese Wertungen
werden mit einer Klasse sowie einer Sportart/Station verknüpft.
Daraufhin lässt sich auf der Indexseite die Rangliste darstellen.

## Installation

Um *Endspurt* zu installieren, folgen Sie bitte den [Anweisungen zum
Einrichten einer
Entwicklungsumgebung](CONTRIBUTING.md#einrichten-der-entwicklungsumgebung).
Da diese Umgebung bei einem Fehler umfangreiche Debuginformationen
ausspuckt, sollten Sie darüber nachdenken, Django für die
Veröffentlichung zu konfigurieren.  Mehr Informationen darüber finden
Sie [hier](https://docs.djangoproject.com/en/4.2/howto/deployment/).

## Benutzung

Unter untenstehenden Pfaden finden Sie folgende Seiten mit
entsprechenden Funktionen:

| Name | Pfad | Erklärung |
|---|---|---|
| Index | | Darstellung der Ergebnisse |
| Anzeigetafel | /anzeigetafel/ | Darstellung der Ergebnisse mit automatischem Scrollen |
| Anzeigetafel 2 | /anzeigetafel/automatisches-nachladen/ | Darstellung der Ergebnisse mit automatischem Scrollen und Nachladen |
| Admin | /admin/ | Hinzufügen von Klassen, Stationen und Wertungen (Anmeldung mit Benutzerkonto, das mit `python3 manage.py createsuperuser`erstellt wurde) |

## Mitwirken

Wir freuen uns über Ihr Interesse daran, *Endspurt* verbessern zu
wollen.  Bitte besuchen Sie einen der folgenden Links, um...

 - [Einen Fehler zu
melden](https://github.com/guemax/Endspurt/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=)
 - [Sich eine neue Funktion zu
   wünschen](https://github.com/guemax/Endspurt/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.md&title=)

Wenn Sie das Projekt sogar durch eigenen Programmcode unterstützen
möchten, folgen Sie bitte [dieser Anleitung](CONTRIBUTING.md).

## Lizenz

Das Projekt wurde unter der [GNU General Public License Version
3](https://www.gnu.org/licenses/gpl-3.0.en.html) veröffentlicht.  Mehr
Informationen über die Lizenzbedingungen und wie sie unser Projekt
nutzen oder weiterentwickeln dürfen, finden Sie in obenstehendem Link.
