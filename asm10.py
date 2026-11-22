SIZE = 10
hash_table = [None] * SIZE

# Insert using Linear Probing
def insert(key):
    index = key % SIZE

    if hash_table[index] is None:
        hash_table[index] = key
        print(key, "inserted at index", index)
    else:
        print("Collision occurred for", key)

        while hash_table[index] is not None:
            index = (index + 1) % SIZE

        hash_table[index] = key
        print(key, "inserted at index", index)


# Display Hash Table
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])


# Main Program
while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value: "))
        insert(key)

    elif choice == 2:
        display()

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
