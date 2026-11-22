class Node:
    def __init__(self, book_id):
        self.data = book_id
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, book_id):
        new_node = Node(book_id)
        new_node.next = self.head
        self.head = new_node
        print("Book ID inserted successfully.")

    # Insert at End
    def insert_end(self, book_id):
        new_node = Node(book_id)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Book ID inserted successfully.")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty!")
        else:
            print("Deleted Book ID:", self.head.data)
            self.head = self.head.next

    # Display
    def display(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp = self.head
            print("Book IDs:")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


# Main Program
ll = LinkedList()

while True:
    print("\n--- Library Book Management ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        ll.insert_beginning(book_id)

    elif choice == 2:
        book_id = int(input("Enter Book ID: "))
        ll.insert_end(book_id)

    elif choice == 3:
        ll.delete_beginning()

    elif choice == 4:
        ll.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
