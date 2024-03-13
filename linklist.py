class Node:
    def __init__(self,menu,harga):
        self.menu = menu
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self,menu,harga):
        new_node = Node(menu,harga)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,menu,harga):
        new_node = Node(menu,harga)
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
            print("menu : ",temp.menu)
            print("harga :",temp.harga)
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
        return temp.harga
    def jumlah_harga(self):
        index = self.length - 1
        temp = self.head
        jumlah_harga = temp.harga 
        for _ in range(index):
            temp = temp.next
            jumlah_harga += temp.harga 
        print("jumlah harga adalah",jumlah_harga)
        
menu = LinkedList("Miexue Ice Cream",5000)
menu.append('Boba Shake',16000)
menu.append('Mie Sundae',14000)
menu.append('Mie Ganas',5000)
menu.print_list()
menu.jumlah_harga()


