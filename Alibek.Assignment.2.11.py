PRICES = {
    "classic": 0.50,
    "modern": 1.50,
    "premium": 2.50,
}
STOP_WORD = "done"
BONUS_THRESHOLD = 10.00
TOKEN_BONUS = 1.50

print("=== Arcade Game Center Calculator ===")
print("Enter game type: classic, modern, or premium")
print("Type 'done' when finished playing")

total = 0.0

while True:
    print()
    choice = input("Enter game type: ").strip().lower()

    if choice == STOP_WORD:
        break

    if choice in PRICES:
        price = PRICES[choice]
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}")
    else:
        print("Invalid game type. Please enter classic, modern, or premium.")

print()
print("=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")

final_total = total
if total >= BONUS_THRESHOLD:
    final_total = total - TOKEN_BONUS
    print(f"Token Bonus Credit: -${TOKEN_BONUS:.2f}")

print(f"Final Total: ${final_total:.2f}")
print("Thank you for playing!")
