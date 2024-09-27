import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="brukernavn",  # Skriv in ditt brukernavn her
    password="passord",  # Skriv in ditt passsord her
    database="telefonkatalog"
)
cursor = conn.cursor()

def printMeny():
    print()
    print("┌-------------Telefonkatalog--------------┐")
    print("| [1.] Legg til ny kontakt                |\n| [2.] Søk opp kontakt eller telefonnummer |\n| [3.] Vis alle kontakter                 |\n| [4.] Endre informasjon                  |\n| [5.] Slett kontakt og telefonnummer     |\n| [6.] Avslutt                            |")
    print("└-----------------------------------------┘")
    menyvalg = input("Skriv inn tall for å velge fra menyen (1-6): ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerKontakt()
    elif valgtTall == "2":
        sokKontakt()
        printMeny()
    elif valgtTall == "3":
        visAlleKontakter()
    elif valgtTall == "4":
        endreKontakt()
    elif valgtTall == "5":
        slettKontakt()
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if bekreftelse.lower() in ["j", "ja"]:
            exit()
        else:
            printMeny()
    else:
        nyttForsok = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsok)

def registrerKontakt():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    while True:
        telefonnummer = input("Skriv inn telefonnummer: ")
        if telefonnummer.isdigit():
            break
        else:
            print("[!] Telefonnummeret kan kun inneholde tall. Prøv igjen.")

    cursor.execute("INSERT INTO kontakter (fornavn, etternavn, telefonnummer) VALUES (%s, %s, %s)", (fornavn, etternavn, telefonnummer))
    conn.commit()

    print("{0} {1} er registrert med telefonnummer: {2}".format(fornavn, etternavn, telefonnummer))
    input("Trykk enter for å gå tilbake til menyen...")
    printMeny()

def visAlleKontakter():
    cursor.execute("SELECT fornavn, etternavn, telefonnummer FROM kontakter")
    result = cursor.fetchall()

    if not result:
        print("[!] Det er ingen registrerte kontakter i katalogen [!]")
    else:
        for kontakt in result:
            info = "Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}".format(kontakt[0], kontakt[1], kontakt[2])
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)
    input("\nTrykk enter for å gå tilbake til menyen...")
    printMeny()

def sokKontakt():
    print("1. Søk på fornavn")
    print("2. Søk på etternavn")
    print("3. Søk på telefonnummer")
    sokefelt = input("Velg ønsket søk 1-3: ")

    if sokefelt == "1":
        navn = input("Fornavn: ")
        cursor.execute("SELECT fornavn, etternavn, telefonnummer FROM kontakter WHERE fornavn = %s", (navn,))
    elif sokefelt == "2":
        navn = input("Etternavn: ")
        cursor.execute("SELECT fornavn, etternavn, telefonnummer FROM kontakter WHERE etternavn = %s", (navn,))
    elif sokefelt == "3":
        nummer = input("Telefonnummer: ")
        cursor.execute("SELECT fornavn, etternavn, telefonnummer FROM kontakter WHERE telefonnummer = %s", (nummer,))
    else:
        printMeny()
        return

    result = cursor.fetchall()
    if not result:
        print("Finner ingen kontakter")
    else:
        for kontakt in result:
            info = "{0} {1} har telefonnummer {2}".format(kontakt[0], kontakt[1], kontakt[2])
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)

def slettKontakt():
    telefonnummer = input("Skriv inn telefonnummeret til kontakten du vil slette: ")
    cursor.execute("DELETE FROM kontakter WHERE telefonnummer = %s", (telefonnummer,))
    conn.commit()

    if cursor.rowcount > 0:
        print("[!] Kontakten er slettet fra telefonkatalogen. [!]")
    else:
        print("[!] Ingen kontakt funnet med telefonnummer {0}. [!]".format(telefonnummer))

    printMeny()

def endreKontakt():
    telefonnummer = input("Skriv inn telefonnummeret til kontakten du vil endre: ")
    cursor.execute("SELECT * FROM kontakter WHERE telefonnummer = %s", (telefonnummer,))
    kontakt = cursor.fetchone()

    if kontakt:
        nyttFornavn = input(f"Nytt fornavn (trykk Enter for å beholde '{kontakt[1]}'): ") or kontakt[1]
        nyttEtternavn = input(f"Nytt etternavn (trykk Enter for å beholde '{kontakt[2]}'): ") or kontakt[2]
        nyttTelefonnummer = input(f"Nytt telefonnummer (trykk Enter for å beholde '{kontakt[3]}'): ") or kontakt[3]

        cursor.execute("UPDATE kontakter SET fornavn = %s, etternavn = %s, telefonnummer = %s WHERE telefonnummer = %s",
                       (nyttFornavn, nyttEtternavn, nyttTelefonnummer, telefonnummer))
        conn.commit()
        print("[!] Kontaktinformasjon oppdatert. [!]")
    else:
        print("[!] Ingen kontakt funnet med telefonnummer {0}. [!]".format(telefonnummer))
    printMeny()

def print_dashed_line(text):
    print("-" * len(text))

printMeny()
