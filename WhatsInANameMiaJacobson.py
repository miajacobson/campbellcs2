#Mia Jacobson
#CS2 - "What's in a Name?"
#2/29/24
#Bugs: function (8) does not work for one word names, function 16 does not include a middle name
#Bonuses: #12,13,15,17 on spec

import random

def main():
    
    word = input("Please enter your name, or a random word you like.")
    
    while True: #menu for inputs
        print("Enter a number... or 'Q' to (Q)uit:")
        print("1) Count vowels")
        print("2) Count consonants")
        print("3) Reverse and display")
        print("4) Convert String to Lowercase")
        print("5) Convert String to Uppercase")
        print("6) Return First Name")
        print("7) Return Last Name")
        print("8) Return Middle Name")
        print("9) There is a Hyphen in This Name. T/F?")
        print("10) Print initials")
        print("11) Randomize Name")
        print("12) This Name is a Palindrome. T/F? ")
        print("13) This Name Has a Title. T/F? ")
        print("14) Return Fullname as a Sorted Array of Characters")
        print("15) Find the Length of Your Name")
        print("16) Print name in Last, First Format")


        select = input() #calling corresponding function based on user's number choice

        if select == '1':
            counter = vowel_count(word)
            print("There are" ,  counter , " vowels in " , "'" , word, "'")
        
        elif select == '2':
            counter = consonant_count(word)
            print("There are" ,  counter , "consonants in" , "'" , word, "'")
        
        elif select == '3':
            print(reverse_word(word))
        
        elif select == '4':
            print(convert_lower(word))

        elif select == '5':
            print(convert_upper(word))

        elif select == '6':
            print(first_name(word))
       
        elif select == '7':
            print(last_name(word))
        
        elif select == '8':
            print(middle_name(word))
        
        elif select == '9':
            print(check_hyphen(word))

        elif select == '10':
            print(make_initials(word))

        elif select == '11':
            print(random_name(word))

        elif select == '12':
            print(check_palindrome(word))
        
        elif select == '13':
            print(check_title(word))

        elif select == '14':
            print(sorted_array(word))
        
        elif select == '15':
            print(len_name(word))
        
        elif select == '16':
            print(format_name(word))

        elif select == 'Q':
            print("bye!")
            break
            

def vowel_count(word): #determines vowel frequency of a name
    counter = 0
    for letter in word:
        if letter == "a":
            counter = counter +1
        elif letter == "i":
            counter = counter +1
        elif letter == "e":
            counter = counter +1
        elif letter == "o":
            counter = counter +1
        elif letter == "u":
            counter = counter +1
        elif letter == "y":
            counter = counter +1
    return counter
   
def consonant_count(word): #determines consonant frequency of a name
    counter = 0
    vowels = ["a","e","i","o","u","y"]
    space = [" "]
    for letter in word:
        if letter not in vowels and letter not in space: #checks to make sure character is not a vowel or a space before adding 1 to the counter
            counter = counter +1
    return counter

def reverse_word(word):
    return word[::-1] #returns  word, but reversed
        
def convert_lower(word): #converts string to lowercase
    new_word = ""
    for letter in word:
        if ord(letter) in range(65,90): #checks to see if a character is uppercase based on corresonding ascii number values 
            new_word += chr(ord(letter) + 32) #adds 32 (the number needed to make a letter lowercase) to the ascii value
        else:
            new_word += letter
    return new_word

def convert_upper(word): #converts string to uppercase
    new_word = ""
    for letter in word:
        if ord(letter) in range(97,122): #checks to see if a character is lowercase  based on corresonding ascii number values
            new_word += chr(ord(letter) - 32) #subtracts 32 (the number needed to make a letter uppercase) to the ascii value
        else:
            new_word += letter
    return new_word

def first_name(word): #returns first name
    for i, letter in enumerate(word): 
        if letter == " ":
            return word[:i]   
        
    return word

def last_name(word): #returns last name
    for i, letter in enumerate(word[::-1]): #iterates through word backward
        if letter == " ":
            return word[len(word) - i:]
        
def middle_name(word): #returns middle name
    for i, letter in enumerate(word):
        if letter == " ":
            start = i
            break
    
    for i, letter in enumerate(word[::-1]):
        if letter == " ":
            end = len(word) - i
            break
    
    if start +1 != end: #checks to see if there is a word between the first and last name
        return word[start + 1:end]

def check_hyphen(word): #checks if there is a hyphen in word
    return "-" in word

def make_initials(word): #returns the first letter of each word in inputted name
    return ' '.join([first_name(word)[0], middle_name(word)[0], last_name(word)[0]]) #returns the first letter of each word back into a string form

def random_name(word):
    word = list(word)
    random.shuffle(word) #shuffles thr letters of the word using the imported random
    return ''.join(word) #returns word back into a string form

def check_palindrome(word): #checks if the name is the same forward and backward
    return first_name(word) == first_name(word)[::-1]


def check_title(word): #checks to see if the name contains a title
    title = ["Mr.", "Mrs.", "Dr.", "Sir", "Esq", "Ph.d", "Ms.", "Miss", "Lord", "Lady", "Dame", "Gen", "Lt. Gen", "Maj. Gen", "Capt."]
    for prefix in title: #for any of the given options (e.g. Mr., Mrs., etc.) in the list names "title"
        if prefix in word:
            return "True"
    return "False"

def sorted_array(word): #changes the name into an array of characters in an alphabetical order
    name = list(word)
    name.sort() 
    return ''.join(name) #returns word back into a string form

def len_name(word): #returns the length of the word
    return len(word)

def format_name(word): #formats word in last, first format
    return last_name(word) + "," + first_name(word)



if __name__ == '__main__':
        main()