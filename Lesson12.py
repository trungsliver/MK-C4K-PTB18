# Ôn tập

# Bài 1: Nhập từ bàn phím điểm trung bình của học sinh. Hãy xếp hạng học lực của học sinh đó, biết rằng:
# Giỏi: [8,10], Khá: [6.5, 8), TB: [5, 6.5), Yếu: [0, 5)
# Nhập điểm trung bình từ bàn phím
# diem_trung_binh = float(input("Nhập điểm trung bình: "))

# # Xếp hạng học lực
# if diem_trung_binh >= 8:
#     print("Học lực: Giỏi")
# elif diem_trung_binh >= 6.5:
#     print("Học lực: Khá")
# elif diem_trung_binh >= 5:
#     print("Học lực: Trung bình")
# else:
#     print("Học lực: Yếu")


# # Bài 2: Nhập từ bàn phím số giây cần chuyển đổi. In ra màn hình thời gian sau chuyển đổi, định dạng: giờ - phút - giây
# # VD: 3661s = 1h 1m 1s
# # Nhập số giây từ bàn phím
# seconds = int(input("Nhập số giây cần chuyển đổi: "))

# # Chuyển đổi số giây sang giờ, phút, giây
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# seconds = seconds % 60

# # In ra màn hình thời gian sau chuyển đổi
# print(f"{hours}h {minutes}m {seconds}s")


# Bài 3: Nhập 2 số nguyên a và b từ bàn phím
# Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
# Yêu cầu 2: Tính tổng các số chẵn trong khoảng vừa in
# Yêu cầu 3: Tính trung bình cộng các số nguyên trong khoảng trên

# Bài 4: Viết hàm/chương trình con kiểm tra 1 số có phải là số nguyên tố hay không, biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó.
# In ra số nguyên tố trong khoảng [10,100].

# Bài 5: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
# Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
# Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
# Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.
# Yêu cầu 4: Sắp xếp các phần tử trong danh sách num_list theo thứ tự từ lớn đến nhỏ.

# Bài 6: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2. 
# Yếu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
# Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
# Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2

# Bài 7: Hãy nhập từ bàn phím họ tên của bạn.
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
# Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
# Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu

# Dãy Fibonacci: 1 1 2 3 5 8 13

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(0, 10):
    print(fibonacci(i), end = ' ')