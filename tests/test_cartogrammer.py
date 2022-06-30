import cartogrammer

def test_cartogram():
    
    cart = cartogrammer.Cartogram("./tests/assets/federal-canada.zip", export="canada.geojson")
    
    assert cart