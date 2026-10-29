print(" wellcome to the data analyzer and Transformer program")
print("main menu:")
print("1. input data")
print("2. display data summary")
print("3. calculater factorial")
print("4. fliter data by threshold")
print("5. sort data")
print("6. display dataset statistics")
print("7. exit program")

while True:
    choice = input("Please enter your choice: ")

    if choice == "1":
        data = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Data stored successfully!")
        print("Data:", data)

    elif choice == "2":
        if "data" not in globals() or len(data) == 0:
            print("Please enter data first!")
        else:
            def display_summary(**kwargs):
                print("Data Summary:")
                print("Total elements:", len(data))
                print("Minimum value:", min(data))
                print("Maximum value:", max(data))
                print("Sum of all values:", sum(data))
                print("Average value:", round(sum(data) / len(data), 2))

                print("Additional Information:")
                for key, value in kwargs.items():
                    print(key, ":", value)

            display_summary(
                Data_Type="Integer",
                Data_Status="Available"
            )

    elif choice == "3":
        def factorial(n):
            if n == 0 or n == 1:
                return 1

            return n * factorial(n - 1)

        number = int(input("Enter a non-negative number: "))

        if number < 0:
            print("Negative numbers are not allowed!")
        else:
            print("Factorial:", factorial(number))

    elif choice == "4":
        if "data" not in globals() or len(data) == 0:
            print("Please enter data first!")
        else:
            threshold = int(input("Enter threshold value: "))

            result = list(filter(lambda x: x >= threshold, data))

            print("Filtered Data:", result)

    elif choice == "5":
        if "data" not in globals() or len(data) == 0:
            print("Please enter data first!")
        else:
            print("1. Ascending Order")
            print("2. Descending Order")

            sort_choice = input("Enter your choice: ")

            if sort_choice == "1":
                print("Sorted Data:", sorted(data))

            elif sort_choice == "2":
                print("Sorted Data:", sorted(data, reverse=True))

            else:
                print("Invalid choice!")

    elif choice == "6":
        if "data" not in globals() or len(data) == 0:
            print("Please enter data first!")
        else:
            def dataset_statistics(values):
                minimum = min(values)
                maximum = max(values)
                total = sum(values)
                average = total / len(values)

                return minimum, maximum, total, average

            minimum, maximum, total, average = dataset_statistics(data)

            print("\nDataset Statistics:")
            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Total:", total)
            print("Average:", round(average, 2))

    elif choice == "7":
        print("Thank you for using Data Analyzer Program!")
        break

    else:
        print("Invalid choice! Please select 1 to 7") 