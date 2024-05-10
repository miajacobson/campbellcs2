#Mia Jacobson
#CS2 - "Recursive Algorithms"
#Description: This assignment takes in a single number from the user. It then prompts the user to choose a recursive manipulation to act upon the number.
#5/8/24
#Manipulations Included: 1, 2, 4, 5, 7

def main():
#main function

    number = int(input("Please enter a number to manipulate."))


    while True:#menu for inputs
        print("Enter a number... or 'Q' to (Q)uit:")
        print("1) Find the factorial of your number.")
        print("2) Find the summation of your number.")
        print("3) Find the value of the nth term in the Fibbonaci sequence.")
        print("4) Find the product of two whole numbers.")
        print("5) Find the sum of the digits of your number.")


        select = input() #calling corresponding function based on user's number choice

        if select == '1':
            print("The factorial of your number" , "(" , number , ")", "is" , calculate_factorial(number), ".")
        
        elif select == '2':
            print("The summation of your number" , "(" , number , ")", "is" , calculate_summation(number), ".")
        
        elif select == '3':
            print("The", number , "nd/rd/th", "term in the Fibbonaci sequence is" , calculate_fibbonaci(number - 1), ".")
        
        elif select == '4':
            a = int(input("Enter an integer."))
            b = int(input("Enter a second integer."))
            print("The product of these numbers is", product_two_whole(a,b), ".")
        
        elif select == '5':
            print("The sum of the digits of your number ", "(" , number , ")", "is", sum_of_digits(number), ".")
        
        elif select == 'Q':
            print("bye!")
            break

        else: #dangling else for all non-valid inputs
            print("Invalid response. Please select an integer between 1 and 3, or type 'Q' to quit. ")


def calculate_factorial(number):
    #calculates factorial of a number
    #parameter: a number
    #returns factorial of inputted number
    if number > 0:
        return number*(calculate_factorial(number-1))
    elif number == 0:
        return 1
    else:
        print("Factorial cannot be calculated because your number it is less than 0.")
    

def calculate_summation(number):
    #calculates summation of a number
    #parameter: a number
    #returns summation of inputted number
    if number > 0:
        return number + (calculate_summation(number-1))
    elif number == 0:
        return 0
    else:
        print("Summation cannot be calculated because your number is less than 0.")
        

def calculate_fibbonaci(number):
    #calculates the value of the nth term in the fibbonacci sequence, with n being the number in putted by the user
    #parameter: a number
    #returns value of nth term
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number > 1:
        return calculate_fibbonaci(number-1) + calculate_fibbonaci(number-2)
            
    else:
        print("Fibbonaci cannot be calculated because your number is less than 0.")


def product_two_whole(a,b):
    #calculates the product of two whole numbers
    #parameter: two numbers inputted by the user
    #returns the product of the two inputted numbers
    if b > 0:
        return a + product_two_whole(a,b-1)
    elif b == 0:
        return 0


def sum_of_digits(number):
    #calculates the sum of the digits of a number
    #parameter: a number
    #returns factorial of inputted number
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number//10)


    
if __name__ == '__main__':
        main()