import sys
import os
import time

from modul.parser import Parser
from modul.graph import Graph
from modul.trie import Trie


def load_main_menu():
	print("################################################################################")
	print("Unesite apsolutnu putanju do direktorijuma, otkucajte TEST za pokretanje sa test direktorijumom ili 0 za izlazak:")
	print("\n################################################################################")
	control_value = 0
	while True:
		user_input = input(">>>>")
		if user_input == "TEST":
			return user_input
		elif user_input == "0":
			exit()
		elif os.path.isdir(user_input): #proveravamo da li direktorijum sadrzi poddirektorijum i validne HTML fajlove
			for file_name in os.listdir(user_input):
				tmp_name  = os.path.join(user_input, file_name)
				if tmp_name.endswith('.html') or os.path.isdir(tmp_name): # direktorijum sadrzi barem jedan poddirektorju ili HTML fajl
					control_value = 1
			if control_value == 1:
				return user_input
			print("Uneli ste neispravnu putanju, pokusajte ponovo")
		else:
			print("Greska pri unosu, pokusajte ponovo")

def custom_set(resoult_array):
	output_tmp = []
	output_result = {}
	i = 0
	for x in resoult_array:

		if x not in output_tmp:
			output_tmp.append(x)
			output_result[x] = 1
		else:
			output_result[x] += 1
		i=i+1
	return output_result

def actions_view(trie):
	run=True
	while run:

		print("################################################################################")
		print("Unosom odgovarajuceg broja, odaberite jednu od sledecih akcija:")
		print("1 - Pretraga reci")
		print("2 - Promena broja stranica za prikaz")
		print("0 - Izlaz")
		print("################################################################################")
		user_input_action = input(">>>>")
		if user_input_action == "1":
			querry = input("-Unesite rec koju trazite: ")
			search_result = trie.search(querry)
			result = custom_set(search_result)
			for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True):
				print("%s: -\t\t %s" % (value, key))
		elif user_input_action == "0":
			run = False
		else:
			print("----Pogresan unos, pokusajte ponovo----")

#Funkcija obliazi zadati direktorijum u dubinu i dodaje sve reci u stablo, i za svaku rec vezuje putanju ka datom fajlu 
def look_file_walker(path, trie):
	start_time = time.time()
	for root_dir, dir_name, file_names in os.walk(path):
		for file_name in file_names:
			if file_name.endswith('.html'):
				file_path = os.path.join(root_dir,file_name)
				links, words = parser.parse(file_path)
				for i,word in enumerate(words):
					trie.insert(word,file_path)
	end_time = time.time()
	print("Stablo je indeksirano, vreme indeksiranja " + str(round(end_time - start_time, 2)) + "s")


if __name__ == "__main__":
	parser = Parser()
	graph = Graph()
	trie = Trie()

	# NOTE putanja ka folderu za pretragu, po defoltu napravljena za rad na test skupu
	root_dir_path = os.getcwd() + os.path.sep + "test_skup" + os.path.sep + "python-2.7.7-docs-html"

	user_input = load_main_menu()
	if user_input != 'TEST':
		root_dir_path = user_input

	print("Molimo sacekajte stablo se indeksira...")
	look_file_walker(root_dir_path, trie)
	actions_view(trie)

