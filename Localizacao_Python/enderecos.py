from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo '
resultado = Geocoder('AIzaSyBYC1tSIbzOsV0etWmgJYP_2NzpPgtB6s0'). reverse_geocode(-23.5703022, -46.6451267)
print(resultado)                                                  #Reverse_geocode é usado para gerar o nome da
                                                                  # rua com latitude e longitude