from datetime import datetime
from . import masks


def mask_account_info(info: str) -> str:
    """Маскирование информации о карте или счете в зависимости от типа."""
    info_parts = info.split()
    if info_parts[0] == "Счет" and len(info_parts[1]) == 20:
        masked_info = masks.mask_account_number(int(info_parts[1]))
        return f"{info_parts[0]} {masked_info}"
    elif info_parts[0] in ["Visa", "Maestro", "MasterCard"]:
        card_type_and_name = " ".join(info_parts[0:2])
        card_number_parts = []
        for part in info_parts[2:]:
            if part.isdigit():
                card_number_parts.append(part)
        card_number = "".join(card_number_parts)
        if len(card_number) == 16:
            masked_info = masks.mask_card_number(int(card_number))
            return f"{card_type_and_name} {masked_info[:4]} {masked_info[5:7]}** **** {masked_info[-4:]}"
    return "Неверный формат номера карты"


def format_date(date_string: str) -> str:
    """Преобразование строки даты и времени в строку с датой в формате ДД.ММ.ГГГГ."""

    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date


if __name__ == "__main__":
    print(mask_account_info("Visa Platinum 8990922113665229"))
    print(mask_account_info("Счет 73654108430135874302"))
    print(format_date("2018-07-11T02:26:18.671407"))
