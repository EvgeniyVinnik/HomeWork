def mask_account_card(user_input: str) -> str:
    """Функция принимает на вход пользовательские данные и достает номер карты или счета."""
    number = ""
    card_name = " "
    for i in user_input:
        if i.isdigit():
            number += i
        else:
            card_name += i
    # блок, который определяет, что это, номер карты или счета
    if len(number) == 16:
        from masks import get_mask_card_number
        card_number = number
        return f"{card_name} {get_mask_card_number(card_number)}"
    elif len(number) > 16:
        from masks import get_mask_account
        account_number = number
        return f"{card_name} {get_mask_account(account_number)}"
    else:
        pass


def get_date(date_input: str) -> str:
    """Функция принимает дату в некорректном виде и возвращает в корректном"""
    index_date = list(date_input)
    day = index_date[8] + index_date[9]
    month = index_date[5] + index_date[6]
    year = index_date[0] + index_date[1] + index_date[2] + index_date[3]
    correct_date = day + '.' + month + '.' + year
    return correct_date


print(mask_account_card("Счет 64686473678894779589"))