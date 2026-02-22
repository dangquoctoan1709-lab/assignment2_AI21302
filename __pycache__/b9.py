# cấu trúc dữ liệu
list=["John".23,40000]
# thay vì a="John"
#         b=23
#         c=40000
for i in list:
    print(i)

# danh sách lop
sv=["tuan",23,56]
# kiểu ma trận
sv1=["tuan",23,56]
sv2=["minh",23,56]
clasS=[sv1,sv2]
# cách khác
class2=[
["tuan",23,56],
["minh",23,56]
]

so_nguyen_to= [2,34,23,35,12,16]
# sắp xếp dãy
so_nguyen_to.sort()
print(so_nguyen_to)
lop=["minh","an","phú"]
#sap xep theo aphaB
lop.sort()
print(lop)
# dao ngược lại
lop.reverse()
print(lop)

#danh sách lồng nhau
danh_sach=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in danh_sach:
    print("---------",i)



#danh sách lồng nhau
danh_sach2=[
    ["a","b","c"]
    ["d","e","f"]
    ["g","h","k"]
]
list1= ["a","b","c"]
print(danh_sach2[0][0])
print(danh_sach2[0][1])
print(danh_sach2[0][2])
print(danh_sach2[1][0]) 