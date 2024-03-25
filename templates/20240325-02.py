for i in range(10):
    print(i)
    print("=" + str(i+1) + "=")

for i in range(10):
    print(str("*")*(i+1))

for i in range(10):
    print(str("*")*(10-i))

for i in range(20-1):
    if i < 10:
        print(str("*")*(i+1))
    else:
        print(str("*")*(20-1-i))

print("==================================")

c = -1
for i in range(11):
    a = " "
    b = " "
    if i < 6:
        c = c+2
        x = 5-i
        print(str(a)*x + str("*")*c + str(b)*x)
    else:
        c = c-2
        x = i-5
        print(str(a)*x + str("*")*c + str(b)*x)

size = 6  # 다이아몬드 크기 (홀수)

for i in range(-size + 1, size):
    print(" " * abs(i) + "*" * (2 * (size - abs(i)) - 1))

# 어떤 주식의 가격은 매일 한 번 동전을 던져서 앞면이 나오면 전날 가격의 2배가 되고, 뒷면이 나오면 전날 가격의 절반이 된다. 1일에 주식의 가격이 1,024원이었을 때, 4일 주식의 가격이 나올 수 있는 경우를 모두 구한다. (힌트: for 반복문이 3개 중첩되어야 한다)

print("==================================")
price = 1024
for i in range(2):
    if i == 0:
        price = price * 2
    else:
        price = price / 2
    for j in range(2):
        if j == 0:
            price = price * 2
        else:
            price = price / 2
        for k in range(2):
            if k == 0:
                price = price * 2
            else:
                price = price / 2
            print(price)
            if k == 0:
                price = price / 2
            else:
                price = price * 2
        if j == 0:
            price = price / 2
        else:
            price = price * 2
    if i == 0:
        price = price / 2
    else:
        price = price * 2

for i in [2, 1/2]:
    for j in [2, 1/2]:
        for k in [2, 1/2]:
            print(1024 * i * j * k)

