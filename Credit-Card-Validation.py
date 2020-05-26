# card_number = input('Payment Card Validator\n Type in a card number to validate it.')

card_number = '4578 4230 1376 9219'
# card_number = '4465 4203 3974 7768'
omit_list = [' ', '-', '_', '.', ',']
number_list = [elem for elem in card_number if elem not in omit_list]

print(number_list)

start = 0
for elem in number_list:

