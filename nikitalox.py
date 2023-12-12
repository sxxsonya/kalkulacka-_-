x = input("zadejte pomenou x: ")
y = input("zadejte pomenou y: ")

x = int(x)
y = int(y)

print("zadejte pro scitani +")
print("zadejte pro odcitani - ")
print("zadejte pro nasobeni *")
print("zadejte pro deleni /")
print("zadejte pro mocneni**, x ==mocnenec a y == mocnitel")
print("zadejte pro odmocneni /*, x = odmocnenec a y ==odmocnitel")

znamenko = input("vyber moznosti:")

if znamenko == "+":
  print(x+y)
elif znamenko == "-":
  print (x-y)
elif znamenko == "*":
  print(x*y)
elif znamenko == "/":
  if y == 0:
    print("nelze delit nulou")
  else:
    print(x/y)
elif znamenko == "**":
  print(x**y)
if znamenko == "/*" :
    print(x**(y/1))