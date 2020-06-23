asking1 = input("Are you regestered or not?  Yes or No?   ")
if asking1 == "Yes":
    false = False
    userpass   = {
    "Nesh" :  "12p",
    "Malli" : "21p",
    "OOF" : "OOF",
    "LOL" : "HAHAH"
    }
    while not false:
        username = input("Username:  ")
        password = input("Password:  ")
        if username  == userpass and password == password:
            continue
        elif username not in user:
            print("This username is not available")     
        elif password != userpass[username]:
            print("Password is invalid")
        elif password == user[username]:
            print("Welcome {username}")
            print("Seeya")
            

elif asking1 == "No":
    print("Hello. We are going to get you regestered")
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    c = userpass[username] = password
    d = userpass.update(c)
    logic()
  # inputs()   
  