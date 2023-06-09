import mysql.connector
import json

#Erstellt die Datenbank "lastMinuteCampingTentEdition" sofern sie noch nicht existiert
def createDatenbank():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS lastMinuteCampingTentEdition")

#Erstellt die Tabelle "dataTable" sofern sie noch nicht existiert mit - in .execute - definierten Datentypen und -größen
def createTabelle():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )

    mycursor = mydb.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS dataTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), postleitzahl VARCHAR(5), ort VARCHAR(30), straße VARCHAR(30), hausnummer VARCHAR(15), telefonnummer VARCHAR(30), öffnungszeitenAnfang VARCHAR(5), öffnungszeitenEnde VARCHAR(5), bewertung VARCHAR(3), preis VARCHAR(7), anzahlFreierPlätze SMALLINT, WC BOOLEAN, dusche BOOLEAN, spielplatz BOOLEAN, tiereErlaubt BOOLEAN, barrierefrei BOOLEAN, bademöglichkeit BOOLEAN, kiosk BOOLEAN, WLAN BOOLEAN, strom BOOLEAN, waschmaschine BOOLEAN, bildLink VARCHAR(255))"
    )

#Fügt der Tabelle einen Datensatz hinzu und führt dann die writeToJSON Funktion aus (siehe unten), sofern der Name in der Datenbank noch nicht vorhanden ist
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

    sql = "SELECT * FROM dataTable WHERE name = %s"
    val = (name,)
    mycursor.execute(sql, val)
    tabelle = mycursor.fetchall()
    if tabelle:
        print(f"\n\033[1m{name} ist bereits vorhanden!\033[0m")
        return 
    
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
    writeDatabaseToJSON()
        

#Zeigt alle Datensätze in Form definierter Attribute an, sofern vorhanden
def showCampingplätze():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dataTable")
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
        print("\n\033[1mEs konnten keine Einträge gefunden werden!\033[0m")

#Sucht einen bestimmten Campingplatz anhand des Namens und gibt diesen, sofern er gefunden wird, mit definierten Attributen aus
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

#Durchsucht anhand des Namens die Datenbank nach entsprechendem Datensatz und ändert in diesem, sofern es einen Treffer gibt, die Anzahl freier Campingplätze 
# und führt anschließend die writeToJSON Funktion aus
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
        writeDatabaseToJSON()
    else:
        print(f"\n\033[1m{name} konnte in der Datenbank nicht gefunden werden!\033[0m")
    

#Durchsucht die Datenbank anhand des Namens. Bei einem Treffer wird der entsprechende Datensatz gelöscht und anschließend die writeToJSON Funktion ausgeführt
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
        writeDatabaseToJSON()
    else:
        print(f"\n\033[1m{name} konnte in der Datenbank nicht gefunden werden!\033[0m")

#Fügt der Datenbank zur Veranschaulichung Testdaten hinzu.
def seeder():
    addCampingplatz(
        "Nature camping","18403","Nature","Naturestreet","5","0436543","00:00","24:00","4.3","22.00","11",True,True,False,True,True,True,True,False,True,True,"https://www.usnews.com/object/image/00000172-0a48-dd19-af73-dfc9adc60000/1-intro.jpg?update-time=1589312815886&size=responsive640"
    )
    addCampingplatz(
        "Forest camping","24500","Neuwald","Neuer waldweg","13","04046387387436543","08:00","21:00","4.5","20.00","7",True,True,True,True,True,False,True,True,True,False,"https://eurekacamping.johnsonoutdoors.com/sites/default/files/tent-camping-at-sunset.jpg"
    )
    addCampingplatz(
        "Nok camping","24768","Rendsburg","Kanalstra\u00dfe","66a","04356374356","06:00","22:00","3.9","12.80","35",True,True,True,True,False,True,False,False,True,True,"https://mediafiles.urlaubsguru.de/wp-content/uploads/2015/04/three-friends-camping-on-mountain-at-sunset-istock_48107094_xlarge-2.jpg"
    )
    addCampingplatz(
        "Neum\u00fcnster camping","24536","Neum\u00fcnster","Hauptstra\u00dfe","18a","0785486732","07:00","21:00","3.3","16.50","52",True,True,False,False,True,False,True,True,True,True,"https://www.fnp.de/bilder/2020/09/04/90037396/23894747-teilweise-kann-wildcampen-in-deutschland-richtig-teuer-werden-3sfe.jpg"
    )
    addCampingplatz(
        "Bordesholm camping","25235","Bordesholm","Dorfstra\u00dfe","12","075837443543","08:00","20:00","4.6","13.50","24",True,True,True,True,True,True,False,False,False,False,"https://blog-6aa0.kxcdn.com/wp-content/uploads/2021/02/camping-reiseziele-in-deutschland-titel-bild.jpg"
    )
    addCampingplatz(
        "Kieler campingparadies","28764","Kiel","Achterbahn","65","04376587353","10:00","19:00","2.3","75.60","45",True,True,False,False,False,False,True,False,False,False,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCTvreuZjNlKBC3gZGOCjPMnrjfpZxzeYHDhmhGTIVwa3IzRXoUaeUMRAPlyGRQb30Jw4&usqp=CAU"
    )
    
