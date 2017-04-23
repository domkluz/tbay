import dbconnection


def new_user():    
# obtaining username and password
    
    print("Enter a username")
    username_input = str(input())

    user_name_validation = dbconnection.session.query(dbconnection.User.username).filter(dbconnection.User.username==username_input).first()
    
    if user_name_validation == None:
        
        print("Enter your password")
        password_input=str(input())
        
        current_user=dbconnection.User(username=username_input,password=password_input) 
        dbconnection.session.add(current_user)
        dbconnection.session.commit()
        
        global current_user_name
        current_user_name = username_input
       
        
    else:
        print("this username is taken")
        new_user()


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
        
        
        while password_tries <=1:    
        
            print("Please enter your passowrd")
            password_input = str(input())
                
            # Have to work on this to setup correctly.
            # example session.query(Item.description).filter(Item.name == "baseball").all()
            password_verification = dbconnection.session.query(dbconnection.User.password).filter(dbconnection.User.username == username_input).first()
            
                # TypeError: 'NoneType' object is not subscriptable
            if password_input == password_verification[0]:
                    
                print("welcome:  " + str(username_input))
                current_user=username_verification[0]
                password_tries+=2    
                
                current_user = username_input
                
            else:
                print("sorry we could not find your password")
                password_tries +=1
                print("You have two attempts before your password is reset")
                
    
                print("Please enter a new password to continue")
                # need to call the object dbconnection.User instead of dbconnection.User.password
                username_verification2 = dbconnection.session.query(dbconnection.User).filter(dbconnection.User.username == username_input).first()
                username_verification2.password = str(input())
                dbconnection.session.commit()
        
        global current_user_name
        current_user_name=username_input
     
        
def sale():
    
    print("What is the name of what you would like to auction")
    item_name=str(input())
    
    print("Can you describe the item you would like to auction?")
    item_description=str(input())
    
    #dbconnection.engine.execute(dbconnection.Item.insert(), name= item_name,description=item_description, owner_id= User.id)
    
    current_user = dbconnection.session.query(dbconnection.User.id).filter(dbconnection.User.username == current_user_name).first()
    
    item=dbconnection.Item(name=item_name,description=item_description, owner_id=current_user)

    dbconnection.session.add(item)
    dbconnection.session.commit()
    

def bid():
    print("these are the items we currently have on offer at tbay")
    
    items_available = dbconnection.session.query(dbconnection.Item.name,dbconnection.Item.description).all()
    for x in items_available:
        print(x)
    
    print("Which item would you like to bid on - input the name")
    
    bid_item = str(input())
    
    # find the item id.
    find_item_id = dbconnection.session.query(dbconnection.Item.id).filter(dbconnection.Item.name == bid_item).first()
    find_item_bid = dbconnection.session.query(dbconnection.Bid.price).filter(dbconnection.Bid.item_id == find_item_id).all()
    
    print("the current bid for this item is " & max(find_item_bid))
    
    print("how much are you willing to bid")
    
    bid_price = float(input())
    
    current_bid_item = dbconnection.session.query(dbconnection.Item.id).filter(dbconnection.Item.name == bid_item).first()
    current_user = dbconnection.session.query(dbconnection.User.id).filter(dbconnection.User.username == current_user_name).first()
    
    bid_placed = dbconnection.Bid(price=bid_price,item_id = current_bid_item,bid_id =current_user)
    dbconnection.session.add(bid_placed)
    dbconnection.session.commit()
    
    
        
        
        
        
        
        
        

   




