# "Оператор "with"
# "Найдёт везде"

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        znaki_prep = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            n = 0
            with open(i, encoding='utf-8') as file:
                line1 = []
                lines = len(file.readlines())
                for l in range(0, lines):
                    line1.append(0)
            with open(i, encoding='utf-8') as file:
                for line in file:
                    m = 0
                    line = line.lower()
                    for k in line:
                        for j in znaki_prep:
                            if k == j:
                                m += 1
                                line1[n] = line.replace(k,"")
                        if m == 0:
                            line1[n] = line
                    n += 1
            words = []
            wordspodriad = []
            for j in line1:
                words.append(j.split())
                wordspodriad = sum(words,[])
            all_words[i] = wordspodriad
        return all_words
    def find(self, word):
        word_finding = {}
        n_word = 1
        for file_name in self.file_names:
            for item in self.get_all_words()[file_name]:
                if item != word.lower():
                    n_word += 1
                else:
                    word_finding[file_name] = n_word
                    break
        return word_finding
    def count(self, word):
        word_counting = {}
        number_word = 0
        for file_name in self.file_names:
            for item in self.get_all_words()[file_name]:
                if item == word.lower():
                    number_word += 1
                else:
                    continue
            word_counting[file_name] = number_word
        return word_counting
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
