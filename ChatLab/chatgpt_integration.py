"""
Модуль chatgpt_integration.

Отвечает за взаимодействие с моделью ChatGPT:
отправку запросов и получение ответов (заглушка).
"""

def send_message(prompt: str) -> str:
    """
    Отправляет строку запроса к ChatGPT и возвращает
    сгенерированный ответ.

    Args:
        prompt (str): Текст запроса от пользователя.

    Returns:
        str: Ответ, сгенерированный языковой моделью.
    """
    return f"[AI response to: {prompt}]"
