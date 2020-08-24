import sys
import os
import time

from modul.parser import Parser
from modul.graph import Graph
from modul.trie import Trie
from modul.set import Set


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



def actions_view(trie,set,graph):
	run=True
	broj=6
	while run:
		print("#######################################Meni#####################################")
		print("Unosom odgovarajuceg broja, odaberite jednu od sledecih akcija:")
		print("--------------------------------------------------------------------------------")
		print("1 - Pretraga reci")
		print("2 - Promena broja stranica za prikaz (broj je %d)" %broj)
		print("0 - Izlaz")
		print("################################################################################")
		user_input_action = input(">>>>")
		if user_input_action == "1":
			query = input("-Unesite rec koju trazite: ")
			if set.generate(trie,query) == True:
				print_resoult(set.all_files, graph)
			else:
				continue
			#set.generate(trie,query)
			#if set.all_files == 0:
			#	continue
			#else:
			#	print_resoult(set.all_files)
		#	print (set.all_files)
		#	search_result = trie.search(query)
		#	result = custom_set(search_result)

		elif user_input_action == "2":
			runNum=True
			while runNum:
				print("Unesite broj, koliko stranica zelite da se prikaze:")
				try:
					temp=int(input(">>>>"))
				except ValueError:
					print("Pogresan unos broja, pokusajte ponovo")
				if broj<1:
					print("Broj premali! \t Minimalan broj stranica za prikaz je 1, pokusajte ponovo")
				elif broj>40:
					print("Broj prevelik! \t Maksimalan broj stranica za prikaz je 40, pokusajte ponovo")
				else:
					broj=temp
					#za prvih broj rangova
					print_resoult(set.all_files)
					runNum=False
					print("#######################################Meni#####################################")
					print("Unosom odgovarajuceg broja, odaberite jednu od sledecih akcija:")
					print("--------------------------------------------------------------------------------")
					print("1 - prethodne %d stranice" %broj)
					print("2 - sledece %d stranice" % broj)
					print("3 - nazad na glavni meni")
					print("0 - Izlaz")
					print("################################################################################")
					user_input_action2 = input(">>>>")
					if user_input_action2 == "3":
						user_input_action==1
						continue
					elif user_input_action2 == "2":
						# za od trenutni-broj do trenutni-1
						print_resoult(set.all_files)
					elif user_input_action2 == "1":
						# za trenutni+broj+1 rangova
						print_resoult(set.all_files)
					elif user_input_action2 == "0":
						runNum = False
					else:
						print("----Pogresan unos, pokusajte ponovo----")


		elif user_input_action == "0":
			run = False
		else:
			print("----Pogresan unos, pokusajte ponovo----")

#Funkcija obliazi zadati direktorijum u dubinu i dodaje sve reci u stablo, i za svaku rec vezuje putanju ka datom fajlu 
def look_file_walker(path, trie,raw_graph):
	start_time = time.time()
	for root_dir, dir_name, file_names in os.walk(path):
		for file_name in file_names:
			if file_name.endswith('.html'):
				file_path = os.path.join(root_dir,file_name)
				links, words = parser.parse(file_path)
				raw_graph[file_path] = links
				for i,word in enumerate(words):
					trie.insert(word,file_path)
	end_time = time.time()
	print("Stablo je indeksirano, vreme indeksiranja " + str(round(end_time - start_time, 2)) + "s")

def print_resoult( result,graph ):
	for prime_key in result.keys():
		print(prime_key)
		for key in result[prime_key].keys():
			print(graph.vertex_degree(key))
			print("%s: -\t\t %s" % (result[prime_key][key], key))
if __name__ == "__main__":
	parser = Parser()
	trie = Trie()
	set = Set()
	raw_graph = {}

	curent_page = 0
	paggination_offest = 10

	# NOTE putanja ka folderu za pretragu, po defoltu napravljena za rad na test skupu
	root_dir_path = os.getcwd() + os.path.sep + "test_skup" + os.path.sep + "python-2.7.7-docs-html"

	user_input = load_main_menu()
	if user_input != 'TEST':
		root_dir_path = user_input

	print("Molimo sacekajte stablo se indeksira...")
	look_file_walker(root_dir_path, trie,raw_graph)
	graph = Graph(raw_graph)
	actions_view(trie,set,graph)

