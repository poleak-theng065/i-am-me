# enter your password: 123
# if you ennter correct "123" message "your password is correct"
# if you enter wrong password will message: "Try again"
password=None
while password != 123:
    password = int(input("Enter your Password"))
    if password == 123 :
        print("Your password is correct")
    else:
        print("Try agian")
