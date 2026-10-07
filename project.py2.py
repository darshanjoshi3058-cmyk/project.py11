print("wellcome to the pattern Generator and number analyzer!")
while True:
    print("select an option:")
    print("1.Generate a Pattern:")
    print("2.Analyze a Range of Numbers:")
    print("3.Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Generate Pattern...")
    elif choice == "2":
        print("Analyze a Range of Numbers...")
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
