def is_anagram(k, l):
    if len(k) != len(l):
        return False
        
    k_list = []
    l_list = []

    for letter in k:
        k_list.append(letter)

    for letter in l:
        l_list.append(letter)

    
    if k_list.sort() == l_list.sort():
        return True
    
    return False

    

k = input()
l = input()


if is_anagram(k, l):
    print("TAK")
else:
    print("NIE")

"""Anagramem słowa k nazywamy takie słowo l,
które składa się z takich samych liter,
co słowo k lecz w dowolnej kolejności.
Wejście: W dwóch wierszach standardowego wejścia
podano słowa k oraz l o długości do 200 znaków,
złożone wyłącznie z małych liter alfabetu angielskiego.
Wyjście: W jedynym wierszu standardowego wyjścia
należy wypisad TAK, jeśli słowo l jest anagramem słowa k,
bądź NIE, jeśli słowo l nie jest anagramem słowa k."""