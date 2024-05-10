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
        else: #dangling else for all non-valid inputs
            print("Invalid response. Please select an integer between 1 and 16, or type 'Q' to quit. ")
            

def vowel_count(word): 
    #determines vowel frequency of a word
    #parameter(what function takes in): the word
    #returns number of vowels in a word
    
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
   
def consonant_count(word): 
    #determines consonant frequency of a word
    #parameter: the word
    #returns number of consonants in a word
    counter = 0
    vowels = ["a","e","i","o","u","y"]
    space = [" "]
    for letter in word:
        if letter not in vowels and letter not in space: #checks to make sure character is not a vowel or a space before adding 1 to the counter
            counter = counter +1
    return counter

def reverse_word(word):
    #determines the inputted word in reverse
    #parameter: the word
    #returns the word backwards

    return word[::-1] #returns  word, but reversed
        
def convert_lower(word): 
    #converts string to lowercase
    #parameter: the word
    #returns lowercase version of word
    new_word = ""
    for letter in word:
        if ord(letter) in range(65,90): #checks to see if a character is uppercase based on correponding ascii number values 
            new_word += chr(ord(letter) + 32) #adds 32 (the number needed to make a letter lowercase) to the ascii value
        else:
            new_word += letter
    return new_word

def convert_upper(word):
    #converts string to uppercase
    #parameter: the word
    #returns uppercase version of word
    new_word = ""
    for letter in word:
        if ord(letter) in range(97,122): #checks to see if a character is lowercase  based on corresonding ascii number values
            new_word += chr(ord(letter) - 32) #subtracts 32 (the number needed to make a letter uppercase) to the ascii value
        else:
            new_word += letter
    return new_word

def first_name(word): 
    #determines first name 
    #parameter: a full name
    #returns first name

    for i, letter in enumerate(word): #iterate through list by position, letter
        if letter == " ": #if letter is a space...
            return word[:i] #returns all letters before the space
        
    return word

def last_name(word):
    #determines last name 
    #parameter: a full name
    #returns last name
    for i, letter in enumerate(word[::-1]): #iterate through list backwards by position, letter
        if letter == " ": #if letter is a space...
            return word[len(word) - i:] #returns all letters after space(when iterated through backwards)
        
def middle_name(word): 
    #determines middle name 
    #parameter: a full name
    #returns middle name

    for i, letter in enumerate(word): #iterate through list by position, letter
        if letter == " ": #if letter is a space...
            start = i   #new word is identified to start after space
            break
    
    for i, letter in enumerate(word[::-1]): #iterate through list backwards by position, letter
        if letter == " ": #if letter is a space...
            end = len(word) - i #counter tool to determine last space
            break
    
    if start +1 != end: #checks to see if there is a word between the first and last name
        return word[start + 1:end]

def check_hyphen(word): 
    #determines the presence of a hyphen in a word 
    #parameter: a word
    #returns T/F if there is a hyphen
    return "-" in word

def make_initials(word): 
    #returns the first letter of each name (initials)
    #parameter: a full name
    #returns initials
    return ' '.join([first_name(word)[0], middle_name(word)[0], last_name(word)[0]]) #returns the first letter of each word back into a string form

def random_name(word):
    #returns the word with the letters in randomized order
    #parameter: a word
    #returns scrambled name
    word = list(word)
    random.shuffle(word) 
    return ''.join(word) #returns word back into a string form

def check_palindrome(word): 
    #determines the presence of a palindrome in a word 
    #parameter: a word
    #returns T/F if word is a palindrome
    return first_name(word) == first_name(word)[::-1]


def check_title(word): 
    #checks to see if the name contains a title
    #parameter: a name
    #returns T/F if name has a title

    title = ["Mr.", "Mrs.", "Dr.", "Sir", "Esq", "Ph.d", "Ms.", "Miss", "Lord", "Lady", "Dame", "Gen", "Lt. Gen", "Maj. Gen", "Capt."]
    for prefix in title: #for any of the given options (e.g. Mr., Mrs., etc.) in the list names "title"
        if prefix in word:
            return "True"
    return "False"

def sorted_array(word): 
    #changes the name into an array of characters in an alphabetical order
    #parameter: a name
    #returns name with letters in alphabetical order

    name = list(word)
    name.sort() 
    return ''.join(name) #returns word back into a string form

def len_name(word): 
    #determines the length of the word
    #parameter: a word
    #returns number of letters in word
    return len(word)

def format_name(word): 
    #displays name in last, first format
    #parameter: a name
    #returns name in "last name, first name" format
    return last_name(word) + "," + first_name(word)


if __name__ == '__main__':
        main()
