import contact_manager as cm
while True:
    print("1.Them lien he")
    print("2.Hien thi danh ba")
    print("3.Thoat")
    chon = input("Chon chuc nang:")
    if chon == "1":
        ten = input("Nhap ten:")
        sdt = input("Nhap so dien thoai")
        cm.them_lien_he(ten,sdt)
    elif chon == "2":
        danh_ba = cm.lay_danh_ba()
        if danh_ba == []:
            print("Danh ba trong")
        else:
            for lh in danh_ba:
                print(f"ten:{lh['ten']} - sdt:{lh['sdt']}")
    elif chon == "3":
        print("Thoat chuong trinh")
        break
    else:
        print("Lua chon khong hơp le")
