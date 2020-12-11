print("\tLogin")
uname=input("Username:")
password=input("Password: ")

#verify user info
if uname.lower()=="Jerry" and password=="1234":
    print("Login Sucessful")
else:
    print("Invalid Username or Password")