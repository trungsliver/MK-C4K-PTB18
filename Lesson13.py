# Quy tắc đặt tên: [Lớp]_[Tên]_hackathon.py
# VD: PTB18_DucTrung_hackathon.py

# =============== CHỮA BÀI =============

# Câu 1:
    # Tạo 2 số nguyên ngẫu nhiên
import random
a = random.randint(1, 100)
b = random.randint(1, 100)
    # Hiển thị kết quả
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ^ {b} = {pow(a, b)}")
print(f"{a} // {b} = {a // b} du {a % b}")

# Câu 2:
age_list = []
    # Nhập tuổi và thêm vào danh sách
for i in range(3):
    age = int(input(f"Nhập tuổi người thứ {i+1}: "))
    age_list.append(age)
    # Tìm vị trí người nhỏ tuổi nhất:
for i in range(len(age_list)):
    if age_list[i] == min(age_list):
        min_index = i + 1
    # Hiển thị kết quả
print(f"Người thứ {min_index} nhỏ tuổi nhất: {min(age_list)} tuổi")

# Câu 3: 
    # Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print('Vui lòng nhập 1 số nguyên dương!')
    n = int(input("\nNhập số nguyên dương n: "))
    # Hiển thị các số lẻ từ 1 đến n
print(f'Các số lẻ từ 1 đến {n} là:')
for x in range(n + 1):
    if x % 2 == 1:
        print(x, end = ' ')

# Câu 4:
n = int(input("Nhập 1 số nguyên: "))
    # Cách 1:
print(f"Giá trị tuyệt đối của {n} là: {abs(n)}")
    # Cách 2:
if n < 0: 
    n = -n
    print(f"Giá trị tuyệt đối của {-n} là: {n}")
else:
    print(f"Giá trị tuyệt đối của {-n} là: {n}")

# Câu 5:
    # Tạo danh sách ngẫu nhiên gồm 5 phần tử
import random
num_list = [random.randint(1,50) for i in range(5)]
print(num_list)
    # Hiển thị số nhỏ nhất của danh sách
print('Số nhỏ nhất của danh sách:', min(num_list))
    # Hiển thị số lớn nhất của danh sách
print('Số nhỏ nhất của danh sách:', max(num_list))
    # Tổng giá trị các số lẻ của danh sách
sum_odd = 0
for num in num_list:
    if num%2 == 1:
        sum_odd += num
print('Tổng các số lẻ trong danh sách:', sum_odd)

# Câu 6:
    # Nhập và tách thành danh sách chiều cao
h_input = input('Nhập danh sách chiều cao (cách bởi khoảng trắng): ')
h_list = h_input.split()
    # Chuyển đổi kiểu dữ liệu các phần tử trong danh sách
height_list = [float(item) for item in h_list]
print(height_list)
    # Đếm số lượng người nhỏ hơn 1.5m
count = 0
for item in height_list:
    if item < 1.5:
        count += 1
    # Hiển thị kết quả ra màn hình
if count == 0: 
    print('Không có người nào nhỏ hơn 1.5m')
else:
    print(f'Số lượng người nhỏ hơn 1.5m là: {count}')

# Bài 7:
    # Khởi tạo danh sách điểm
score_list = [8, 8, 8, 9, 9]

    # Tạo hàm tính điểm TB
def avg_score(arr):
    # Tính tổng điểm (điểm cuối hệ số 2):
    sum_arr = sum(arr) + arr[-1]
    # Tính điểm trung bình
    avg = sum_arr / (len(arr)+1)
    # Làm tròn điểm trung bình
    avg = round(avg, 2)
    return avg

    # Hiển thị kết quả
print(f'Điểm trung bình của {score_list} là: {avg_score(score_list)}')