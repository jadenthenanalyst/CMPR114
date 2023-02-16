quantity = int(input("Please enter number of packages: "))
price = 99
before_discount = float(quantity*price)
if quantity <=9:
    print("NO discount")
    print("Total amount after NO discount: $" + str(before_discount))
elif quantity > 9 and quantity < 20:
    discount = .1 * before_discount
    total = before_discount - discount
    print("10 percent discount: $" + str(round(discount,2)))
    print("Total amount after 10 percent discount: $" + (str(round(total,2))))
elif quantity >= 20 and quantity < 50:
    discount = .2 * before_discount
    total = before_discount - discount
    print("20 percent discount: $" + str(round(discount,2)))
    print("Total amount after 20 percent discount: $" + (str(round(total,2))))
elif quantity >= 50 and quantity < 100:
    discount = .3 * before_discount
    total = before_discount - discount
    print("30 percent discount: $" + str(round(discount,2)))
    print("Total amount after 30 percent discount: $" + (str(round(total,2))))
elif quantity >= 100 :
    discount = .4 * before_discount
    total = before_discount - discount
    print("40 percent discount: $" + str(discount))
    print("Total amount after 40 percent discount: $" + (str(round(total,2))))

