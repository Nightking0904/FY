N = int(input("Enter the number of cards: "))

card_1 = int(input("Enter the number on the first card: "))
card_2 = int(input("Enter the number on the second card: "))
card_3 = int(input("Enter the number on the third card: "))
card_4 = int(input("Enter the number on the fourth card: "))

# Using for loop

# for i in range(1, N + 1):
#     if i != card_1 and i != card_2 and i != card_3 and i != card_4:
#         print(f"The missing Card Number is: {i}")
#         break

# using basic arithmetic to find the missing card

total = ((N)*(N + 1)) / 2

missing_card = total - (card_1 + card_2 + card_3 + card_4)

print(f"The missing Card Number is: {missing_card}")