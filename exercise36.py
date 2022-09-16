from sys import exit

def english_lang():
    print("Select you have a option: ")
    print("> 'Check Balance', \n'History', '\nWithdraw': ")

    choice = input("> ")

    if choice == "check balance":
        print("Enter your 4 digit pin.")
        pin = int(input(">  "))

        if pin > 999 and pin < 10000 :
            print("your Balance is 'xxxx'")
            print("Thank you! for Banking.")
            exit(0)

        else :
            print("your 4 digit pin has wrong.")   
            exit(0)

    if choice == "history":
        print("Enter your 4 digit pin.")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            print("your last transaction is 'xxxx'")
            print("Thank you! for Banking.")
            exit(0)

        else:
            print("your 4 digit pin has wrong.")
            exit(0)


   


    if choice == "withdraw":

        def valid():               
            print("Your transaction is succesfull.")
            print("Thank you! for Banking.")
            exit(0)  

        def invalid():         
            print("This amount is not valid for ATM")
            # exit(0)
            a = input("back or exit")
            if a =="b":
                english_lang()
            elif a=="e":
                exit(0)
            else:
                exit(0)    



        print("Enter your 4 digit pin.")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            #print("Enter your amount.")
            amount = int(input("Entre amount=")) 

            if amount >= 100 and amount <= 50000 : 
                s = 0
                for i in range(1,500):
                    s = s + 100
                    if s== amount:
                        valid()
                invalid()    
            else:
                invalid()       


          
        
##########################################################################################
def marathi_lang():
    print("Select you have a option: ")
    print("> 'Check Balance', \n'History', '\nWithdraw': ")

    choice = input("> ")

    if choice == "check balance":
        print("Enter your 4 digit pin.")
        pin = int(input(">  "))

        if pin > 999 and pin < 10000 :
            print("your Balance is 'xxxx'")
            print("Thank you! for Banking.")
            exit(0)

        else :
            print("your 4 digit pin has wrong.")   
            exit(0)

    if choice == "history":
        print("Enter your 4 digit pin.")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            print("your last transaction is 'xxxx'")
            print("Thank you! for Banking.")
            exit(0)

        else:
            print("your 4 digit pin has wrong.")
            exit(0)

    # if choice == "withdraw":
    #     print("Enter your 4 digit pin.")
    #     print = int(input("> "))

    #     if pin > 999 and pin < 10000 :
    #         print("Enter your amount.")

    #     if amount <100 and amount >50000 :
    #         print("Your transaction is succesfull.")
    #         print("Thank you! for Banking.")
    #         exit(0)

    #     else:
    #         print("This amount is not valid for ATM")
    #         exit(0)
################################################################################################

def hindi_lang():
    print("Select you have a option: ")
    print("> 'Check Balance', \n'History', '\nWithdraw': ")

    choice = input("> ")

    if choice == "check balance":
        print("क्रिपया अपना  गुप्त ४ अंक  दबाये")
        pin = int(input(">  "))

        if pin > 999 and pin < 10000 :
            print("आपके खाते मैं xxx पैसा है !")
            print("बैंक आपका धन्यवाद करती है !")
            exit(0)

        else :
            print("आपका गुप्त ४ अंक ग़लत है !")   
            exit(0)

    if choice == "history":
        print("क्रिपया अपना  गुप्त ४ अंक  दबाये")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            print("तुम्हारा आख़री लेणदेण 'xxxx'")
            print("बैंक आपका धन्यवाद करती है !")
            exit(0)

        else:
            print("आपका गुप्त ४ अंक ग़लत है !")
            exit(0)

    # if choice == "withdraw":
    #     print("Enter your 4 digit pin.")
    #     print = int(input("> "))

    #     if pin > 999 and pin < 10000 :
    #         print("Enter your amount.")

    #     if amount <100 and amount >50000 :
    #         print("Your transaction is succesfull.")
    #         print("Thank you! for Banking.")
    #         exit(0)

    #     else:
    #         print("This amount is not valid for ATM")
    #         exit(0)


########################################################################################################################

def start():
    print("Welcome to ATM.")
    print("Swap your ATM.")
    print("select your language: ")
    print("Marathi,", "Hindi,", "English")

    choice = input("> ")

    if choice == "marathi":
        marathi_lang()

    elif choice == "hindi":
        hindi_lang()

    elif choice == "english":
        english_lang()
    
    else:
        print("You chose the wrong language...")
        print("select your language: ")
        print("marathi,", "hindi,", "english")
    choice = input("> ")
    exit(0)

start()