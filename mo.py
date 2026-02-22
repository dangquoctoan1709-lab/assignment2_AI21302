import json
import os

FILENAME = 'products.json'

def load_data():
    """Đọc dữ liệu từ file JSON, trả về danh sách trống nếu file không tồn tại."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(products):
    """Ghi danh sách sản phẩm vào file JSON."""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def add_product(products):
    """Thêm sản phẩm mới vào danh sách."""
    print("\n--- Thêm sản phẩm mới ---")
    # Tự động tạo mã sản phẩm dựa trên số lượng hiện có
    id_num = len(products) + 1
    product_id = f"LT{id_num:02d}"
    
    name = input("Nhập tên laptop: ")
    brand = input("Nhập thương hiệu: ")
    while True:
        try:
            price = int(input("Nhập giá: "))
            stock = int(input("Nhập số lượng tồn kho: "))
            break
        except ValueError:
            print("Lỗi: Giá và số lượng phải là số nguyên!")

    new_product = {
        "id": product_id,
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock
    }
    products.append(new_product)
    print(f"Đã thêm sản phẩm thành công với mã: {product_id}")
    return products

def update_product(products):
    """Cập nhật thông tin sản phẩm theo mã ID."""
    search_id = input("Nhập mã sản phẩm cần cập nhật (ví dụ LT01): ").upper()
    for p in products:
        if p['id'] == search_id:
            print(f"Đang sửa: {p['name']}")
            p['name'] = input("Nhập tên mới: ")
            p['brand'] = input("Nhập thương hiệu mới: ")
            p['price'] = int(input("Nhập giá mới: "))
            p['stock'] = int(input("Nhập số lượng mới: "))
            print("Cập nhật thành công!")
            return products
    print("Không tìm thấy sản phẩm!")
    return products

def delete_product(products):
    """Xóa sản phẩm theo mã ID."""
    search_id = input("Nhập mã sản phẩm cần xóa: ").upper()
    for i, p in enumerate(products):
        if p['id'] == search_id:
            confirm = input(f"Bạn có chắc muốn xóa {p['name']}? (y/n): ")
            if confirm.lower() == 'y':
                products.pop(i)
                print("Đã xóa sản phẩm.")
            return products
    print("Không tìm thấy sản phẩm!")
    return products

def search_product_by_name(products):
    """Tìm kiếm sản phẩm theo từ khóa tên."""
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]
    
    if results:
        display_all_products(results)
    else:
        print("Không tìm thấy sản phẩm nào phù hợp.")

def display_all_products(products):
    """Hiển thị danh sách sản phẩm dưới dạng bảng."""
    if not products:
        print("\nKho hàng trống.")
        return

    print("\n" + "="*70)
    print(f"{'Mã ID':<8} | {'Tên Sản Phẩm':<25} | {'Thương Hiệu':<15} | {'Giá':<10} | {'SL'}")
    print("-" * 70)
    for p in products:
        print(f"{p['id']:<8} | {p['name']:<25} | {p['brand']:<15} | {p['price']:<10} | {p['stock']}")
    print("="*70)
    import product_manager as pm

def main():
    # Tải dữ liệu khi bắt đầu chương trình
    products = pm.load_data()
    
    while True:
        print("\n===== QUẢN LÝ CỬA HÀNG LAPTOP POLY-LAP =====")
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Cập nhật sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm theo tên")
        print("6. Lưu và Thoát")
        
        choice = input("Chọn chức năng (1-6): ")
        
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '3':
            products = pm.update_product(products)
        elif choice == '4':
            products = pm.delete_product(products)
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '6':
            pm.save_data(products)
            print("Dữ liệu đã được lưu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()