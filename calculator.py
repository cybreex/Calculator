# Coded by Yusuf Kibar
# .-. coding: utf-8 .-.

import colorama
from colorama import Fore
colorama.init()

while True:
  
  print(Fore.GREEN + """
  -------------------------
  | Instagram: @ysufkibar |
  -------------------------
  | 1-)Collection         |
  | 2-)Extraction         |
  | 3-)Impact             |
  | 4-)Division           |
  | 5-)Exit               |
  -------------------------
                    """)

  process = input(Fore.GREEN + ">> Select: ")

  if (process == '1'):
    number1 = int(input(Fore.GREEN + ">> Number 1: "))
    number2 = int(input(Fore.GREEN + ">> Number 2:  "))
    conclusion1 = number1 + number2
    print(Fore.BLUE + ">> " + str(conclusion1))
    break
    
  if (process == '2'):
    number1 = int(input(Fore.GREEN + ">> Number 1: "))
    number2 = int(input(Fore.GREEN + ">> Number 2: "))
    conclusion2 = number1 - number2
    print(Fore.BLUE + ">> " + str(conclusion2))
    break

  if (process == '3'):
    number1 = int(input(Fore.GREEN + ">> Number 1: "))
    number2 = int(input(Fore.GREEN + ">> Number 2: "))
    conclusion3 = number1 * number2
    print(Fore.BLUE + ">> " + str(conclusion3))
    break

  if (process == '4'):
    number1 = int(input(Fore.GREEN + ">> Number 1: "))
    number2 = int(input(Fore.GREEN + ">> Number 2: "))
    conclusion4 = number1 // number2
    print(Fore.BLUE + ">> " + str(conclusion4))
    break

  if (process == '5'):
    print(Fore.YELLOW + ">> Good Bye!")
    break
  
  else:
    print(Fore.RED + ">> Please enter a valid option!")
