"""Константы и функции, позволяющие форматировать текст в консоли"""



RESET = "\x1B[0m"  # Сброс форматирования



class Color:
    """Цвета"""

    BLACK = "\x1B[30m"
    RED = "\x1B[31m"
    GREEN = "\x1B[32m"
    YELLOW = "\x1B[33m"
    BLUE = "\x1B[34m"
    MAGENTA = "\x1B[35m"
    CYAN = "\x1B[36m"
    WHITE = "\x1B[37m"
    RESET = "\x1B[39m"


class Style:
    """Стили текста"""

    B = "\x1B[1m"  # Жирный
    I = "\x1B[3m"  # Курсив
    U = "\x1B[4m"  # Подчёркнутый
    S = "\x1B[9m"  # Зачёркнутый



if __name__ == "__main__":
    print(f"""Данный модуль позволяет писать в консоли {Style.B}жирным{RESET},
          {Style.I}курсивом{RESET}, {Style.U}подчёркнутым{RESET} и {Style.S}зачёркнутым{RESET},
          а также менять {Color.RED}ц{Color.GREEN}в{Color.YELLOW}е{Color.BLUE}т{Color.MAGENTA}а{RESET}!
          """)
