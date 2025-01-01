# noktaların koordinatları
points=[(3,5),(4,-7),(2,6),(-5,8)]

# öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(p1,p2):
  x1,y1=p1
  x2,y2=p2
  ed=((x2-x1)**2+(y2-y1)**2)**(1/2)
  return ed

# hesaplanan mesafelerin listesi
distances=[]

# tekrara düşmeyecek şekilde iki noktayı seçip fonksiyona uygulayan döngü ve fonksiyon sonuçlarının "distances" listesine eklenmesi
for i in range(len(points)):
  for j in range(i+1,len(points)):
    distance=euclideanDistance(points[i],points[j])
    distances.append(distance)

# "distances" listesinin yazdırılması
print(distances)

# "distances" listesindeki en küçük elemanın belirlenip yazdırılması
print(min(distances))