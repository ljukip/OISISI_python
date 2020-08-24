from modul import trie


class Set():
    def __init__(self):

        self.all_files = {}
        self.logic_operation = 0
        #self.generate(trie, query)
        # 1 - union
        # 2 - intersection
        # 3 - complement

    def generate(self, trie, query):
        self.all_files = {}
        split_query = query.strip().split()
        if len(split_query) == 3:
            if split_query[1] == 'OR':
                self.logic_operation = 1
                split_query.pop(1)
            if split_query[1] == 'AND':
                self.logic_operation = 2
                split_query.pop(1)
            if split_query[1] == 'NOT':
                self.logic_operation = 3
                split_query.pop(1)

        for search in split_query:
            self.all_files[search] = trie.search(search)
        for key in self.all_files.keys():
            if self.all_files[key]:
                self.all_files[key] = self.custom_set(self.all_files[key])
            elif self.all_files[key] == False:
                print("Rec koju ste uneli se ne nalazi u folderu koji se pretrazuje")
                return False

        return True

    def custom_set(self, result_array):
        output_tmp = []
        output_result = {}
        result = {}
        i = 0
        for x in result_array:

            if x not in output_tmp:
                output_tmp.append(x)
                output_result[x] = 1
            else:
                output_result[x] += 1
            i = i + 1

        for key, value in sorted(output_result.items(), key=lambda item: item[1], reverse=True):
            result[key] = value
        return result
