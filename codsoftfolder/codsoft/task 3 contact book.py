contacts = {}

while True:
    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = phone, email, address
        print("Contact Added")

    elif choice == "2":
        for name in contacts:
            print(name, "-", contacts[name][0])

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("Phone:", contacts[name][0])
            print("Email:", contacts[name][1])
            print("Address:", contacts[name][2])
        else:
            print("Contact Not Found")

    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in contacts:
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")

            contacts[name] = phone, email, address
            print("Contact Updated")
        else:
            print("Contact Not Found")

    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid Choice")
