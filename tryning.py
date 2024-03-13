class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.next = None

class Order:
    def __init__(self):
        self.head = None

    def menu(self, nama, harga):
        new_item = MenuItem(nama, harga)
        new_item.next = self.head
        self.head = new_item

    def display_order(self):
        current = self.head
        total = 0
        while current:
            print(current.nama, "\t\t\t\tRp", current.harga)
            total += current.harga
            current = current.next
        print("====================================================== +|")
        print("|Total biaya yang harus dibayarkan adalah\tRp", total, "|")
        print("\n=========================================================")
        print("|            Terimakasih sudah memesan                  |")
        print("=========================================================\n")

def main():
    menu_order = Order()
    while True:
        print("      =============== Daftar Menu  ==============")
        print("      |  1.  Miexue Ice Cream         Rp5.000   |")
        print("      |  2.  Boba Shake               Rp16.000  |")
        print("      |  3.  Mi Sundae                Rp14.000  |")
        print("      |  4.  Mi Ganas                 Rp11.000  |")
        print("      |  5.  Creamy Mango Boba        Rp22.000  |")
        print("      |  6.  Selesai dan Tampilkan Pesanan      |")
        print("      ============================================")
        pilihan = int(input("Masukkan pilihan menu : "))

        if pilihan == 6:
            print("=========================================================")
            print("             Menu yang anda pesan adalah : \n")
            menu_order.display_order()
            break
        elif pilihan in range(1, 6):
            if pilihan == 1:
                menu_order.menu("Miexue Ice Cream", 5000)
            elif pilihan == 2:
                menu_order.menu("Boba Shake\t", 16000)
            elif pilihan == 3:
                menu_order.menu("Mi Sundae\t", 14000)
            elif pilihan == 4:
                menu_order.menu("Mi Ganas\t", 11000)
            elif pilihan == 5:
                menu_order.menu("Creamy Mango Boba", 22000)
            print("Menu telah ditambahkan ke keranjang")
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
