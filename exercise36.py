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
                print("your 4 digit pin has wrong.")
                exit(0)    



        print("Enter your 4 digit pin.")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            #print("Enter your amount.")
            amount = int(input("Entre amount=")) 

            b = input("Comfirm your amount: ")
            if b == "yes":
                valid()
            elif b == "no":
                print("Last transacation is Disabled.")
                exit(0)
            else:
                exit(0)            

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
        print("??????????????? ??? ???????????? ????????? ????????????.")
        pin = int(input(">  "))

        if pin > 999 and pin < 10000 :
            print("??????????????? ?????????????????? 'xxxx'")
            print("????????????????????????????????? ?????????????????????!")
            exit(0)

        else :
            print("??????????????? ??? ???????????? ????????? ?????????????????? ?????????.")   
            #exit(0)

    if choice == "history":
        print("??????????????? ??? ???????????? ????????? ????????????.")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            print("??????????????? ?????????????????? ????????????????????? 'xxx' ?????????.")
            print("????????????????????????????????? ?????????????????????!")
            exit(0)

        else:
            print("??????????????? ??? ???????????? ????????? ?????????????????? ?????????.")
            exit(0)

    if choice == "withdraw":

        def valid():               
            print("??????????????? ????????????????????? ?????????????????? ???????????? ?????????.")
            print("????????????????????????????????? ?????????????????????!")
            exit(0)  

        def invalid():         
            print("?????? ??????????????? ATM ???????????? ????????? ????????????.")
            # exit(0)
            a = input("back or exit")
            if a =="b":
                english_lang()
            elif a=="e":
                exit(0)
            else:
                print("??????????????? ??? ???????????? ????????? ?????????????????? ?????????.")
                exit(0)    



        print("??????????????? ??? ???????????? ????????? ????????????.")
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

################################################################################################

def hindi_lang():
    print("Select you have a option: ")
    print("> 'Check Balance', \n'History', '\nWithdraw': ")

    choice = input("> ")

    if choice == "check balance":
        print("???????????? 4 ??????????????? ?????? ????????? ???????????? ????????????!")
        pin = int(input(">  "))

        if pin > 999 and pin < 10000 :
            print("???????????? ???????????? ????????? xxx ???????????? ?????? !")
            print("????????????????????? ?????? ????????? ?????????????????????!")
            exit(0)

        else :
            print("???????????? 4 ??????????????? ?????? ????????? ????????? ??????!")   
            exit(0)

    if choice == "history":
        print("???????????? 4 ??????????????? ?????? ????????? ???????????? ????????????!")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
            print("???????????? ??????????????? ?????????????????? ?????? 'xxxx'")
            print("????????????????????? ?????? ????????? ?????????????????????!")
            exit(0)

        else:
            print("???????????? 4 ??????????????? ?????? ????????? ????????? ??????!")
            exit(0)

    if choice == "withdraw":

        def valid():               
            print("???????????? ?????????-????????? ????????? ??????!")
            print("????????????????????? ?????? ????????? ?????????????????????!")
            exit(0)  

        def invalid():         
            print("?????? ???????????? ATM ?????? ?????????????????? ???????????? ?????????!")
            # exit(0)
            a = input("back or exit")
            if a =="b":
                english_lang()
            elif a=="e":
                exit(0)
            else:
                exit(0)    



        print("???????????? 4 ??????????????? ?????? ????????? ???????????? ????????????!")
        pin = int(input("> "))

        if pin > 999 and pin < 10000 :
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

    if choice == "marathi":
        marathi_lang()

    elif choice == "hindi":
        hindi_lang()

    elif choice == "english":
        english_lang()
    exit(0)

start()