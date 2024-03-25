a = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
print(a)
print(len(a))

b = list(range(5))
print(b)

for i in [0, 1, 2, 3, 4]:
    print(i)

for i, e in enumerate(["a", "b", "c"]):
    print("i = %d, e = %s" % (i, e))

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]
for i, (a1i, a2i) in enumerate(zip(a1, a2)):
    s[i] = a1i + a2i

print(s)

a12 = list(zip(a1, a2))
print(a12)

a12 = [(90, 95),
       (85, 90),
       (95, 90),
       (80, 90),
       (90, 95),
       (100, 100),
       (85, 90),
       (75, 80),
       (85, 95),
       (80, 90)]

print(a12)

a21 = list(zip(*a12))

print(a21)

a22 = list(zip(*a21))

print(a22)

print("============")

x = {"a": 10, "b": 20}
print(len(x))

print(x["a"])

x["a"] = 30

print(x)

x["c"] = 40

print(x)

del x["b"]

print(x)

x1 = "a" in x

print(x1)

x2 = "d" in x

print(x2)

for k in x:
    print(k)

print(x.keys())

for k in x.keys():
    print(k)

print(x.values())

for v in x.values():
    print(v)

for k, v in x.items():
    print("key [%s] => value [%d]" % (k, v))












