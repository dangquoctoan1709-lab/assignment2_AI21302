def tinh_bmi(can_nang,chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)
    return bmi
# người 1
bmi_1 = tinh_bmi(70,1.75)
print(f"Chi so bmi cua nguoi 1 la: {bmi_1}")
# người 2
bmi_2 = tinh_bmi(55,1.60)
print(f"Chi so bmi cua nguoi 2 la: {bmi_2}")
def xep_loai_hoc_luc(diem_tb):
    if diem_tb >= 8:
        return "giỏi"
    elif diem_tb >= 6.5:
        return "khá"
    elif diem_tb >= 5:
        return "trung bình"
    else:
        return "yếu"
# chườn trình chính 
diem = float(input("Nhập điểm trung bình:"))
hoc_luc = xep_loai_hoc_luc(diem)
print(f"Điểm trung bình: {diem}")
print(f"Xếp loại học lực: {hoc_luc}") 
