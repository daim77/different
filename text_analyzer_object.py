# TEXT CLEANER FROM TXT FILE WHICH IS IN SAME ROOT
# RESULT SAVED TO clean_result.txt IN SAME ROOT
# remove punctuation
# convert all char to lower
# remove all words with len 4 and less
# dict with word: occurences
# remove everything wit occurences 2 or less
# save dict

import string
import os


class TextAnalyzer:

    def __init__(self, file_path: str, clean_file_name='clean_text.txt'):
        if os.path.isfile(file_path):
            self._full_path = file_path
        else:
            print('wrong path or file name')
            exit()
        self.dir_path = os.path.dirname(file_path)
        self.new_name = clean_file_name
        self._raw_text = self.file_opener()
        self.clean_text = self.text_cleaner()
        self._result_file = self.top_words()

    def file_opener(self):
        with open(self._full_path, 'r') as file:
            self._raw_text = file.read()
        return self._raw_text

    def file_writer(self):
        with open(self.dir_path + self.new_name, 'w') as file:
            file.write(''.join(self._result_file))

    def text_cleaner(self):
        self.clean_text = [word.strip(string.punctuation + '\n').lower()
                           for word in self._raw_text.split() if len(word) > 4
                           ]
        return self.clean_text

    def top_words(self, top_x=3):
        my_dict, self._result_file = {}, []

        for word in self.clean_text:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1

        top_list_values = sorted(my_dict.values())[:top_x]

        for word in my_dict:
            if my_dict[word] in top_list_values:
                self._result_file.append(word)
        return self._result_file


if __name__ == '__main__':
    trvalky = TextAnalyzer('/Users/martindanek/Downloads/raw_text.txt')
    print(trvalky.dir_path)
    print(trvalky.new_name)
    print(trvalky.clean_text)
    trvalky.top_words(5)
    trvalky.file_writer()
