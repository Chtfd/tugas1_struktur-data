class Node:
    def __init__(self,nim, nama):
        self.nama = nama
        self.nim = nim
        self.next = None

class LinkedList:
    def __init__(self,nim,nama):
        new_node = Node(nim,nama)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, nim,nama):
        new_node = Node(nim,nama)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        print(self.length)
        temp = self.head
        while temp is not None:
            print("NIM : ",temp.nim)
            print("Nama :",temp.nama)
            temp = temp.next
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.nim
    def jumlah_nim(self):
        index = self.length - 1
        temp = self.head
        jumlah_nim = temp.nim 
        for _ in range(index):
            temp = temp.next
            jumlah_nim += temp.nim 
        print("jumlah nim adalah",jumlah_nim)

mahasiswaPrestasi = LinkedList(11,"Novelita")
mahasiswaPrestasi.append(23,"Roaini")
mahasiswaPrestasi.append(34,"Bathari")
mahasiswaPrestasi.print_list()
mahasiswaPrestasi.jumlah_nim()

