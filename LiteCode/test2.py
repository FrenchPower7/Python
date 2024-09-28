import random
import matplotlib.pyplot as plt
import numpy as np

# Création du dictionnaire
array_info = {}

# Boucle pour stocker des valeurs aléatoires de 1 à 36
for num in range(1, 37):
    array_info[num] = random.randint(1, 100)  

# Données à afficher dans la heatmap
donnees = np.array([[array_info[3], array_info[6], array_info[9], array_info[12], array_info[15], array_info[18], array_info[21], array_info[24], array_info[27], array_info[30], array_info[33], array_info[36]],
                    [array_info[2], array_info[5], array_info[8], array_info[11], array_info[14], array_info[17], array_info[20], array_info[23], array_info[26], array_info[29], array_info[32], array_info[35]],
                    [array_info[1], array_info[4], array_info[7], array_info[10], array_info[13], array_info[16], array_info[19], array_info[22], array_info[25], array_info[28], array_info[31], array_info[34]]])

# Création de la heatmap
fig, ax = plt.subplots()
heatmap = ax.imshow(donnees, cmap='RdYlBu_r')

# Affichage des valeurs
for i in range(len(donnees)):
    for j in range(len(donnees[0])):
        text = ax.text(j, i, str(donnees[i, j]),
                       ha='center', va='center', color='w')

# Ajout d'une barre de couleur
cbar = ax.figure.colorbar(heatmap, ax=ax)

# Afficher la heatmap
plt.show()

# Afficher le dictionnaire
print("Dictionnaire array_info:", array_info)
# Addition de toutes les valeurs des clés du tableau
total = sum(array_info.values())
# Afficher le total
print("Somme de toutes les valeurs:", total)
