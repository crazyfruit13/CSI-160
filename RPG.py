#Dungeons & Dragons is owned by Wizards of The Coast. All content used/referenced within this game is provided by The D&D 5e Systems Reference Document(SRD) under the Open-Gaming License (OGL). The SRD can be found here:http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf
import time
import random
#Global lists for accepting/denying inputs
no = ['no', 'n', 'NO', 'No', 'N']
yes = ['yes', 'y', 'YES', 'Yes', 'Y']
bagofholding = []
#Global variables for reference by every function
global name 
global rpgclass
sergi = 0
sergihostile = 0
statbump = 1

#Game Over
def gameover():
        print("--------------------------------------------------------------------------------------------------------------")
        deathmessage = input(str("GAME OVER: You've Met With a Terrible Fate, Haven't You? Would You Like To Restart? (Enter Yes or No) "))
        print("--------------------------------------------------------------------------------------------------------------")
        if deathmessage in yes:
                quit()
                
        else:
                quit()
#Start Game
class Main:
        #Important Variables needed in functions
        dead = 0
        #Start-Up Screen 
        def RPG(): 
                time.sleep(1)
        print("-------------------------------------------------------------------------------------------------------------------------------------------")
        print("Dungeons & Dragons is owned by Wizards of The Coast.\nAll content used/referenced within this game is provided by The D&D 5e Systems Reference Document(SRD) under the Open-Gaming License (OGL).\nThe SRD can be found here:http://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        print("--------------------------------------------------------------------------------------------------------------")
        print("Welcome to Above the Outpost! This is a text-based RGP where your decisions decide the fate of your character.")
        print("--------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        name = input(str("What is your name, adventurer: "))
        # Prologue
        time.sleep(1)
        print("--------------------------------------------------------------------------------------------------------------")
        print("Hello",name + ',',  "Welcome to The World of Rosenhall!\nYou have been drafted into The Great War by the royal milita, The Lords Alliance.\nWill you crush the Orc rebellion underneath your boot or help the beasts defeat humanity?\nThe choice is yours!")
        print("--------------------------------------------------------------------------------------------------------------")
        time.sleep(3)
        #Chapter 1
        def Chapter1():
                time.sleep(0)
        print("--------------------------------------------------------------------------------------------------------------")
        print("Sergi:" "Rise and shine, maggot.\nYou've been asleep in the cart for almost six hours!")
        print("--------------------------------------------------------------------------------------------------------------")
        time.sleep(1)
        response1 = input("Please Select How You Would Like To Respond: (Select a Number!) 1: Question where you are. 2: Introduce yourself. 3: Skip the intro. ")
        if response1 == "1":
                print("",name + ':',"Woah, who are you? and where am I heading?")
                time.sleep(1)
                print("--------------------------------------------------------------------------------------------------------------")
                print("Sergi: I'm Sergi, Captain of The Lord's Alliance.\nYou've been drafted to fight in The Great War; We're almost to The Misty Cliffs, I hope you're ready for a fight.")
                print("--------------------------------------------------------------------------------------------------------------")
                time.sleep(3)
        elif response1 == "2":
                print("",name + ':',"Hey, I'm",name + ',' "I'm very proud to be serving the empire.")
                time.sleep(1)
                print("--------------------------------------------------------------------------------------------------------------")
                print("Sergi: I'm Sergi, Captain of The Lord's Alliance. We're almost to The Misty Cliffs, I hope you're ready for a fight,",name +'!',)
                print("--------------------------------------------------------------------------------------------------------------")
                time.sleep(3)
        else:
                print("",name + ':', "I feel like I've heard this before... I'm going back to sleep.")
                time.sleep(1)
                
        #Class Select Screen
        def SelectClass():
                time.sleep(1)
        classselect = 0
        while classselect != 1:
                rpgclass = input(str("Please select your class!\nYou May Pick Between These 4 Options: Wizard, Fighter, Cleric, Ranger\nPlease type the full name of your choice: "))
                #WizardPath
                if rpgclass == "Wizard" or rpgclass == "wizard":
                        classselect = 1
                        time.sleep(1)
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Wizards are supreme magic-users, defined and united as a class by the spells they cast.\nDrawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, and brute-force mind control.\nTheir magic conjures monsters from other planes of existence, glimpses the future, or turns slain foes into zombies.\nTheir mightiest spells change one substance into another, call meteors down from the sky, or open portals to other worlds.")
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        bagofholding.append('spellbook')
                        bagofholding.append('staff')
                        bagofholding.append('potion of invisibility')
                        print("Your starting equitment has been added to your bag of holding.\nYour bag of holding now contains:" ,bagofholding,)
                        time.sleep(2)
                        global statbump
                        statbump = 4
                        print("Your knowledge gives you a +3 boost to your stats!")
                        time.sleep(3)
                #FighterPath
                elif rpgclass == "Fighter" or rpgclass == "fighter":
                        classselect = 1
                        time.sleep(1)
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Fighters excel at controlling the battlefield.\nThey specialize in combat maneuvers that distract, goad, and manipulate their enemies with deadly precision.\nThey are well rounded fighters who have a trick for nearly every situation.")
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        bagofholding.append('shield')
                        bagofholding.append('sword')
                        bagofholding.append('heavy armor')
                        time.sleep(2)
                        print("Your starting equitment has been added to your bag of holding.\nYour bag of holding now contains:" ,bagofholding,)
                        statbump = 2
                        print("Your training in one area only grants you a +1 to stats.")
                        time.sleep(3)
                #ClericPath
                elif rpgclass == "Cleric" or rpgclass == "cleric":
                        classselect = 1
                        time.sleep(1)
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Clerics combine the helpful magic of healing and inspiring their allies with spells that harm and hinder foes.\nThey can provoke awe and dread, lay curses of plague or poison, and even call down flames from heaven to consume their enemies.\nFor those evildoers who will benefit most from a mace to the head, clerics depend on their combat training to let them wade into melee with the power of the gods on their side.")
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        bagofholding.append('holy symbol')
                        bagofholding.append('mace')
                        bagofholding.append('medium armor')
                        print("Your starting equitment has been added to your bag of holding.\nYour bag of holding now contains:" ,bagofholding,)
                        time.sleep(2)
                        statbump = 3
                        print("Your divine blessing grants you a +2 bonus to stats.")
                        time.sleep(3)
                #RangerPath
                elif rpgclass == "Ranger" or rpgclass == "ranger":
                        classselect = 1
                        time.sleep(1)
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Warriors of the wilderness, rangers specialize in hunting the monsters that threaten the edges of civilization;\nrampaging beasts and monstrosities, terrible giants, and deadly dragons, to name a few.\nThey learn to track their quarry as a predator does, moving stealthily through the wilds and hiding themselves in brush and rubble.\nRangers focus their combat training on techniques that are particularly useful against their specific favored foes.")
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        bagofholding.append('quiver')
                        bagofholding.append('bow')
                        bagofholding.append('light armor')
                        print("Your starting equitment has been added to your bag of holding.\nYour bag of holding now contains:" ,bagofholding,)
                        time.sleep(2)
                        statbump = 2
                        print("Your training in one area only grants you a +1 to stats.")
                        time.sleep(3)
                #ErrorHandling        
                else:
                        print("That isn't one of the above options!")
                        classselect = 0
        #Chapter2
        def Chapter2():
                time.sleep(0)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("The cart comes to a sudden stop infront of a small colony of mountains, barely visible through an uncomprehendible amount of fog.\nThe sound of blood curdling screams can faintly be heard in the distance, drowned out by animalistic war cries.\nFurthermore, the all too familiar sound of steel against steel can be heard echoing throughout the freezing valley, it sends chills down your spine.")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        time.sleep(3)
        print("Sergi: Alright,",rpgclass, "It's your time to shine!\nThree Orc War Lords remain inside the valley, send them back to Kingdom Come, or die trying.")
        time.sleep(2)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        response2 = input("Respond to Sergi: (Yes or No) ")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if response2 in yes:
                #AgreeToFight
                print("",name + ':', "Yes, Sir! I will bleed the Orcs dry like swine; for the Empress!")
                time.sleep(1)
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Sergi: You're going to make her proud today,",name, "I believe in you!")
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(2)
                print("OUTCOME: You leave your captain standing guard by the cart and engulf yourself in the fog.")
                global sergi
                sergi = 1
                global sergihostile
                sergihostile = 0
        else:
                #RefuseToFight
                print("",name + ':', "No, Sir. I refuse to slaughter them; they're just animals.")
                time.sleep(1)
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("Sergi:",rpgclass + ',', "Either you go and lay waste to that valley, or you'll be going home in a casket!")
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(2)
                sergihostile = 1
                time.sleep(1)
                #Intimidationroll
                intimidationroll1 = random.randint(1, 20)
                insightroll1 = random.randint(statbump, 20)
                if sergihostile == 1 and intimidationroll1 > insightroll1:
                        print("Sergi rolls a" ,intimidationroll1, "on his intimidation check.")
                        time.sleep(1)
                        print("You rolled a" ,insightroll1, "on your insight check.")
                        time.sleep(2)
                        print("",name + ':', "Knowing that Sergi could best you in a fight, you have no other choice other than to follow his orders.")
                        sergi = 1
                         #DeclareAttack
                if sergihostile == 1 and intimidationroll1 < insightroll1:
                        print("Sergi rolls a" ,intimidationroll1, "on his intimidation check.")
                        time.sleep(1)
                        print("You rolled a" ,insightroll1, "on your insight check.")
                        print("",name + ':', "You laugh at Sergi's weak attempt at scaring you. Your dominant hand twitches towards your",bagofholding[1],)
                        response3 = input("OPTION: Attack the poor excuse of a leader? (Yes or No) ")
                        time.sleep(1)                               
                        battle1 = random.randint(statbump, 20)
                        sergibattle = random.randint(1, 20)
                        #SergiKillsPlayer 
                        if sergibattle > battle1:
                                print("Sergi rolls a" ,sergibattle, "on his attackroll.")
                                time.sleep(1)
                                print("You roll a" ,battle1, "on your attackroll.")
                                time.sleep(1)
                                print("OUTCOME: Before you can even pull your weapon, Sergi impales you with his sword.")
                                print("Sergi: Traitorous Coward!")
                                time.sleep(2)
                                gameover()
                                #DamageCalcs 
                        if sergibattle < battle1:
                                print("Sergi rolls a" ,sergibattle, "on his attackroll.")
                                time.sleep(1)
                                print("You roll a" ,battle1, "on your attackroll.")
                                time.sleep(1)
                                sergi = 2
                                #DeathFlavorText
                        if sergi == 2 and bagofholding[1] == "sword":
                                print("You decapitate Sergi with two quick slashes perfectly aimed at the neck.")
                                time.sleep(2)
                                print("OUTCOME: You begrudgingly head into the valley.")
                
                        if sergi == 2 and bagofholding[1] == "bow":
                                print("You quickly shoot out 2 arrows from your bow; piercing Sergi twice in the chest.")
                                time.sleep(2)
                                print("OUTCOME: You begrudgingly head into the valley.")
        
                        if sergi == 2 and bagofholding[1] == "staff" or bagofholding[1] == "mace" :
                                print("You smash your" ,bagofholding[1], "straight into Sergi's skull, killing him with a single blow.")
                                time.sleep(2)
                                print("OUTCOME: You begrudgingly head into the valley.")

                        if sergi == 2 and bagofholding[1] == "staff":
                                breakchange = random.randint(1, 4)
                                if breakchange == 1:
                                        print("RANDOM EVENT: Your staff shatters into a hundred pieces as it collides with Sergi's skull; talk about being thick headed...")
                                        bagofholding.pop(1)
                                        print("Your current inventory:" ,bagofholding,)

                                
                        #GoodTermsNegate 
                        if sergihostile == 0:
                                time.sleep(1)
                                sergi == 1
                        
        

                
        #Chapter3
        def Chapter3():
                time.sleep(1)
        #AgreeToFightOutcome
        if sergi == 1:
                print("OUTCOME: You go into the valley bent on a path of destruction")
                print("Thank You for playing the BETA of Above The Outpost! Please give me feedback, it really helps.")
        #SergiDeathOutcome              
        else:
                print("OUTCOME: Your murder of Sergi ignites a fire within your soul.")
                print("Thank You for playing the BETA of Above The Outpost! Please give me feedback, it really helps.")
                

                                                          
                                      
                                      
                      
                                      


                      
                              
                      
                      
         
        
        
        









