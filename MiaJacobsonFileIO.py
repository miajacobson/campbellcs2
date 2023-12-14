#Mia Jacobson
#CS1 File IO Assignment
#12/14
#Bugs: if a user adds to a record with inputs that dont make sense (letters for grade inquiry, etc.) it will not send an error message and add them to the new fle anyways
#Bugs: records added by the user do not alphebetize correctly in 7), rather they stay at the end where they were appended to
#Bugs: if there is more than one person with the same name in a given grade, the find a student function will print the first one in the record, and not the other subsequent one(s)
#Bonuses: Specs created: 1,2,3,4,5,6,7,9,9a,9b,10,10a,12
#Log: 1.0 - Created main      
#     1.1 - Added function 1
#     1.2 - Added functions 2,3,4
#     1.3 - Refined menu
#     1.4 - Added functions 5,6
#     1.5 - Added function 7
#     1.6 - Created a new file for add student function
#     1.7 - Added function 8-and tested/ debugged
#     1.8 - Documentation
#     1.9 - Changed open file to w+ from r+
#     2.0 - Changes import file type from a+ to a

import os                                                           #imports libraries for use in the code
from pathlib import Path

def main():

    current_dir = Path(__file__).parent
    file_path = current_dir / "gcds_data2.csv"

    file_in = open(file_path)

  
    while True:                                                     #creates infinity loop for menu below
        print("Menu: Enter Choice or 'Q' to (Q)uit:")
        print("1) Print All Student in Grade 12")
        print("2) Print Total Students who live in CT vs NY")
        print("3) Print All Students who live in Bedford")
        print("4) Print All Female students without a Middle Name")
        print("5) Find a student")
        print("6) Add a record")
        print("7) Print all students alplabetically by last name")
        print("8) Delete a Record")
    

        select = input("")                      #menu for inputs

        if select == '1':
            check_seniors(file_in)

        elif select == '2':
            state_count(file_in)

        elif select == '3':
            find_carpool(file_in)
        
        elif select == '4':
            female_middle(file_in)
      
        elif select == '5':
            find_student(file_in)
        
        elif select == '6':
            file_in = open(file_path,"a+")
            add_record(file_in)
            file_in = open(file_path,"r")

        elif select == '7':
            sort_last(file_in)
        
        elif select == '8':
            delete_record(file_in)

        elif select == 'Q':
             print("bye")
             break


def check_seniors(file_in):
    """
    Description: Finds all senior students in the data set
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(1)                                     #move pointer to line 1

    for record in file_in:                              #iterates through file looking for all females without a middle name
        kid = record.split(",")                         #breaks record of each kid into segments at each comma
        
        if kid[0] == '\n':                              #recognizes a blank row in the data set to avoid errors
            continue                                    #passes over blank line

        if kid[3] == "12":                              #checks file for the number 12 in the third slot of each record
            print(kid[0] + " " + kid[2])                #prints first and last name of senior
        

def state_count(file_in):
    """
    Description: Compares all students who live in New York Versus Connecticut
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(1)
    
    #creates counters for states
    ny_count = 0                                         
    ct_count = 0                                         
    
    for record in file_in:                                                #iterates through file looking for all females without a middle name
        kid = record.split(",")                                           #breaks record of each kid into segments at each comma
        
        if kid[0] == '\n':                                                #recognizes a blank row in the data set to avoid errors
            continue                                                      #passes over blank line

        if kid [8] == "NY":                                               #checks for NY in the 8th slot of every record   
            ny_count = ny_count +1                                        #adds 1 to the count of kids in ny
       
        if kid[8] == "CT":                                                #checks for CT in the 7th slot of record
            ct_count = ct_count +1                                        #adds 1 to the count of kids in ct
                                                                          
    print("NY" + ":" + str(ny_count))                                     #prints final count of students who live in NY
    print("CT" + ":" + str(ct_count))                                     #prints final count of students who live in CT
    
      
def find_carpool(file_in):
    """
    Description: Finds all students who live in the town of Bedford
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(1)                                       #move pointer to line 1

    for record in file_in:                                #iterates through file looking for all females without a middle name
        kid = record.split(",")                           #breaks record of each kid into segments at each comma

        if kid[0] == '\n':                                #recognizes a blank row in the data set to avoid errors             
            continue                                      #passes over blank line
        
        if kid[7] == "Bedford":                           #checks for Bedford in the 7th slot of record
            print(kid[0] + " " + kid[2])                  #prints first and last name of student


def female_middle(file_in):
    """
    Description: Finds all females without a middle name
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(0)                                     #move pointer to line 1

    for record in file_in:                              #iterates through file looking for all females without a middle name
        kid = record.split(",")                         #breaks record of one kid into segments at each comma    

        if kid[0] == '\n':                              #recognizes a blank row in the data set to avoid errors
            continue                                    #passes over blank line
        
        if kid[4] == "F" and len(kid[1]) == 1:          #checks for "F" to determine female, and checks for the length of the characters in the middle name column (lookd for 1 because of one space) to see if there is an empty space in middle name box of record
            print(kid[0] + " " + kid[2])                #prints name of female without a middle name


