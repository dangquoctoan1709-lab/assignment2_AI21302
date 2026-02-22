def bai_1_L_1():
    # tính giảm giá đơn hàng
    tong_don_hang = float(input("Nhập tổng giá trị đơn hàng(VND): "))
    if tong_don_hang >= 1_000_000:
        giam_gia = tong_don_hang * 0.10
    else:
        giam_gia = 0

    thanh_toan = tong_don_hang - giam_gia
    print("Số tiền được giảm:",giam_gia,"VND")
    print("Số tiền phải thanh toán:",thanh_toan,"VND")
def bai_2_L_1():
    # tính tiền điện
    so_kwh = int(input("Nhập số kwh điện tiêu thụ: "))
    if so_kwh <=50:
        tien_dien = so_kwh * 1500
    elif so_kwh <=100:
        tien_dien = (50 * 1500) + (so_kwh - 50) * 1700
    else:
        tien_dien = (50 * 1500) + (50 * 1700) + (so_kwh - 100) * 2000

    print("Tiền điện phải trả:",tien_dien,"VND")
def bai_3_L1():
    # kiểm tra năm nhuận
    nam = int(input("Năm dương lịch:"))
    if nam % 400 == 0:
        print(nam,"Là năm nhuận")
    elif nam % 100 == 0:
        print(nam,"Không phải là năm nhuận")
    elif nam % 4 == 0:
        print(nam,"Là năm nhuận")
    else:
        print(nam,"Không phải là năm nhuận")
def bai1_L2():
    # tính giai thừa n
    n = int(input("n là số nguyên không âm:"))
    giai_thua = 1
    for i in range(1,n + 1):
        giai_thua *= i
    print(f"{n}! = {giai_thua}")
def bai2_L2():
    # chương trình menu
    while True:
        print("\n====MENU====")
        print("1. Tính tổng hai số")
        print("2. Tính hiệu hai số")
        print("0. Thoát chương trình")
        mo = input("Chọn chức năng:")
        if mo == "1":
            a = float(input("Nhập số thứ nhất:"))
            b = float(input("Nhập số thứ hai:"))
            print("Tổng=",a+b)
        elif mo == "2":
            a = float(input("Nhập số thứ nhất:"))
            b = float(input("Nhập số thứ hai"))
            print("Hiệu=",a-b)
        elif mo == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")
def bai3_L2():
    # kiểm tra số nguyên tố
    n= int(input("Nhập số nguyên dương:"))
    if n <=1:
        print(n,"Không phải số nguyên tố")
    else:
        la_so_nguyen_to = True
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                la_so_nguyen_to = False
                break
        if la_so_nguyen_to:
            print(n,"Là số nguyên tố")
        else:
            print(n,"Không phải là số nguyên tố")
bai_1_L_1()
bai_2_L_1()
bai_3_L1()
bai1_L2()
bai2_L2()
bai3_L2()