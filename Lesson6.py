# CRUD: Create - Read - Update - Delete
# Danh sách: aray - list

# Create - Khởi tạo danh sách
arrHS = ['Phương Thúy', 'Duy Long', 'Đức Trung', 'Quốc Khanh']

    # Hàm len() - trả về kích thước / độ dài
# name = 'Doan Quoc Khanh'
# print(len(arrHS))

# Read - Đọc/Hiển thị các phần tử của danh sách
    # Hiện các phần tử bằng chỉ số index (đếm từ 0)
# print(arrHS[0])
    # Hiện phần tử cuối cùng của danh sách
# print(arrHS[-1])

    # Hiển thị toàn bộ phần tử danh sách
        # Cách 1: áp dụng khi lấy cả index và value
# for i in range(len(arrHS)):
#     print(f'[{i}] {arrHS[i]}')

        # Cách 2: chỉ áp dụng khi muốn lấy value
# for i in arrHS:
#     print(i)

        # Cách 3: 
# for index, item in enumerate(arrHS):
#     print(f'[{index + 1}] {item}')

        # Cách 4: Để test
# print(arrHS)

# update - Chỉnh sửa phần tử trong danh sách
    # Thêm phần tử vào cuối danh sách - append()
arrHS.append('Pham Ly')

    # Thêm phần tử vào vị trí chỉ định - insert()
arrHS.insert(2, 'Imposter')

    # Chỉnh sửa phần tử trong danh sách
arrHS[2] = 'Imposter 666'
# print(arrHS)

# Delete - Xóa phần tử trongh danh sách
    # Xóa phần tử bằng giá trị - remove()
arrHS.remove('Pham Ly')

    # Xóa phần tử bằng index - pop()
arrHS.pop(2)

    # Xóa toàn bộ phần tử của danh sách - clear()
arrHS.clear()
# print(arrHS)

arrNum = [5, 78, 31, 12, 62, 45]
# print(arrNum)
# Sắp xếp phần tử trong danh sách - sort()
    # Sắp xếp từ nhỏ tới lớn
arrNum.sort()
    # Sắp xếp từ lớn tới nhỏ
arrNum.sort(reverse=True)

# print(arrNum)

# Bài tập 1: Viết một chương trình cho phép người dùng nhập n phần tử
# Sau đó thêm các phần tử vừa nhập vào mảng và in ra màn hình mảng đó.
# A = []
# n = int(input('Số lượng phần tử muốn nhập: '))

# for i in range(n):
#     item = int(input(f'Nhập phần tử thứ {i+1}: '))
#     A.append(item)
# print(A)

# Bài tập: tìm phần tử chung của 2 danh sách
# arr1 = []
# arr2 = []
#     # Thêm phần tử vào danh sách arr1
# for i in range(1,16):
#     arr1.append(i)
#     # Thêm phần tử vào danh sách arr2
# for i in range(10,26):
#     arr2.append(i)
#     # Hiện phần tử của 2 danh sách
# print(arr1)
# print(arr2)
#     # arr3 sẽ dùng để lưu các phần tử chung của arr1 và arr2
# arr3 = []

# for item1 in arr1:
#     for item2 in arr2:
#         if item1 == item2:
#             arr3.append(item1)
# print('Phần tử chung cả 2 arr:' ,arr3)

# Bài tập 3: cho danh sách gồm phần tử từ 1 đến 15
# In ra các số chẵn trong danh sách
# for item in arr1:
#     if item % 2 == 0:
#         print(item)

# Bài tập 4: Tính tổng phần tử của danh sách
arr = [1,2,3,4]
sum2 = 0
for item in arr:
    sum2 = sum2 + item
    # sum += item
print('Tổng các phần tử của danh sách là:', sum2)
print('Tổng các phần tử của danh sách là:', sum(arr))

