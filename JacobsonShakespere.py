#Mia Jacobson
#CS11 Shakespeare Assignment
#4/1/24
#Bonuses: Use of Plotly, Sort dictionary

import os                                                       
from pathlib import Path
import plotly.express as px
import re

def main():

    current_dir = Path(__file__).parent
    #opens files for use in program
    file_path_MSND = current_dir / "ShakesperetxtFile.txt"
    file_path_RJ = current_dir / "romeoandjuliettxtfile.txt"

    file_in_MSND = open(file_path_MSND)
    file_in_RJ = open(file_path_RJ)


    while True:    #creates infinity loop for menu below                                         
        print("Menu: Enter Choice or 'Q' to (Q)uit:")
        print("1) Print Mid Summer Night's Dream Dictionary and Graph")
        print("2) Print Romeo and Juliet Dictionary and Graph")
    
    

        select = input("")    #menu for inputs             

        if select == '1':
            create_dictionary_MSND(file_in_MSND)
        
        if select == '2':
            create_dictionary_RJ(file_in_RJ)
        

#words to remove from the raw file
remove = ["and", "or", "I", "the", ":", ";", "?", "a", "is", "in", "to", "of", "that", "=", "And", "you", "with", "my", "", " ", "as", "this", "for", "the", "A", "not", "The", "it", "See", "me", "your", "be", "his", "well", "her", "on", "do", "our", "so", "was", "are", "have", "he", "will", "all", "by", "from", "i.", "no", "we", "but", "MIDSUMMERNIGHTS", "DREAM.", "their", "shall", "thou", "To", "what", "at", "ii.", "thy", "she", "one", "But", "am", "they", "which", "see", "What", "II.", "here", "him", "This", "an", "when", "if", "these", "more", "IV.", "thee", "must", "play", "O", "That", "Dem.", "were", "[Act", ".", "The.", "III.", "should", "For", "I.", "would", "Bot.", "did", "make", "hath", "her", "Bot.", "Lys.", "now", "Her.", "some", "there", "come", "Scene", "then", "can", "With", "than", "In", "V.", "may", "You", "When", "Puck.", "Enter", "like", "If", "It", "ROMEO", "JULIET", "NURSE", "Romeo", "CAPULET", "[Enter", "Ill", "BENVOLIO", "MERCUTIO", "FRIAR", "LAWRENCE", "My", "up", "LADY", "too", "Tybalt", "Thou"]

def create_dictionary_MSND(file_in_MSND):
    file_in_MSND.seek(1)                                       #move pointer to line 1

    dictionary = {}

    for record in file_in_MSND:                                #iterates through file
        sentence = record.split(" ")                           #splits the record at every space
        for word in sentence:
            clean = ""
            for char in word:                                                                 
                if char.lower() in "abcdefghijklmnopqrstuvwxyz:;.[": #removes anything from raw text that is not in the listed characters 
                    clean += char
            if clean in remove:                                #skips over all words listed in "remove" variable
                continue
            
            if word in dictionary.keys():
                dictionary[word] += 1                          #counter for value of each key(in this case, the key is the word)
            else:
                dictionary[word] = 1
    file1 = open("output1.txt", "w")                           #opens a new file and writes dictionary onto it
    file1.write(str(dictionary))                             
    file1.close()                                       

    sortables = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))#sorts dictionary in descending order
    print(sortables)#prints sorted dictionary
    graphables = px.pie(values = list(sortables.values())[:10], names = list(sortables.keys())[:10], title = "Breakdown of top 10 words in Mid-Summer Night's Dream")#only takes into account the top ten values of the sorted dictionary
    graphables.show()#opens a web browser and shows a pie chart of the top ten sorted values by percentage

#same code as above function, just different file being manipulated
def create_dictionary_RJ(file_in_RJ):
    file_in_RJ.seek(1)                                     

    dictionary = {}

    for record in file_in_RJ:                              
        sentence = record.split(" ")
        for word in sentence:
            clean = ""
            for char in word:
                if char.lower() in "abcdefghijklmnopqrstuvwxyz:;.[":
                    clean += char
            if clean in remove:
                continue
            
            if clean in dictionary.keys():
                dictionary[clean] += 1
            else:
                dictionary[clean] = 1
    file2 = open("output2.txt", "w")
    file2.write(str(dictionary))
    file2.close()
    
    sortables = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse=True))
    print(sortables)
    graphables = px.pie(values = list(sortables.values())[:10], names = list(sortables.keys())[:10], title ='Breakdown of top 10 words in Romeo and Juliet')
    graphables.show()


if __name__ == '__main__':
    main()