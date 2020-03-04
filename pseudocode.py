#Name: tFawaz#
#Class: CS30
#Topic: RPG Pseodocode
#Date Modified: March 1, 2020
#Teacher: MS Cotcher

print("system start")
name = input("what is your name")
while True:

    print("Hello and welcome to fTI, " + name)

    # This variable defines the question statement for the starting choice

    print("You are about to steal a very expensive shoe and according to your research, wednesday and
    thursday are the best day to steal it because they have less workers on those days.")

    # This variable makes the user either choose to eat Rice in the morning of Pizza in the morning

    option = input("which option will you pick? Rice in the morning or pizza in the morning?")

    if option == ("pizza"):

        print("you loose, Not healthy enough....")

        print("End")

    if option == ("rice"):
    # This variable defines the question statement

        print("you are moving on. lucky for you, eating rice in the morning is way more healthy than eating pizza in the morning")

        print("so you found out that there is no rice in the house but there is Apple. ")
     # This variable makes the user either choose to eat apple or will prefer to eat the pizzam

        option = input("will you prefer to eat the apple? or will you prefer to eat the pizza?")

        if option == ("pizza"):
          print("correct")
        if option == ("apple"):
          print("incorrect")

    print("you ate pizza and you started having a stomach pain.")

    option = input("will you prefer to use tylenol or just take some rest?")

    if option == ("tylenol"):

                print("Ooops! the stomach pain is getting worse. The tylenol must have affected something else in your body system.")
        #This code tells the person to take a rest because he is having a stomach pain
    if option == "just take a rest":

          print("Good Idea")
    if option == "take tylenol":
          print("Incorrect")
    print("you are rushed to the hopital and the doctor says that you have a kidney problem and for the reason, you will not be able to eat some kind of foods. for example chicken. Meanwhile chicken is one of you favourite.")
    option == input("will you still eat the chicken because it is your favourite? or you will obey the doctor and not eat chicken?")

    if option == "obey the doctor and not eat chicken":

        print("That is a very good option")

    if option == "still eat the chicken":

        print("thats bad")

    print("Now you are getting better and you are back from the hospital.")

    option == input("will you prefer to create a eating plan?")

    if option == "yes":

        print("that is not healthy")

    if option == "no":

        print("That is good")

    print("you are asked to go learn about food nutrition.")

    option == input("will you go to the program? or you will refuse because you feel like you are matured enough to take care of yourself?")

    if option == "refuse":

        print("it will benefit you if you go for the nutrition program")

    if option == "will go":

        print("good answer")

    elif option == "stop":

            print("you woke up again")

            print("Error, system is shutting down")

            print("End")
