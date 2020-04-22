# HEYYYYYYYYYYYYYYYYYYYY GUYS! Please check out my repls!                        -Pythonmaster24, Editor of Room 3, creator of choice 7, 8, and 9

import time, random
# This is the Text Base Game!

items = []

def intro():
    print("Welcome to the silent staring game")
    time.sleep(2)
    print("A game where nothing happens, silently")
    time.sleep(2)
    print('''
    You have nine choices:
    Press 1 for Room 1
    Press 2 for Room 2
    Press 3 to shriek like a dinosaur
    Press 4 to hear a joke
    Press 5 to think and wonder
    Press 6 to grab the pikaxe leaning against the wall
    Press 7 to die
    Press 8 to take a chance
    Press 9 to knock against the tungsten doors with the titanium knockers
    Press 10 to jump into the portal
  ''')
    choice = input("Please enter a choice ")
    choice = int(choice)
    
    if choice == 1:
        print("you enter the cat room")
        room1()
    elif choice == 2:
        print("You decide to go to room2")
        room2()
    elif choice == 3:
        print("You decide to go to scream like a dino")
        time.sleep(1)
        room3()
    elif choice == 5:
        print("How? You figured out my secret! I can't have people learning about this. I'm sorry, but I must kill you.")
        choice()
    elif choice == 6:
        print("You grabed the pikaxe and it turns into a hat. You put it on nothing happens but it looks cool (because it is a fez all fezs are cool!)")
        choice()
    elif choice == 7:
      room7()
    elif choice == 8:
      print("You took a chance and died. But before you died, you find a portal! You have no choice but to go into the portal unless you choose to go into hell. (P/H Portal or Hell respectively)")
      choice = input("Portal or Hell (P/H)?")
      if choice == "P":
        mayaintro()
      else:
        die()
        choice()
    elif choice == 4:
        print("You decide to go to the joke room")
        time.sleep(2)
        print("There has never been, nor will there be anything more funny than this amazing joke")
        time.sleep(1)
        room4()
    elif choice == 9:
      furyfire()
    elif choice == 10:
      print("You jumped into a portal.")
      time.sleep(2)
      mayaintro(items)

def room1():
    print("This is room 1 aka cat room")
    print("You find a bunch of Cats that want to snuggle and give you a home. Do you accept their gifts? y/n ")
    choice = input("Pick an option ")
    time.sleep(2)
    if choice == 'y':
        print("You feel better and one of the cats wants to join you in exploring the world")
        print("You explore the world and during the epic world exploration you defeat evil madmen, warlords, Evil Dragons, Evil Empires, and have an epic life. After a long time, it comes to an end. You feel fufilled with your life.")
    else:
        print("The cats are sad and do not wear their smiles any more. They will become depressed and will be forever sad. You are a terible person! A cat God comes and takes you to cat hell and you are stuck there forever. YOU DIED (and you deserved it)!")  
    intro()


def room2():
    print("This is the room2")
    print("you look around the room, noticing that there is nothing down there but a single lonesome dog")
    print("Choice 1: go and prt the dog")
    print("Choice 2 ignore the dog")
    choice = input("what will you do")
    if choice == 1:
        print("the dog turns out tou be a rabid MONSTER, it instantly kills you")
        intro()
    elif choice == 2:
        print("you ignore the dog and you see a door")
        print("Option 1 go through the door")
        print("Option 2 go back and pet the dog")
        choice = input("what do you do now")
        if choice == 1:
          ("you go into the door, it leads to where you started")
          intro()
        else:
            ("the dog does a dance and takes you to a room")
            time.sleep(2)
            room4()
            # #import turtle
            # my_turtle = turtle.Turtle()
            # def square():
            #     y=90
            #     x=100
            #     my_turtle.forward(x)
            #     my_turtle.right(y)
            #     my_turtle.forward(x)
            #     my_turtle.right(y)
            #     my_turtle.forward(x)
            #     my_turtle.right(y)
            #     my_turtle.forward(x)
            # for x in range (399):
            #     square()
            #     my_turtle
      
    
