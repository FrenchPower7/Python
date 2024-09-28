import time

def rechTriplonsRapide(tab):
    occurrences = set()
    for num in tab:
        if num in occurrences:
            return True
        occurrences.add(num)
    return False

def rechTriplonsBruteForce(tab):
    n = len(tab)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if tab[i] == tab[j] == tab[k]:
                    return True
    return False

def generate_random_array(size):
    import random
    return [random.randint(1, 1000) for _ in range(size)]

sizes = [100, 1000, 10000]
for size in sizes:
    array = generate_random_array(size)
    
    start_time = time.time()
    result_fast = rechTriplonsRapide(array)
    end_time = time.time()
    print(f"Taille du tableau: {size}, Recherche rapide de triplons: {result_fast}, Temps d'exécution: {end_time - start_time:.6f} secondes")

    start_time = time.time()
    result_brute = rechTriplonsBruteForce(array)
    end_time = time.time()
    print(f"Taille du tableau: {size}, Recherche brute de triplons: {result_brute}, Temps d'exécution: {end_time - start_time:.6f} secondes")
