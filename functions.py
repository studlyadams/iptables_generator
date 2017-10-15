#functions.py

from subprocess import call
from menu_content import * 
from sys import exit
from os import system

#universal aliases:
admin="sudo "
v4=" iptables "
v6=" ip6tables "
flush = " -F "
shownumbers = " --line-numbers "
delete = " -D "
Input = " INPUT "
Output = " OUTPUT "


def not_implemented(): #{{{
    '''Prints message when function has not yet been
       implemented'''

    input("\nFunction not Implemented yet.\n"\
            +"-- Press Enter to Continue. --"
            )
    pass
#}}}

def iptofile(): #{{{
    ipv6 = "./ipv6.txt"
    ipv4 = "./ipv4.txt"

    system("sudo iptables -L --line-number >" + ipv4)
    system("sudo ip6tables -L --line-number >" + ipv6)
#}}}

def derive_chain(ipv): #{{{
    """function to add chains to chain list. """
    
    if ipv == "ipv4":
        Cfile="./ipv4.txt"
    else:
        Cfile="./ipv6.txt"

    iptofile()
    chain_dict=()
    with open(Cfile) as file_object:
        lines = file_object.readlines()

        for line in lines:        
            if "chain" in line.lower():
                word = ""
                for value in range(6,len(lines)):
                    if line[value] == " ":
                        chain_dict.append(word)
                        break
                    else:
                        word += line[value] 

    print("chains = ",chain_dict)
    input(" ")
    return chain_dict
#}}}

def List_Rules(ipv="both"): #{{{ 
    
    """Function to List IPtables  rules for IPv4/6."""
    
    ipv6 = "./ipv6.txt"
    ipv4 = "./ipv4.txt"
    term = ("chain","num")     
    
    def string_iterate(term,line):
        #create a container to hold the contents of each word in the line. 
        word = ""
        #cycle through each letter in line. 
        for letter in line:
            #if letter is a space, compare word to term list, if True print the line and break the sequence.
            #if not, clear word and continue.
            if letter == " ":
                if word.lower() in term:
                    print("\n" + line.rstrip())
                    word = ""
                    break
                else:
                    word = ""
                    pass
            #if letter is not a space, add letter to the word container and continue.
            else:
                word += letter
                pass
    #save iptables list for v4 and v6 to a file
    iptofile()

    #system call to save ipv6tables to file.
    if ipv == "ipv6" or ipv == "both":
        
        with open(ipv6) as file_object:
            lines = file_object.readlines()
            print("=" * 32 + "\nIPV6 Rules\n" + "=" * 32)
            
            #iterate through each line, print if first character is a number, or if the line contain a 
            #word listed in "term"
            for line in lines: 
                if line[0].isdigit():
                    print(line.rstrip())
                else:
                    string_iterate(term, line)
    
    #system call to save ipv4 tables to file.
    if ipv == "ipv4" or ipv == "both":
 
        with open(ipv4) as file_object: 
            lines = file_object.readlines() 
            print("=" * 32 + "\nIPV4 Rules\n" + "=" * 32)

            for line in lines: 
                if line[0].isdigit():
                    print(line.rstrip())                
                else:
                    string_iterate(term, line)
        
    
    
    
#}}}

def Get_Column_Width(dict,preamble=3): #{{{
    
    """Function used to calculate the proper column width
       Based on the length of the longest "key + value" in a 
       dictionary plus preamble(defaultsize of 3). """
    
    longest=0
    
    for key,value in dict.items():
        #run through dictionary and compare string lengths.
        current_test_value = len(key) + len(value)
        if current_test_value > longest:
            longest = current_test_value
        else:
            pass
    
    max_width = longest + preamble
    print(max_width)
    return max_width
#}}}

def Clear_Screen(): #{{{
  
    """Function to clear the screen"""

    call(['echo', '-en',"\ec"]) 

#}}}

def List_Menu(dict): #{{{
    
    """Function to list out menu items stored in
    a Dictionary. """
    
    border = "="
    sides="|"
    preamble = 3
    width = Get_Column_Width(dict,preamble)
    top_bottom = (border * (width+1))
    left_bookend=(sides * (preamble - 2)+" ")
    
    print("\n\n")
    print(top_bottom)
    
    for index, key in sorted(dict.items()) :
        right_bookend =(\
                " " *   
                (width - (len(index) + len(left_bookend)
                   + len(key))) + sides)

        print(left_bookend + index + key + right_bookend)
        #print(line)
    print(top_bottom)
    
#}}}

def clear_iptables(input): #{{{
    #Define iptables command to be called in next logic flow.
   
    flushv4 = admin + v4 + flush
    flushv6 = admin + v6 + flush

    if input == "all":
        #run system call to clear all rules 
        system(flushv4)
        system(flushv6)
    elif input == "v4":
        #run system call to clear ipv4 rules only
        system(flushv4) 
    elif input == "v6":
        #run system call to clear ipv6 rules only
        system(flushv6) 
    else:
        not_implemented()

#}}}

def clear_by_number(ipv): #{{{
    
    while True: 
        #Blank variables used in function. 
        direction = ""
        number = ""
        user_chain=""
        #clear screen
        Clear_Screen()

        #List Rules:
        List_Rules(ipv)
        
        chains = ""
        #define possible directions.
        chain_list=derive_chain()
        for chain in chain_list:    
            if chain == chain_list[0]:
                chains += chain 
            else:
                chains += ", " + chain

        #Prompt user about direction. compare answer to direction list to ensure the correct answer is given.  
        while user_chain.lower() not in chain_list:
            #Clear screen
            Clear_Screen()
            
            #list rules
            List_Rules(ipv)
            
            #prompt user
            user_chain = input("press q to exit.\n\n" + "[" + chains + "]: ")
            
            
            #define break trigger.
            if direction == "q":
                return 

            #capitalize direction for use in command. 
            direction = direction.upper()
        
            #Prompts user for rule number
   
        while number.isnumeric() == False:
            
            #clear screen. 
            Clear_Screen()
            
            #list rules
            List_Rules(ipv)
           
            #prompt user
            number=input("\nType q to return.\n\nWhich rule #?: ")
            
            #define break trigger.
            if number == "q":
                return
        
        #Inform the user what is going to be done next.
        answer=input("\
                \nwe're going to remove the " + ipv + " rule, #" + number\
                + " from the " + direction \
                + " Chain.\n\nPress Y to continue, press N to return.: ")
        
        #check users answer to continue or cancel.  
        if answer.lower() == "n":
            return                
        elif answer.lower() == "y":
            pass
        
        #Process IPv4 command. 
        if ipv == "ipv4":
            command = admin + v4 + delete + direction + " " + number
            system(command)
        
        #Process IPv6 command.
        elif ipv == "ipv6":    
            command = admin + v6 + delete + direction + " " + number
            system(command)
        
    #}}}

