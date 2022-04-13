class Node (object):

    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
        
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

# Inisialisasi node baru
        new_node = Node(data)
 
 # Menunjuk node berikutnya dari node baru ke node yang ditunjuk oleh HEAD
        new_node.set_next(self.head)

 # HEAD menunjuk ke node baru
        self.head = new_node
 
 # Menghitung panjang list
    def size(self):
 
 # Membuat pointer baru menunjuk ke node yang ditunjuk oleh HEAD
        current = self.head
        count = 0
 
 # Perulangan untuk menghitung node
        while current:
            count += 1
            current = current.get_next()
        return count
 
 # Mencari sebuah data pada list
    def search(self, data):
 
 # Membuat pointer baru menunjuk ke node yang ditunjukoleh HEAD
        current = self.head
        found = False
# Perulangan mencari node yang dicari
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        return found
 
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
 
 # Menampilkan isi dari list
    def showData(self):
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        current_node = self.head
        while current_node is not None:
            print (current_node.data),
            print (" ->"),
            print (current_node.next_node.data) if hasattr(current_node.next_node, "data") else None
            current_node = current_node.next_node
 
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
            print("6. Tampil data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda:")))
            if(pilihan=="1"):
                obj = str(input("Masukan data yang ingin anda tambahkan didepannya: "))
                # self.insert(obj)
                self.insert(0,x)
            elif(pilihan=="2"):
                obj = str(input("Masukan data yang ingin anda tambahkan dibelakangnya: "))
                self.insert(obj)
                self.append(x)
                x = input("")
            elif(pilihan=="3"):
                obj = str(input("Masukan data yang ingin anda dihapus didepannya: "))
                self.delete(0,x)
                x = input("")
            elif(pilihan=="4"):
                obj = str(input("Masukan data yang ingin anda dihapus dibelakangnya: "))
                self.delete(x,0)
                x = input("")
            elif(pilihan=="5"):
                self.clear()
                x = input("")
            elif(pilihan=="6"):
                self.showData()
                x = input("")
            else:
                pilih="n"

if __name__ == "__main__":
 # execute only if run as a script
    l = LinkedList()
    l.mainmenu()


