contacts = []
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} | {c['phone']}")

def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}, Address: {c['address']}")
            found = True
    if not found:
        print("No match found.")


def update_contact():
    name = input("Enter name of contact to update: ")
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = input("New Phone: ")
            c["email"] = input("New Email: ")
            c["address"] = input("New Address: ")
            print("Contact updated.")
            return
    print("Contact not found.")


def delete_contact():
    name = input("Enter name of contact to delete: ")
    for i, c in enumerate(contacts):
        if c["name"].lower() == name.lower():
            del contacts[i]
            print("Contact deleted.")
            return
    print("Contact not found.")


while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search\n4. Update\n5. Delete\n6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
