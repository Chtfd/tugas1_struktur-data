
class WeightedGraph:
    def __init__(self):
        self.cityList = {}

    def printGraph(self):
        for city in self.cityList:
            print(city, ":", self.cityList[city])

            for neighbor, distance in self.cityList[city].items():
                #print tetangga dan jarak
                print("    ->", neighbor, ":", distance, "Km")

    def tambahkanKota(self, kota):
        #jika kota tidak ada di cityList
        if kota not in self.cityList:
            #maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False

    def hapusKota(self, kotaDihapus):
        #jika kotaDihapus ada di cityList
        if kotaDihapus in self.cityList:
            del self.cityList[kotaDihapus]
            for kota in self.cityList:
                #jika kotaDihapus ada di cityList[kota]
                if kotaDihapus in self.cityList[kota]:
                    #maka hapus kotaDihapus
                    del self.cityList[kota][kotaDihapus]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False

    def djikstra(self, source):
        distances = {}
        for city in self.cityList:
            distances[city] = float('inf')
        
        distances[source] = 0
        print (distances)
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        #unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)

      while unvisited_cities:
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city

            unvisited_cities.remove(closest_city)

            # Update distances to neighboring cities
            for neighbor, weight in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
    
petajawatimur = WeightedGraph()
petajawatimur.tambahkanKota("SURABAYA")
petajawatimur.tambahkanKota("PASURUAN")
petajawatimur.tambahkanKota("PROBOLINGGO")
petajawatimur.tambahkanKota("SITUBONDO")
petajawatimur.tambahkanKota("BANYUWANGI")
petajawatimur.tambahkanKota("JEMBER")
petajawatimur.tambahkanKota("LUMAJANG")
petajawatimur.tambahkanKota("MALANG")
petajawatimur.tambahkanKota("BLITAR")
petajawatimur.tambahkanKota("NGANJUK")
petajawatimur.tambahkanKota("BOJONEGORO")
petajawatimur.tambahkanKota("LAMONGAN")

petajawatimur.tambahkanJalan("SURABAYA","PASURUAN", 54)
petajawatimur.tambahkanJalan("PASURUAN","PROBOLINGGO", 36)
petajawatimur.tambahkanJalan("PROBOLINGGO","SITUBONDO", 98)
petajawatimur.tambahkanJalan("SITUBONDO","BANYUWANGI", 97)
petajawatimur.tambahkanJalan("BANYUWANGI","JEMBER", 103)
petajawatimur.tambahkanJalan("JEMBER","LUMAJANG", 62)
petajawatimur.tambahkanJalan("LUMAJANG","MALANG", 142)
petajawatimur.tambahkanJalan("MALANG","BLITAR", 79)
petajawatimur.tambahkanJalan("BLITAR","NGANJUk", 76)
petajawatimur.tambahkanJalan("NGANJUK","BOJONEGORO", 55)
petajawatimur.tambahkanJalan("BOJONEGORO","LAMONGAN", 68)
petajawatimur.tambahkanJalan("LAMONGAN","SURABAYA", 45)

petajawatimur.printGraph()
shortest_distances = petajawatimur.djikstra("SURABAYA")
print("Jarak antar kota ")
for city, distance in shortest_distances.items():
    print(city, "=", distance, "km", )
