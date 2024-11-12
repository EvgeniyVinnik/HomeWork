import mask_account_card

if len(number) == 16:
    card_number = number
elif len(number) > 16:
    account_number = number
def get_mask_card_number(card_number: str) -> str:
    """Функция которая принимает номер карты и возвращает маску карты"""
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    return private_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета через инпут и возвращает маску счета"""
    private_account = (len(account_number[0:-4]) * "*") + account_number[-4:]
    return private_account

print(get_mask_card_number)