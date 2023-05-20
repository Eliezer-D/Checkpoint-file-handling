#Checkpoint sur la lecture et manipulation de fichier en pyton avec Numpy

import numpy as np

# Ouverture du fichier
#le fichier data(Lending-Company-Saving.csv) se retrouve dans le meme dossier source que le fichier python qui contient le code
file = open("Lending-Company-Saving.csv", "r")

# Lecture des données avec la fonction genfromtxt
data = np.genfromtxt(file, delimiter=",")

# Analyse statistique de base
amounts = data[:, 6]  # Montants des prêts (colonne index 6)
#print(amounts)
mean_amount = np.nanmean(amounts)
median_amount = np.nanmedian(amounts)
std_amount = np.nanstd(amounts)

# Fermeture du fichier
#file.close()

# Affichage des résultats
print("Moyenne des montants de prêt :", mean_amount)
print("Médiane des montants de prêt :", median_amount)
print("Écart type des montants de prêt :", std_amount)
