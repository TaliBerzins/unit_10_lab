from pathlib import Path
import string

"""Word Count Project
Tali Berzins
To analyze files
03/29/2026
"""

class WordAnalyzer:
    
    """Counts number of words in a given text file by first letter

    Attributes:

    """

    def __init__(self, filepath):
        self.__filepath = Path(filepath)

        self.__frequencies = {}

    def process_file(self):
        with open(self.__filepath, 'r') as file:
            #For loop to create each line to a list without punctuation and all lower case of words
            for line in file:
                translator = str.maketrans('', '', string.punctuation)
                clean_s = line.translate(translator)
                clean_s = clean_s.lower()
                print(clean_s)
                word_list = clean_s.split()
                #Updating the count of each word in the dictionary
                for i in range(len(word_list)):
                    if word_list[i] in self.__frequencies:
                      self.__frequencies[word_list[i]]+=1
                    else:
                      self.__frequencies[word_list[i]]=1
                    
                    
                    
                



def main():

    analyzer = WordAnalyzer(input("Enter a file to analyze"))
    analyzer.process_file()


if __name__ == "__main__":
    main()



    
   
        
    
        

