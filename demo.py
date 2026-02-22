# mô phỏng việc tung con xúc xắc 
import random
# các kết quả có thể đạt được 
outcomes = [1,2,3,4,5,6]# mô phỏng việc thực hiện 1 phép thử
# lấy ra 1 kết quả ngẫu nhiên từ outcomes
result = random.choice(outcomes)
print("kết quả của việc tung con xúc xắc là:", result)
# biến cố và các phép toán cơ bản trên biến cố
# không gian mẫu
omega = {1,2,3,4,5,6}
# biến cố A: lấy ra được mặt lẻ
A = {1,3,5}
# biến cố B: lấy ra được mặt chấm lớn hơn 4
B = {5,6}
# hợp của 2 biến cố A và B
print("hợp 2 biến cố A và B:",A|B)
# giao của 2 biến cố A và B
print(" giao 2 biến cố A và B:",A&B)
# phần bù của biến cố A
print("phần bù của biến cố A:",omega - A)
# định nghĩa xác suất cổ điển
# P(A) = số lượng phần tử của biến cố A/ tổng số phần tử của ko gian mẫu
P_A = len(A) / len(omega)
print("xác suất của biến cố A là:",P_A)
# định nghĩa xác suất theo thống kê
# P_A = k/n ( sấp sỉ )
#n là số lần thực hiện phép thử
n = 100000
# k: số lần biến cố A xảy ra
k = 0
# thực hiện n lần tung con xúc xắc 
for i in range (1, n+1): # lặp từ 1->n
    if random.choice(outcomes)== 6:
        k+=1;
    if i % 100 == 0:
        print("lần thứ",i,"kết quả là 6 xuất hiện",k,"lần và tuần xuất là",k/i,"%")