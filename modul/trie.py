class TrieNode:
    def __init__(self, ch , paths = []):
        self.char = ch
        self.children = {}
        self.paths = paths
        self.end = False

    def get_child(self, char):
        return_value = None
        for child in self.children:
            if child.char.lower() == char.lower():
                return_value = child
                break
        return return_value

class Trie:

    #NOTE Kreira se koren stabla
    def __init__(self):
        self.root = TrieNode(None)


    #NOTE Funkcija za ubaciavanje u stablo, krajni cvor sadrzi listu gde ka dokumentu koji ima tu rec u sebi
    def insert(self, word, path):

        parent = self.root
        for i, char in enumerate (word):
            if parent.get_child(char) is not None:
                parent = parent.get_child(char)
            else:
                new_node = Trie(char, [])
                parent.children.append(new_node)
                parent = new_node
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

    