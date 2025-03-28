class ArrayBasedList:
    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def append(self, element):
        self.data.append(element)

    def insert(self, element, index):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, element)


    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    my_list = ArrayBasedList()
    while True:
        command = input("Enter command (append, insert): ").strip()
        if command == "append":
            value = input("Enter character: ")
            my_list.append(value)
        elif command == "insert":
            value = input("Enter character: ")
            index = int(input("Enter index: "))
            try:
                my_list.insert(value, index)
            except IndexError as e:
                print(e)
        else:
            print("Unknown command.")
        print("Current list:", my_list)