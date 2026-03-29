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
                word_list = clean_s.split()
                #Updating the count of each word in the dictionary
                for i in range(len(word_list)):
                    if word_list[i] in self.__frequencies:
                      self.__frequencies[word_list[i]]+=1
                    else:
                      self.__frequencies[word_list[i]]=1
    
    #Print function to print dictionary alphabetically
    def print_report(self):
        sorted_dict = dict(sorted(self.__frequencies.items()))
        for key, value in sorted_dict.items():
            print(f"{key:<15} ::{value}")

                    
                    
                    
                


#Main function where we will loop until the user exits
def main():
    print("--- Word Analyzer ---")
    print("Please select a file to analyze:")

    
    base_path = Path.cwd()
    files = {
        "1": base_path / "monte_cristo.txt",
        "2": base_path / "princess_mars.txt",
        "3": base_path / "Tarzan.txt",
        "4": base_path / "treasure_island.txt"
    }
    file_names = {
        "1": "Monte Cristo",
        "2": "Princess Mars",
        "3": "Tarzan",
        "4": "Treasure Island",
        "5": "Exit"
    }
    print(file_names)
    user_choice = input("Enter your choice")
    if(user_choice == "5"):
        print("Goodbye!")
        return
    else:
        
    
     while(user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4"):
        user_choice = input("Invalid choice. Please select from 1-5")
    
     while(user_choice == "1" or user_choice == "2" or user_choice == "3"or user_choice == "4"):
       analyzer = WordAnalyzer(files[user_choice])
       analyzer.process_file()
       analyzer.print_report()
          
       user_choice = input("Enter your choice")
    
       while(user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4"):
        if(user_choice == "5"):
           print("Goodbye!")
           return
        else:
         user_choice = input("Invalid choice. Please select from 1-5")

        


if __name__ == "__main__":
    main()



    
   
        
    
        