# WIAT username1233 you need to use python with turtle I'm telling you It's going to crash MARK MY woRDS IT IS GOING TO CRASH

      
    # Who are you, username 1233
    #somebody
    # somebody who is secretive, that's for sure. Andrew? Or who tell me plz
def room3():
    print("This is the room3")
    time.sleep(2)
    print("Why would you do that, anyway?")
    time.sleep(1)
    print("You thought that nobody would hear it. ")
    print("Pretty stupid of you, really, since you should have noticed that nothing ever goes your way here. ")
    time.sleep(1)
    print("WELCOME TO THE VOLCANO DUNGEON. A voice booms from behind you.")
    time.sleep(2)
    print("You find that you have some items with you.")
    time.sleep(2)
    print("What do you do? You can: ")
    print("1. Use your concealed Dynamite and TNT pack to blow the room up and hope you don't die")
    print("2. Fight the crazy donkey-man that has sneaked up behind you")
    print("3. Wait")
    
    choice = input("What do you choose? ")
    if choice == 1:
        blowup()
    elif choice == 2:
      print("The donkey man explodes when you hit him. You find yourself in a room. ")
      room2()
    else:
        print("You wait for them to attack. But you end up waiting for you whole life. When you are about to die, you realize that that was animation and you really had been waiting for nothing. The End. ")
        time.sleep(5)
        print("JUST KIDDING! You are reincarnated and start over. ")
        time.sleep(2)
        intro()

    
def blowup():
    print("That actually worked. You blew them up, distracting them. Instead of hitting you, it was deflected thanks to the sweet Grand Dragon Lord armor that you got. ")
    time.sleep(3)
    print("1. You run away while they're distracted")
    print("2. You strike as many of them as you can with your Iceburn Volcanic Frost Sword of Destiny(where did you get that, anyway?)")
    print("3. Stop to pet the cat that appeared next to you")
    print("4. Chase the apparation that appears to have magical powers")
    choice = input("What do you choose? ")
    if choice == 4:
      puppo()
    if choice == 3:
      print("It growls, snatches you, and pulls you to a different room. ")
      room1()
    if choice == 1:
      print("You run away and escape. You live a contented life and die with no regrets.")
      room7()
    else:
      print("You kill as many as you can. After you kill a particularly weird looking one, your sword slips from your hand. Dang. But you realize that you are still holding the handle, and the blade has slipped. The blade punctures a Zombie Night and you find that the blade has regenerated. The largest jewel of the many encrusted on the Sword shines brightly. What do you do?")
      time.sleep(2)
      print('''You can:
      1. Push the jewel
      2. Keep mowing down zombies
      3. Die''')
      choice = input("Enter an answer: ")
      if choice == 1:
        print("You push the jewel. The sword transforms into a bow. On it is engraved symbols that you translate to The Royal Bow of the Ancient Oracle. Then you realize that the weird looking one was actually a high ranking officer in the zombie army, and he had a magical charm that was transferred to you when you killed him. The sword realized your power and let you unlock its other power, the bow.")
        time.sleep(5)
        items.append("bow")

    print("You chase the apparation. You chase it into a corner.")
    print("The portcullis slams shut behind you. How could you be so foolish? It was a trap! You turn back to the corner and find that, in the place of the apparation there is a dog-like form. ")
    print("'Hi. I am Cooklieratinus, a crossbreed betweeen the last Jumperdoggo and one of the only Puppi left. Sadly, the last remaining Jumperdoggo is nowhere to be seen, and there are only seven Puppi left in the galaxy.' he says. 'You can call me Cookie for short. Do you want to take me as a pet?'")
    choice = input("Yes or no(Y or N)?")
    if choice == "Y":
      print("'I will take you.' you say. 'Yay!' he sqeals. He jumps on you and slobbers. You play with him. He says, 'This way!' and he opens a secret trapdoor in the ground. He pulls you in and you find yourself warping through the fabric of Time itself. But that's only half of you; the other half is slicing through Space, the partner of Time. Together, they created Existance, the fact that we exist. ")
      laumanorYN()
    else:
      print("'Goodbye.' He shakes his head sadly. 'I was hoping for an owner. Thank you for considering it.' ")
      time.sleep(3)
      print("He dissapears. You find the portcullis unable to open, and you spend your life there. ")
      intro()

