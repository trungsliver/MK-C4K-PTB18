# Lập trình hướng đối tương - OOP
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender='male'):
        # name, age, gender là thuộc tính
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức - Hành động của object
    def __str__(self):
        return f'{self.name} - {self.age} tuổi - {self.gender}'
    
    def greeting(self):
        print(f'{self.name} xin chào tất cả mọi người')

    # Cập nhật thông tin
    def change_gender(self, new_gender):
        self.gender = new_gender

class Animal:
    def __init__(self, ten, giong, mau_sac, tuoi, can_nang):
        self.ten = ten
        self.giong = giong
        self.mau_sac = mau_sac
        self.tuoi = tuoi
        self.can_nang = can_nang

    def __str__(self) -> str:
        return f'{self.ten} - {self.giong} - {self.mau_sac} - {self.tuoi} - {self.can_nang}'
    
    def doi_mau_long(self, new_color):
        self.mau_sac = new_color

import math
class HinhThoi():
    def __init__(self, d1:float, d2):
        self.d1 = d1
        self.d2 = d2
        self.canh = math.sqrt((d1/2)**2 + (d2/2)**2)

    def __str__(self):
        return f'{self.d1} - {self.d2} - {self.canh}'
    
    def ChuVi(self):
        return round(4 * self.canh, 2)
    
    def DienTich(self):
        return round((self.d1 * self.d2) / 2, 2)
    
    def say(self):
        print('Tôi là hình thoi')
    

class HinhVuong(HinhThoi):
    def __init__(self, d1):
        super().__init__(d1, d2 = d1)
        self.d2 = d1
        self.canh = math.sqrt(2) * (d1/2) 
    
    def DienTich2(self):
        return round(self.canh**2, 2)
    
    def say(self):
        print('Tôi là hình vuông')