class Graph:
    def __init__(self):
        self.cityList = {}
    
    def printGraph(self):
        for vertex in self.cityList :
            print(vertex, "=", self.cityList[vertex])
    
    def masukanVertex(self,vertex):
        if vertex not in self.cityList:
            self.cityList[vertex] = []
            return True
        return False
    
    def masukanEdge(self,v1,v2):
        if v1 in self.cityList and v2 in self.cityList:
            self.cityList[v1].append(v2)
            self.cityList[v2].append(v1)
            return True
        return False    

  

myGraph = Graph()
myGraph.masukanVertex("SURABAYA")
myGraph.masukanVertex("PASURUAN")
myGraph.masukanVertex("PROBOLINGGO")
myGraph.masukanVertex("SITUBONDO")
myGraph.masukanVertex("BANYUWANGI")
myGraph.masukanVertex("JEMBER")
myGraph.masukanVertex("LUMAJANG")
myGraph.masukanVertex("MALANG")
myGraph.masukanVertex("BLITAR")
myGraph.masukanVertex("NGANJUK")
myGraph.masukanVertex("BOJONEGORO")
myGraph.masukanVertex("LAMONGAN")
myGraph.masukanEdge("SURABAYA","PASURUAN")
myGraph.masukanEdge("SURABAYA","PROBOLINGGO")
myGraph.masukanEdge("SURABAYA","SITUBONDO")
myGraph.masukanEdge("SURABAYA","BANYUWANGI")
myGraph.masukanEdge("SURABAYA","JEMBER")
myGraph.masukanEdge("SURABAYA","LUMAJANG")
myGraph.masukanEdge("SURABAYA","MALANG")
myGraph.masukanEdge("SURABAYA","BLITAR")
myGraph.masukanEdge("SURABAYA","NGANJUK")
myGraph.masukanEdge("SURABAYA","BOJONEGORO")
myGraph.masukanEdge("SURABAYA","LAMONGAN")
myGraph.masukanEdge("PASURUAN","PROBOLINGGO")
myGraph.masukanEdge("PASURUAN","SITUBONDO")
myGraph.masukanEdge("PASURUAN","BANYUWANGI")
myGraph.masukanEdge("PASURUAN","JEMBER")
myGraph.masukanEdge("PASURUAN","LUMAJANG")
myGraph.masukanEdge("PASURUAN","MALANG")
myGraph.masukanEdge("PASURUAN","BLITAR")
myGraph.masukanEdge("PASURUAN","NGANJUK")
myGraph.masukanEdge("PASURUAN","BOJONEGORO")
myGraph.masukanEdge("PASURUAN","LAMONGAN")
myGraph.masukanEdge("PROBOLINGGO","SITUBONDO")
myGraph.masukanEdge("PROBOLINGGO","BANYUWANGI")
myGraph.masukanEdge("PROBOLINGGO","JEMBER")
myGraph.masukanEdge("PROBOLINGGO","LUMAJANG")
myGraph.masukanEdge("PROBOLINGGO","MALANG")
myGraph.masukanEdge("PROBOLINGGO","BLITAR")
myGraph.masukanEdge("PROBOLINGGO","NGANJUK")
myGraph.masukanEdge("PROBOLINGGO","BOJONEGORO")
myGraph.masukanEdge("PROBOLINGGO","LAMONGAN")
myGraph.masukanEdge("SITUBONDO","BANYUWANGI")
myGraph.masukanEdge("SITUBONDO","JEMBER")
myGraph.masukanEdge("SITUBONDO","LUMAJANG")
myGraph.masukanEdge("SITUBONDO","MALANG")
myGraph.masukanEdge("SITUBONDO","BLITAR")
myGraph.masukanEdge("SITUBONDO","NGANJUK")
myGraph.masukanEdge("SITUBONDO","BOJONEGORO")
myGraph.masukanEdge("SITUBONDO","LAMONGAN")
myGraph.masukanEdge("BANYUWANGI","JEMBER")
myGraph.masukanEdge("BANYUWANGI","LUMAJANG")
myGraph.masukanEdge("BANYUWANGI","MALANG")
myGraph.masukanEdge("BANYUWANGI","BLITAR")
myGraph.masukanEdge("BANYUWANGI","NGANJUK")
myGraph.masukanEdge("BANYUWANGI","BOJONEGORO")
myGraph.masukanEdge("BANYUWANGI","LAMONGAN")
myGraph.masukanEdge("JEMBER","LUMAJANG")
myGraph.masukanEdge("JEMBER","MALANG")
myGraph.masukanEdge("JEMBER","BLITAR")
myGraph.masukanEdge("JEMBER","NGANJUK")
myGraph.masukanEdge("JEMBER","BOJONEGORO")
myGraph.masukanEdge("JEMBER","LAMONGAN")
myGraph.masukanEdge("LUMAJANG","MALANG")
myGraph.masukanEdge("LUMAJANG","BLITAR")
myGraph.masukanEdge("LUMAJANG","NGANJUK")
myGraph.masukanEdge("LUMAJANG","BOJONEGORO")
myGraph.masukanEdge("LUMAJANG","LAMONGAN")
myGraph.masukanEdge("MALANG","BLITAR")
myGraph.masukanEdge("MALANG","NGANJUK")
myGraph.masukanEdge("MALANG","BOJONEGORO")
myGraph.masukanEdge("MALANG","LAMONGAN")
myGraph.masukanEdge("BLITAR","NGANJUK")
myGraph.masukanEdge("BLITAR","BOJONEGORO")
myGraph.masukanEdge("BLITAR","LAMONGAN")
myGraph.masukanEdge("NGANJUK","BOJONEGORO")
myGraph.masukanEdge("NGANJUK","LAMONGAN")
myGraph.masukanEdge("BOJONEGORO","LAMONGAN")

myGraph.printGraph()
