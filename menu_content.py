#menu_content.py

from functions import *

class Menus: 
    """Class to store menu dictionaries."""
    
    def __init__(self):

       #initial menu. {{{
        self.First_Menu = First_Menu={
               "1. " : "Refresh Page",
               "2. " : "Clear Rules",
               "3. " : "run premade script",
               "4. " : "quit"
               } #}}}
        
        #Clear Rules Menu. {{{
        self.clear_rules = clear_rules={
                "1. " : "clear IPv4 rules",
                "2. " : "clear ipv6 rules",
                "3. " : "clear ipv4 rule by number",
                "4. " : "clear ipv6 rule by number",
                "5. " : "clear all rules",
                "6. " : "return",
                "7. " : "quit"
                } #}}}



