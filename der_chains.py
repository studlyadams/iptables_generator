#test for derive function


from subprocess import call
from sys import exit
from os import system


from functions import *


def der_chain():
    """function to add chains to chain list. """
    
    ipv=("./ipv6.txt","./ipv4.txt")

    iptofile()

    chain_dict=[]

    for type in ipv:
        with open(type) as file_object:
            lines = file_object.readlines()
            

        for line in lines:        
            if "chain" in line.lower():
                word = ""
                input(line)
                for value in range(6,len(lines)):
                    if line[value] == " ":
                        chain_dict.append(word)
                        break
                    else:
                        word += line[value]

    return chain_dict





