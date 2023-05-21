liste = ["banana", "orange", "apple", "banana", "apple", 45, 23, 45, 89, "apple"]
a = {}
for i in liste:
    a.update({i: liste.count(i)})
#     a[i] = liste.count(i)

for key1 in a.keys():
    print(key1, " : ", a[key1], " Piece")
#Liste elemanlarını güncelleme 