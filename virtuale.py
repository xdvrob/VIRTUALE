import random
import os
import time


print("""
    ________  ______  ____  ____  ____________
   / ____/ / / / __ \/ __ \/ __ )/ ____/_  __/
  / __/ / / / / /_/ / / / / __  / __/   / /   
 / /___/ /_/ / _, _/ /_/ / /_/ / /___  / /    
/_____/\____/_/ |_|\_____/_____/_____/ /_/     
                                          
""")

print("⚽ Benvenuto da Eurobet!⚽")
print("Sai già che perderai ma sai anche che il 99% dei giocatori si ferma prima della grande vincita, decidi di entrare...")
squadre = ["Napoli", "Bari", "Milan", "Inter", "Juventus"]
giocatori = {"Napoli": ["Maradona", "Kvara", "Lavezzi", "Cavani", "Hamsik"], "Bari": ["Barreto", "Cassano", "Almiron", "Caputo", "Kamata"],
             "Milan":["Robinho", "Maldini", "Seedorf", "Yepes", "Zapata"], "Inter": ["Zanetti", "Milito", "Samuel"
              ,"Eto'o", "Lautaro"], "Juventus": ["Cristiano Ronaldo", "Paulo Dybala", "Alex Del Piero", "Federico Chiesa"]}

LARGHEZZA_CAMPO = 30
ALTEZZA_CAMPO = 10
LARGHEZZA_PORTA = 5

# Funzione per pulire il terminale
def pulisci_terminale():
    # Controllo del sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # (Linux, macOS)
        os.system('clear')

# Funzione per disegnare il campo
def disegna_campo():
    pulisci_terminale()
    print("-" * (LARGHEZZA_CAMPO + 2))
    for i in range(ALTEZZA_CAMPO):
        print("|" + " " * LARGHEZZA_CAMPO + "|")
    print("-" * (LARGHEZZA_CAMPO + 2))

# Funzione per disegnare la porta
def disegna_porta():
    righe_porta = ["|" + " " * ((LARGHEZZA_CAMPO - LARGHEZZA_PORTA) // 2) + "|||" + " " * ((LARGHEZZA_CAMPO - LARGHEZZA_PORTA) // 2) + "|"]
    for riga in righe_porta:
        print(riga)

# Funzione per animare il goal
def anima_goal():
    for i in range(10):
        disegna_campo()
        print(" " * i + "\U000026BD" + " " * (LARGHEZZA_CAMPO - 1 - i) + "|")
        time.sleep(0.1)
    time.sleep(1)  # Attendiamo un secondo dopo l'animazione

# Funzione per animare la palla che va fuori dalla porta
def anima_palla_fuori():
    for i in range(5):
        disegna_porta()
        print(" " * i + "\U000026BD" + " " * (LARGHEZZA_PORTA - 1 - i) + "|")
        time.sleep(0.2)
    time.sleep(1)  # Attendiamo un secondo dopo l'animazione

# Funzione per estrarre casualmente una partita e un marcatore
def estrai_partita_e_marcatore():
    squadra_casa = random.choice(squadre)
    squadre_restanti = squadre.copy()
    squadre_restanti.remove(squadra_casa)
    squadra_ospite = random.choice(squadre_restanti)
    marcatore = random.choice(giocatori[squadra_casa])
    return squadra_casa, squadra_ospite, marcatore

# Funzione per simulare una partita
def simula_partita(squadra_casa, squadra_ospite, marcatore):
    gol_casa = 0
    gol_ospite = 0
    azioni_totali = 0
    max_tentativi = 3  # Numero massimo di tentativi totali
    print("Partita in corso...")
    while azioni_totali < max_tentativi:
        azioni_totali += 1
        marcatore_casa = random.choice(giocatori[squadra_casa])
        marcatore_ospite = random.choice(giocatori[squadra_ospite])
        esito_azione_casa = random.choice(["goal", "fuori"])
        esito_azione_ospite = random.choice(["goal", "fuori"])

        # Tentativo di segnare per la squadra di casa
        print("\nTentativo di", marcatore_casa, "per", squadra_casa, "...")
        if esito_azione_casa == "goal":
            probabilita_goal = random.random()
            if probabilita_goal > 0.3:  # Probabilità di segnare
                gol_casa += 1
                anima_goal()
                print("\U000026BD GOAL per", squadra_casa, "!", marcatore_casa, "segna!")
            else:
                print("Ma la palla va fuori!")
                anima_palla_fuori()
        else:
            print("Ma la palla va fuori!")
            anima_palla_fuori()
        time.sleep(1)

        # Tentativo di segnare per la squadra ospite
        print("\nTentativo di", marcatore_ospite, "per", squadra_ospite, "...")
        if esito_azione_ospite == "goal":
            probabilita_goal = random.random()
            if probabilita_goal > 0.3:  # Probabilità di segnare
                gol_ospite += 1
                anima_goal()
                print("\U000026BD GOAL per", squadra_ospite, "!", marcatore_ospite, "segna!")
            else:
                print("Ma la palla va fuori!")
                anima_palla_fuori()
        else:
            print("Ma la palla va fuori!")
            anima_palla_fuori()
        time.sleep(1)

    print("\nRisultato finale:")
    print(squadra_casa, gol_casa, "-", squadra_ospite, gol_ospite)
    return gol_casa, gol_ospite

# Funzione per gestire la puntata
def gestisci_puntata(saldo):
    puntata = int(input("Quanto vuoi puntare? "))
    if puntata > saldo:
        print("Puntata non valida. Il saldo è inferiore alla puntata.")
        return 0
    squadra_casa, squadra_ospite, marcatore = estrai_partita_e_marcatore()
    print("Partita:", squadra_casa, "vs", squadra_ospite)
    scelta = input("Su quale squadra vuoi puntare? (casa/ospite/pareggio) ").lower()
    if scelta == "casa":
        gol_casa, gol_ospite = simula_partita(squadra_casa, squadra_ospite, marcatore)
        if gol_casa > gol_ospite:
            print("Hai vinto! La squadra di casa ha vinto la partita!")
            print("Hai raddoppiato la tua puntata!")
            return puntata
        elif gol_casa == gol_ospite:
            print("Hai pareggiato! Nessuna squadra ha vinto la partita.")
            return 0
        else:
            print("Hai perso! La squadra di casa non ha vinto la partita!")
            return -puntata
    elif scelta == "ospite":
        gol_ospite, gol_casa = simula_partita(squadra_ospite, squadra_casa, marcatore)
        if gol_ospite > gol_casa:
            print("Hai vinto! La squadra ospite ha vinto la partita!")
            print("Hai raddoppiato la tua puntata!")
            return puntata
        elif gol_ospite == gol_casa:
            print("Hai pareggiato! Nessuna squadra ha vinto la partita.")
            return 0
        else:
            print("Hai perso! La squadra ospite non ha vinto la partita!")
            return -puntata
    elif scelta == "pareggio":
        gol_casa, gol_ospite = simula_partita(squadra_casa, squadra_ospite, marcatore)
        if gol_casa == gol_ospite:
            print("Hai vinto! La partita è finita in pareggio.")
            print("Hai raddoppiato la tua puntata!")
            return puntata
        else:
            print("Hai perso! La partita non è finita in pareggio.")
            return -puntata
    else:
        print("Scelta non valida.")
        return 0

# Funzione per gestire il gioco
def gioca():
    saldo = 100  
    disegna_porta()
    while saldo > 0:
        print("\nSaldo attuale:", saldo)
        saldo += gestisci_puntata(saldo)
    print("Hai esaurito il saldo. Grazie per aver giocato!")

# Avvia il gioco
gioca()



