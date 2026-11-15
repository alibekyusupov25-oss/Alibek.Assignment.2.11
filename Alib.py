PRICES = {
    "bath": 15.00,
    "trim": 25.00,
    "full": 40.00,}
STOP_WORD = "done"
DISCOUNT_THRESHOLD = 75.00
DISCOUNT = 12.00

print("=== Pet Grooming Service Calculator ===")
print("Enter service package: bath, trim, or full")
print("Type 'done' when finished selecting services")

total = 0.0

while True:
    print()
    choice = input("Enter service package: ").strip().lower()

    if choice == STOP_WORD:
        break

    if choice in PRICES:
        price = PRICES[choice]
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}")
    else:
        print("Invalid package. Please enter bath, trim, or full.")

print()
print("=== Service Summary ===")
print(f"Subtotal: ${total:.2f}")

final_total = total
if total >= DISCOUNT_THRESHOLD:
    final_total = total - DISCOUNT
    print(f"Multi-Pet Discount: -${DISCOUNT:.2f}")

print(f"Final Total: ${final_total:.2f}")
print("Thank you for choosing our salon!")