def laumanorYN():
  print("The doors open. You find yourself in a garden full of beautiful plants and flowers, not to mention the majestic trees with leaves of gold and silver. There are animals of more than every kind, that ever existed, and that would ever exist. 'Where can this be?' you wonder. You walk and find a huge mansion. On the arch above the entrance, it says: THE PALACE OF THE MYSTERIOUS DRAGONS. You knock on these doors. The doors open. ")
  time.sleep(10)
  print("Do you enter (Y or N)?")
  choice = input("What is your choice?")
  if choice == "Y":
    furyfire()
  if choice == "N":
    print("Suddenly, a gust of wind blew you out of the mansion. You are blown out of the walls and is now back where you started. ")
    intro()

def furyfire():
  print("You enter the mansion. ")
  print("A Phoenix comes out to escort you. 'Hello,' he tells you. 'We don't get visitors often. Please, help thyself. Would thou like to see The Developer?'(Y/N)")
  choice = input("What is thy choice (ugh, writing in Shakespearian makes it stuck in my head)?")
  if choice == "Y":
    print("'Ok.' He starts walking. You follow him. You walk for what seems like hours until you come to a stretch of wall.")
    time.sleep(2)
    print("He knocks on the wall and removes the flowers from a short flowerpot on the wall. He concentrates and produces a key out of shining green sparks. He puts the key into the flowerpot and turns. Then a mosaic on the wall turns to him. 'Passcode?' the mosaic says. 'Yuewxqswuiul.' he responds. THe mosaic opens its mouth wide and it becomes a door. He produced another key and unlocked the door.")
    time.sleep(4)
    print("A lock clicks inside and he produces more and more keys as the lock changes shape. Finally, the door swings open. ")
    time.sleep(2)
    print("You are amazed at what you see. On a throne, there is a golden phoenix that welcomes you.")
    time.sleep(2)
    print("'Welcome, explorer.' says a soft voice. You realize that the phoenix said that. He has a crown laced with poison whereas the only antidote runs in the royal family's veins. How do you know that? You have no clue.")
    time.sleep(2)
    print("'To find what you desire, go on an adventure to the Lost World where you may meet the Trioxplorers, my allies.' the phoenix continutes. 'The Nightmares will be here soon. I will be discussing a deal with them for poison and weapons in exchange for prisoners. Based on your look, they will want you. For the sake of your safety, run.'")
    time.sleep(5)
    print("You thank him.")
    time.sleep(2)
    print("'Do not thank me, young explorer. It is also for our deal, as they will reject our deal if they see you. And make sure you take care of yourselves.' He eyes Cookie. 'And what is that?'")
    time.sleep(3)
    print("'Oh, that's just Cookie. I found him on my way here.' you say. 'Furyfire?' squeals Cookie. 'Cookie?' says the phoenix, whose name must me Furyfire. 'You found my lost pet!' They run and hug each other. Are you jealous? Y/N")
    x = input()
    if x == "Y":
      print("You get dizzy and die.")
      intro()
    else:
      print("You feel proud of yourself for not getting jealous. 'You may keep Cookie. As long as you visit me with him, ok?' he says. 'Cookie squeals and runs back to you. 'Now I can rest assured that he is safe.' Furyfire sighs. He hands you a token. On it is engraved CAFILYEM FIOISL. He motions for a guard and speaks to him. He salutes and walks away. He comes back with supplies. 'For you.' the guard says. 'What are these bones for?' you ask. 'For Cookie.' Furyfire says. 'He likes chewing on them. Don't worry, they're UGEVWMIUWRL ivory. Ugevwmiuwrl shed their bones, horns, and tusks regularly. They are one of the toughest animals, along with the toughest tusks and horns. The bones are relatively strong, though not as strong as human steel.'")
      time.sleep(10)
      print("A guard runs to the chamber. 'The Nightmares are here, sire.' He nods and dismisses the guard. 'Come here.' he says to you. You come closer.")
      time.sleep(2)
      print("He pushes you into the fireplace.")
      time.sleep(2)
      print("You are shocked, but you realize the fire was a portal. You find yourself in a jungle.")
      mayaintro(items)

  else:
    print("'Thou never shalt have said that,' he signed. 'Goodbye, friend. Let us meet again.' The ground shakes and the mansion collapses. You feel no pain, and you find yourself where you started.")
    intro()

