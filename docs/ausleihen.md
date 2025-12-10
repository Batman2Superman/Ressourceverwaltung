# Aktivitätsdiagramm: Ressource ausleihen

```mermaid
flowchart TD
    Start([Start])
    Eingabe[[Eingabe: Benutzer-ID, Ressourcen-ID, geplantes Rückgabedatum]]

    CheckUser{Benutzer existiert?}
    CheckRes{Ressource existiert?}
    CheckAvail{Ressource verfügbar?}

    ErrorUser[/Fehlermeldung: Benutzer\nnicht gefunden/]
    ErrorRes[/Fehlermeldung: Ressource\nnicht gefunden/]
    ErrorAvail[/Fehlermeldung: Ressource\nnicht verfügbar/]

    CreateLoan[[DB: Ausleihdatensatz einfügen]]
    UpdateStatus[[DB: Ressourcenstatus = "verliehen"\naktualisieren]]

    Success([Transaktion erfolgreich abgeschlossen])
    End([Ende])

    Start --> Eingabe --> CheckUser

    CheckUser -- Nein --> ErrorUser --> End
    CheckUser -- Ja --> CheckRes

    CheckRes -- Nein --> ErrorRes --> End
    CheckRes -- Ja --> CheckAvail

    CheckAvail -- Nein --> ErrorAvail --> End
    CheckAvail -- Ja --> CreateLoan --> UpdateStatus --> Success --> End
```