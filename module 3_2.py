def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if ('@' and ".com" or ".ru" or ".net") not in recipient and ('@' and ".com" or ".ru" or ".net") not in sender:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)