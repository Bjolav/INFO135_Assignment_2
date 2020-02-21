def task1():
    oxford = 171476
    korean = 1100373
    italian = 260000

    counter = 0
    while oxford > 1:
        oxford = oxford / 2
        if oxford >= 0.5:
            counter += 1
    print(f"The Oxford dictionary requires", counter, "steps")
    counter = 0
    while korean > 1:
        korean = korean / 2
        if korean >= 0.5:
            counter += 1
    print(f"The Korean dictionary requires", counter, "steps")
    counter = 0
    while italian > 1:
        italian = italian / 2
        if italian >= 0.5:
            counter += 1
    print(f"The Italian dictionary requires", counter, "steps")

def task2():
    class House:
        def __init__(self):
            owner.self = owner
            owner = "landlord"

        def print_welcome():
            print("Welcome landlord!")

def task3():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def print_list(self):
            if self.head != None:
                start = self.head
                while self.head != None:
                    print(self.head.data)
                    self.head = self.head.next
                self.head = start
            elif self.head == None:
                print("Nothing is in this linked list")

        def add(self, data_new):
            node_next = Node(data_new)
            if self.head == None:
                self.head = node_next
                return None
            node_last = self.head
            while node_last.next != None:
                node_last = node_last.next
            node_last.next = node_next


    linked_list = LinkedList()

def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()