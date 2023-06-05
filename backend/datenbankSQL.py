import mysql.connector
import json


def createDatenbank():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS lastMinuteCampingTentEdition")


def createTabelle():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )

    mycursor = mydb.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS dataTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), postleitzahl VARCHAR(5), ort VARCHAR(30), straße VARCHAR(30), hausnummer VARCHAR(15), telefonnummer VARCHAR(30), öffnungszeitenAnfang VARCHAR(5), öffnungszeitenEnde VARCHAR(5), bewertung VARCHAR(3), preis VARCHAR(6), anzahlFreierPlätze VARCHAR(5), WC VARCHAR(4), dusche VARCHAR(4), spielplatz VARCHAR(4), tiereErlaubt VARCHAR(4), barrierefrei VARCHAR(4), bademöglichkeit VARCHAR(4), kiosk VARCHAR(4), WLAN VARCHAR(4), strom VARCHAR(4), waschmaschine VARCHAR(4), bildLink VARCHAR(255))"
    )


def addCampingplatz(
    name,
    postleitzahl,
    ort,
    straße,
    hausnummer,
    telefonnummer,
    öffnungszeitenAnfang,
    öffnungszeitenEnde,
    bewertung,
    preis,
    anzahlFreierPlätze,
    WC,
    dusche,
    spielplatz,
    tiereErlaubt,
    barrierefrei,
    bademöglichkeit,
    kiosk,
    WLAN,
    strom,
    waschmaschine,
    bildLink,
):
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO dataTable (name, postleitzahl, ort, straße, hausnummer, telefonnummer, öffnungszeitenAnfang, öffnungszeitenEnde, bewertung, preis, anzahlFreierPlätze, WC, dusche, spielplatz, tiereErlaubt, barrierefrei, bademöglichkeit, kiosk, WLAN, strom, waschmaschine, bildLink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
        name,
        postleitzahl,
        ort,
        straße,
        hausnummer,
        telefonnummer,
        öffnungszeitenAnfang,
        öffnungszeitenEnde,
        bewertung,
        preis,
        anzahlFreierPlätze,
        WC,
        dusche,
        spielplatz,
        tiereErlaubt,
        barrierefrei,
        bademöglichkeit,
        kiosk,
        WLAN,
        strom,
        waschmaschine,
        bildLink,
    )
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"\n\033[1m{name} wurde der Datenbank hinzugefügt!\033[0m")
    # hier datenbank auslesen und .json neu erstellen


def showCampingplätze():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dataTable")
    tabelle = mycursor.fetchall()
    print(tabelle)
    if tabelle:
        for datensatz in tabelle:
            datenArr = []
            for attribut in datensatz:
                datenArr.append(attribut)
            print(
                f"\033[1mName: {datenArr[1]}, Postleitzahl: {datenArr[2]}, Ort: {datenArr[3]}, Straße: {datenArr[4]}, Hausnummer: {datenArr[5]}, Telefonnummer: {datenArr[6]}\033[0m"
            )
    else:
        print("\n\033[1mEs konnten keine Einträge gefunden werden!\033[0m")


def searchCampingplatz(name):
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    name = name.capitalize()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM dataTable WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    tabelle = mycursor.fetchall()
    if tabelle:
        for datensatz in tabelle:
            datenArr = []
            for attribut in datensatz:
                datenArr.append(attribut)
            print(
                f"\033[1mName: {datenArr[1]}, Postleitzahl: {datenArr[2]}, Ort: {datenArr[3]}, Straße: {datenArr[4]}, Hausnummer: {datenArr[5]}, Telefonnummer: {datenArr[6]}\033[0m"
            )
    else:
        print(f"\n\033[1m{name} konnte in der Datenbank nicht gefunden werden!\033[0m")


