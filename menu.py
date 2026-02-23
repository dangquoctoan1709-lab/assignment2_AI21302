import module as pm

def menu():
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====")
    print("1. Thêm sản phẩm")
    print("2. Cập nhật sản phẩm")
    print("3. Xóa sản phẩm")
    print("4. Tìm kiếm theo tên")
    print("5. Hiển thị tất cả")
    print("6. Thoát")

def main():
    products = pm.load_data()

    while True:
        menu()
        choice = input("Chọn (1-6): ")

        if choice == "1":
            products = pm.add_product(products)

        elif choice == "2":
            products = pm.update_product(products)

        elif choice == "3":
            products = pm.delete_product(products)

        elif choice == "4":
            pm.search_product_by_name(products)

        elif choice == "5":
            pm.display_all_products(products)

        elif choice == "6":
            pm.save_data(products)
            print("Đã lưu và thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()