# Cấu trúc xấu ký tự
# name = 'Phuong Thuy'
# print(len(name))
# for item in name:
#     print(item)

#   # Xâu con 
# str1 = 'ductrung123456'
# str2 = 'ductrung'
# str3 = '789'
#     # Kiểm tra xâu con: hàm in()
# print(str2 in str1)
# print(str3 in str1)
#     # Kiểm tra vị trí của xâu con: find()
# print(str1.find(str2))
# print(str1.find(str3))
#         # Cấu trúc đầy đủ hàm find(): [Xâu mẹ].find([xâu con], start, stop)
# print(str1.find(str2, 0, 10))
# print(str1.find(str2, 5, 10))

    # Slicing - cắt chuỗi
# name = 'Duy Long'
# print(name[1:4])        # uy
# print(name[:3])        # Duy
# print(name[4:])        # Long

# a = [1,2,3,4,5,6,7,8,9]
# b = a[:-1]
# print(b)

    # Strip() - Xóa khoảng trắng ở đầu và cuối 
# name = '     hihi        '
# print(name.strip())

# replace() - thay thế 1 đoạn chuỗi bằng chuỗi khác
# name = 'Duy Long'
# name2 = name.replace('Long', 'Thúy')
# print(name2)
#     # Thay thế nhiều giá trị
# name = 'Duy Long Long Long Long Long Long'
# name2 = name.replace('Long', 'Thúy')
# name3 = name.replace('Long', 'Thúy', 2)
# print(name3)

    # join() - kết hợp chuỗi
# name = ['Khanh', 'Trung', 'Long', 'Thuy']
# print(' '.join(name))

    # split() - tách chuỗi
a = '1 2 3 4 5 6 7 8 9'
b = 'a,s,d,f,g,h,j,k,l'
arr = a.split()
# arr = b.split(',')
print(arr)

# user = 'admin:123456'
# username, password = user.split(':')
# print(username, password)

# Chuyển đổi kiểu dữ liệu trong danh sách
    # Cách 1:
arr2 = []
for item in arr:
    arr2.append(int(item))
print(arr2)

    # Cách 2:
arr3 = [int(item) for item in arr]
print(arr3)

# Bài tập
#     # Tính tổng phần tử danh sách
#         # Cách cũ:
# tong = 0
# for item in arr2:
#     tong = tong + item
#         # Cách mới
# tong = sum(item for item in arr2)

# print(tong)

#     # Tính tổng phần tử chẵn danh sách
#         # Cách cũ:
# tong = 0
# for item in arr2:
#     if item%2 == 0:
#         tong = tong + item

#         # Cách mới
# tong = sum(item for item in arr2 if item%2==0)

# print('Tổng phần tử chẵn:', tong)

#     # Đếm phần tử chẵn trong danh sách
# count = sum(1 for item in arr2 if item%2==0)
# print('số lượng lượng phần tử chẵn:', count)

# -------------------------Luyện tập-----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ
# ho = input('Nhập họ: ')
# ten = input('Nhập tên: ')
# ho = ho.strip()
# ten = ten.strip()
# print(ho, ten)

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
# date1 = input('Nhập chuỗi dạng dd/mm/yyyy: ')
# date2 = date1.replace('/', ' tháng ', 1)
# date3 = date2.replace('/', ' năm ', 1)
# print(date3)

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc
username = 'ductrung'
password = 'hihi123'

info = input('Nhập thông tin dạng username:password: ')

while (':' not in info):
    print('Nhập sai định dạng, vui lòng nhập lại!')
    info = input('\nNhập thông tin dạng username:password: ')

info_split = info.split(':')

while info_split[0] != username or info_split[1] != password:
    print('Nhập sai thông tin, vui lòng nhập lại')
    info = input('\nNhập thông tin dạng username:password: ')
    while (':' not in info):
        print('Nhập sai định dạng, vui lòng nhập lại!')
        info = input('\nNhập thông tin dạng username:password: ')
    info_split = info.split(':')
print("Đăng nhập thành công!")
