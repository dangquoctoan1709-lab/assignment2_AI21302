import product_manager as pm

def main():
    # 1) Tải dữ liệu khi bắt đầu
    products = pm.load_data()
    
    # 2) Vòng lặp Menu chính
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ LAPTOP POLY-LAP ---")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm theo tên")
        print("6. Thoát")
        
        choice = input("Chọn chức năng (1-6): ")
    
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '3':
            pm.update_product(products)
        elif choice == '4':
            pm.delete_product(products)
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '6':
            # 3) Lưu dữ liệu trước khi thoát
            pm.save_data(products)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()