def changeFreiePlätze(name, campingplatzPlätze):
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    name = name.capitalize()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM dataTable WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    tabelle = mycursor.fetchall()
    if tabelle:
        sql = "UPDATE dataTable SET anzahlFreierPlätze = %s WHERE name = %s"
        val = (
            campingplatzPlätze,
            name,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        print(
            f"\033[1mDie Anzahl freier Plätze für {name} wurde auf {campingplatzPlätze} aktualisiert.\033[0m"
        )
        # hier datenbank auslesen und .json neu erstellen
    else:
        print(f"\n\033[1m{name} konnte in der Datenbank nicht gefunden werden!\033[0m")
    


def deleteCampingplatz(name):
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    name = name.capitalize()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM dataTable WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    tabelle = mycursor.fetchall()
    if tabelle:
        sql = "DELETE FROM dataTable WHERE name = %s"
        val = (name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"\n\033[1m{name} wurde aus der Datenbank entfernt!\033[0m")
        # hier datenbank auslesen und .json neu erstellen
    else:
        print(f"\n\033[1m{name} konnte in der Datenbank nicht gefunden werden!\033[0m")
    

def writeDatabaseToJSON():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dataTable")
    tabelle = mycursor.fetchall()
    json.dumps(tabelle, f)


createDatenbank()
createTabelle()
import json

data = [{
    "name": "John",
    "age": 30,
    "city": "New York"
}]

with open('data.json', 'w') as f:
    json.dump(data, f)

# hier datenbank auslesen und .json erstellen


goOn = True
while goOn:
    print("\n\033[1mWas kann ich für dich tun?\033[0m")
    print("\033[1m1\033[0m - Um alle Campingplätze anzuzeigen.")
    print("\033[1m2\033[0m - Um einen Campingplatz zu suchen.")
    print("\033[1m3\033[0m - Um einen Campingplatz hinzuzufügen.")
    print("\033[1m4\033[0m - Um die Anzahl freier Plätze zu bearbeiten.")
    print("\033[1m5\033[0m - Um einen Campingplatz zu löschen.")
    print("\033[1m6\033[0m - Um das Programm zu beenden.")
    nextTask = input(
        "\n\033[1mWelche Option möchtest du durchführen? \nOption: \033[0m"
    )

    if nextTask == "6":
        print("\n\033[1mBis zum nächsten Mal!\033[0m")
        goOn = False
    elif nextTask == "5":
        entryToBeDeleted = input(
            "\n\033[1mWelcher Campingplatz soll aus der Datenbank entfernt werden? \nName: \033[0m"
        )
        deleteCampingplatz(entryToBeDeleted)
    elif nextTask == "4":
        campingplatzToBeEdited = input(
            "\n\033[1mFür welchen Campingplatz soll die Anzahl freier Plätze bearbeitet werden? \nName: \033[0m"
        )
        neuePlatzanzahl = input(
            "\n\033[1mWie viele freie Plätze sind nun vorhanden? \nFreie Plätze: \033[0m"
        )
        changeFreiePlätze(campingplatzToBeEdited, neuePlatzanzahl)
    elif nextTask == "3":
        campingplatzName = input(
            "\033[1mWie lautet der Name des Campingplatzes? \nName: \033[0m"
        )
        campingplatzName = campingplatzName.capitalize()
        campingplatzPLZ = input(
            f"\n\033[1mWie lautet die Postleitzahl von {campingplatzName}? \nPostleitzahl: \033[0m"
        )
        campingplatzOrt = input(
            f"\n\033[1mIn welchem Ort liegt {campingplatzName}? \nOrt: \033[0m"
        )
        campingplatzOrt = campingplatzOrt.capitalize()
        campingplatzStraße = input(
            f"\n\033[1mIn welcher Straße liegt {campingplatzName}? \nStraße: \033[0m"
        )
        campingplatzStraße = campingplatzStraße.capitalize()
        campingplatzHausnummer = input(
            f"\n\033[1mWie lautet die Hausnummer von {campingplatzName}? \nHausnummer: \033[0m"
        )
        campingplatzTelefonnummer = input(
            f"\n\033[1mWie lautet die Telefonnummer von {campingplatzName}? \nTelefonnummer: \033[0m"
        )
        campingplatzÖffnet = input(
            f"\n\033[1mWann öffnet {campingplatzName}? (XX:XX)\nÖffnet: \033[0m"
        )
        campingplatzSchließt = input(
            f"\n\033[1mWann schließt {campingplatzName}? (XX:XX)\nSchließt: \033[0m"
        )
        campingplatzBewertung = input(
            f"\n\033[1mWelche Bewertung hat {campingplatzName}? (1.0 - 5.0)\nBewertung: \033[0m"
        )
        campingplatzPreis = input(
            f"\n\033[1mWie viel kostet eine Übernachtung bei {campingplatzName} pro Person? \nPreis: \033[0m"
        )
        campingplatzPlätze = input(
            f"\n\033[1mWie viele Plätze sind bei {campingplatzName} aktuell frei? \nFreie Plätze: \033[0m"
        )
        campingplatzWC = input(
            f"\n\033[1mSind bei {campingplatzName} WC's vorhanden? (Ja/Nein) \nWC's vorhanden: \033[0m"
        )
        campingplatzWC = campingplatzWC.capitalize()
        campingplatzDusche = input(
            f"\n\033[1mSind bei {campingplatzName} Duschen vorhanden? (Ja/Nein) \nDuschen vorhanden: \033[0m"
        )
        campingplatzDusche = campingplatzDusche.capitalize()
        campingplatzSpielplatz = input(
            f"\n\033[1mSind bei {campingplatzName} Spielplätze vorhanden? (Ja/Nein) \nSpielplätze vorhanden: \033[0m"
        )
        campingplatzSpielplatz = campingplatzSpielplatz.capitalize()
        campingplatzHaustiere = input(
            f"\n\033[1mSind bei {campingplatzName} Haustiere erlaubt? (Ja/Nein) \nHaustiere erlaubt: \033[0m"
        )
        campingplatzHaustiere = campingplatzHaustiere.capitalize()
        campingplatzBarrierefrei = input(
            f"\n\033[1mIst {campingplatzName} barrierefrei? (Ja/Nein) \nIst barrierefrei: \033[0m"
        )
        campingplatzBarrierefrei = campingplatzBarrierefrei.capitalize()
        campingplatzBademöglichkeit = input(
            f"\n\033[1mSind bei {campingplatzName} Bademöglichkeiten vorhanden? (Ja/Nein) \nBademöglichkeiten vorhanden: \033[0m"
        )
        campingplatzBademöglichkeit = campingplatzBademöglichkeit.capitalize()
        campingplatzKiosk = input(
            f"\n\033[1mIst bei {campingplatzName} ein Kiosk vorhanden? (Ja/Nein) \nKiosk vorhanden: \033[0m"
        )
        campingplatzKiosk = campingplatzKiosk.capitalize()
        campingplatzWLAN = input(
            f"\n\033[1mIst bei {campingplatzName} WLAN verfügbar? (Ja/Nein) \nWLAN verfügbar: \033[0m"
        )
        campingplatzWLAN = campingplatzWLAN.capitalize()
        campingplatzStrom = input(
            f"\n\033[1mIst bei {campingplatzName} Strom verfügbar? (Ja/Nein) \nStrom verfügbar: \033[0m"
        )
        campingplatzStrom = campingplatzStrom.capitalize()
        campingplatzWaschmaschine = input(
            f"\n\033[1mSind bei {campingplatzName} Waschmaschinen vorhanden? (Ja/Nein) \nWaschmaschinen vorhanden: \033[0m"
        )
        campingplatzWaschmaschine = campingplatzWaschmaschine.capitalize()
        campingplatzBildLink = input(
            f"\n\033[1mGib hier die URL des Bildes für {campingplatzName} ein. \nURL: \033[0m"
        )

        addCampingplatz(
            campingplatzName,
            campingplatzPLZ,
            campingplatzOrt,
            campingplatzStraße,
            campingplatzHausnummer,
            campingplatzTelefonnummer,
            campingplatzÖffnet,
            campingplatzSchließt,
            campingplatzBewertung,
            campingplatzPreis,
            campingplatzPlätze,
            campingplatzWC,
            campingplatzDusche,
            campingplatzSpielplatz,
            campingplatzHaustiere,
            campingplatzBarrierefrei,
            campingplatzBademöglichkeit,
            campingplatzKiosk,
            campingplatzWLAN,
            campingplatzStrom,
            campingplatzWaschmaschine,
            campingplatzBildLink,
        )
    elif nextTask == "2":
        campingplatzToAddToSearchFor = input(
            "\n\033[1mNach welchem Campingplatz möchtest du suchen? \nName: \033[0m"
        )
        searchCampingplatz(campingplatzToAddToSearchFor)
    elif nextTask == "1":
        print("")
        showCampingplätze()
    else:
        print(
            "\n\033[1mDeine Eingabe ist nicht gültig, bitte versuche es noch einmal...\033[0m"
        )