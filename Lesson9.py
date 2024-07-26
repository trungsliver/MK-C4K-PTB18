# # 4 kiểu print
# name = 'Bui Duc Trung'
# age = 25
#     # Cách 1: dùng dấu +
# print(name + str(age))
#     # Cách 2: dùng dấu ,
# print(name, age)
#     # Cách 3: truyền dữ liệu vào string
# print(f'Họ tên: {name}. Tuổi: {age}')
#     # Cách 4: In dữ liệu trên nhiều dòng
# print(f"""
# Họ tên: {name}
# Tuổi: {age}
# """)

# Data types - kiểu dữ liệu
    # String: chuỗi, xâu ký tự
    # Int: số nguyên
    # Float: số thực
    # Bool/Boolean: True/False - Đúng/Sai
    # Xác định kiểu dữ liệu: type()

# Các phép toán:
    # Thông thường: + - * /
    # Chia lấy dư: %
    # Chia lấy nguyên: //
    # Lũy thừa: **

# Câu điều kiện:
    # Các phép so sánh: ==, !=, <, >, <=, >=
    # Các phép toán: and, or, not
    # Cấu trúc/dạng:
        # Dạng thiếu: if
        # Dạng đủ: if else
        # Dạng đa nhánh: if elif elif ... else

# Vòng lặp hữu hạn - Vòng lặp for
    # range(n): chạy từ 0 đến n-1
    # range(start, stop, step):

# Vòng lặp vô hạn - Vòng lặp while
    # while <điều kiện>: lặp đến khi điều kiện sai

# Danh sách: array/list - CRUD
    # C - Create: PTB11 = ['KA', 'MT', 'DT']
    # R - Read: Duyệt danh sách
        # Cách 1: for i in range(len(arr))
        # Cách 2: for item in arr
        # Cách 3: for index, item in enumerate(arr)
        # Cách 4: print(arr)
    # U - Update:
        # append(item): thêm phần tử vào cuối danh sách
        # insert(index, item): thêm phần tử vào vị trí chỉ định
        # arr[i] = new_value
    # D - Delete:
        # remove(item): xóa phần tử bằng giá trị
        # pop(index): xóa phần tử qua vị trí
        # clear(): xóa tất cả phần tử
    # Sắp xếp:
        # sort(): thứ tự từ bé đến lớn
        # sort(reverse=True): thứ tự từ lớn đến bé

# Đề bài: Nhập 1 số nguyên dương n từ bàn phím. Hãy kiểm tra xem n có phải số nguyên tố không?
    # Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó.
# n = int(input('Nhập 1 số nguyên: '))
for n in range(1,101):
    count = 0
    for i in range (1, n+1): 
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, 'là số nguyên tố')
    else:
        print(n, 'không là số nguyên tố')
    
# Quy tắc đặt tên: [Tên lớp]_[Họ tên]_CP2.py
# VD: PTB18_DuyLong_CP2.py