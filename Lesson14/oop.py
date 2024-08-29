from Lesson14 import Human, Animal, HinhThoi, HinhVuong
import math
# Khai báo đối tượng
# human1 = Human('Duc Trung', 25, 'male')
# human2 = Human('Quoc Khanh', 25, 'male')

# print(human1)
# human2.greeting()

# human1.change_gender('meow')
# print(human1)

# human3 = Human(name="ABC", age=2)
# print(human3.name)

# animal1 = Animal('Bơ', 'Chó', 'Vàng', 2, '4kg')
# print(animal1)

# animal1.doi_mau_long('hồng')
# print(animal1)

ht1 = HinhThoi(4, 4)
# print(ht1)
# print('Chu vi:', ht1.ChuVi())
# print('Diện tích:', ht1.DienTich())

a = math.sqrt(2) * 2
hv1 = HinhVuong(a)
print(hv1)
print('Chu vi:', hv1.ChuVi())
print('Diện tích:', hv1.DienTich())
print('Diện tích:', hv1.DienTich2())

ht1.say()
hv1.say()
