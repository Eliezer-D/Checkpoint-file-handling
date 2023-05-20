#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np

# Ouverture du fichier
file = open("Lending-Company-Saving.csv", "r")
#print(file.read())
#file.close()

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


# In[ ]:




