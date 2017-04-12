import dbconnection

def new_user():    
# obtaining username and password
    
    print("Enter your username")
    username_input = str(input())

    print("Enter your password")

    password_input=str(input())
        
    current_user=dbconnection.User(username=username_input,password=password_input) 
    dbconnection.session.add(current_user)
    dbconnection.session.commit()


def returning_user():
    print("Welcome back to TBAY")
    print("please enter you username")
    username_input = str(input())
    
    username_verification = dbconnection.session.query(dbconnection.User.username).filter(dbconnection.User.username == username_input).first()
    
    
    # I think there is a way to be able to filter based on name

    # how to deal with when you return none. Is my solution okay of using try and except?
    
    password_tries = 0
    

    if username_verification==None: #username_verification[0]:
        print("no username found")
            
    else:
        
        while password_tries <=2:    
        
            print("Please enter your passowrd")
            password_input = str(input())
                
            # Have to work on this to setup correctly.
            # example session.query(Item.description).filter(Item.name == "baseball").all()
            password_verification = dbconnection.session.query(dbconnection.User.password).filter(dbconnection.User.password == username_input).first()
                
                # TypeError: 'NoneType' object is not subscriptable
            if password_input == password_verification[0]:
                    
                print("welcome:  " + str(username_input))
                current_user=username_verification[0]
                
            else:
                print("sorry we could not find your username")
                password_tries +=1
        
    
    print("Please enter a new password to continue")
    new_password = dbconnection.User()
    # for this to work will need to pull details or try Hoa's method
    


def sale():
    
    print("What is the name of what you would like to auction")
    item_name=str(input())
    
    print("Can you describe the item you would like to auction?")
    item_description=str(input())
    
    item=dbconnection.Item(name=item_name,description=item_description, items2=current_user) 

    dbconnection.session.add(item)
    dbconnection.session.commit()
    

def bid():
    print("these are the items we currently have on offer at tbay")
    
    items_available = session.query(Item.name,Item.description).all()
    for x in items_available:
        print(x)
    
    print("Which item would you like to bid on - input the name")
        
        
        

   