def find_student(file_in):
    """
    Description: Finds a student's last name using their first name and grade inputted by the user
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(1)                                                 #moves pointer to line 1
    
    #defines open variables for input from the user
    first_name = ""
    student_grade = ""
    
    #starts a counter
    counter = 0
    
    first_name = input("What is the first name of the student whose last name you would like to find?")                 #asks user for first name of student they are trying to find
    student_grade = input ("What is the grade of the student you are looking for? (PK, K, 1,2,3,4,5,6,7,8,9,10,11,12)") #asks user for grade of student they are trying to find

    for record in file_in:                                           #iterates through file looking for all females without a middle name 
        kid = record.split(",")                                      #breaks record of one kid into segments at each comma 
        
        if kid[0] == '\n':                                           #recognizes a blank row in the data set to avoid errors
            continue                                                 #passes over blank line
        
        if first_name.capitalize() == kid[0] and student_grade == kid[3]:         #checks to make sure name given by the user is in the data set
           
           print(kid[0] + "'s last name is: " + kid[2])                                             #prints last name of kid
           counter = counter + 1                                     #adds one to the counter to avoid moving to "elif counter == 0 statement"
           break                                                     #ends for loop
    
    if counter == 0:
        print ("Sorry, there is no student named " +  first_name + " in grade " + student_grade + "." ) #prints error statement


def add_record(file_in):
    """
    Description: Adds a record to the dats set
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(0)   #moves pointer to line 1

    add_kid = []      #creates an open variable for input from the user

    #routine to capture information to add a record
    add_kid.append(input("What is the first name of the student?"))
    add_kid.append(input("What is the middle name of the student?"))
    add_kid.append(input("What is the last name of the student? ") )
    add_kid.append(input("What is the grade of the student? ")) 
    add_kid.append(input("What is the sex of the student (F/M)? "))
    add_kid.append(input("Who is the students advisor? "))
    add_kid.append(input("What town does the student live in? "))
    add_kid.append(input("What state does the student live in (2 letter state abbreviation)? "))
    add_kid.append(input("What is the zip code of the student? "))

    #uses above information from user to write a new record, add it to the data set, and print
    file_in.write("\n" + add_kid[0] + "," +  add_kid[1] + "," + add_kid[2] + "," + add_kid[3] + "," + add_kid[4] + "," + add_kid[5] + "," + add_kid[6] + "," + add_kid[7] + "," + add_kid[8]) # \n pushes the following information to the next line down on the excel spreadsheet
    print("Record added!")

    file_in.close()


def sort_last(file_in):
    """
    Description: Sorts all students by last name
    Parameter: file_in: a pointer to an open file containing student data
    Returns: void

    """
    file_in.seek(0)                              #moves pointer to line 1
    
    for record in file_in:                       #iterates through file looking for all females without a middle name               
        kid = record.split(",")                  #breaks record of one kid into segments at each comma 
       
        if kid[0] == '\n':                       #recognizes a blank row in the data set to avoid errors
            continue                             #passes over blank line
        
        print(kid[2], ",", kid[0])               #prints student name in the format "last,first"


def delete_record(file_in):
        """
        Description: Deletes a record from the data set
        Parameter: file_in: a pointer to an open file containing student data
        Returns: void
        """

        if file_in.closed == False:                                                    #checks to see if file is closed                                             
            file_in.close()                                                            #if it is not closed, close it

        current_dir = Path(__file__).parent                                             
        f1 = current_dir / "gcds_data2.csv"
        file_one = open(f1, "r")                                                       #opens file one in read mode
        
        f2 = current_dir / "gcds_data_empty.csv"
        file_two = open(f2, "w")                                                       #opene file in write mode

        file_one.seek(0)                                                               #moves pointer to line 1

        #gets name
        fn_delete = input("What is the first name of the student you would like to delete?")
        ln_delete = input("What is the last name of the student you would like to delete?")


        found = False                                                                  #creats a true/false operation
        
        for record in file_one:                                                        #iterates through file looking for all females without a middle name
            kid = record.split(",")                                                    #breaks record of one kid into segments at each comma      
                   
            if kid[0] == '\n':                                                         #recognizes a blank row in the data set to avoid errors
                continue                                                               #passes over blank line

            if fn_delete == kid[0] and ln_delete == kid[2]:                             #checks if name given by user is in data set
                found = True
                continue
            else:
                file_two.writelines(record)                                             #write everybody out BUT the kid to the empty file
    
        if found == True:
            print (print(f"{fn_delete}" + " " + f"{ln_delete}" + " " + "deleted!"))     #prints the first and last name of the deleted record
        else:
            print("Cannot delete because student is not listed.")                       #prints an error statement letting the user know the student they entered is not in the data set, and therefore cannot be deleted

        file_one.close()                                                                #closes original file                                      
        file_two.close()                                                                #closes new file
        
        os.remove(f1)                                                                   #deletes original file
        os.rename(f2, f1)                                                               #renames new file to the name of the original file


if __name__ == '__main__':
    main()


