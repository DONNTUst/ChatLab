"""
Модуль client_interface.

Обеспечивает функционал для консольного интерфейса чат-бота ChatLab.
"""

def run_client():
    """
    Запускает консольный интерфейс ChatLab.

    Функция инициализирует чат-бот и ожидает ввода от пользователя,
    передавая запросы в модуль chatgpt_integration для получения ответа
    от (псевдо) ChatGPT.

    Returns:
        None
    """
    print("Client Interface started...")
