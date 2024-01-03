from colorama import Fore, Style, init
init(convert=True)
import requests
import time
import threading
import os

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
white = Fore.WHITE


def rinfybot():
    print(fr"""{red}
         _       ____      __         __ 
   _____(_)___  / __/_  __/ /_  ____  / /_
  / ___/ / __ \/ /_/ / / / __ \/ __ \/ __/
 / /  / / / / / __/ /_/ / /_/ / /_/ / /_  
/_/  /_/_/ /_/_/  \__, /_.___/\____/\__/  
                 /____/                   """)

rinfybot()
user = input(fr"{red}Enter a user:{white} ")
token = input(fr"{red}ENTER TOKEN: ")
print(f"USER: {user}")
print(f"KEY: {token}")
start = fr"{green}{user}{white}@{green}root{white}~${white}"
input = input(start )
if input in ["1", "01"]:
    print(fr"{red} FIRE IN THE HOLE")
    print(fr"{red} FIRE IN THE HOLE")
    print(fr"{red} FIRE IN THE HOLE")
    print(fr"{red} FIRE IN THE HOLE")
    headers = {
            "Authorization": token,
            "Content-Type": "application/json"
    }
    data = {"content": "FIRE IN THE HOLE (testing rinfybot)"}
    while True:
        time.sleep(0.3)
        test = requests.post("https://discord.com/api/v9/channels/1183198912153133130/messages", headers=headers, json=data)
        print(fr"{red} FIRE IN THE HOLE")
