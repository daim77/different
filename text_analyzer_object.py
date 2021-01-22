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

    def __init__(self, file_path: str, clean_file_name='clean_text.txt'):
        self._full_path = file_path if os.path.isfile(file_path) else AttributeError
        self.dir_path = os.path.dirname(file_path)
        self.new_name = clean_file_name
        self._raw_text = self.file_opener()
        self._clean_text = self.text_cleaner()

    def file_opener(self):
        with open(self._full_path, 'r') as file:
            self._raw_text = file.read()
        return self._raw_text

    def text_cleaner(self):
        self._clean_text = [word.strip(string.punctuation) for word in self._raw_text.split()]
        return self._clean_text

    def most_frekquent_words(self):
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