def room4():
    print("This is the room4, the room of jokes")
    choice = input("Do you need glasses? y/n ")
  
    if choice == 'y':
      print('You must be a programmer, because you cant see sharp\n\n\n\n\n')
      time.sleep(2)
      print("Let me tell you a story")
      print("A long time ago, in a far away space planet,")
      print("There was a meep (a Martian sheep), call Meepulls")
      print("Meeps (for short) ran all over Mars and did sheep stuff")
      intro()
    else:
      print("GO AWAY\n")
      intro()

def room7():
  url = open("pythonssong.txt")
  html = url.read()
  print("Good for you! You died and in your afterlife, you manage to find this song about the language that this was written in. ")
  time.sleep(3)
  print("It goes like this.")
  time.sleep(1)
  print(html)
  intro()


def mayaintro(items):  
  print('You are in a forest')
  time.sleep(2)
  print('You hear a zombie moaning sound')
  time.sleep(2)
  print('You look in your pocket')
  time.sleep(2)
  print('You have a fez and a phone, but you also find something on the ground')
  time.sleep(2)
  choice = input("Do you want to pick it up? y/n ")


  if choice == 'y':
    print("you pick up the object and it is a lazer sword (yes, spelled lazer with a z)")
    time.sleep(2)
    items.append("lazer sword")
    print('You now have')
    for item in items:
      print("\t",item)
    print("You come to a fork in the path. Which fork do you take?")
    print('''
    1. Left Path
    2. Right Path
    
    3. Crash through the jungle in the middle''')
    choice = input("CHOOSE 1,2, or 3. ")
    choice = int(choice)
    if choice == 1:
      left(items)
    elif choice == 2:
      right(items)
      print("")
  elif choice == 'n': 
    print("You Journey ahead. Suddenly, a tiger jumps on you. ")
    time.sleep(2)
    print("'Easy prey.' the tiger mutters. 'This one didn't even pick the sword up.'")
    time.sleep(2)
    print("You realize you should have picked the sword up.")
    time.sleep(2)
    print("the tiger promptly eats you")
    die() # why do you die?

def left(items):
  print("You took the left path.")
  time.sleep(2)
  print("You walk for hours and hours until you glimpse a town ahead.")
  time.sleep(2)
  print("But in front of the town, there is a cyclops guarding the pathway. ")
  time.sleep(2)
  print("But behind you, a lion is pacing back and forth. And who knows what lies in the jungle?")
  time.sleep(2)
  print('''What do you do? You can
  1. go back
  2. fall down and sob and wait for your death
  3. go charging at the cyclops with your lazer sword
  4. jump into the fire marked PORTAL''')
  choice = input("CHOOSE 123")
  choice = int(choice)
  
  if choice == 3:
    sugarYN(items)
  elif choice == 2:
    die()
  elif choice == 4:
    intro()
  else:
    print("You find yourself back where you started. ")
    time.sleep(2)
    intro(items)

def sugarYN(items):
  print("You head to the city.")
  time.sleep(2)
  print("The cyclops looks at you and decides that you are not a threat.")
  time.sleep(2)
  use = random.choices(items)
  print("You hit the cyclops on the back with a " + use + "and it stumbles. You climb on top of it and it talks.")
  time.sleep(2)
  print("It yells. Lots of cyclopses flood out. Are you scared?")
  choice = input("Y/N")
  if choice == "Y":
    print("They overcome you. You die.")
    choice()
  else:
    print("They know you're not afraid of them and each of them dissapear in a puff of smoke. 1")
  
def die():
  message = "You died. Do you wish to play again? y/n "
  choice = input(message)
  if choice == 'y':
    time.sleep(2)
    print("Maybe you will do better this time and not die, good luck!")
    intro()
  else:
    print("Goodbye.")

