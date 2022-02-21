# Definice proměných
kolo = 1
hrac = ""
cislo = 0
v_rade = int()  # Kolik znaků musí být v řade
pole_velikost = int()  # Velikost hracího pole
oddelovac = ("=" * 40)
oddeleni = ("-" * 40)
hranice_zacatek = "+---+"
hranice_pridavek = "---+"
hraci_pole = []


# Funkce
def vstup(nazev, tisk):
    while True:
        text = input(nazev)
        if text.isnumeric():
            if 0 < int(text) < 100:
                break
            else:
                print("Input number btw. 1 and 99!")
        else:
            print("Input number!")
        print(tisk)
    return int(text)


def tisk_matice(pole):
    for b in range(len(pole)):
        print(hranice_zacatek + hranice_pridavek * (len(pole[0]) - 1))
        for a in range(len(pole[0])):
            if pole[b][a] == 0:
                znak = " "
            else:
                znak = pole[b][a]
            if a == (pole_velikost - 1):
                print("| " + znak + " |")
            else:
                print("| " + znak, end=" ")
    print(hranice_zacatek + hranice_pridavek * (len(pole[0]) - 1))


def posuny(s, x, r, delka):
    if x < 0:
        xp = s + x
        xk = x
        xs = x
        return [n for n in range(xp, xk, xs)]
    elif x > 0:
        xp = s + x
        xk = delka
        xs = x
        return [o for o in range(xp, xk, xs)]
    else:
        return [s] * (delka - r - 1)


def kontrola(pole, pocet_v_rade):
    smer = [[1, 0], [1, 1], [0, 1], [-1, 1]]
    velikost_x = len(pole[0])
    velikost_y = len(pole)
    for r in range(velikost_y):
        for s in range(velikost_x):
            if pole[r][s] != 0:
                for x, y in smer:
                    pocet = 1
                    pozice = [[], []]
                    if (s == 0 and x == -1) or (s == (velikost_x - 1) and x == 1):
                        continue
                    if r == (velikost_y - 1) and y == 1:
                        continue
                    pozice[0] = posuny(s, x, r, velikost_x)
                    pozice[1] = posuny(r, y, s, velikost_y)
                    for px, py in zip(pozice[0], pozice[1]):
                        if pole[py][px] != pole[r][s]:
                            break
                        else:
                            pocet += 1
                            if pocet >= pocet_v_rade:
                                return True


# Pozdravení uživatele
print("Welcome to Tic Tac Toe")
print(oddelovac)
print("""GAME RULES:
Each player can place one mark (or stone)
per turn on the grid. The WINNER is
who succeeds in placing their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
print(oddelovac)

# Zadání velikosti pole a pocet v rade
while True:
    v_rade = vstup("Input number to choose how many marks in line: ", oddeleni)
    pole_velikost = vstup("Input number to choose size of grid (Input: 7, leads to grid: 7x7): ", oddeleni)
    if v_rade <= pole_velikost:
        break
    else:
        print("U can not win this.")


# Vytvoření hracího pole
for v in range(pole_velikost):
    hraci_pole.append(list())
    for i in range(pole_velikost):
        hraci_pole[v].append(0)

print(oddeleni)
print("Let's start the game")
print(oddeleni)
print(pole_velikost, v_rade)
tisk_matice(hraci_pole)
print(oddelovac)

while True:
    # Výběr hráče
    if kolo % 2 == 0:
        hrac = "o"
    else:
        hrac = "x"
    cislo = input(f"Player {hrac} | Please enter your move number: ")
    print(oddelovac)
    # Kontrola vstupního čísla
    if not cislo.isnumeric():
        print("Input number")
        continue
    if not 0 < int(cislo) <= (len(hraci_pole[0]) * len(hraci_pole)):
        print(f"Input number btw. 1 a {(len(hraci_pole[0]) * len(hraci_pole))}")
        continue
    # Výpočet a kontrola pozice
    ix = (int(cislo) - 1) % len(hraci_pole[0])
    iy = int((int(cislo) - ix) / len(hraci_pole[0]))
    if hraci_pole[iy][ix] != 0:
        print("Position is occupied")
        print(oddelovac)
        continue
    # Zapsání do pole
    hraci_pole[iy][ix] = hrac
    kolo += 1
    tisk_matice(hraci_pole)
    print(oddelovac)
    # Vyhodnocení
    if kontrola(hraci_pole, v_rade):
        print(f"Congratulations, the player {hrac} WON!")
        break
    elif kolo > len(hraci_pole) * len(hraci_pole[0]):
        print("Draw")
        break

print(oddelovac)
