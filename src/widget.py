def mask_account_card(user_input: str) -> str:
    """Функция принимает на вход пользовательские данные и достает номер карты или счета."""
    number = ""
    card_name = " "
    card_number = ''
    account_number = ''
    for i in user_input:
        if i.isdigit():
            number += i
        else:
            card_name += i

    return [number, card_name]

output_data = mask_account_card("Счет 73654108430135874305")

def get_date(date_input: str) -> str:
    index_date = list(date_input)
    day = index_date[8] + index_date[9]
    month = index_date[5] + index_date[6]
    year = index_date[0] + index_date[1] + index_date[2] + index_date[3]
    correct_date = day + '.' + month + '.' + year
    return correct_date

