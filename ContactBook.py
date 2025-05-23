contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n📋 All Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        print()


def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: {contact['name']} - {contact['phone']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")


def show_menu():
    print("📱 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


# 🔁 Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")