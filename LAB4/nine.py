phonebook = {}

while True:
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        num = input("Number: ")
        phonebook[name] = num

    elif ch == 2:
        name = input("Name to search: ")
        print(phonebook.get(name, "Not found"))

    elif ch == 3:
        name = input("Name to update: ")
        if name in phonebook:
            phonebook[name] = input("New number: ")
        else:
            print("Not found")

    elif ch == 4:
        name = input("Name to delete: ")
        phonebook.pop(name, "Not found")

    elif ch == 5:
        break

    else:
        print("Invalid choice")
