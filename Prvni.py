#first_name = "Vanda"
#last_name = "Hoj"
#print(first_name, last_name)
#print(f"Hello {last_name}")
#print("Hello",first_name)
#student = True
#if student:
#    print("Jsi studentem")
#else:
#    print("Nejsi studntem")
#print(type(first_name))

#Kalkulačka v terminálu

#String functions
#vysledek = len(jmeno)
#vysledek = jmeno.find(" ")
#vysledek = jmeno.rfind("h")
#jmeno = jmeno.capitalize()
#jmeno = jmeno.upper()
#jmeno = jmeno.lower()
#vysledek = jmeno.isdigit()
#vysledek = jmeno.isalpha()
#vysledek = tel_cislo.count("-")
#vysledek = tel_cislo.replace("-", " ")
#print(help(str))

#Tvorba hesla
'''
username = input("Zadej svůj username: ")

if len(username) > 5:
    print("Heslo nemůže být delší jak 5")
elif username.find(" ") >= 0:
    print("Žádné mezery")
elif username.__contains__("Q"):
    print("Obsahuje písmeno Q")
elif username.isalpha():
    print("Zde je tvé jméno", username)
'''

#Indexing
'''
kreditniCislo = "1234-5678-9123-4567"
print(kreditniCislo[0]) 1
print(kreditniCislo[0:4]) 1234
print(kreditniCislo[5:9]) 5678
print(kreditniCislo[5:]) 5678-9123-4567
print(kreditniCislo[-2]) 6
print(kreditniCislo[::2]) 13-6892-57 Každý druhý charakter

kreditniCislo = "1234-5678-9123-4567"
#posledniCisla = kreditniCislo[-4:]
#print(f"XXXX-XXXX-XXXX-{posledniCisla}")

kreditniCislo = kreditniCislo[::-1]
print(kreditniCislo)
'''
#format specifiers
'''
price1 = 3.14159
price2 = -987.17
price3 = 56.89

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:10}")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:.^10}")
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3:+,.2f}")
'''
#WHILE loop
'''
jmeno = input("Zadej své jméno: ")

while jmeno == "":
    print("Nezadal jsi své jméno")
    jmeno = input("Zadej své jméno: ")

print("Ahoj", jmeno)
'''
#FOR LOOPS
#DIGITAL CLOCK
'''
import time

cas = 965

#vteriny = int(input("Zadej počet vteřin: "))
#minuty = int(input("Zadej počet minuty: "))
#hodiny = int(input("Zadej počet hodiny: "))



for x in range(cas,0, -1):
    vteriny = x % 60
    minuty = int(x / 60) % 60
    hodiny = int(x / 60 / 60) % 60
    print(f"{hodiny:02}:{minuty:02}:{vteriny:02}")
    time.sleep(1)
    break
    
print("Konec loopu")


strana_x = int(input("Zadej první stranu obdelníku: "))
strana_y = int(input("Zadej druhou stranu obdelníku: "))
for x in range(strana_x):
    for y in range(strana_y):
        print("*", end="")
    print()
'''
#COLLECTIONS
    # List  [] seřazené a měnitelné. Duplicitní
    # Set   {} neseřazené a neměnné, Add/Remove OK. Neduplicitní
    # Tuple () seřazené a měnitelné. Duplicitní, Rychlejší

#fruits = ["apple", "orange", "banana", "pineapple", "jackfruit"]
#fruits = {"apple", "orange", "banana", "pineapple", "jackfruit"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

#fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("pineapple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits.index("apple")
# fruits.()
#
#SET
#fruits.add("pineapple")
#fruits.remove("apple")
#fruits.clear()
#fruits.pop()
#print(dir(fruits))

#NUM PAD
'''
numPad = ((7, 8, 9),
          (4, 5, 6),
          (1, 2, 3),
          ("#", 0, "*"))

for row in numPad:
    for colm in row:
        print(colm, end=" ")
    print()
'''
#QUIZ GAME
'''
otazky = (("Jaké jídlo nemám rád: "),
          ("V jakém jazyku se právě učím: "),
          ("Kolik má člověk kostí v těle: "))

moznosti = (("A. Špagety", "B. Mák", "C. Banán"),
            ("A. C#", "B. Java", "C. Python"),
            ("A. 204", "B. 206", "C. 208"))

score = 0
cislo_otazky = 0


odpovedi = ("B", "C", "B")

for otazka in otazky:
    print("----------------------------")
    print(otazka)
    
    for moznost in moznosti[cislo_otazky]:
        print(moznost)
        
    output = input("Zadej správnou odpověď: ").upper()
    if(output == odpovedi[cislo_otazky]):
        score+= 1
    else:
        score-= 1

    cislo_otazky+= 1
print()
print("Zde je tvé skóre: ", score)
print("*************")
print(f"Správné odpovědi byly: {odpovedi}")
'''
#DICTIONARY = ordered, changable. no dulpicates
# 
'''
capitals = {"USA": "Washingtom D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))

if capitals.get("Russia"):
    print("Existuje")
else:
    print("Neexistuje")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroid"})
capitals.clear()
capitals.pop("China")
capitals.popitem()
'''




