queue = []
MAX = 5

while True:
    print("\n--- Ticket Booking Queue ---")
    print("1. Enqueue (Add Customer)")
    print("2. Dequeue (Serve Customer)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == MAX:
            print("Queue is Full!")
        else:
            name = input("Enter customer name: ")
            queue.append(name)
            print(name, "added to the queue.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty!")
        else:
            print("Serving Customer:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty!")
        else:
            print("Customers in Queue:")
            for customer in queue:
                print(customer)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
