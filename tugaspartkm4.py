
#from coba import Node
import os

class Node(object):
    def __init__(self, data):
            self.data=data
            self.ref=None
            self.next=None

    def getData(self):
            return self.value

    def getNext(self):
            return self.next

    def setData(self,newData):
            self.value=newData

    def setNext(self,newNext):
            self.next=newNext

class LinkedList:
    def __init__(self):
        self.head = None

#Menambahkan didepan
    def print_LL(self):
        if self.head is None :
            print("linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

#menambahkan dibelakang
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head + new_node
        else :
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


#Menghapus di depan
    def detele_begin(self):
        if self.head is None:
            print("LL is empty so u cant delete nodes!")
        else:
            self.head = self.head.ref

#Menghapus di belakang
    def delete_end(self):
        if self.head is None:
            print("LL is empty so u cant delete nodes!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            
#Hapus Semua
    #delete all nodes of the list
    def deleteAllNodes(self):
        while (self.head!= None):
            n = self.head
            self.head = self.head.ref
            n = None
        print("All nodes are deleted successfully.")  

    #display the content of the list
    def PrintList(self):
        n = self.head
        if(n != None):
                print("The list contains:", end=" ")
        while (n != None):
                print(n.data, end=" ")
                n = n.ref
                print()
        else:
                print("The list is empty.") 
    
#Menampilkan Data
    def showData(self):
        if self.head is None :
            print("linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print("Show Data :",n.data)
                n = n.ref
        
# Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("===============================")
            print("| Menu aplikasi linked list |")
            print("===============================")
            print("1. Insert Depan data")
            print("2. Insert Belakang data")
            print("3. Hapus Depan")
            print("4. Hapus Belakang")
            print("5. Hapus Semua")
            print("6. Tampilkan data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda:")))
            if(pilihan=="1"):
                obj = str(input("Masukan data yang ingin anda tambahkan di depannya: "))
                self.add_begin(obj)
                x = input("")

            elif(pilihan=="2"):
                obj = str(input("Masukan data yang ingin anda tambahkan dibelakangnya: "))
                self.add_end(obj)
                x = input("")

            elif(pilihan=="3"):
                self.detele_begin()

            elif(pilihan=="4"):
                self.delete_end()

            elif(pilihan=="5"):
                self.deleteAllNodes()

            elif(pilihan=="6"):
                self.showData()

            else:
                print("Mending Pulang")

if __name__ == "__main__":
    LLl = LinkedList()
    LLl.mainmenu()
    
