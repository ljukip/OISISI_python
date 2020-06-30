import sys
import os

from modul.parser import Parser
from modul.graph import Graph


def load_main_menu():
    print("#################################################################################################################")
    print("Unesite absolutnu putanju do direktorijuma, okucajte TEST da se pokrene sa test direktorijumom ili 0 za izlazak")
    print("#################################################################################################################")
    while True:
        user_input = input(">>>>")
        if os.path.isdir(user_input):
            return user_input
        elif user_input == "TEST":
            return user_input
        elif user_input == "0":
            exit()
        else:
            print("Uneliste neispravnu putanju, pokusajte ponovo")


if __name__ == "__main__":
    parser = Parser()
    graph = Graph(True)

    #NOTE putanja ka folderu  pretragu, po defoltu napravljena za rad na test skupu 
    root_dir_path = os.getcwd() + os.path.sep + "test_skup" + os.path.sep + "python-2.7.7-docs-html"

    user_input = load_main_menu()
    if user_input != 'TEST':
        root_dir_path = user_input
        
    print(root_dir_path)