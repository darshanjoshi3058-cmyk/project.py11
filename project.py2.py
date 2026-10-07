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

    if choice == "1":
        row=int(input("enter the number of rows: "))   
        for i in range(1,row+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

        start=int(input("enter the starting number: "))
        end=int(input("enter the ending number: "))
        for i in range(start, end + 1):
            if i % 2 == 0:
               print(i, "is an even number")
            else:
                print(i, "is an odd number")        
            
        
        start=int(input("enter the starting number: "))
        end=int(input("enter the ending number: "))
        for i in range(start, end + 1):
            if i % 2 == 0:
                print(i, "is an even number")
            else:
                print(i, "is an odd number")

                total = 0
                for i in range(start, end + 1):
                    total += i
                print("the sum of numbers from", start, "to", end, "is:", total) 
                # i used chat gtp for help with sum total logic



        

         
