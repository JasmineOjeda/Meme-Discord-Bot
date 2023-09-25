import random

def meow_variations():
    choice = random.choice([1, 1, 2, 2, 3])
    
    if (choice == 1):
        return random.choice(["MEOW", "meow", "MEOW", "meow", "*miau*"])
    if (choice == 2):
        R = ("r" * random.randint(0, 3)) 
        E = ("e" * random.randint(0, 3))
        O = (random.choice(["o", "o", "ow"]) * random.randint(1, 5))
        W =("w" * random.randint(1, 5))
        meow_variate = "m" + R + E + O + W
        
        if (random.randint(1, 2) == 1):
            meow_variate.upper()
        return meow_variate
    if (choice == 3):
        return bark_variations()

def bark_variations():
    bark_variate = ""
    repeat = random.randint(1, 15)
    
    while (repeat > 0):
        repeat-=1
        bark_variate = bark_variate + random.choice(["BARK ", "WOOF "])
    
    return bark_variate

def cheer_variation():
    vowels = random.randint(6, 12)
    yahoo = "YAH" + ("O" * vowels)
    yipee = "YIP" + ("E" * vowels)
    yeah = "YEA" + ("A" * vowels) 
    lets_go = "LE" + random.choice(["T", ""]) + "S G" + ("O" * vowels)
    woo = "W" + ("O" * vowels)
    return random.choice([yahoo, yipee, yeah, lets_go, woo, "noice", "cool"])
  