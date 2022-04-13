
class Node(object):
    def __init__(self, data):
        self.data = data
        self.item = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.head = None;    

# Insert element at the start
    def append(self, data):
        n=Node(data)
        temp=self.start_node
        self.start_node=n
        n.next=temp
        self.start_node=n

# Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

# Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

 # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

# Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

#Menampilkan Menu
    def menuUmum(self):
                pilih = "y"
                while ((pilih == "y") or (pilih == "Y")):
                    print('Pilih menu yang anda inginkan')
                    print('==============================')
                    print('1. Tambah data di depan')
                    print('2. Tambahkan data di belakang')
                    print('3. Hapus data didepan')
                    print("4. Hapus data dibelakang")
                    print('5. Tampilkan data')
                    pilihan = str(input("Masukkan Menu yang anda pilih= "))
                    if(pilihan == "1"):
                        obj = str(input("Masukan data yang ingin anda tambahkan di depannya: "))
                        self.append(obj)
                        x = input("")
                    elif(pilihan == "2"):
                        obj = str(input("Masukan data yang ingin anda tambahkan di depannya: "))
                        self.InsertToEnd(obj)
                        x = input("")
                    elif(pilihan == "3"):
                        self.DeleteAtStart()
                    elif(pilihan == "4"):
                        self.delete_at_end()
                    elif(pilihan == "5"):
                        self.Display()
                        x = input("")
                    else :
                        pilih ="n"

if __name__ == "__main__":
 # execute only if run as a script
 d = doublyLinkedList()
 d.menuUmum()