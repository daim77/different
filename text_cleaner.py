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


class TextCleaner:


    def __init__(self, file_path: str, clean_file_name = 'clean_text.txt'):
        self._fullPath = file_path if os.path.isfile(file_path) else AttributeError
        self.dirPath = os.path.dirname(file_path)
        self.newName = clean_file_name
        self._rawText = self.file_opener()
        self._cleanText = self.text_cleaner()

    def file_opener():
        with open(self._fullPath, 'r') as file:
            self._rawText = file.read()
        return self._rawText

    def text_cleaner():
        self._clean_text = [word.strip(string.punctuation) for word in self._raw_text.split()]
        return self._clean_text

    def most_frekquent_words():
        my_dict, top_list = {}, []

        for word in self._clean_text:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1

        top_list_values = sorted(my_dict.values())[:4]

        for word in my_dict:
            if my_dict[word] in top_list_values:
                top_list.append(word)
        return top_list

