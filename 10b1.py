def bai1():
    san_pham = {
        "name" : "Laptop",
        "price" : 20000000
        }
    price = san_pham["price"]
    print("Giá sản phẩm:",price)
    if "stock" in san_pham:
        stock = san_pham[stock]
    else:
        stock = 0
    print("Số lượng tồn kho:",stock)
#bai1()
def bai2():
    ung_vien1 = ["Python","Java","SQL","Git"]
    ung_vien2 = ["Java","Docker","Go","SQL"]
    set_1 = set(ung_vien1)
    set_2 = set(ung_vien2)
    tat_ca_ki_nang = set_1 | set_2
    print("Tất cả kĩ năng của hai ứng viên",tat_ca_ki_nang)
    ki_nang_chung = set_1 & set_2
    print("Kĩ năng mà ứng viên 1 và 2 đều có:",ki_nang_chung)
    ki_nang_1_co_2_khong = set_1 - set_2
    print("Kĩ năng ứng viên 1 có 2 không:",ki_nang_1_co_2_khong)
#bai2()
def lad5_1():
    danh_sach_cv = []
    while True:
        print("\n====Danh sách quản lý công việc====")
        print("1.Danh sách tất cả công việc")
        print("2.Thêm công việc mới")
        print("3.Xóa công việc đã hoàn thành")
        print("4.Thoát chương trình")
        lua_chon = input("Chọn chức năng từ (1-4):")
        if lua_chon == "1":
            print("Danh sách công việc:")
            sst = 1
            for cv in danh_sach_cv:
                print(stt,"-",cv)
                sst = stt + 1
        elif lua_chon == "2":
            moi = input("Nhập công việc mới:")
            danh_sach_cv.append(moi)
        elif lua_chon == "3":
            xoa = input("Nhập tên công việc muốn xóa:")
            cv_moi = []
            for cv in danh_sach_cv:
                if cv != xoa:
                    cv_moi.append(cv)
            danh_sach_cv = cv_moi
            print("Đã cập nhập danh sach.")
        elif lua_chon == "4":
            print("Đã thoát.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")
# lad5_1()
def lad5_2():
    chuoi = input("Nhập dãy số (cách nhau bởi dấu phẩy): ")
    numbers = []
    so_tam = ""
    for ky_tu in chuoi:
        if ky_tu != ",":
            so_tam = so_tam + ky_tu  
        else:
            if so_tam != "":
                numbers.append(float(so_tam))
                so_tam = ""  
    if so_tam != "":
        numbers.append(float(so_tam))
    lon_nhat = None
    co_so = False 
    for n in numbers:
        if co_so == False: 
            lon_nhat = n
            co_so = True
        elif n > lon_nhat:
            lon_nhat = n
    if co_so == True:
        print("Số lớn nhất là:", lon_nhat)
    else:
        print("Bạn chưa nhập số nào!")
# lad5_2()
def lad5_3():
    grade_book = [
    ["An", 8.0, 7.5, 9.0],
    ["Binh", 9.5, 9.0, 9.5],
    ["Cuong", 5.0, 6.0, 7.0]
    ]
    sv_max = ""
    diem_max = 0
    for sv in grade_book:
        tong = 0
        dem = 0
        for i in range(1, 4): 
            tong += sv[i]
            dem += 1
        tb = tong / dem
        print(sv[0], ":", tb)
        if tb > diem_max:
            diem_max = tb
            sv_max = sv[0]
    print("Cao nhất:", sv_max)
# lad5_3()
def lad6_1():
    tu_dien = {
        "hello": "xin chào",
        "apple": "quả táo",
        "computer": "máy tính",
        "program": "chương trình"
    }
    tu_can_tra = input("Nhập từ tiếng Anh cần tra: ").lower()
    nghia = tu_dien.get(tu_can_tra, "Không tìm thấy từ này trong từ điển.")
    print("Nghĩa tiếng Việt:{}".format(nghia))
# lad6_1()
def lad6_2():
    khach_hang_A = {"An", "Bình", "Chi", "Dũng"}
    khach_hang_B = {"Chi", "Dũng", "Giang", "Hương"}
    tat_ca_khach = khach_hang_A | khach_hang_B
    print("Tất cả khách hàng:",tat_ca_khach)
    khach_mua_ca_hai = khach_hang_A & khach_hang_B
    print("Khách hàng mua cả A và B:",khach_mua_ca_hai)
    khach_chi_mua_A = khach_hang_A - khach_hang_B
    print("Khách hàng chỉ mua sản phẩm A:",khach_chi_mua_A)
# lad6_2()
def lad6_3():
    thuc_don = [
        {"ten":"Phở bò",
        "gia":50000,
        "danh_muc":"Món chính"},
        {"ten":"Nước cam",
        "gia":25000,
        "danh_muc":"Đồ uống"}
    ]
    dm_can_tinh = input("Nhập danh mục:")
    tong_tien = 0
    for mon in thuc_don:
        if mon["danh_muc"].lower() == dm_can_tinh.lower():
            tong_tien += mon["gia"]
    print("Tổng giá trị các món trong danh mục{} là:{}VND".format(dm_can_tinh,tong_tien))
lad6_3()