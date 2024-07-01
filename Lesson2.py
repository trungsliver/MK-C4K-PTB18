# Biến số - Phép gán
    # Biến số: dùng để lưu trữ dữ liệu, có thể thay đổi trong khi lập trình
    # Phép gán: [Tên biến] = [Giá trị]
x = 10
a, b, c = 5, 6, 7
# print(x, a, b, c)

# Data types - Kiểu dữ liệu
    # String - chuỗi ký tự / xâu ký tự
name = 'Bui Duc Trung'
    # Int - số nguyên
age = 25
    # Float - số thực
score = 8.9
    # Bool/Boolean - True/False - Đúng/Sai
male = True

# Ôn tập 4 kiểu print()
    # Cách 1: Dùng dấu cộng (nối chuỗi, chỉ áp dụng khi data type = string)
# print('Họ tên: ' + name)
    # Cách 2: Dùng dấu phẩy (không phân biệt data types, dữ liệu cách nhau 1 khoảng trắng)
# print('Tuổi:', age)
    # Cách 3: Dùng f trước dấu nháy (truyền dữ liệu vào string thông qua ngoặc nhọn {})
# print(f'Điểm: {score}')
    # Cách 4: Dùng 3 dấu nháy kép để in trên nhiều dòng
# print("""Giới tính nam:""", male)

# Quy tắc đặt tên biến
    # Chỉ bao gồm chữ, số 0-9, ký tự gạch dưới
    # Không được bắt đầu bằng số
    # Phân biệt chữ hoa và chữ thường
    # Không được trùng từ khóa

    # VD đúng: ductrung, long123, l_o_n_g, _name6
    # VD sai: trung$$, 123long, for

# Cách kiểm tra kiểu dữ liệu - type()
# print(type(name), type(age), type(score), type(male))

# Xác định kiểu dữ liệu khi nhập (DataTypes - Input)
# name = str(input('Họ tên: '))
# age = int(input('Tuổi: '))
# score = float(input('Điểm: '))
# male = bool(input('Giới tính nam: '))

# Chuyển đổi giữa các kiểu dữ liệu
    # int(): có thể chuyển đổi số thực hoặc chuỗi chứa số nguyên
    # float(): chuyển đối số nguyên, chuỗi chứa số thực
    # str(): có thể chuyển đổi tất cả các loại dữ liệu khác
# x = 5
# y = float(x)
# print(x, y)
# print(type(x), type(y))

# Các phép toán: + - * / % // **

# Bài tập
print('Chào mừng bạn đến với Currency Converter - chuyển đổi tiền tệ')
dollar = int(input("Vui lòng nhập số tiền cần chuyển (đô la Mỹ): $"))
print('Số tiền sẽ được quy đổi ra Việt Nam Đồng (VNĐ)')
vnd = dollar * 25000
vnd = int(vnd)
print(f"${dollar} quy đổi ra được {int(vnd)}đ")

