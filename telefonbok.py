telefonkatalog = []

def printMeny():
    print()
    print("┌-------------Telefonkatalog--------------┐")
    print("| [1.] Legg til ny person                 |\n| [2.] Søk opp person eller telefonnummer |\n| [3.] Vis alle personer                  |\n| [4.] Endre informasjon                  |\n| [5.] Slett person og telefonnummer      |\n| [6.] Avslutt                            |")
    print("└-----------------------------------------┘")
    menyvalg = input("Skriv inn tall for å velge fra menyen (1-6): ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        endrePerson()
    elif valgtTall == "5":
        slettPerson()
    elif valgtTall == "6":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N ")
        if bekreftelse.lower() in ["j", "ja"]:  # Sjekker bare for ja
            exit()
        else:
            printMeny()
    else:
        nyttForsok = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsok)

def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    while True:
        telefonnummer = input("Skriv inn telefonnummer: ")
        if telefonnummer.isdigit():
            break
        else:
            print("[!] Telefonnummeret kan kun inneholde tall. Prøv igjen.")

    nyRegistrering = [fornavn, etternavn, telefonnummer]
    telefonkatalog.append(nyRegistrering)

    print("")
    print("{0} {1} er registrert med telefonnummer: {2}".format(fornavn, etternavn, telefonnummer))
    input("Trykk enter for å gå tilbake til menyen...")
    printMeny()

def visAllePersoner():
    if not telefonkatalog:
        print("")
        print("[!] Det er ingen registrerte personer i katalogen [!]")
        input("Trykk enter for å gå tilbake til menyen...")
        printMeny()
    else:
        for personer in telefonkatalog:
            info = "Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}".format(personer[0], personer[1], personer[2])
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)
        input("\nTrykk enter for å gå tilbake til menyen...")
        printMeny()

def sokPerson():
    if not telefonkatalog:
        print("")
        print("[!] Det er ingen registrerte personer i katalogen [!]")
        printMeny()
    else:
        print("")
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            nummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", nummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print("")
            print("[!] Ugyldig valg. [!] \n Velg et tall mellom 1-4: ")
            sokPerson()

def finnPerson(typeSok, sokeTekst):
    svar = []
    sokeTekst = sokeTekst.lower()
    for personer in telefonkatalog:
        if typeSok == "fornavn" and personer[0].lower() == sokeTekst:
            svar.append(personer)
        elif typeSok == "etternavn" and personer[1].lower() == sokeTekst:
            svar.append(personer)
        elif typeSok == "telefonnummer" and personer[2] == sokeTekst:
            svar.append(personer)

    if not svar:
        print("finner ingen personer")
    else:
        for personer in svar:
            info = "{0} {1} har telefonnummer {2}".format(personer[0], personer[1], personer[2])
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)

def slettPerson():
    if not telefonkatalog:
        print("")
        print("[!] Det er ingen registrerte personer i katalogen [!]")
        printMeny()
    else:
        print("")
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnOgSlettPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnOgSlettPerson("etternavn", navn)
        elif sokefelt == "3":
            nummer = input("Telefonnummer: ")
            finnOgSlettPerson("telefonnummer", nummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print("")
            print("[!] Ugyldig valg. [!] \n Velg et tall mellom 1-4: ")
            slettPerson()

def finnOgSlettPerson(typeSok, sokeTekst):
    sokeTekst = sokeTekst.lower()
    for idx, personer in enumerate(telefonkatalog):
        if (typeSok == "fornavn" and personer[0].lower() == sokeTekst) or \
           (typeSok == "etternavn" and personer[1].lower() == sokeTekst) or \
           (typeSok == "telefonnummer" and personer[2] == sokeTekst):
            print("")
            info = "Følgende person vil bli slettet: {0} {1} telefonnummer: {2}".format(personer[0], personer[1], personer[2]) 
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)
            bekreftelse = input("Er du sikker på at du vil slette? J/N ")
            if bekreftelse.lower() in ["j", "ja"]:
                del telefonkatalog[idx]
                print("[!] Personen er slettet fra telefonkatalogen. [!]")
            else:
                print("[!] Sletting avbrutt. [!]")
            break
    else:
        print("[!] Ingen treff for søk med " + sokeTekst + ". [!]")
    printMeny()

def endrePerson():
    if not telefonkatalog:
        print("")
        print("[!] Det er ingen registrerte personer i katalogen [!]")
        print("")
        printMeny()
    else:
        print("")
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnOgEndrePerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnOgEndrePerson("etternavn", navn)
        elif sokefelt == "3":
            nummer = input("Telefonnummer: ")
            finnOgEndrePerson("telefonnummer", nummer)
        elif sokefelt == "4":
            printMeny()
        else:
            print("")
            print("[!] Ugyldig valg. [!] \n Velg et tall mellom 1-4: ")
            endrePerson()

def finnOgEndrePerson(typeSok, sokeTekst):
    sokeTekst = sokeTekst.lower()
    for idx, personer in enumerate(telefonkatalog):
        if (typeSok == "fornavn" and personer[0].lower() == sokeTekst) or \
           (typeSok == "etternavn" and personer[1].lower() == sokeTekst) or \
           (typeSok == "telefonnummer" and personer[2] == sokeTekst):
            info = "Endrer informasjon for: {0} {1}, telefonnummer {2}".format(personer[0], personer[1], personer[2])
            print_dashed_line(info)
            print(info)
            print_dashed_line(info)

            nyttFornavn = input(f"Nytt fornavn (trykk Enter for å beholde '{personer[0]}'): ")
            nyttEtternavn = input(f"Nytt etternavn (trykk Enter for å beholde '{personer[1]}'): ")
            nyttTelefonnummer = input(f"Nytt telefonnummer (trykk Enter for å beholde '{personer[2]}'): ")

            if nyttFornavn:
                personer[0] = nyttFornavn
            if nyttEtternavn:
                personer[1] = nyttEtternavn
            if nyttTelefonnummer:
                personer[2] = nyttTelefonnummer

            oppdatert_info = "Oppdatert informasjon: {0} {1}, telefonnummer {2}".format(personer[0], personer[1], personer[2])
            print_dashed_line(oppdatert_info)
            print(oppdatert_info)
            print_dashed_line(oppdatert_info)
            break
    else:
        print("[!] Ingen treff for søk med " + sokeTekst + ". [!]")
    print("")
    printMeny()

def print_dashed_line(text):
    """Helper function to print a dashed line based on the length of the text."""
    length = len(text)
    print("-" * length)

printMeny()  # Starter programmet ved å skrive menyen første gang
