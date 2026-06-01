import time
def excuse_me_sir(): 
    print ("guess a character from the boys. no caps, type exit to quit.")
    
    score = 0
    name = input("what's your name? ")
    time.sleep(2)
    while True:
    
        guess = input("who looks into the sky? ").lower()
        if guess == "exit":
            print (f"oi! {name}! thanks for playing! your score was: {score}")
            break
        elif guess == "billy butcher":
            print ("excuse me sir, there must be someone you've confused me for.")
            score += 1
        elif guess == "the deep":
            print ("real eyes, realize, real lies.")
            score += 1
        elif guess == "buca di beppo":
            print ("you, and your little bieber, edging, in the back your rav4 in the car park of buca di beppo.")
            score += 1
        elif guess == "a train":
            print ("i get messages from the stars.")
            score += 1
        elif guess == "homelander":
            print ("ashley, look at me!")
            score += 1
        else:
            print ("Nah, you're a larper!")
excuse_me_sir()