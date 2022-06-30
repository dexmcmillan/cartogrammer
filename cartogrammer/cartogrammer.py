import geopandas
from shapely.geometry import Point
from shapely import affinity
from math import sqrt, floor

class Cartogram:
    
    global data
    global export
    global scale
    
    def __init__(self, file: str, export: str, scale: int = 1):
        
        self.export = export
        self.scale = scale
        
        raw_data = geopandas.read_file(file).to_crs("EPSG:4326")
        raw_data = raw_data.iloc[::-1]
        
        self.data = self.gridify(raw_data)
        


    def _to_square(self, polygon):
        
        minx, miny, maxx, maxy = polygon.bounds
        
        # get the centroid
        centroid = [(maxx+minx)/2, (maxy+miny)/2]
        
        # get the diagonal
        diagonal = self.scale
        
        return Point(centroid).buffer(diagonal/sqrt(2.)/2., cap_style=3)



    def _to_coords(self, polygon, x, y):
        offsetx = -polygon.centroid.x + x
        offsety = -polygon.centroid.y + y
        
        return affinity.translate(polygon, xoff=offsetx, yoff=offsety)
    
    
    def gridify(self, data):
        
        group = floor(len(data)/10)
        diff = len(data) - group*10
        extra = list(range(1, (diff*self.scale)+1, self.scale))
        
        data["offsety"] = (list(range(0, 10*self.scale, self.scale)) *group) + extra
        data["offsetx"] = data.reset_index()["index"].apply(lambda x: floor(int(x)/10) + 1)
        
        data["geometry"] = data["geometry"].apply(lambda x: self._to_square(x))

        for i, row in data.iterrows():
            data.at[i, "geometry"] = self._to_coords(row["geometry"], row["offsetx"], row["offsety"])
            
        data.to_file(self.export, driver="GeoJSON")
        
        return data
        
        
