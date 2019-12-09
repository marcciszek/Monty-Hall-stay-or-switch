import random
import os
from random import randint

zmiana_licznik=0
bez_zmiany_licznik=0
ilosc_prob_licznik=0

while True:  
    os.system("cls")
    print(f'-> ilosc prob: {ilosc_prob_licznik}')
    print(f'-> ilosc wygranych po zmianie: {zmiana_licznik}')
    print(f'-> ilosc wygranych bez zmiany: {bez_zmiany_licznik}')   
    print("Podaj ilosc drzwi z zakresu (3-10), 0 konczy program")

    while True:
            try:                                      #probujemy pobrac wartosc
                ilosc = int(input("> "))
                break
            except ValueError:                        #pomijamy wartosc ktora prowadzi do bledu programu
                print('\n Wpisz poprawna liczbe!')

    if ilosc==0: break
    elif ilosc>=3 and ilosc<=10:
        tablica=["koza"]*ilosc                        #drzwi "od tyłu"
        tablica_wyswietlana=["X"]*ilosc               #drzwi widoczne dla gracza

        wygrana = randint(0,ilosc-1)                  #losowanie miejsca wygranej
        tablica[wygrana]="WYGRANA"                    #ustawienie wygranej za drzwiami
        print(tablica_wyswietlana)
        print("Podaj swoj wybor: ")

        while True:
            try:                                      #probujemy pobrac wartosc
                wybor=int(input("> "))-1
                break
            except ValueError:                        #pomijamy wartosc ktora prowadzi do bledu programu
                print('\n Wpisz poprawna liczbe!')

        pomocnicza_pozycja=wygrana
        licznik=0
        for i in range(ilosc):                        #otwieranie drzwi bez wyboru gracza i wygranej
            if(wygrana==wybor):
                while(pomocnicza_pozycja==wygrana):
                    pomocnicza_pozycja=randint(0,ilosc-1)
                if (tablica[i]!="WYGRANA" and i!=pomocnicza_pozycja):
                    tablica_wyswietlana[i]=tablica[i]
                    licznik+=1
                if (licznik>=(ilosc-2)): break
            else:
                if (tablica[i]!="WYGRANA" and i!=wybor):
                    tablica_wyswietlana[i]=tablica[i]
                    licznik+=1
                if (licznik>=(ilosc-2)): break
       
        print(tablica_wyswietlana)
        print("Czy chcesz zmienic wybor? [t/n]")
        zmiana=input("> ")

        if(zmiana=='t'):
            wybor,pomocnicza_pozycja=pomocnicza_pozycja,wybor
        if(wybor==wygrana):
            print("Wygrales!")
            if(zmiana=='t'): 
                zmiana_licznik+=1
            else: 
                bez_zmiany_licznik+=1
        else: 
            print("Nie wygrales :(")        
        ilosc_prob_licznik+=1
        
        print(tablica)
        input("Wcisnij cokolwiek, aby kontynuowac")