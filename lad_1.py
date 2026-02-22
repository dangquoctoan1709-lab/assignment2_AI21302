# Bài 1
# Không gian mẫu
omega = {"A","B","AB","O"}

# Biến cố 
P_A = {"A","AB"} # Có kháng nguyên A
P_B = {"B","AB"} # Có kháng nguyên B
# Suy ra 
P_O = omega - (P_A | P_B) # Không có A và B
P_AB = P_A & P_B # Có cả A và B
print("Không gian mẫu:",omega)
print("Biến cố A(có kháng nguyên A):",P_A)
print("Biến cố B(có kháng nguyên B):",P_B)
print("Biến cố O(có nhóm máu O):",P_O)
print("Biến cố AB(có nhóm máu AB):",P_AB)

# Tính xác suất từ dữ liệu mẫu
# dữ liệu mẫu
data = ["A", "O", "B", "A", "AB", "O", "A", "B", "O", "O"]
# Tính xác suất nhóm máu O
P_O = data.count("O") / len(data)
print("\n dữ liệu mẫu:",data)
print("Xác suất chọn được người nhóm máu O;",P_O)

# Bài 2
import itertools

# Các chất và giá trị
suits = ["Cơ", "Rô", "Chuồn", "Bích"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# Không gian mẫu
omega = list(itertools.product(ranks, suits))
sample_space_size = len(omega)

# Biến cố A: rút được lá Át
P_A = [card for card in omega if card[0] == "A"]

# Biến cố B: rút được lá Cơ
P_B = [card for card in omega if card[1] == "Cơ"]

# Giao A và B: Át Cơ
P_A_andB = [card for card in P_A if card in P_B]

# Hợp A và B
P_A_union_B = list(set(P_A) | set(P_B))
# Xác suất
P_A = len(P_A) / sample_space_size
P_B = len(P_B) / sample_space_size
P_A_and_B = len(P_A_and_B) / sample_space_size
P_A_union_B = len(P_A_union_B) / sample_space_size

# In kết quả
print("P(A) – Rút được Át:", P_A)
print("P(B) – Rút được Cơ:", P_B)
print("P(A ∩ B) – Át Cơ:", P_A_and_B)
print("P(A ∪ B) – Át hoặc Cơ:", P_A_union_B)