#Pet store program
#All ASCII art obtained from: 
#(ascii art nets) all credit rightfully goes to the them for the pets!
import os
import sys
from termcolor import colored
import time
import random

def print_slow(str, interval = 0.03):
    for letter in str:
        #print(letter, end='')
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(interval)
    print('')

def pet_play(pet):
  print(pet)

doggo = """
          __
 \ ______/ V`-,
  }        /~~
 /_)^ --,r'
|b      |b
"""



cato = """
  ^~^  ,
 ('Y') )
 /   \/ 
(\|||/)
"""


fish = """
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `**´´\¸.·´
"""



penguino = """
   .-.
  /'v'\
 (/   \)
 """




bluejay = """
   /""\      ,
   <>^  L____/|
    `) /`   , /
     \ `---' /
      `'";\)`
        _/_Y
"""




chick = """
  ,~
 ('v)__
(/ (``/
 \__>' 
  ^^
"""





osospecial = """
     (()__(()
     /       \ 
    ( /    \  \
     \ o o    /
     (_()_)__/ \ 
    / _,==.____ \
   (   |--|      )
   /\_.|__|'-.__/\_
  / (        /     \ 
  \  \      (      /
   )  '._____)    /    
(((____.--(((____/
"""




hamster = """
  .     .
            (>\---/<)
            ,'     `.
           /  o   o  \
          (  >(_Y_)<  )
           >-' `-' `-<-.
          /  _.== ,=.,- \
         /,    )`  '(    )
        ; `._.'      `--<
       :     \        |  )
       \      )       ;_/  hjw
        `._ _/_  ___.'-///
           `--///
"""


store = """
          __/_\__
         /\-'o'-/\
        _||:<_>:||_
       /\_/=====\_/\
      _|:_:_[I]_:_:|_
   _/::::::::::::::::\_
 _/::::::::::::::::::::\_
/::::::::::::::::::::::::\
"""
feeling = random.choice(["nausy","sad","happy","joyous","angry","nervous","fearful"])
inventory = []
total_exp = 0
name = input(colored("What is your name? ","cyan"))
print_slow(colored("Nice to meet you "+name,"green"))
print_slow(colored("Lets go get a pet!","yellow"))
print_slow(colored("Hooray! We made it to the pet store!","red"))
print(colored(store,"cyan"))
print_slow("Which pet should we get?")
time.sleep(1.5)
print_slow(colored("Looks like the pets they have in stock are \n\t\tHamster,Bear,Chick,Dog,Cat,Fish,Bluejay,Penguin","yellow"))
time.sleep(1.5)
print_slow(colored("Wait a second don't penguins live in the artic?!","magenta"))
print_slow(colored("HMMMMMMMMMMMMMMMMMMMMMMMM","blue"))
pet = input(colored("So which one will you choose? ","green"))
pet = pet.lower() #All lower case
good_choice = True
if pet == "bear" :
  choice = pet_play(osospecial)
elif pet == "hamster" :
  choice = pet_play(hamster)
elif pet == "chick" :
  choice = pet_play(chick)
elif pet == "bluejay" :
  choice = pet_play(bluejay)
elif pet == "penguin" :
  choice = pet_play(penguino)
elif pet == "fish" :
  choice = pet_play(fish)
elif pet == "cat" :
  choice = pet_play(cato)
elif pet == "dog" :
  choice = pet_play(doggo)
else : #Invalid pet choice
  print("Pet not found, sorry!")
  good_choice = False

while good_choice:
  exp = random.choice([64, 27, 98, 24, 372, 94, 32])
  print_slow("0. Stop playing")
  print_slow("1. Play with your pet ")
  print_slow("2. Feed your pet ")
  print_slow("3. Give your pet water ")
  print_slow("4. Shop")
  print_slow("5. Give your pet belly rubs ")
  print_slow("6. Check your pets feeling")
  print_slow("7. Inventory")
  print_slow("8. Check experience")
  choice = input(colored("What do you want to do? ","green"))

  if choice == "0":
    break
  elif choice == "1" :
    print_slow(colored(f"You got {exp} exp for playing with your pet!","blue"))
    total_exp += exp
  elif choice == "2":
    print_slow(colored("You fed your pet some food!","red"))
  elif choice == "3":
    print_slow(colored("You fed your pet some water!","cyan"))      
  elif choice == "4":
    print_slow("Here you can get some food and water for your pet!")
    time.sleep(1.5)
    if total_exp > 50 :
      print_slow(colored("You got some food!","yellow"))
      inventory.append("food")
    if total_exp < 50 :
      print_slow(colored("Not enough exp to get food!","yellow"))
      inventory.append("food")
    if total_exp > 30 :
      print_slow(colored("You got some water!","red"))
      inventory.append("water")
    if total_exp < 30 :
      print_slow(colored("Not enough money to get water!"))
  elif choice == "5":
    print_slow(f"Your pet enjoyed your rub (You got {exp} exp from giving your pet belly rubs)")
    total_exp += exp
  elif choice == "6":
    print_slow(f"Your pet is feeling {feeling} today.")
    print_slow("Maybe try feeding,giving water,belly rubs,etc. so your pet can be happy.")
  elif choice == "7":
    print_slow(f"{', '.join(inventory)}") 
  elif choice == "8":
    print_slow(f"EXP = {total_exp}")
