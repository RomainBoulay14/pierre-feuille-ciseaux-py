import random

def determine_gagnant(choix_joueur, choix_ordi):
    if choix_joueur == choix_ordi:
        return "Égalité"
    elif (choix_joueur == 'Pierre' and choix_ordi == 'Ciseaux') or \
         (choix_joueur == 'Feuille' and choix_ordi == 'Pierre') or \
         (choix_joueur == 'Ciseaux' and choix_ordi == 'Feuille'):
        return "Joueur gagne !"
    else:
        return "Ordinateur gagne !"

def main():
    choix_possibles = ['Pierre', 'Feuille', 'Ciseaux']
    
    while True:
        print("\nVeuillez choisir (Pierre, Feuille, Ciseaux) ou 'Q' pour quitter : ")
        choix_joueur = input().capitalize()
        
        if choix_joueur == 'Q':
            print("Au revoir !")
            break
        
        if choix_joueur not in choix_possibles:
            print("Choix invalide. Veuillez choisir entre Pierre, Feuille ou Ciseaux.")
            continue
        
        choix_ordi = random.choice(choix_possibles)
        print("L'ordinateur choisit:", choix_ordi)
        
        resultat = determine_gagnant(choix_joueur, choix_ordi)
        print(resultat)

if __name__ == "__main__":
    main()