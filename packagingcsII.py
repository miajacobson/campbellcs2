#GCDS Rush Removal: Post Office Assignment
#Mia Jacobson
#Due 9/30/23
def main():                                                                                          #defines main function
    print ("hi! welcome to the post office!")                                                        #prints welsome message 
    length = int(input("What is the length of your package in inches?"))                             #asks user for length of their item
    height = int(input("What is the height of your package in inches?"))                             #asks user for height of their item
    width = float(input("What is the thickness of your package in inches?"))                         #asks user for width of their item
    initialzip = int(input("What is the zip code of the place you are sending your package from?"))  #asks user for zip of place where sending from
    finalzip = int(input("What is the zip code of the place you are sending your package to?"))      #asks user for zip of place where sending to

    pkg_type = getsize(length, height, width)                                   #this is for dimensions of package
    total_travel = abs(getzip(initialzip) - getzip(finalzip) )                  #this is for zip codes
    cost = calculate(pkg_type, total_travel)                                    #this takes the package type and total travel distance and tells you the final cost

    print (total_travel)                                                         #prints amount of zones package has to travel thru 
    print ("the package type is:" + pkg_type)                                    #prints the type of packaging item will need
    print ("the package cost is:" + "$" + str(cost))                                    #prints total cost customer owes
 
def getsize(length, height, width):                                              #calls getsize function

    if (length >= 3.5 and length <= 4.25) and (height >= 3.5 and height <= 6) and (width >= .007 and width <= .016):             #this is requirements for a regular post card
        return "regular pc"                                                                                                      #returns label regular post card
    elif (length > 4.25 and length < 6) and (height > 6 and height < 11.5) and (width >= .007 and width <= .015):                #this is requirements for a large post card
        return "large pc"                                                                                                        #returns label large post card
    elif (length >= 3.5 and length <= 6.125) and (height >= 5 and height <= 11.5) and (width > .016 and width < .25):            #this is requirements for envelope
        return "envp"                                                                                                            #returns label regular envelope
    elif (length > 6.125 and length < 24) and (height >= 11 and height <= 18) and (width >= .25 and width <= .5):                #this is requirements for large envelope
        return "large envp"                                                                                                      #returns label large envelope
    elif (((length > 24) or (height > 18) or (width > .5)) and (length + length + width + width + height + height <= 84)):                         #this is the requirements for a  pgk
        return "pkg"                                                                                                             #returns label pkg
    elif (((length > 24) or (height > 18) or (width > .5)) and ((length + length + width + width + height + height > 84) and (length + length + width + width + height + height <= 130))):#this is the requirements for a lg pgk
        return "lg pkg"                                                                                                          #returns label for lg pkg
    else:                                                                                                                        #if none of these perameters work, do the following
        return "Sorry! This is unmailable."                                                                                      #tell user their package is not mailable


def getzip(zip):                         #calls getzip function
    if zip >= 1 and zip<= 6999:          #defines first zip zone
        return 1                         #returns zone number 1
    elif zip >= 7000 and zip <= 19999:   #defines second zip zone
        return 2                         #returns zone number 2
    elif zip >= 20000 and zip <= 35999:  #defines third zip zone
        return 3                         #returns zone number 3
    elif zip >= 36000 and zip <= 62999:  #defines fourth zip zone
        return 4                         #returns zone number 4
    elif zip >= 63000 and zip <= 84999:  #defines fifth zip zone
        return 5                         #returns zone number 5
    elif zip >= 85000 and zip <= 99999:  #defines sixth zip zone
        return 6                         #returns zone number 6
    

def calculate(postage_class, zone_travel):        #calls getzip function
                            
    if postage_class == "regular pc":             #deals with regular post card class after it is defined
        cost = .20 + .03 * zone_travel            #defines cost function for reg pc
    elif postage_class == "large pc":             #deals with large post card class after it is defined
        cost = .37 + .03 * zone_travel            #defines cost function for large pc
    elif postage_class == "envp":                 #deals with envelope class after it is defined
        cost = .37 + .04 * zone_travel            #defines cost function for envp
    elif postage_class == "large envp":           #deals with large envelope class after it is defined
        cost = .60 + .05 * zone_travel            #defines cost function for lg envp
    elif postage_class == "pkg":                  #deals with package class after it is defined
        cost = 2.95 + .25 * zone_travel           #defines cost function for pkg
    elif postage_class == "lg pkg":            #deals with large package class after it is defined
        cost = 3.95 + .35 * zone_travel           #defines cost function for lg pkg
    return cost                                   #tells user final cost to mail their package
    
if __name__ == '__main__':
    main()




