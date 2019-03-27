Hello = input("Hello are you a registered user? yes or no:-")
if Hello == "yes":
    username = input("Enter your username:-")
    password = input("Enter your password:-")

    with open("Login.txt", "r") as loginfile:
        if (username + "," + password + "\n") in loginfile.readlines():
            print("Welcome!")
        else:
            print("Wrong credintials! Bye")



else:
    name = input("Please enter your name:- ")
    age = input("Now please enter you age:- ")

    username = input("Please enter your username:-")
    print ("Your username has been created and is", username, ".")

    password = input("Now please create a password:- ")

    file = open("Login.txt","a")
    file.write (username)
    file.write (",")
    file.write (password)
    file.write ("\n")
    file.close()

    print ("Your login details have been saved in Login.txt ")

    file = open("Details.txt","a")
    file.write (name)
    file.write (",")
    file.write (age)
    file.write ("\n")
    file.close()

    print ("your personal details is in Details.txt")
