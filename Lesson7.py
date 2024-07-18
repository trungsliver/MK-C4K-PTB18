# Chữa BTVN
    # Bài 1: Nhập số nguyên dương n
        # Tính tổng số chẵn từ 1 đến n và in ra màn hình.
# n = int(input('Nhập số nguyên dương n: '))
# sum = 0

# while n <=0 :
#     print('Bạn đã nhập sai, vui lòng nhập lại')
#     n = int(input('\nNhập số nguyên dương n: '))
# print('Nhập dữ liệu thành công')

# for i in range (1, n+1):
#     if i % 2 == 0:
#         sum = sum + i
# print(f'Tổng các số chẵn từ 1 đến {n} là: {sum}')

    # Bài 2:
# n = int(input('Nhập số nguyên dương n: '))
# sum = 0
# i = 1

# while n <=0 :
#     print('Bạn đã nhập sai, vui lòng nhập lại')
#     n = int(input('\nNhập số nguyên dương n: '))
# print('Nhập dữ liệu thành công')

# while sum <= n:
#     print(i, end=' ')
#     sum = sum + i
#     i = i+1 

# Bài 3: Cho 1 danh sách, tìm min max
A = [5,2,3,15,1,6,7,11,9,10,8,12,13,14,4]

    # Cách 1:
# min1, max1 = A[0], A[0]
# for item in A:
#     if item < min1:
#         min1 = item
#     if item > max1:
#         max1 = item
# print('Số lớn nhất:', max1)
# print('Số nhỏ nhất:', min1)

    # Cách 2:
# A.sort()
# print('Số lớn nhất:', A[-1])
# print('Số nhỏ nhất:', A[0])

    # Cách 3:
# print('Số lớn nhất:', max(A))
# print('Số nhỏ nhất:', min(A))

    # Tìm vị trí số nhỏ nhất và lớn nhất trong mảng
# num_max, num_min = A[0], A[0]
# index_max, index_min = 0, 0
#         # Cách 1:
# for i in range(len(A)):
#     if A[i] < num_min:
#         num_min = A[i]
#         index_min = i
#     if A[i] > num_max:
#         num_max = A[i]
#         index_max = i
# print('Vị trí số lớn nhất:', index_max)
# print('Vị trí số nhỏ nhất:', index_min)

    # Cách 2:
# for i in range(len(A)):
#     if A[i] == max(A):
#         index_max = i
#     if A[i] == min(A):
#         index_min = i
# print('Vị trí số lớn nhất:', index_max)
# print('Vị trí số nhỏ nhất:', index_min)

#  Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    #  Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
# import random
# num = random.randint(0,100)
# print('Số cần tìm (bí mật):', num)
# n = int(input('Nhập dự đoán của bạn: '))
# count = 1
# while n != num:
#     if n < num:
#         print(n, 'nhỏ hơn số bí ẩn')
#     else:
#         print(n, 'lớn hơn số bí ẩn')
#     n = int(input('\nNhập dự đoán của bạn: '))
#     count = count + 1
# print('Dự đoán thành công !!!')
# print('Số lần dự đoán:', count)

# Đề bài: Viết chương trình quản lý bán hàng với các thao tác CRUD

    # Khai báo danh sách sản phẩm và giỏ hàng
products = ['Quần', 'Áo', 'Laptop', 'Người', 'Đồ ăn', 'Vũ khí']
cart = []

    # Chọn chức năng
while True:
    print('\n========== SHOPPING CART ==========')
    print('1. Xem danh sách sản phẩm.')
    print('2. Xem giỏ hàng.')
    print('3. Thêm sản phẩm vào giỏ hàng.')
    print('4. Xóa sản phẩm khỏi giỏ hàng.')
    print('5. Thoát.')
    print('===================================')
    choice = int(input('Hãy nhập lựa chọn của bạn: '))
    
    # Chức năng 1:
    if choice == 1:
        print('\n========== SẢN PHẨM ==========')
        for i in range(len(products)):
            print(f'[{i+1}] {products[i]}')
        print('==============================')

    # Chức năng 2
    elif choice == 2:
        if not cart:
            print('Giỏ hàng trống.')
        else:
            print('\n========== GIỎ HÀNG ==========')
            for i in range(len(cart)):
                print(f'[{i+1}] {cart[i]}')
            print('=============================')
    # Chức năng 3
    elif choice == 3:
        print('\n========== THÊM SẢN PHẨM VÀO GIỎ HÀNG ==========')
        addPro = int(input('Nhập chỉ số sản phẩm muốn thêm vào giỏ hàng: '))
        addPro = addPro - 1 # Đưa index đúng với danh sách
        if abs(addPro) < len(products):
            cart.append(products[addPro])
            print('Thêm sản phẩm thành công!')
        else:
            print('Thêm sản phẩm thất bại!')
        print('============================================')

    # Chức năng 4
    elif choice == 4:
        print('\n========== XÓA SẢN PHẨM KHỎI GIỎ HÀNG ==========')
        delPro = int(input('Nhập chỉ số sản phẩm muốn xóa khỏi giỏ hàng: '))
        delPro = delPro - 1 # Đưa index đúng với danh sách
        if abs(delPro) < len(products):
            cart.pop(delPro)
            print('Xóa sản phẩm thành công!')
        else:
            print('Xóa sản phẩm thất bại!')
        print('============================================')
    else:
        break