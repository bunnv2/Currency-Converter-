import requests
from bs4 import BeautifulSoup

url = 'https://kantoronline.pl/kursy-walut'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
body = soup.body
table = body.find('table', {'id': 'tableofcurrency'})

usd: int = table.find('td', {'id': 'usdsell'}).text
eur: int = table.find('td', {'id': 'eursell'}).text
gbp: int = table.find('td', {'id': 'gbpsell'}).text
pln = 1.0000
usd_pln = float(table.find('td', {'id': 'usdsell'}).text)     # Tyle dostaniemy za 1 USD i analogicznie z resztą
eur_pln = float(table.find('td', {'id': 'eursell'}).text)
gbp_pln = float(table.find('td', {'id': 'gbpsell'}).text)
pln_usd = float(table.find('td', {'id': 'usdbuy'}).text)      # Tyle zapłacimy za 1 USD i analogicznie z resztą
pln_eur = float(table.find('td', {'id': 'eurbuy'}).text)
pln_gbp = float(table.find('td', {'id': 'gbpbuy'}).text)

print(usd, eur, gbp, sep="\n")
print("Witam w prostym przeliczniku walut. Oferujemy przeliczenie PLN na USD, EUR, GBP oraz na odwrót.")
print("Aby skorzystać z naszych usług proszę napisać typ wymiany do przeliczenia.")
print("Przykład typu wymiany : PLN na EUR")
print("Proszę o używanie dużych liter przy wpisywaniu walut.")

zmienna = True

while zmienna:
    wymiana = input("Tutaj proszę wpisać typ wymiany : ")
    if wymiana == 'PLN na USD':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma / pln_usd, 2), "$")
    elif wymiana == 'PLN na EUR':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma / pln_eur, 2), "€")
    elif wymiana == 'PLN na GBP':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma / pln_gbp, 2), "£")
    elif wymiana == 'USD na PLN':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma * usd_pln, 2), "zł")
    elif wymiana == 'EUR na PLN':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma * eur_pln, 2), "zł")
    elif wymiana == 'GBP na PLN':
        suma = float(input("Proszę wpisać sumę pieniędzy do przeliczenia : "))
        print("Wynik :", round(suma * gbp_pln, 2), "zł")

    kontynuuj = input("Czy chcesz skorzystać z programu jeszcze raz? (wpisz 'tak' lub 'nie') : ")
    if kontynuuj == "tak":
        zmienna = True
    else:
        zmienna = False
