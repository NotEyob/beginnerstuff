import time
def mindblown():
    name = input("What is your name?")
    print ("Let me guess...")
    time.sleep(2)
    print ("Still guessing...")
    time.sleep(2)
    print (f"Your name is {name}! Am I right?")
    time.sleep(1.5)
mindblown()