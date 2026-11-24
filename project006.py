
from datetime import datetime

file_name = "journal.txt"


def add_entry():
    entry = input("Enter your journal entry: ")

    date = datetime.now()

    file = open(file_name, "a")
    file.write(date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    file.write(entry + "\n\n")
    file.close()

    print("Entry added successfully!")


def view_entries():
    file = open(file_name, "r")
    data = file.read()
    file.close()

    if data == "":
        print("No journal entries found.")
    else:
        print("Your Journal Entries:")
        print(data)


def search_entry():
    keyword = input("Enter keyword to search: ")

    file = open(file_name, "r")
    data = file.read()
    file.close()

    if keyword in data:
        print("Entry Found!")
        print(data)
    else:
        print("No entry found.")


def delete_entries():
    confirm = input("Are you sure? (yes/no): ")

    if confirm == "yes":
        file = open(file_name, "w")
        file.close()

        print("All entries deleted.")

    else:
        print("Delete cancelled.")


while True:

    print("\nWelcome to Personal Journal Manager!")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entry()

    elif choice == "4":
        delete_entries()

    elif choice == "5":
        print("Thank you! Goodbye!")
        break

    else:
        print("Invalid option!")
