# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988
import decimal
n = decimal.Decimal(input("Введите число = "))
d = (input("Введите требуемую точность '0.0001' = "))
print(n.quantize(decimal.Decimal(d)))