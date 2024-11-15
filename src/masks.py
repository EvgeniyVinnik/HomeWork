import widget
from widget import output_data
widget.mask_account_card("Счет 73654108430135874305")


if len(output_data[0]) == 16:
    card_number = output_data[0]
elif len(output_data[0]) > 16:
    account_number = output_data[0]
else:
    pass


def get_mask_card_number(card_number: str) -> str:
    """Функция которая принимает номер карты и возвращает маску карты"""
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    return f"{output_data[1]} {private_number}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета через инпут и возвращает маску счета"""
    private_account = (len(account_number[0:-4]) * "*") + account_number[-4:]
    return f"{output_data[1]} {private_account}"


print(get_mask_account(account_number))