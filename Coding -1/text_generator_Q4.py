import random
import codecs
class TextGenerator:
    def __init__(self):
        self.prefix_dict = {}
        
    def assimilateText(self, file_name):
        """
        This function reads all the text in the file and creates a prefix dictionary 
        that maps a pair (2-tuple) of words to a list of words which follow that pair in the text.
        """
        #open the file and read the text
        '''error occurs when trying to read a file that contains characters that are not compatible
        with the character encoding used by the system'''
        #with open(file_name, 'r') as file:
        with codecs.open(file_name, "r", encoding='utf-8', errors='ignore') as file:
            text = file.read()
            # split the text into words
            words = text.split()
            #iterating through the words
            for i in range(len(words)-2):
                prefix = (words[i], words[i+1])
                #check if prefix is already in prefix_dict
                if prefix in self.prefix_dict:
                    self.prefix_dict[prefix].append(words[i+2])
                else:
                    self.prefix_dict[prefix] = [words[i+2]]
                    
    def generateText(self, num_words, start_word = None):
         """
        This function creates random text based on the triplets contained in the prefix dictionary.
        It has a mandatory argument that let it know the number of words to be produced in this random manner.
        It also takes an additional argument that fixes the first word in the random text it produces.
        If it is not able to produce random text with the specified start word, it throws an exception.
        """
        #if start_word is given
        if start_word:
            prefix = None
            #iterating through prefix_dict to find the key containing start_word
            for key in self.prefix_dict.keys():
                if start_word in key:
                    prefix = key
                    break
            #if prefix not found raise exception
            if not prefix:
                raise Exception("Unable to produce text with the specified start word.")
        else:
            #choosing random prefix
            prefix = random.choice(list(self.prefix_dict.keys()))
        output = list(prefix)
        
        for i in range(num_words-2):
            suffix = self.prefix_dict[prefix]
            next_word = random.choice(suffix)
            output.append(next_word)
            prefix = (prefix[1], next_word)
        return " ".join(output)
t = TextGenerator()
t.assimilateText('sherlock.txt')
print(t.generateText(100))
print('\n')
print(t.generateText(50, 'London'))
print('\n')
print(t.generateText(50, 'Wedge'))
