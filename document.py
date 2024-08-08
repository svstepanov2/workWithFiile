import os

PHONEBOOK_FILE = "phonebook.txt"

def load_phonebook(file):
    phonebook = []
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(", ")
                phonebook.append({
                    "lastname": data[0],
                    "firstname": data[1],
                    "middlename": data[2],
                    "phone": data[3]
                })
    return phonebook

def save_phonebook(phonebook, file):
    with open(file, "w", encoding="utf-8") as f:
        for entry in phonebook:
            f.write(f"{entry['lastname']}, {entry['firstname']}, {entry['middlename']}, {entry['phone']}\n")

def display_phonebook(phonebook):
    for entry in phonebook:
        print(f"{entry['lastname']} {entry['firstname']} {entry['middlename']} - {entry['phone']}")

def add_entry(phonebook):
    lastname = input("Enter lastname: ")
    firstname = input("Enter firstname: ")
    middlename = input("Enter middlename: ")
    phone = input("Enter phone number: ")
    phonebook.append({
        "lastname": lastname,
        "firstname": firstname,
        "middlename": middlename,
        "phone": phone
    })

def search_entry(phonebook, keyword):
    results = [entry for entry in phonebook if keyword.lower() in entry['lastname'].lower() or 
               keyword.lower() in entry['firstname'].lower()]
    return results

def update_entry(phonebook, keyword):
    for entry in phonebook:
        if keyword.lower() in entry['lastname'].lower() or keyword.lower() in entry['firstname'].lower():
            print(f"Found: {entry['lastname']} {entry['firstname']} {entry['middlename']} - {entry['phone']}")
            entry['lastname'] = input("Enter new lastname (leave blank to keep current): ") or entry['lastname']
            entry['firstname'] = input("Enter new firstname (leave blank to keep current): ") or entry['firstname']
            entry['middlename'] = input("Enter new middlename (leave blank to keep current): ") or entry['middlename']
            entry['phone'] = input("Enter new phone number (leave blank to keep current): ") or entry['phone']
            return True
    return False

def delete_entry(phonebook, keyword):
    for i, entry in enumerate(phonebook):
        if keyword.lower() in entry['lastname'].lower() or keyword.lower() in entry['firstname'].lower():
            print(f"Deleting: {entry['lastname']} {entry['firstname']} {entry['middlename']} - {entry['phone']}")
            del phonebook[i]
            return True
    return False

def main():
    phonebook = load_phonebook(PHONEBOOK_FILE)
    while True:
        print("\nPhonebook Menu:")
        print("1. Display all entries")
        print("2. Add new entry")
        print("3. Search entry")
        print("4. Update entry")
        print("5. Delete entry")
        print("6. Save and exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_phonebook(phonebook)
        elif choice == '2':
            add_entry(phonebook)
        elif choice == '3':
            keyword = input("Enter name or lastname to search: ")
            results = search_entry(phonebook, keyword)
            if results:
                for entry in results:
                    print(f"{entry['lastname']} {entry['firstname']} {entry['middlename']} - {entry['phone']}")
            else:
                print("No entries found.")
        elif choice == '4':
            keyword = input("Enter name or lastname to update: ")
            if not update_entry(phonebook, keyword):
                print("No entries found.")
        elif choice == '5':
            keyword = input("Enter name or lastname to delete: ")
            if not delete_entry(phonebook, keyword):
                print("No entries found.")
        elif choice == '6':
            save_phonebook(phonebook, PHONEBOOK_FILE)
            print("Phonebook saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()