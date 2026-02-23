import json

FILE = "products.json"

def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_product(data):
    name = input("Tên: ")
    brand = input("Hãng: ")
    price = int(input("Giá: "))
    quantity = int(input("Số lượng: "))
    
    new_id = 1 if not data else data[-1]["id"] + 1
    data.append({
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    })
    print("Đã thêm thành công!")
    return data

def update_product(data):
    id_update = int(input("Nhập ID cần cập nhật: "))
    for p in data:
        if p["id"] == id_update:
            p["name"] = input(f"Tên mới ({p['name']}): ") or p["name"]
            p["brand"] = input(f"Hãng mới ({p['brand']}): ") or p["brand"]
            p["price"] = int(input(f"Giá mới ({p['price']}): ") or p["price"])
            p["quantity"] = int(input(f"Số lượng mới ({p['quantity']}): ") or p["quantity"])
            print("Đã cập nhật!")
            return data
    print("Không tìm thấy ID!")
    return data

def delete_product(data):
    id_delete = int(input("Nhập ID cần xóa: "))
    for p in data:
        if p["id"] == id_delete:
            data.remove(p)
            print("Đã xóa!")
            return data
    print("Không tìm thấy ID!")
    return data

def search_product_by_name(data):
    name_search = input("Nhập tên sản phẩm cần tìm: ").lower()
    results = [p for p in data if name_search in p["name"].lower()]
    display_all_products(results)

def display_all_products(data):
    if not data:
        print("Danh sách trống!")
    else:
        for p in data:
            print(p)