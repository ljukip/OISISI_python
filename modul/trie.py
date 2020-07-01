class TrieNode:
    def __init__(self, ch , paths):
        self.char = ch
        self.children = {}
        self.paths = []
        self.end = False

class Trie:

    #NOTE Kreira se koren stabla
    def __init__(self):
        self.root = TrieNode(None)


    #NOTE Funkcija za ubaciavanje u stablo, krajni cvor sadrzi listu gde ka dokumentu koji ima tu rec u sebi
    def insert(self, word, path):

        parent = self.root
        for i, char in enumerate (word):
            if char in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            if i == len(word)-1:
                parent.end = True
                parent.paths.append(path)
   #NOTE funkcija za pretragu sluzi da prodje kroz stablo i nadje rece, ukoliko nadje vraca listu dokumenata
    def search(self, word):

        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        if parent.end == True:
            return parent.paths
        return False

    