#Die komplette Tabelle wird aus der Datenbank ausgelesen, in eine liste von Objekten überführt und anschließend in einer .JSON Datei gespeichert, 
# welche von unserem Front-End als Datenquelle verwendet wird. Da nach jeder Veränderung der Daten in der Datenbank auch die .JSON Datei neu erstellt wird, 
# kann man diese als Zwischenspeicher ansehen wobei die datenbank weiterhin als "Source-of-truth" fungiert.
def writeDatabaseToJSON():
    mydb = mysql.connector.connect(
        host="localhost", user="root", database="lastMinuteCampingTentEdition"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dataTable")
    tabelle = mycursor.fetchall()
    data = []
    for datensatz in tabelle:
        dateaObj = {
            "id": datensatz[0],
            "name": datensatz[1],
            "plz": datensatz[2],
            "ort": datensatz[3],
            "straße": datensatz[4],
            "hausnummer": datensatz[5],
            "telefonnummer": datensatz[6],
            "oeffnungszeitenAnfang": datensatz[7],
            "oeffnungszeitenEnde": datensatz[8],
            "bewertung": datensatz[9],
            "preis": datensatz[10],
            "anzahlFreierPlaetze": datensatz[11],
            "WC": datensatz[12],
            "dusche": datensatz[13],
            "spielplatz": datensatz[14],
            "haustiere": datensatz[15],
            "barrierefrei": datensatz[16],
            "bademöglichkeit": datensatz[17],
            "kiosk": datensatz[18],
            "WLAN": datensatz[19],
            "strom": datensatz[20],
            "waschmaschine": datensatz[21],
            "bildURL": datensatz[22],
        }
        data.append(dateaObj)
    with open('data.json', 'w') as f:
        json.dump(data, f)
            


createDatenbank()
createTabelle()



goOn = True

while goOn:
    print("\n\033[1mWas kann ich für dich tun?\033[0m")
    print("\033[1m1\033[0m - Um alle Campingplätze anzuzeigen.")
    print("\033[1m2\033[0m - Um einen Campingplatz zu suchen.")
    print("\033[1m3\033[0m - Um einen Campingplatz hinzuzufügen.")
    print("\033[1m4\033[0m - Um die Anzahl freier Plätze zu bearbeiten.")
    print("\033[1m5\033[0m - Um einen Campingplatz zu löschen.")
    print("\033[1m6\033[0m - Um Testdaten in die Datenbank einzufügen.")
    print("\033[1m7\033[0m - Um das Programm zu beenden.")
    nextTask = input(
        "\n\033[1mWelche Option möchtest du durchführen? \nOption: \033[0m"
    )

    if nextTask == "7":
        print("\n\033[1mBis zum nächsten Mal!\033[0m")
        goOn = False
    elif nextTask == "6":
        seeder()
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
            f"\n\033[1mSind bei {campingplatzName} WC's vorhanden? (True/False) \nWC's vorhanden: \033[0m"
        )
        campingplatzWC = campingplatzWC.capitalize()
        campingplatzDusche = input(
            f"\n\033[1mSind bei {campingplatzName} Duschen vorhanden? (True/False) \nDuschen vorhanden: \033[0m"
        )
        campingplatzDusche = campingplatzDusche.capitalize()
        campingplatzSpielplatz = input(
            f"\n\033[1mSind bei {campingplatzName} Spielplätze vorhanden? (True/False) \nSpielplätze vorhanden: \033[0m"
        )
        campingplatzSpielplatz = campingplatzSpielplatz.capitalize()
        campingplatzHaustiere = input(
            f"\n\033[1mSind bei {campingplatzName} Haustiere erlaubt? (True/False) \nHaustiere erlaubt: \033[0m"
        )
        campingplatzHaustiere = campingplatzHaustiere.capitalize()
        campingplatzBarrierefrei = input(
            f"\n\033[1mIst {campingplatzName} barrierefrei? (True/False) \nIst barrierefrei: \033[0m"
        )
        campingplatzBarrierefrei = campingplatzBarrierefrei.capitalize()
        campingplatzBademöglichkeit = input(
            f"\n\033[1mSind bei {campingplatzName} Bademöglichkeiten vorhanden? (True/False) \nBademöglichkeiten vorhanden: \033[0m"
        )
        campingplatzBademöglichkeit = campingplatzBademöglichkeit.capitalize()
        campingplatzKiosk = input(
            f"\n\033[1mIst bei {campingplatzName} ein Kiosk vorhanden? (True/False) \nKiosk vorhanden: \033[0m"
        )
        campingplatzKiosk = campingplatzKiosk.capitalize()
        campingplatzWLAN = input(
            f"\n\033[1mIst bei {campingplatzName} WLAN verfügbar? (True/False) \nWLAN verfügbar: \033[0m"
        )
        campingplatzWLAN = campingplatzWLAN.capitalize()
        campingplatzStrom = input(
            f"\n\033[1mIst bei {campingplatzName} Strom verfügbar? (True/False) \nStrom verfügbar: \033[0m"
        )
        campingplatzStrom = campingplatzStrom.capitalize()
        campingplatzWaschmaschine = input(
            f"\n\033[1mSind bei {campingplatzName} Waschmaschinen vorhanden? (True/False) \nWaschmaschinen vorhanden: \033[0m"
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
