contacts = {}

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        new_phone = input(f"Enter new phone number for {name}: ")
        contacts[name] = new_phone
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()