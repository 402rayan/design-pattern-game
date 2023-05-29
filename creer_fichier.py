# Fonction permettant de créer un fichier texte avec toutes les lignes écrites dans le dossier actuel

import os

def creer_fichier_dossier():
    dossier_actuel = os.getcwd()  # Récupère le chemin du dossier actuel
    fichier_sortie = os.path.join(dossier_actuel, "dossier.txt")  # Chemin du fichier de sortie

    with open(fichier_sortie, "w") as f_sortie:
        for fichier in os.listdir(dossier_actuel):
            if os.path.isfile(os.path.join(dossier_actuel, fichier)):
                with open(os.path.join(dossier_actuel, fichier), "r") as f_entree:
                    contenu = f_entree.read()
                    f_sortie.write(contenu + "\n")

    print("Le fichier dossier.txt a été créé avec succès!")

# Appel de la fonction
creer_fichier_dossier()
