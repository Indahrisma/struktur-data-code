
import sys


class Node (object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node
    self.ref = None

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


class LinkedList(object):
  def __init__(self):
    self.head = None

  def insert(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.get_next()
    return count

# Menambahkan didepan
  def print_LL(self):
    if self.head is None:
      print("linked list is empty!")
    else:
      n = self.head
      while n is not None:
        print(n.data)
        n = n.ref

  def add_begin(self, data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

# Menambahkan dibelakang
  def AtEnd(self, newdata):
    NewNode = Node(newdata)
    if self.head is None:
      self.head = NewNode
      return
    laste = self.head
    while(laste.nextval):
      laste = laste.nextval
    laste.nextval = NewNode

# Menghapus di depan
  def removeFirstNode(head):
    if not head:
      return None
    temp = head
    head = head.next
    temp = None
    return head

# # Function to push node at head
  def push(head, data):
    if not head:
      return Node(data)
    temp = Node(data)
    temp.next = head
    head = temp
    return head

# Hapus belakang
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def deleteNode(self, key):
    temp = self.head
    if (temp is not None):
      if (temp.data == key):
        self.head = temp.next
        temp = None
        return
    while(temp is not None):
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    if(temp == None):
      return
    prev.next = temp.next
    temp = None

 # Hapus semua
  def RemoveNode(self, Removekey):
    head = self.head

    if (head is not None):
      if (head.data == Removekey):
        self.head = head.next
        head = None
        return
    while (head is not None):
      if head.data == Removekey:
        break
      prev = head
      head = head.next

    if (head == None):
      return
    prev.next = head.next
    head = None

 # Menampilkan isi dari list
  def showData(self):
    print("Tampilkan list data:")
    current_node = self.head
    while current_node is not None:
      print(current_node.data),
      print(current_node.next_node.data) if hasattr(
          current_node.next_node, "data") else None
      current_node = current_node.next_node

 # Main menu aplikasi
  def mainmenu(self):
    pilih = "y"
    while (pilih == "y"):
      print("===============================")
      print("| Menu aplikasi linked list |")
      print("===============================")
      print("1. Insert data")
      print("2. Insert data depan")
      print("3. Insert data belakang")
      print("4. Hapus data depan")
      print("5. Hapus data belakang")
      print("6. Delete semua data")
      print("7. Cari data")
      print("8. Panjang dari linked list")
      print("9. Tampil data")
      print("===============================")
      pilihan = str(input(("Silakan masukan pilihan anda:")))
      if(pilihan == "1"):
        obj = str(input("Masukan data yang ingin anda tambahkan: "))
        self.insert(obj)
      elif(pilihan == "2"):
        obj = str(input("Masukan data yang ingin anda tambahkan didepan: "))
        self.add_begin(obj)
        x = input("")
      elif(pilihan == "3"):
        obj = str(input("Masukan data yang ingin anda tambahkan dibelakang: "))
        self.AtEnd(obj)
        x = input("")
      elif(pilihan == "4"):
        # obj = str(input("Masukan data yang ingin anda dihapus di depan: "))
        self.removeFirstNode
        x = input("")
      elif(pilihan == "5"):
        # obj = str(input("Masukan data yang ingin anda dihapus dibelakang: "))
        self.deleteNode
        x = input("")
      elif(pilihan == "6"):
        # obj = str(input("Masukan data yang ingin anda dihapus: "))
        self.RemoveNode
        x = input("")
      elif(pilihan == "7"):
        obj = str(input("Masukan data yang ingin anda dicari: "))
        status = self.search(obj)
        if status == True:
          print("Data ditemukan pada list")
        else:
          print("Data tidak ditemukan")
        x = input("")
      elif(pilihan == "8"):
        print("Panjang dari linked list adalah: "+str(self.size()))
        x = input("")
      elif(pilihan == "9"):
        self.showData()
        x = input("")
      else:
        pilih = "n"


if __name__ == "__main__":
 # execute only if run as a script
  LLl = LinkedList()
  LLl.mainmenu()

  # while(head):
  #     print("{} ".format(head.data), end ="")
  #     head = head.next
