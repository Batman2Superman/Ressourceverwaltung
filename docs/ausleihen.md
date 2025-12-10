```mermaid
flowchart TD
    Start([Start])
    Eingabe[[Eingabe: Benutzer-ID, Ressourcen-ID, geplantes Rückgabedatum]]

    CheckUser{Benutzer existiert?}
    CheckRes{Ressource existiert?}
    CheckAvail{Ressource verfügbar?}

    ErrorUser[/Fehlermeldung: Benutzer nicht gefunden/]
    ErrorRes[/Fehlermeldung: Ressource nicht gefunden/]
    ErrorAvail[/Fehlermeldung: Ressource nicht verfügbar/]

    CreateLoan[[DB: Ausleihdatensatz einfügen]]
    UpdateStatus[[DB: Ressourcenstatus auf "verliehen" aktualisieren]]

    Success([Transaktion erfolgreich])
    End([Ende])

    Start --> Eingabe --> CheckUser

    CheckUser -- Nein --> ErrorUser --> End
    CheckUser -- Ja --> CheckRes

    CheckRes -- Nein --> ErrorRes --> End
    CheckRes -- Ja --> CheckAvail

    CheckAvail -- Nein --> ErrorAvail --> End
    CheckAvail -- Ja --> CreateLoan --> UpdateStatus --> Success --> End

```
