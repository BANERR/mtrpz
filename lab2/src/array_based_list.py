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

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def deleteAll(self, element):
        self.data = [x for x in self.data if x != element]

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self):
        cloned_list = ArrayBasedList()
        cloned_list.data = self.data.copy()
        return cloned_list


    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    my_list = ArrayBasedList()
    while True:
        command = input("Enter command (append, insert, delete, get, deleteAll, clone): ").strip()
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
        elif command == "delete":
            index = int(input("Enter index: "))
            try:
                print("Deleted:", my_list.delete(index))
            except IndexError as e:
                print(e)
        elif command == "deleteAll":
            value = input("Enter character: ")
            my_list.deleteAll(value)
        elif command == "clone":
            my_list.clone()
        elif command == "get":
            index = int(input("Enter index: "))
            try:
                print("Value:", my_list.get(index))
            except IndexError as e:
                print(e)
        else:
            print("Unknown command.")
        print("Current list:", my_list)