def send_email(message, recipient, sender='university.help@gmail.com'):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")) or \
            "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if recipient == sender:
        return print(f"Невозможно отправить письмо самому себе!")
    if sender == 'university.help@gmail.com':
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


