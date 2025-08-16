def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying discount.
    If discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final Price: {final_price}")

except ValueError:
    print("Please enter valid numeric values.")