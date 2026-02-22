def bai1():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        else:
            print(i)
def bai2():
    so_bi_mat =78
    while True:
        so_doan = int(input("Nhập số đoán:"))
        if so_doan>so_bi_mat:
            print("Số bạn đoán quá lớn! Vui lòng thử lại.")
        elif so_doan<so_bi_mat:
            print("Số đoán quá nhỏ! Vui lòng thử lại.")
        else:
            print("Chúc mừng! Bạn đã đoán đúng con số bí mật.")
            break
# bai1()
bai2()