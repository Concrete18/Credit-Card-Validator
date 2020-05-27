def card_check(num):
    if num % 10 == 0:
        return True
    else:
        return False


# card_number = input('Payment Card Validator\n Type in a card number to validate it.')

card_number = '4578 4230 1376 9219'
# card_number = '4465 4203 3974 7768'
omit_list = [' ', '-', '_', '.', ',']
number_list = [int(elem) for elem in card_number if elem not in omit_list]

print(number_list)

odd = 0
mod_list = []
for elem in number_list:
    if odd == 0:
        elem = elem*2
        if elem > 9:
            Sum = 0
            while elem > 0:
                Reminder = elem % 10
                Sum = Sum + Reminder
                elem = elem // 10
        mod_list.append(elem)
        odd = 1
    else:
        mod_list.append(int(elem))
        odd = 0
print(mod_list)

print(card_check(sum(mod_list)))


