import math

class DBScan:
    
    def __init__(self, coordenadas):
        self.coords = coordenadas 

    def distancia_ponto_centroid(self, ponto_especifico, pontos):
        # ponto_conjunto x1 e y1
        x1 = pontos[0]
        y1 = pontos[1]
        # print(f" x1 e y1: {x1}, {y1}")

        # ponto_centroid x2 e y2
        x2 = ponto_especifico[0]
        y2 = ponto_especifico[1]
        # print(f" x2 e y2: {x2}, {y2}")
        x_calc = (x1 - x2) **2
        y_calc = (y1 - y2) **2

        #distancia = mp.sqrt(mp.exp(x1 - x2) + mp.exp(y1 - y2))
        #distancia = math.sqrt(math.exp(x1 - x2) + math.exp(y1 - y2))
        distancia = math.sqrt(x_calc + y_calc)
        resultado = float(str(distancia))
        return resultado


    def neighbour_points(self, ponto, epsilon):
        points = []
        label_index = []
        for i in range(len(self.coords)):
            coord = self.coords[i]
            dist = self.distancia_ponto_centroid(coord, ponto)
            if(dist <= epsilon) and (coord not in points):
                points.append(coord)
                label_index.append(i)
                
        return label_index, points

    def make_labels(self, spec_coord, epsilon, labels, min_points, cluster_val):
        label_index, neighbours = self.neighbour_points(spec_coord, epsilon)

        if len(neighbours) < min_points:
            for i in range(0, len(labels) ): 
                if i in label_index:
                     labels[i] = -1
        
        if len(neighbours) > min_points:
            for i in range(0, len(labels) ): 
                if i in label_index:
                     labels[i] = cluster_val

        return labels

    def make_clusters( self, min_pts, eps ):
        labels = [0] * len(self.coords)
        val_c = 1
        for i in range(0, len(self.coords) ):
            coord = self.coords[i]
            if labels[i] == 0:
                labels = self.make_labels(coord, eps, labels, min_pts, val_c)
                val_c = val_c + 1
        
        return labels
