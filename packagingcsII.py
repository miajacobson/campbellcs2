#GCDS Rush Removal: Post Office Assignment
#Mia Jacobson
#Due 9/30/23

for x in range (0,5):
        
    def main(): #calls main function
        #variables below are defined
        data = input("").split(",")
        length = float(data[0])                                                                        
        height = float(data[1])                                                                          
        width = float(data[2])                                                                          
        initialzip = int(data[3])                                                                      
        finalzip = int(data[4])                                                                          

        #calls functions
        pkg_type = getsize(length, height, width)                                   
        total_travel = abs(getzip(initialzip) - getzip(finalzip) )                  
        cost = calculate(pkg_type, total_travel)                                  
        cost = str(cost)
        cost = "{:.2f}".format(float(cost))
        cost = cost.lstrip("0")
        print (cost)                                                               
    
    def getsize(length, height, width):    
        #getsize - returns an integer representing correct package type
        #zip - parameter holding package type requirements to determine
        #returns proper package type based on passed parameter
        
        #routine below determines package type                                        
        if (length >= 3.5 and length <= 4.25) and (height >= 3.5 and height <= 6) and (width >= .007 and width <= .016):             
            return "regular pc"                                                                                                      
        elif (length > 4.25 and length < 6) and (height > 6 and height < 11.5) and (width >= .007 and width <= .015):              
            return "large pc"                                                                                                       
        elif (length >= 3.5 and length <= 6.125) and (height >= 5 and height <= 11.5) and (width > .016 and width < .25):            
            return "envp"                                                                                                          
        elif (length > 6.125 and length < 24) and (height >= 11 and height <= 18) and (width >= .25 and width <= .5):                
            return "large envp"                                                                                                      
        elif (((length > 24) or (height > 18) or (width > .5)) and (length + length + width + width + height + height <= 84)):                       
            return "pkg"                                                                                                             
        elif (((length > 24) or (height > 18) or (width > .5)) and ((length + length + width + width + height + height > 84) and (length + length + width + width + height + height <= 130))):
            return "lg pkg"                                                                                                        
        else:                                                                                                                        
            return "Sorry! This is unmailable."


    def getzip(zip):   
        #getzip - returns an integer representing a zone
        #zip - parameter holding zip code to determine
        #returns proper zone based on passed parameter
        
        #routine below determines a zone
        if zip >= 1 and zip<= 6999:         
            return 1                         
        elif zip >= 7000 and zip <= 19999:   
            return 2                        
        elif zip >= 20000 and zip <= 35999: 
            return 3                         
        elif zip >= 36000 and zip <= 62999: 
            return 4                         
        elif zip >= 63000 and zip <= 84999:  
            return 5                         
        elif zip >= 85000 and zip <= 99999: 
            return 6                         
        

    def calculate(postage_class, zone_travel): 
        #calculate - returns an integer representing a cost
        #postage_class, zone_travel - parameters holding cost to determine
        #returns proper cpst based on passed parameter
        
        #routine below determines a cost                                
        if postage_class == "regular pc":             
            cost = .20 + .03 * zone_travel           
        elif postage_class == "large pc":            
            cost = .37 + .03 * zone_travel          
        elif postage_class == "envp":               
            cost = .37 + .04 * zone_travel           
        elif postage_class == "large envp":          
            cost = .60 + .05 * zone_travel         
        elif postage_class == "pkg":                 
            cost = 2.95 + .25 * zone_travel        
        elif postage_class == "lg pkg":               
            cost = 3.95 + .35 * zone_travel           
        return cost                               
        
    if __name__ == '__main__':
        main()
