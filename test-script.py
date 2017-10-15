

def List_Rules(): #{{{{
    """Function to List IPtables  rules for IPv4/6."""
    
    ipv6 = "./ipv6.txt"
    ipv4 = "./ipv4.txt"
    
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
    
    #system call to save ipv6tables to file.
    system("sudo ip6tables -L --line-number >" + ipv6)
    
    #system call to save ipv4 tables to file.
    system("sudo iptables -L --line-number >" + ipv4)
    
    
    #Read and format ipv4/6.txt files saved previously. 
    
    with open(ipv6) as file_object:
        lines = file_object.readlines()
        print("\n" + "=" * 32 + "\nIPV6 Rules\n" + "=" * 32)
        for line in lines: 
            if line[0].isdigit():
                print(line.rstrip())
            
            else:
                term = ("chain","num")  
                string_iterate(term, line)
    
    with open(ipv4) as file_object:
        lines = file_object.readlines()
        print("\n" + "=" * 32 + "\nIPV4 Rules\n" + "=" * 32)
        for line in lines: 
            if line[0].isdigit():
                print(line.rstrip())
            
            else:
                term = ("chain","num")  
                string_iterate(term, line)
#}}}
