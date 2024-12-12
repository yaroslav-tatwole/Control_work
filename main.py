#Контрольная работа, Средний уровень
#Карпенко Ярослав Х-71
# № 1

# def calculate_volume(lenght, width, height):
#     """
#     вычисляет обьем молекулы по данным размерам
#     args:
#     lenght (float): Длина молекулы
#     width (float): Ширина молекулы
#     height (float): Высота молекулы
#     Returns:
#     float : Обьем молекулы
#     """
#     return lenght * width * height
#
#
# def compare_volumes(volume1, volume2):
#     """
#     Сравнивает обьемы двух молекул.
#     Args:
#     volume1 (float): Обьем первой молекулы
#     volume2 (float): Обьем второй молекулы
#     Returns:
#     str: Сообщение о сравнении обьемов
#     """
#     if volume1 > volume2:
#         return "Обьем первой молекулы больше"
#     elif volume1 < volume2:
#         return "Обьем второй молекулы больше"
#     else:
#         return "Обьемы молекул равны"
#
# def main():
# lenght1 =float(input(" Введите длину первой молекулы"))
# width1 = float (input("Введите ширину первой молекулы"))
# height1 = float (input("Введите высоту первой молекулы"))
#
# lenght2= float (input("Введите длину второй молекулы"))
# width2 = float(input("Введите ширину второй молекулы"))
# height2 = float(input("Введите высоту второй молекулы"))
#
# volume1 = calculate_volume (lenght1,width1,height1)
# volume2 = calculate_volume(lenght2, width2, height2)
# result = compare_volumes(volume1,volume2)
# print(result)
# if __name__ == "__main__":
#     main()

# № 2

# i = 7
# h = i+2
# m = h//4
# for i in range(i,i+1) :
#     if (i<= m ) :
#         print("" * (m-i) + "*" * (2*i) + "" * (h-2*i-2*m)+ "*" * (2*1) + "" * (m-1))
#     else:
#         print("" * (i-2*m+1)+ "*" * (h-2*(i-2*m+1)) + "" * (i-2*m+1))

# № 3

# def compare_atomic_masses(m1,m2,element1,element2):
#     """
#     Сравнивает массы двух атомных элементов
#      Args:
# m1(float): Масса первого атомного элемента
# m2(float): Масса второго атомного элемента
# element1 (str): Название первого атомного элемента
# element2 (str): Название второго атомного элемента
# Raises:
#     ValueError: Если масса первого элемента не меньше массы второго элемента
#     """
#     if m1 >= m2:
#         raise ValueError(f"Масса {element1} ({m1}) не меньше массы {element2} ({m2})")
#     try:
#         compare_atomic_masses(1.00794,15.9994,"Водород","Кислород")
#         print("Масса водорода меньше массы кислорода")
#     except ValueError as e:
#         print(e)
#         try:
#             compare_atomic_masses(15.9994,1.00794,"Кислород","Водород")
#         except ValueError as e:
#             print(e)
