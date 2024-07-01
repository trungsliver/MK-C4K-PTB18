# Câu điều kiện
    # Câu điều kiện dạng thiếu:
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi.')

    # Câu điều kiện dạng đủ:
# a = int(input('Hãy nhập 1 số nguyên: '))
# if a % 5 == 0:
#     print(a, 'chia hết cho 5.')
# else:
#     print(a, 'không chia hết cho 5.')

    # Câu điều kiện đa nhánh
        # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
# diem = float(input('Hãy nhập điểm của bạn: '))

# if diem >= 8 and diem <= 10:
#     print('Xếp loại: Giỏi')
# elif diem >= 6.5 and diem < 8:
#     print('Xếp loại: Khá')
# elif diem >= 5 and diem < 6.5:
#     print('Xếp loại: Trung Bình')
# elif diem >= 0 and diem < 5:
#     print('Xếp loại: Yếu')
# else: 
#     print('Bạn đã nhập sai điểm.')

# Bài tập: Nhập 1 số nhuyên từ bàn phím.
# Nếu đó là số chẵn, in ra màn hình 'đây là số chẵn', các trường hợp còn lại in ra 'đây là số lẻ'

# num = int(input('Nhập 1 số nguyên bất kì: '))
# if num%2 == 0:
#     num *= -1; 
#     # num = num * -1
# else:
#     print('Đây là số lẻ')

# Bài tập: Nhập 1 số thực từ bàn phím.
# Nếu đó là số âm, in ra giá trị tuyệt đối ra màn hình. Các trường hợp còn lại thì in ra
# màn hình kết quả 

# Bài tập: Viết chương trình nhập số điểm của 3 bạn học sinh, 
# in ra màn hình bạn có điểm thấp nhất và bạn có điểm cao nhất.
a = float(input("Input A's score: "))
b = float(input("Input B's score: "))
c = float(input("Input C's score: "))

if a == b and a == c:
    print('all equal')
else:
    if a >= b and a >= c:
        print('Max: A')
    if b >= a and b >= c:
        print('Max: B')
    if c >= b and c >= a:
        print('Max: C')
    # min: write here