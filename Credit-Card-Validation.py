import re


def card_check():
    card_number = input('Payment Card Validator\nType in a card number to validate it:\n')
    card_number = re.sub('[^0-9]', '', card_number)
    provider_list = {3: 'American Express', 4: 'Visa', 5: 'Mastercard', 6: 'Discover', }
    number_list = [int(elem) for elem in card_number if elem in card_number]
    if number_list[0] in provider_list:
        provider = provider_list[number_list[0]]
    else:
        print(f'{card_number} is not a valid card number.')
        return
    odd = False
    mod_list = []
    for num in number_list:
        if not odd:
            num = num * 2
            num = num % 10 + num // 10
            mod_list.append(num)
        else:
            mod_list.append(int(num))
        odd = (odd+1) % 2
    if sum(mod_list) % 10 == 0:
        print(f'{card_number} is a valid card number with {provider}.')
    else:
        print(f'{card_number} is not a valid card number.')
    response = input('Do you want to validate another card number? Y/N\n')
    if response.lower() == 'y':
        card_check(test)


card_check()
