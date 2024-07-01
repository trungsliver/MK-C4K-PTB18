# Vòng lặp hữu hạn - Vòng lặp for

    # Hàm range(n) => lặp từ 0 đến n-1
# for i in range(11):
#     print(i)

    # Hàm range(start, stop, step)
        # start: số bắt đầu (không bắt buộc)
        # stop: số kết thúc (bắt buộc)
        # step: bước nhảy (không bắt buộc)
# for i in range(1, 11, 2):
#     print(i)

# Ex1: range(stop)
# for i in range(5):
#     print(i)

# Ex2: range(start,stop)
# for i in range(10,16):
#     print(i)

# Ex3: range(start, stop, step)
# for i in range (10, 21, 2):
#     print(i)

# Đề bài: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))

# if a <= b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(b, a+1):
#         print(i)

# Đề bài: Nhập 2 số nguyên a và b. Tính tổng các số chẵn trong khoảng [a, b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0

# for i in range(a, b+1):
#     if i%2 == 0:
#         sum = sum + i
# print(f'Tổng các số chẵn trong khoảng [{a}, {b}] là: {sum}')

# # Sử dụng random
#     # Khai báo thư viện
# import random 
#     # Cú pháp sử hàm trong thư viện: [Tên thư viện].[Tên hàm]
# rd = random.randint(1,10)
# print(rd)

# print('Bảng cửu chương', rd)
# for i in range(1,11):
#     print(f'{rd} * {i} = {rd*i}')

# Đề bài: In bảng cửu chương từ 1 đến 5
    # Thứ tự index trong vòng lặp: i, j, k
# for i in range(1,11):
#     print("\nBảng cửu chương", i)
#     for j in range(1,11):
#         print(f'{i} * {j} = {i*j}')

# Vòng lặp vô hạn  vòng lặp while
# i = 1
# while i < 6:
#     print(i)
#     i = i + 1

# Đề bài 1: Nhập số nguyên n trong khoảng [0,100]
# nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập số tronng khoảng [0,100]: '))

# while n < 0 or  n > 100:
#     print('Bạn đã nhập sai, vui lòng nhập lại!')
#     n = int(input('\nNhập số tronng khoảng [0,100]: '))
# print('Nhập dữ liệu thành công!')

# Đề bài 2: Nhập vào số nguyên dương n
# Tính tổng tất cả các chữ số của n
n = int(input('Nhập số nguyên dương n: '))
sum = 0
while n > 0:
    sum = sum + n%10
    n = n // 10
print(f'Tổng các chữ số của {n} là: {sum}')
