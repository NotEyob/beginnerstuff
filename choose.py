import time

def adventure():
    print("Rules: Type your choice that shows up in the parenthesis. type exit to leave. Enjoy!")


    print("Welcome Adventurer! To start, could you please tell us your name? ")
    time.sleep(1)
    name = input("What is your name? ")
    time.sleep(2)
    
    while True:
        print("You wander into a local town. Where do you go first?")
        choice = input("(Hostel/Guild/Tavern) ").lower()
        if choice == "exit":
            print("Goodbye, traveler!")
            break
        elif choice == "hostel":
            hostel_pay = input("You head to the tavern. It's 50 pence for 1 night. Do you pay? (Yes/No) ").lower()
            if hostel_pay == "yes":
                print("You sleep at the hostel, and leave the town the next morning.")
                break
            elif hostel_pay == "no":
                print("You leave.")
                continue
        elif choice == "guild":
            print("You enter the guild. Only one quest. Fight a bear in the kingdom jail. ")
            guild_work = input("Fight it, or hit the tavern? (Fight/Drink) ").lower()
            if guild_work == "fight":
                print("You fight the bear. It nearly kills you, but you have the upper hand. You get paid beautifully, head to the tavern, and drink like royalty.")
                time.sleep(1)
                break
            elif guild_work == "drink":
                print("You head to the tavern. They look at you funny, but hey, at least the beers good.")
                break
        elif choice == "tavern":
            print("You head over the to tavern. It smells of old men, and wet bread. You grab a seat, politely ordering the frail bartender for a drink.")
            tavern_bev = input("What would you like to drink? (Ale/Beer/Mead)").lower()
            if tavern_bev == "ale":
                print("The bartender gives you a weird look. They pour you some. You pay, and drink. A simple choice, but not that popular.")
                break
            elif tavern_bev == "beer":
                print("The bartender smiles, and pours you some. You pay. It tastes like home.")
                break
            elif tavern_bev == "mead":
                print("The bartender gives you an amazed look. It's the most expensive drink, usually only for the royals and nobles. You pay with what little money you have left, and he pours you some. It tastes great!")
                time.sleep(1)
                alcoholic = input("Another? (Yes/No) ").lower()
                if alcoholic == "yes":
                    print("You drink another. It tastes even better.")
                    time.sleep(1)
                    alcoholic2 = input("One more? (Yes/No) ").lower()
                    if alcoholic2 == "yes":
                        print("You ask the bartender for another. He gives you a concerned look, but pours nonetheless. Yum!")
                        alcoholic3 = input("Dont ya think this is enough, man? (Yes/No) ").lower()
                        if alcoholic3 == "yes":
                            print("Alright. Let's get outta here before we cause any trouble.")
                            break
                        elif alcoholic3 == "no":
                            print("The bartender refuses another drink for you.")
                            time.sleep(1)
                            seriously = input("Do you fight him, or leave? (Fight/Leave) ").lower()
                            if seriously == "fight":
                                print("You fight the bartender, and try to get to the full case of mead, but just then, the royal guards burst in and apprehend you.")
                                time.sleep(2)
                                print("You are now in jail, and it's been so long. This is your life now, all over some mead.")
                                break
                            elif seriously == "leave":
                                print("You finally leave, and you probably don't even know you're walking.")
                                break
                    elif alcoholic2 == "no":
                        print("Now, this is enough. Let's leave.")
                        break
                elif alcoholic == "no":
                    print("You leave.")
                    break
adventure()