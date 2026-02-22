import json

# 1) load_data(): Đọc dữ liệu từ file products.json
def load_data():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Trả về danh sách rỗng nếu file chưa tồn tại lần đầu
        return []
    except Exception as e:
        print(f"Có lỗi khi đọc file: {e}")
        return []

# 2) save_data(products): Ghi dữ liệu vào file
def save_data(products):
    try:
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Có lỗi khi lưu file: {e}")

# 3) add_product(products): Thêm sản phẩm mới
def add_product(products):
    print("\n--- Thêm sản phẩm mới ---")
    # Tự động tạo mã sản phẩm (ví dụ: LT01, LT02...) dựa trên số lượng hiện có
    id_new = f"LT{len(products) + 1:02d}"
    
    name = input("Nhập tên laptop: ")
    brand = input("Nhập thương hiệu: ")
    while True:
        try:
            price = int(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng tồn kho: "))
            break
        except ValueError:
            print("Giá và số lượng phải là số nguyên!")

    new_product = {
        "id": id_new,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    print(f"Đã thêm thành công sản phẩm với mã: {id_new}")
    return products

# 4) update_product(products): Cập nhật thông tin
def update_product(products):
    id_find = input("\nNhập mã sản phẩm cần cập nhật: ").upper()
    for p in products:
        if p['id'] == id_find:
            print("Tìm thấy! Nhập thông tin mới (để trống nếu không muốn đổi):")
            new_name = input(f"Tên mới ({p['name']}): ")
            new_brand = input(f"Thương hiệu mới ({p['brand']}): ")
            new_price = input(f"Giá mới ({p['price']}): ")
            new_qty = input(f"Số lượng mới ({p['quantity']}): ")

            if new_name: p['name'] = new_name
            if new_brand: p['brand'] = new_brand
            if new_price: p['price'] = int(new_price)
            if new_qty: p['quantity'] = int(new_qty)
            
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy mã sản phẩm này.")

# 5) delete_product(products): Xóa sản phẩm
def delete_product(products):
    id_find = input("\nNhập mã sản phẩm cần xóa: ").upper()
    for p in products:
        if p['id'] == id_find:
            products.remove(p)
            print("Đã xóa sản phẩm.")
            return
    print("Mã sản phẩm không tồn tại.")

# 6) search_product_by_name(products): Tìm kiếm theo từ khóa
def search_product_by_name(products):
    keyword = input("\nNhập từ khóa tên sản phẩm cần tìm: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]
    
    if results:
        display_all_products(results)
    else:
        print("Không tìm thấy sản phẩm nào phù hợp.")

# 7) display_all_products(products): Hiển thị danh sách
def display_all_products(products):
    if not products:
        print("\n[Kho hàng trống]")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<10} | {'Tên sản phẩm':<25} | {'Thương hiệu':<15} | {'Giá':<10} | {'SL'}")
    print("-" * 70)
    for p in products:
        print(f"{p['id']:<10} | {p['name']:<25} | {p['brand']:<15} | {p['price']:<10} | {p['quantity']}")
    print("="*70)