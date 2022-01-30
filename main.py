from random import randint
import time
def message_get(name):
  number = randint(1, 20)
  if number == 1:
    message = (name + " the Stupid Dude")
    return message
  elif number == 2:
    message = (name + " is the guy who went to SPACE")
    return message
  elif number == 3:
    message = (name + "TDM")
    return message
  elif number == 4:
    message = (name + "9010")
    return message
  elif number == 5:
    message = (name + " the Cyclops")
    return message
  elif number == 6:
    message = (name + " here and today we are playing Minecraft")
    return message
  elif number == 7:
    message = (name + " here and today we are playing Roblox")
    return message
  elif number == 8:
    message = (name + " here and today we are playing Fortnite")
    return message
  elif number == 9:
    message = (name + " the Smart Dude")
    return message
  elif number == 10:
    message = (name + " wishes to be like Dream")
    return message
  elif number == 11:
    message = (name + " wishes to be like Technoblade")
    return message
  elif number == 12:
    message = (name + "XD9012COOLDUDECAMEFROMOUTERSPACEDANCEOHSOCOOL")
    return message
  elif number == 13:
    message = (name + " Is a ALIEN")
    return message
  elif number == 14:
    message = (name + "-IACD")
    return message
  elif number == 15:
    message = (name + ". He's a simple guy in a simple home who cares about life")
    return message
  elif number == 16:
    message = ("Rockstar " + name)
    return message
  elif number == 17:
    message = ("Withered " + name)
    return message
  elif number == 18:
    message = ("Toy " + name)
    return message
  elif number == 19:
    message = ("Diamond " + name)
    return message
  elif number == 20:
    message = ("Glamrock " + name)
    return message
  else:
    return "Whoops, try again"

print("Hello! I'm the Phony Poor Agent. I will take you're name and turn it into whatever whacky Phony Poor thing I can! Then you can take that thing and turn it into what you want!")
print("")
name = input("But of course, I need your NAME so you just type it right here(Username, don't give your real name to robots): ")

print("You're roll is...")
time.sleep(5)
print(message_get(name))
reroll = input("Do you want to reroll? (y for Yes) ")
if reroll.lower() == "y":
  print("You're roll is...")
  time.sleep(5)
  print(message_get(name))
  print("")
  print("Now GOODBYE!")
else:
  print("NOW GOODBYE")
  exit

