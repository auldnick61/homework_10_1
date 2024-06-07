from typing import Union


def mask_card_number(card_number: Union[int, str]) -> str:
    """Преобразование номера карты в строку и маскирование номера карты"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Неверный формат номера карты"
    return (
        card_number_str[:4]
        + " "
        + card_number_str[4:6]
        + "** **** "
        + card_number_str[-4:]
    )


def mask_account_number(account_number: Union[int, str]) -> str:
    """Преобразование номера счета в строку и маскирование номера счета"""
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        return "Неверный формат номера счета"
    return "****" + account_number_str[-4:]


if __name__ == "__main__":
    print(mask_card_number(7000792289606361))
    print(mask_account_number(73654108430135874302))
