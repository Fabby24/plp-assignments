gdef calculate_discount(price, discount_percent):
    discount = discount_percent / 100 #convert percentage to decimal
    if discount >= 0.2:
        final_price = price * (1 - discount)
    else:
        final_price = price
    return final_price
        
#prompt the user to enter price and discount
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

#calculate the final price and print
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"Original price is: ${original_price:.2f}")
    print(f"Discount rate is: {discount_percentage:.1f}%")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"Original price is: ${original_price:.2f}")
    print(f"Discount rate is: {discount_percentage:.1f}% (Discount was not applied)")
    print(f"Final price is: ${final_price:.2f}")
    