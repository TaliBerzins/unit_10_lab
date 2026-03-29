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
            for line in file:
                translator = str.maketrans('', '', string.punctuation)
                clean_s = line.translate(translator)
                print(clean_s)



def main():

    analyzer = WordAnalyzer(input("Enter a file to analyze"))
    analyzer.process_file()


if __name__ == "__main__":
    main()



    
   
        
    
        