def right():
  print("you decide to go down the right path")
  time.sleep(2)
  print("you continu down the path for a few minutes and you find yourself, in New York City")
  time.sleep(2)
  print("It turns out that the forest you were in was just Central Park")
  time.sleep(2)
  print("you remember everything and you go back to your apartment because you don't want to get covid-19")
  choice()

# Heyyyyyyyy guys! This will be totally awesome! Keep working!
# - Pythonmaster24, creator of the bank money, the chocolate, chocoxplodes, GORILLA, RAVEN, WOLF, and LAND MONSTER, co-editor of the Sugar Game. 
from random import randint as r
from random import choice as rc
from time import sleep as s
from copy import deepcopy


sugar = 0
bank = 5_000_000
chocolate = 0
chocoxplode = 0
cost = 0
landmonsteractivate = False

def sugarintro(sugar, bank, chocolate, chocoxplode, cost):
  print("This is a story about you")
  if landmonsteractivate:
    sugar -= 500
    chocolate += 50
  s(2)
  print("\nIt is a true story\n")
  s(2)
  print(f'Your sugar balance is {sugar}')	
  s(2)
  choice = input("\nHow much sugar would you like?")
  s(1)
  choice = int(choice)
  bank += bank//10
  if choice < 100000:
    sugar += choice
    bank -= choice
    sugarbank(sugar, bank, chocolate, chocoxplode, cost)
  else:
    print('You greedy monkey! No sugar for you.')
    sugarbank(sugar, bank, chocolate, chocoxplode, cost)

