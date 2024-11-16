def get_mask_card_number(card_number: str) -> str:
    """Функция которая принимает номер карты и возвращает маску карты"""
    private_number = (card_number[:4] + " " + card_number[4:6]
                      + "**" + " " + "****" + " " + card_number[-4:])
    return private_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает номер счета через инпут и возвращает маску счета"""
    private_account = "**" + account_number[-4:]
    return private_account
