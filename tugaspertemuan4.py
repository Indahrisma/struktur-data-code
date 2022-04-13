

class Node(object):

    def __init__(self, dataval=None, data=None):
        self.dataval=dataval
        self.nextval=None

    def set_next(self, new_next):
        self.next_node = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self):
        self.headval=None

#insert data
    def insert(self,data):
        new_node=Node(data)
        new_node.set_next(self)
        self.headval=new_node
        new_node=Node(self)
        new_node.set_next(self.headval)
        self.headval=new_node

#menambahkan didepan
    # def listprint(self):
    #     printval=self.headval
    #     while printval is not None:
    #         printval=printval.nextval

    def AtBegining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

#menambahkan dibelakang
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # def listprint(self):
    #     printval = self.headval
    #     while printval is not None:
    #         print (printval.dataval)
    #         printval = printval.nextval

# Menghapus node
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
 

#Hapus semua
    def RemoveNode(self, Removekey):
        headval = self.headval
            
        if (headval is not None):
            if (headval.data == Removekey):
                self.headval = headval.next
                headval = None
                return
        while (headval is not None):
            if headval.data == Removekey:
                break
            prev = headval
            headval = headval.next

        if (headval == None):
            return
        prev.next = headval.next
        headval=None

    def listprint(self):
        printval = self.headval
        while (printval):
            print(printval.data),
            printval = printval.next

# Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.headval
        while current_node is not None:
            print (current_node.dataval),
            print (" ->"),
            print (current_node.next_node.dataval) if hasattr(current_node.next_node, "dataval") else None
            current_node = current_node.next_node


# Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("===============================")
            print("| Menu aplikasi linked list |")
            print("===============================")
            print("1. Insert data")
            print("2. Insert Depan data")
            print("3. Insert Belakang data")
            print("4. Hapus Depan")
            print("5. Hapus Belakang")
            print("6. Hapus Semua")
            print("7. Tampil data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda:")))
            if(pilihan=="1"):
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.insert(obj)
            elif(pilihan=="2"):
                obj = str(input("Masukan data yang ingin anda tambahkan didepannya: "))
                self.AtBegining(obj)
                x = input("")
            elif(pilihan=="3"):
                obj = str(input("Masukan data yang ingin anda tambahkan dibelakangnya: "))
                self.AtEnd(obj)
                x = input("")
            elif(pilihan=="4"):
                obj = str(input("Masukan data yang ingin anda dihapus didepannya: "))
                self.delete(0,x)
                x = input("")
            elif(pilihan=="5"):
                obj = str(input("Masukan data yang ingin anda dihapus dibelakangnya: "))
                self.delete(x,0)
                x = input("")
            elif(pilihan=="6"):
                self.clear()
                x = input("")
            elif(pilihan=="7"):
                self.showData()
                x = input("")
            else:
                pilih="n"

if __name__ == "__main__":
 # execute only if run as a script
    l = LinkedList()
    l.listprint()
    l.mainmenu()