def sugarbank(sugar, bank, chocolate, chocoxplode, cost):
  beforeState = deepcopy([sugar, bank, chocolate, chocoxplode, cost])
  wowword = ["INFINITY", "112409", "PYTHON", "AXOLOTL", "PUPPY", "WOLF", "I WANT CHOCOLATE", "PYTHONMASTER24"]
  theword = rc(wowword)
  s(2)
  print(f'\n\nYour sugar balance is {sugar}')	
  print('''
  Welcome to the sugar bank!
  What would you like to do?
  Type CAT for deposit
  Type SNAKEFACE for withhdrawl
  Type HAMSTER to rob the bank (WARNING: If the bank is in debt you will pay the debt for the bank.)
  Type MANGO to light your sugar on fire
  Type GORILLA to give the bank your money
  Type RAVEN to trade some sugar for chocolate
  Type LADYBUG to play the lottery
  Type WOLF to make chocoxplode (exploding chocolate with enchaned flavor)
  Type BREAD to go buy bread
  Type BANK to see how much money the bank has
  Type LAND MONSTER to try to control the Land Monster.
  ''')

  choice = input("Please pick an option")
    
  if choice == 'CAT':
      choice = input("How many sugars do you want to deposit")
      choice = int(choice)
      print("You deposit {choice} sugars")
      sugar -= choice
      bank += choice
  elif choice == 'HAMSTER':
      print("You rob the bank")
      s(2)
      print("The bank gives you " + str(bank) + "sugars")
      s(2)
      print("You now have a huge amount of sugar")
      sugar += bank
      bank = 0
  elif choice == 'MANGO':
      print("You light your sugar on fire")
      sugar = 0	
      print("You now have no sugar.")
      print("I hope you feel the pain of sugar poverty!\n")
  elif choice == 'GORILLA':
    bank += sugar
    sugar = 0
    print("You give all your sugar to the bank. The bank will remember your kindness.")
    s(2)
    print("But a gorilla hears you calling it so it rampages and nearly kills you. ")
    s(2)
    print("But it kills you. You die. The end,.")
    s(5)
    print("Just kidding! The bank remembers your kindness and gives the gorilla 100 sugar. It agrees to leave you alone. ")
    bank -= 100
  elif choice == 'LADYBUG':
    if sugar < cost:
      print("You can't afford the lottery!")
    else:
      winning = []
      winning.append(r(1,10))
      winning.append(r(1,10))
      winning.append(r(1,10))
      lottery = []
      print("You decide to play the lottery")
      print("The lottery costs {cost} sugar")
      sugar -= cost
      cost *= 1.4
      for i in range(3):
        choice = input("Pick a number ")
        choice = int(choice)
        lottery.append(choice)
      print(f'The winning lottery numbers are:')
      for number in winning:
        print(number)
      if lottery in winning:
        print("You won the lottery!")
        sugar += 10*number
  elif choice == 'BREAD':
    print("You go to the bread bank")
    url = open("bread.txt")
    html = url.read()
    print(html)
  
  elif choice == 'RAVEN':
    print("1 chocobar => 50 sugars (chocolate is better than sugar!)")
    chocolate = input("How many chocobars would you like?")
    
  elif choice == 'WOLF':
    print("10 chocolates + 100 sugars => chocoxplode")
    chocoxplode += int(input("How many chocoxplodes would you like?"))
    chocolate -= int(10*int(chocoxplode))
    sugar -= 100*int(chocoxplode)

  elif choice == 'BANK':
    print(bank)
    
  elif choice == 'LAND MONSTER':
    x = r(0, 2)
    item = ["a Lazer sword", "a newspaper", "an ocotopus you found", "the old man over there", "some sort of ancient relic", "a dinosaur bone"]
    item = rc(item)
    print("You hit the Land Monster with " + item + ".")
    s(2)
    if x == 0:
      print("The Land Monster doesn't respond.")
      s(2)
      print("It swings at you. What do you do?")
      s(2)
      print('''You can:
      1. Keep fighting
      2. Run away
      3. Throw a chocoxplode at it''')
      choice = input("CHOOSE 123.")
      if choice == 1:
        print("You keep fighting. You lose. You are robbed of 1000 sugars.")
        sugar -= 1000
      elif choice == 2:
        print("You run away, but you lose a chocolate on the way.")
        chocolate -= 1
      else:
        print("You threw a chocoxplode into the monster's mouth.")
        chocoxplode -= 1
        s(2)
        print("The Land Monster explodes. It has not died but you have defeated it. ")
        s(2)
        choice = input('''You can:
        1. Take it as a pet and know that you can play with item
        2. Kill it''')
        if choice == 1:
          landmonsteractivate = True
          print("Bonus! It gives you 50 chocolates every time you play again. But the sad thing is it gobbles up 500 sugars ever time it does that. ")
        else:
          print("Turns out it's immortal.")
          s(2)
          print("It eats all your things.")
          sugar = 0
          chocolate = 0
          chocoxplode = 0

    else:
      print("You defeated the Land Monster. Congrats!")
      s(2)
      print('''You can:
      1. Kill it and gain 1,000,000 sugars
      2. Keep it as a tamed pet that gobbles up 500 sugars per minute but gives you 50 chocobars every time you play again
      ''')
      s(2)
      choice = input("CHOOSE 12")
      if choice == 1:
        print("You killed the Land Monster!")
        sugar += 1000000
      else:
        landmonsteractivate = True
  elif choice == theword:
    print("Wow! You found the word! I'll give you 1,000,000,000 sugars, 1,000,000 chocolates, and 100,000 chocoxplodes just for guessing it!")
    sugar += 1000000000
    chocolate += 1000000
    chocoxplode += 100000


  else:
    print("You take 100 sugars")
    sugar += 100
    bank -= 100
      
  print(f'\nYour sugar balance is {sugar}\n')
  print(f'\nYour chocolate balance is {chocolate}\n')
  print(f'\nYour chocoxplode balance is {chocoxplode}\n')
  s(2)	

  if sugar < 0 or chocoxplode < 0 or chocolate < 0:
    print(f'\nYou have spent too much. I''ll turn back time.\n')
    (sugar, bank, chocolate, chocoxplode, cost) = beforeState
  choice = input("Do you want to play again? y/n ")
  s(1)
  if choice == 'y':
    sugarintro(sugar, bank, chocolate, chocoxplode, cost)
  else:
    print("Not like you have much choice.")
    sugarintro(sugar, bank, chocolate, chocoxplode, cost)







#I had 97093 Sugar on 4/20/2020

def choice():
  x = random.randrange(0, 3)
  if x == 1:
    intro()
  elif x == 0:
    mayaintro(items)
  else:
    sugarintro(sugar, bank, chocolate, chocoxplode, cost)

choice()



