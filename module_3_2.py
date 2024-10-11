# "Способы вызова функции"
def send_email(message, recipient, sender = "university.help@gmail.com"):
    l = 0
    if l == len(recipient):
        message = "Нельзя отправить письмо самому себе!"
    if sender == "university.help@gmail.com":
        message = "Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient
    elif len(sender) == len(recipient):
        for l in range(0, len(recipient)):
            if sender[l] == recipient[l]:
                l = l + 1
        if l == len(recipient):
            message = "Нельзя отправить письмо самому себе!"
    else:
        message = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient
    k = 0
    for i in range(len(sender)):
        if sender[i] != "@":
            k = k + 1
    if k == len(sender):
        message = "Невозможно отправить письмо с адреса " + sender + "на адрес " + recipient
    k = 0
    for j in range(len(recipient)):
        if recipient[j] != "@":
            k = k + 1
    if k == len(recipient):
        message = "Невозможно отправить письмо с адреса " + sender + "на адрес " + recipient
    if recipient[-4:] != ".com" and recipient[-4:] != ".net" and recipient[-3:] != ".ru":
        message = "Невозможно отправить письмо с адреса " + sender + "на адрес " + recipient
    if sender[-4:] != ".com" and sender[-4:] != ".net" and sender[-3:] != ".ru":
        message = "Невозможно отправить письмо с адреса " + sender + "на адрес " + recipient
    return message
print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))