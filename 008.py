a=float(input("Entre com a medida em metros: "))
print("A medida " , a ,"metros convertida em Centimetros é :", (a*100))
print("A medida " , a ,"metros convertida em Quilometros é :", (a/1000))
print("A medida " , a ,"metros convertida em Decametro é :", (a/10))
print("A medida " , a ,"metros convertida em Decimetro é :", (a*10))
print("A medida " , a ,"metros convertida em Centimetro é :", (a*100))
print("A medida " , a ,"metros convertida em Milimetro é :", (a*1000))

#outro metodo

a=float(input("Entre com a medida em metros: "))
km = a/1000
hm = a/100
dam = a/10
dm = a*10
cm=a*100
mm = a*1000

print("A medida de {}m corresponde a :{:.2f}km, {:.2f}hm, {:.2f}dam, {:.2f}dm, {:.2f}cm, e {:.2f}mm ".format(a, km, hm, dam, dm, cm, mm))

#
# #outro metodo, mais enxuto:
#
a=float(input("Entre com a medida em metros: "))
print("A medida " , a ,"metros convertida em Quilometros é :", (a/1000), "km")
print("A medida " , a ,"metros convertida em Centimetros é :", (a*100), "cm")
print("A medida " , a ,"metros convertida em Milimetro é :", (a*1000), "mm")
print("A medida " , a ,"metros convertida em Decametro é :", (a/10), "Dec")
print("A medida " , a ,"metros convertida em Decimetro é :", (a*10), "decimetro")
print("A medida " , a ,"metros convertida em Centimetro é :", (a*100), "cm")

