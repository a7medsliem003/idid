products = {
    "soda": "15EGP",
    "juice": "28EGP",
    "tea": "12EGP",
    "coffee": "15EGP"}
x = float(input("Want to ask about the price of a product or a receipt?"))
if x == "receipt":
    y = int(input("enter number of products:"))
    n = 0
    for z in range(0, y):
        k = float(input("please enter price of each product:"))
        n = n + k
    m = float(input("the value of discount:"))
    r = n - m
    print(n, "price before discount")
    print(r, "price after discount")
elif x == "price":
    s = float(input("enter the name of the product :"))
    if s == "soda":
        print(products.get("soda"))
    elif s == "juice":
        print(products.get("juice"))
    elif s == "tea":
        print(products.get("tea"))
    elif s == "coffee":
        print(products.get("coffee"))
    else:
        print("unavailable")
else:
    print("error")
