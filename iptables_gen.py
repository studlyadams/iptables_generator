#iptables-generator.py

from subprocess import call
from functions import *
from menu_content import *

menus= Menus()
current_menu = menus.First_Menu

#Beginning of main loop.
while True:
    
    #Clear Screen {{{
    Clear_Screen()
    #}}}

    #Relist Rules {{{
    List_Rules()
    #}}}
    
    #display menu of available actions. {{{
    List_Menu(current_menu)
    #}}}

#Get user input. {{{

#Prompt user for input. 
    answer = input("Choose an option: ")

#}}}

    #derive action based on answer from user. {{{

    if current_menu == menus.First_Menu: 
        if answer == "1":
            List_Rules()
        elif answer == "2":
            current_menu = menus.clear_rules
        elif answer == "3":
            call(["sudo","./scripts/iptables_script.sh"])
        elif answer == "4":
            Clear_Screen()
            quit()
    
    
    elif current_menu == menus.clear_rules: 
        if answer == "1":
            clear_iptables("v4") 
        elif answer == "2":
            clear_iptables("v6")
        elif answer == "3":
            clear_by_number("ipv4")
        elif answer == "4":
            clear_by_number("ipv6")
        elif answer == "5":
            clear_iptables("all")
        elif answer == "6":
            current_menu = menus.First_Menu
        elif answer == "7":
            Clear_Screen()
            quit()
        
   
    #}}}

#}}}
