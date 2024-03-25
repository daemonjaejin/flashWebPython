a = 1

if a % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

if a % 2 == 0:
    print("짝수입니다.")
elif a % 2 == 1:
    print("홀수입니다.")
else:
    print("0입니다.")

# True는 자백, False는 부인
# XA = True
# XB = True
# YA = '0'
# YB = '0'
#
# if XA and XB:
#     print('각각 5년형이다.')
#     YA = '5년'
#     YB = '5년'
# elif XA and not XB:
#     print('XB 는 10년 형이다.')
#     Yb = '10년'
# elif not XA and XB:
#     print('XA 는 10년 형이다.')
#     YA = '10년'
# else:
#     print('1년만 산다')
#     YA = '1년'
#     YB = '1년'
#
# print('XA는 %s 형을 산다' % YA, 'XB는 %s 형을 산다' % YB)


XA = input("A는 자백했나요?(yes,no)")
XA = bool(XA == "yes")
XB = input("B는 자백했나요?(yes,no)")
XB = bool(XB == "yes")
YA = 0 if XA and not XB else (5 if XA and XB else (10 if not XA and XB else 1))
YB = 0 if XB and not XA else (5 if XB and XA else (10 if not XB and XA else 1))
print("A는" + str(YA) + "년 복역합니다")
print("B는" + str(YB) + "년 복역합니다")
