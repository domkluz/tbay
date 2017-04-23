import menu

response = "start"

while response == "start":

    print("Hi, welcome to TBAY")
    print("Are you a new user to TBAY - Please input - Yes or No\n")
    response = str(input())

    if response == ("yes" or "Yes"):
        menu.new_user()

    else:
        menu.returning_user()

    print("To auction an item enter sale, or enter bid\n")

    response = str(input())


    if response == ("sale" or "Sale"):
        menu.sale()
    else:
        menu.bid()
    
    print("to end enter end or start again press start\n")

    response = str(input())
    





