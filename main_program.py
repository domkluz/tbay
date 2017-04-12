import dbconnection
import menu


print("Hi, welcome to TBAY")
print("Are you a new user to TBAY - Please input - Yes or No")
response = str(input())

if response == ("yes" or "Yes"):
    menu.new_user()

else:
    menu.returning_user()

print("To auction an item enter sale, or enter bid")

response == str(input())

if response == ("sale" or "Sale"):
    menu.sale()
else:
    menu.bid()