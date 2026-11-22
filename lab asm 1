stack = []

while True:
    print("\n--- Library Book Stack ---")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.append(book)
        print(book, "returned successfully.")

    elif choice == 2:
        if len(stack) == 0:
            print("No books to arrange!")
        else:
            print("Arranged Book:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Top Book:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Returned Books (Top to Bottom):")
            for book in reversed(stack):
                print(book)

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
