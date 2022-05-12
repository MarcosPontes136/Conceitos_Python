from pygeocoder import Geocoder        #O PYGEOCODER é o pacote a ser buscado,já GEOCODER é a classe
                                       #a ser importada do pacote

endereco = '97, Rua Valdomiro Lopes de Oliveira, Sao Paulo, SP'
print(Geocoder(' AIzaSyBYC1tSIbzOsV0etWmgJYP_2NzpPgtB6s0 ').geocode(endereco).coodernates)


