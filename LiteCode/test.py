import random
import matplotlib.pyplot as plt

def simulate_game(iterations):
    win_probability = 0.66
    bet_amount = 1000
    win_amount = 500
    total_money = 2000
    money_history = []  # Liste pour stocker la somme à chaque itération

    for i in range(iterations):
        # Simulating a win with a given probability
        if total_money >= 10:  # Ajouter cette condition pour éviter de continuer si le solde est inférieur à 10
            if random.random() < win_probability:
                total_money += win_amount
            else:
                total_money -= bet_amount

        money_history.append(total_money)  # Ajouter la somme actuelle à la liste

    return money_history

# Nombre d'itérations par simulation (à ajuster selon vos besoins)
n_iterations_per_simulation = 100
# Nombre de simulations (à ajuster selon vos besoins)
n_simulations = 100

# Stocker les résultats de chaque simulation
all_results = []

# Effectuer les simulations
for _ in range(n_simulations):
    results = simulate_game(n_iterations_per_simulation)
    all_results.append(results)

# Calculer la moyenne pour chaque itération
average_results = [sum(x) / n_simulations for x in zip(*all_results)]

# Afficher les résultats sous forme de graphique
plt.figure(figsize=(10, 6))

for i in range(n_simulations):
    plt.plot(range(1, n_iterations_per_simulation + 1), all_results[i], label=f'Simulation {i + 1}')

plt.plot(range(1, n_iterations_per_simulation + 1), average_results, label='Moyenne', linestyle='--', linewidth=2)

plt.xlabel('Nombre d\'itérations')
plt.ylabel('Solde')
plt.title('Évolution du solde pour différentes simulations')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)  # Faire en sorte que les courbes soient visibles à partir de 0 sur l'axe des y
plt.show()
