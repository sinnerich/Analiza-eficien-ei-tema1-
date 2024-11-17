import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Algoritmi de sortare
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Oprire timpurie dacă lista este deja sortată

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Generare liste și procesare sortare
rezultate = []
print("Se generează și se sortează listele...")

# Ajustează numărul de liste și intervalul pentru testare sau debug
for i in range(10):  # Schimbă 10 la 1000 pentru set complet de date
    lungime = random.randint(10, 1000)  # Ajustează la lungimi mai mici pentru testare
    lista = [random.randint(0, 100000) for _ in range(lungime)]
    print(f"Lista {i + 1} generată cu lungimea {lungime}.")

    for nume_sortare, functie_sortare in [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Timsort", sorted),
    ]:
        if nume_sortare == "Bubble Sort" and lungime > 1000:
            print(f"Se omite Bubble Sort pentru lista cu lungimea {lungime}.")
            continue

        print(f"Se sortează lista {i + 1} cu {nume_sortare}...")
        copie_lista = lista.copy()
        start_time = time.time()
        if nume_sortare == "Quick Sort":
            copie_lista = functie_sortare(copie_lista)  # Quick Sort returnează o listă nouă
        else:
            functie_sortare(copie_lista)
        end_time = time.time()
        rezultate.append({
            "Algoritm de Sortare": nume_sortare,
            "Lungimea Listei": lungime,
            "Timp (s)": end_time - start_time
        })
        print(f"Sortarea cu {nume_sortare} pentru lista {i + 1} finalizată în {end_time - start_time:.4f} secunde.")

# Salvare rezultate în CSV
print("Se salvează rezultatele în CSV...")
df = pd.DataFrame(rezultate)
df.to_csv("rezultate_sortare.csv", index=False)
print("Rezultatele au fost salvate în rezultatele_sortare.csv.")

# Analiza rezultatelor și generarea graficului
timpuri_medii = df.groupby("Algoritm de Sortare")["Timp (s)"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(timpuri_medii["Algoritm de Sortare"], timpuri_medii["Timp (s)"])
plt.title("Comparația Timpilor de Execuție ai Algoritmilor de Sortare")
plt.xlabel("Algoritm")
plt.ylabel("Timp Mediu (s)")
plt.savefig("comparatie_sortare.png")
plt.show()
print("Graficul a fost salvat ca comparatie_sortare.png.")
