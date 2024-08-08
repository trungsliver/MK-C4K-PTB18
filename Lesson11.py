# Bổ sung các thao tác với xâu - chuỗi ký tự
# import string
# name = 'Duc Trung vIp PrO'
# name2 = name.upper()
# name2 = name.lower()
# name2 = string.capwords(name)
# print(name2)

# Hàm - chương trình con
import random
cdai = []
crong = []
for i in range(10):
    cdai.append(random.randint(10, 20))
    crong.append(random.randint(1, 10))
# print(cdai)
# print(crong)

# Đề bài: Tính chu vi HCN với
    # cdai[5] crong[10]
    # cdai[3] crong[2]

# s1 = (cdai[5] + crong[10]) * 2

    # Hàm không có giá trị trả về
def hello():
    print('Xin chào Đức Trung')
    print('Xin chào Quốc Khanh')
# hello()

    # Hàm có giá trị trả về
def hello2():
    a = 10
    b = 5
    return a+b
# print(hello2())

    # Truyền dữ liệu cho hàm
def avg2(a, b):
    return (a+b)/2

# print(avg2(10,1))

# Ví dụ: Viết chương trình con tính giai thừa 1 số nguyên 
def giaiThua(n):
    gt = 1
    for i in range(1, n+1):
        gt = gt * i
    return gt
# print(giaiThua(6))

# Bài 1: Viết chương trình con tìm giá trị tuyệt đối của 1 số thực
abc = 100
def abs2( n:float ):
    if n >= 0:
        return n
    else:
        return -n
# print(abs2(abc))

# Bài 2: Viết chương trình con tìm vị trí của phần tử lớn nhất trong danh sách
# print(cdai)
def index_maxArr(arr):
    for i in range(len(arr)):
        if arr[i] == max(arr):
            return i
# print('Index of max value:' ,index_maxArr(cdai))

#  Bài tập Đăng nhập - Đăng ký
users = ['admin:123456', 'admin2:123456']

    # Đăng ký:
        # YC1: Nhập đầy đủ nội dung username, password (không tính khoảng trắng)
        # YC2: username đăng ký không được trùng với username đã có trong danh sách
        # YC3: Nếu đăng ký thành công thì thêm user mới vào danh sách 
        # YC4: Hiển thị thông báo đăng ký thành công/không thành công

    # Đăng ký:
        # YC: Tài khoản - mật khẩu trùng nhau
def register():
    # Nhập thông tin
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = True

    # Xóa khoảng trắng 
    username = username.strip()
    password = password.strip()

    # Nếu để trống username hoặc password thì không đki được
    if username == '' or password == '':
        check = False
        print('Nhập thiếu thông tin')
    else:
        # Duyệt tài khoản trong danh sách users
        for user in users:
            # Chia 1 user thành 2 phần: username, password
            stored_username, stored_password = user.split(':', 1)
            # Kiểm tra trùng tên tài khoản
            if username == stored_username:
                check = False
                print('Tài khoản đã tồn tại')

    # Kiểm tra xem có đăng ký thành công không
    if check == True:
        print('Đăng ký thành công')
        # Thêm tài khoản vào danh sách users
        new_acc = username + ':' + password
        users.append(new_acc)
    else:
        print('Đăng ký không thành công')
    
# Đăng nhập
def login():
    # Nhập thông tin
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = False

    # Xóa khoảng trắng 
    username = username.strip()
    password = password.strip()

    # Kiểm tra đăng nhập
    for user in users:
        stored_username, stored_password = user.split(':', 1)
        # Bắt buộc phải trùng cả username và password của 1 user trong danh sách
        if username == stored_username and password == stored_password:
            check = True

    # Kiểm tra đăng nhập thành công
    if check == True:
        print('Đăng nhập thành công')
    else:
        print('Đăng nhập không thành công')

import os
os.system('cls')
# Menu
def main():
    while True:
        print('\n----------LESSON 11----------')
        print('1. Đăng ký')
        print('2. Đăng nhập')
        print('3. Xóa màn hình')
        print('4. Thoát')
        print('----------------------------')
        choice = int(input('Nhập lựa chọn của bạn: '))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            os.system('cls')
        elif choice == 4:
            break
        else:
            print('Lựa chọn không hợp lệ')
main()