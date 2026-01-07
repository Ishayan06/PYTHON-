name = input("Enter your name: ")
msg = input("Enter message (press Enter to use default): ")

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

if msg:
    greet(name, msg=msg)
else:
    greet(name)
