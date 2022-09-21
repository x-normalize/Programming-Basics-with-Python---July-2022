username = input()
actual_password = input()
password = input()
while password != actual_password:
    password = input()
else:
    print(f"Welcome {username}!")
