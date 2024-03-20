import numpy as np

# Create a 1D numpy array
arr = np.array([1, 2, 3, 4, 5])

print("1D array:", arr)

arr1 = np.arange(10)

print("1D array with arange:", arr1)

arr2 = np.arange(2, 10, dtype=float)

print("1D array with arange and dtype:", arr2)

arr3 = np.arange(2, 3, 0.1)

print("1D array with arange and step:", arr3)

arr4 = np.linspace(1., 4., 6)

print("1D array with linspace:", arr4)

print(1 + 1)

print(2 * 4)

print(8 // 4)

print(11 // 4)

print(10 / 4)

print(2 ** 3)

print(2 ** -1)

print(1000 ** 0)

a = 10
b = 10.0

print(type(a))

print(type(b))

n = 10

print("별표를" + str(10) + "번 출력합니다.")
print("*" * n)

print("한 줄 쓰고\n그 다음 줄을 쓴다.")

print("한 줄 쓰고 ", end="")
print("이어서 쓴다.")

multi_line_string = """
    파이썬
    abc
    123
"""

print(multi_line_string)

print("내 이름은 %s입니다." % "홍길동")

print("%d 곱하기 %d은 %d이다." % (2, 3, 6))

# [와] 사이에 20칸의 공백이 있다.
print("[%20s]" % "*")

# [와] 사이에 20칸의 공백 앞쪽에 A를 인쇄한다.
print("[%-20s]" % "A")

print("%.5f" % (1 / 3.0))

print("내 이름은 {}입니다.".format("홍길동"))

print("내 이름은 {{{}}}입니다.".format("홍길동"))

print("[{:<20}]".format("*"))

name = "홍길동"
age = 32
print(f"{name}의 나이는 {age}살이다.")