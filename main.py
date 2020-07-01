import sys
import os

from modul.parser import Parser
from modul.graph import Graph


def load_main_menu():
    print("#################################################################################################################")
    print("Unesite absolutnu putanju do direktorijuma, okucajte TEST da se pokrene sa test direktorijumom ili 0 za izlazak")
    print("#################################################################################################################")
    control_value = 0
    while True:
        user_input = input(">>>>")
        if user_input == "TEST":
            return user_input
        elif user_input == "0":
            exit()
        elif os.path.isdir(user_input): #proveravamo da li direktorijum sadrzi podirektoriju i validne HTML fajlove
            for file_name in os.listdir(user_input):
                tmp_name  = os.path.join(user_input, file_name)
                if tmp_name.endswith('.html') or os.path.isdir(tmp_name): # direktoriju sadrzi barem jedan poddirektorju ili HTML fajl
                    control_value = 1
            if control_value == 1:
                return user_input
            break
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