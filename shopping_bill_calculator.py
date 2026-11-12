price = 450
qty = 3
member = True
coupon = "SAVE10"

total = price * qty
tax = total * 18 / 100
bill = total + tax

print("Subtotal:", total)
print("Tax (18%):", tax)
print("Bill before discount:", bill)

bigOrder = total >= 1000
hasCoupon = coupon == "SAVE10"

print("Big order:", bigOrder)

discount = 1

if discount:
    bill *= 0.9

bill //= 1
bill += 0

print("Final bill:", bill)