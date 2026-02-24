def calculate_discount(price, discount_percent):
    # Apply discount only if 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Output result
if final_price < price:
    print("Final price after discount:", final_price)
else:
    print("No discount applied. Original price:", price)