complete = False
user = {"username1" : "12345", "username2" : "67890" }
 
while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue    
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        print(f"Password is not valid for {username}. ")
        continue
    elif password == user[username]:
        print(f"Welcome {username} ")
        print(f"Thank you for logging on. ")
        complete = True
 
