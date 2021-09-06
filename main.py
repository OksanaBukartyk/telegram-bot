import telebot
import os
PORT = int(os.environ.get('PORT', 5000))
lupa=u'\U0001F50D'
bulavka=u'\U0001F4CC'
backs=u'\U000021A9'
strilky=u'\U0001F53B'
books=u'\U0001F4DC'
TOKEN='1968621740:AAGESlwAL0lvnSc-rS5etPhBUOc6MMcX7IU'
bot = telebot.TeleBot (TOKEN)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Інформація про університет' )
keyboard1.row('Абітурієнт','Студент')
keyboard1.row('Вихід' )

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю в Прикарпатському національному університеті імені '
                                      'Василя Стефаника. \nЯ постараюсь допомогти знайти тобі'
                                      ' всю неоюхідну інфомацію.', reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIFkl7L6pcZSw0fQgOjiP9d77M__kzFAALTAANWnb0K9TKPl9US-T0ZBA')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'інформація про університет':
        any_univer(message)


    elif message.text.lower() == 'вихід':
        bot.send_message(message.chat.id, 'Прощавай.')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIFll7L6t7YKtdXtod0VN-kgMOqjeQJAALkAANWnb0KFpvtj-7xNQQZBA')

    elif message.text.lower() == 'студент':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIFl17L6w_BZVk5Kb4ZT5tslV_SlGv-AALjAANWnb0KD_gizK2mCzcZBA')
        any_student(message)

    elif message.text.lower() == 'абітурієнт':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIKU17M9RnicWAbyeFTPRExXA36d9IYAALhAANWnb0KW8GUi0D406AZBA')
        any_abit(message)
    elif message.text == '123' or message.text=='132' or message.text== '213' or message.text=='231' or message.text=='321' or message.text=='312':
        f7 = open('Information/ЗНО/123.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '124' or message.text=='142' or message.text=='214' or message.text=='241' or message.text=='421' or message.text== '412':
        f7 = open('Information/ЗНО/124.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '125' or message.text=='152' or message.text=='215' or message.text=='251' or message.text=='521' or message.text=='512':
        f7 = open('Information/ЗНО/125.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '126' or message.text=='162' or message.text=='216' or message.text=='261' or message.text=='621' or message.text=='612':
        f7 = open('Information/ЗНО/126.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '134' or message.text=='143' or message.text=='314' or message.text=='341' or message.text=='431' or message.text=='413':
        f7 = open('Information/ЗНО/134.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '135' or message.text=='153' or message.text=='315' or message.text=='351' or message.text=='531' or message.text=='513':
        f7 = open('Information/ЗНО/135.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '136' or message.text=='163' or message.text=='316' or message.text=='361' or message.text=='631' or message.text=='613':
        f7 = open('Information/ЗНО/136.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '138' or message.text=='183' or message.text=='318' or message.text=='381' or message.text=='831' or message.text=='813':
        f7 = open('Information/ЗНО/138.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '145' or message.text=='154' or message.text=='415' or message.text=='451' or message.text=='541' or message.text=='514':
        f7 = open('Information/ЗНО/145.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '146' or message.text=='164' or message.text=='416' or message.text=='461' or message.text=='641' or message.text=='614':
        f7 = open('Information/ЗНО/146.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '147' or message.text=='174' or message.text=='417' or message.text=='471' or message.text=='741' or message.text=='714':
        f7 = open('Information/ЗНО/147.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '148' or message.text=='184' or message.text=='418' or message.text=='481' or message.text=='841' or message.text=='814':
        f7 = open('Information/ЗНО/148.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '156' or message.text=='165' or message.text=='516' or message.text=='561' or message.text=='651' or message.text=='615':
        f7 = open('Information/ЗНО/156.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '157' or message.text=='175' or message.text=='517' or message.text=='571' or message.text=='751' or message.text=='715':
        f7 = open('Information/ЗНО/157.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '158' or message.text=='185' or message.text=='518' or message.text=='581' or message.text=='851' or message.text=='815':
        f7 = open('Information/ЗНО/158.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    elif message.text.lower() == '187' or message.text=='178' or message.text=='418' or message.text=='871' or message.text=='781' or message.text=='718':
        f7 = open('Information/ЗНО/187.txt', 'r')
        bot.send_message(chat_id=message.chat.id, text=f7.read())
        backend(message, 'Back4.8')
    else:
        bot.send_message(message.chat.id, 'Не коректний ввід')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@bot.message_handler(commands = ['url'])   # ДЛя ссилки на сайт
def url(message, url, text, message_text):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_my_site= telebot.types.InlineKeyboardButton(text=text, url=url)
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, message_text, reply_markup = markup)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIFrV7L69XLp2AswXQH1yWxDuxujPVvAALYAANWnb0KiQndv0vxFCcZBA')
    btn1 = telebot.types.InlineKeyboardButton(text='Економічний факультет', callback_data='економічний')
    btn2 = telebot.types.InlineKeyboardButton(text='Педагогічний факультет', callback_data='педагогічний')
    btn3 = telebot.types.InlineKeyboardButton(text='Факультет іноземних мов', callback_data='іноземних мов')
    btn4 = telebot.types.InlineKeyboardButton(text='Філософський факультет', callback_data='філософський')
    btn5 = telebot.types.InlineKeyboardButton(text='Факульмет математики та інформатики', callback_data='математики і інформатики')
    btn6 = telebot.types.InlineKeyboardButton(text='Факультет філології', callback_data='філології')
    btn7 = telebot.types.InlineKeyboardButton(text='Факультет туризму', callback_data='туризму')
    btn8 = telebot.types.InlineKeyboardButton(text='Фізико-технічний факультет', callback_data='фізико-технічний')
    btn9 = telebot.types.InlineKeyboardButton(text='Факульмет історії, політології і міжнародних відносин', callback_data='історії, політології...')
    btn10 = telebot.types.InlineKeyboardButton(text='Факультет природничих наук', callback_data='природничих наук')
    btn11 = telebot.types.InlineKeyboardButton(text='Факультет фізичного  виховання і спорту', callback_data='фіз.виховання і спорту')

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    keyboard.add(btn6)
    keyboard.add(btn7)
    keyboard.add(btn8)
    keyboard.add(btn9)
    keyboard.add(btn10)
    keyboard.add(btn11)
    bot.send_message(message.chat.id, text='Факультети:', reply_markup=keyboard)
    backend(message, 'Back4.4')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    textFac = 'Веб-сайт факультету'
    textInst='Веб-сайт інституту'
    textKol='Веб-сайт коледжу'
    message_textFac = 'Бажаєш перейти на веб сайт? - натисни кнопку нище:'
    if call.message:
        if call.data == 'математики і інформатики':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Математики.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://mif.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'економічний':
            strily(call.message, call.data)
            f6 = open('Information/Факультети/Економічний.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://econ.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'педагогічний':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Педагогічний.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://pedagogical.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'іноземних мов':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/ІноземнихМов.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://fim.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'філософський':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Філософський.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://philosophical.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'філології':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Філології.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://philology.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'туризму':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Туризму.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://ft.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'фізико-технічний':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/Фізико-технічний.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://ftf.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'історії, політології...':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/ІсторіїПолітології.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://ipmv.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'фіз.виховання і спорту':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/ФізичногоВиховання.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://ffvs.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')
        elif call.data == 'природничих наук':
            strily(call.message,call.data)
            f6 = open('Information/Факультети/ПриродничихНаук.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f6.read())
            url(call.message, 'https://fpn.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message, 'Back4.1')

        elif call.data == 'Історія':
                strily(call.message,call.data)
                f6 = open('Information/Університет/Історія.txt', 'r')
                bot.send_message(chat_id=call.message.chat.id, text=f6.read())
                url(call.message, 'https://pnu.edu.ua/історія/', books+'  Історія', 'Для більш детальної інформації переходь сюди:')
                backend(call.message, 'Back1')
        elif call.data == 'Підрозділи':
            strily(call.message,call.data)
            any_units(call.message)
        elif call.data == 'Інститути':
            strily(call.message,call.data)
            any_insityt(call.message)
        elif call.data == 'Факультети':
            strily(call.message,call.data)
            any_msg(call.message)
        elif call.data == 'Коледж':
            strily(call.message,call.data)
            f7 = open('Information/Коледж/Коледж.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f7.read())
            url(call.message, 'https://ifk.pnu.edu.ua/', textKol, message_textFac)
            backend(call.message, 'Back4.4')
        elif call.data == 'Контакти':
            strily(call.message,call.data)
            any_contacts(call.message)
            #bot.send_message(call.message.chat.id, 'Телефонний довідник\n\n')
            url(call.message, 'https://pnu.edu.ua/', 'Веб-сайт університету', 'Якщо ви бажаєте перейти на сайт'
                                                               ' Прикарпатського університету - натисніть кнопку нище:')
            backend(call.message, 'Back1')


        elif call.data=='Навчальний процес':
            strily(call.message,call.data)
            url(call.message, 'https://nmv.pnu.edu.ua/wp-content/uploads/sites/118/2019/07/розпорядження-95-р.pdf',
                'Графік навч. процесу', 'Графік навч. процесу на 2019-2020рік можна знайти за посиланням:')
            backend(call.message,'Back2')
        elif call.data=='Наукова бібліотека':
            strily(call.message,call.data)
            f7 = open('Information/Університет/НауковаБібліотека.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f7.read())
            bot.send_message(chat_id=call.message.chat.id, text='Адрес: вул. Галицька,201Б м.Івано-Франківськ \n'
                                                                'тел. (0342)78-81-05 \nE-mail: ftur@pnu.edu.ua')
            url(call.message, 'https://lib.pnu.edu.ua/', textFac, message_textFac)
            backend(call.message,'Back2')
        elif call.data=='Дистанційне навчання':
            strily(call.message,call.data)
            smile(call.message)
            f8 = open('Information/Студент,Абітурієнт/ДистНавчання.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f8.read())
            url(call.message, 'https://d-learn.pnu.edu.ua/', 'Сайт дистанційного навчання', 'Для того щоб перейти '
                                                    'на веб-сайт дистанційного навчання ПНУ - перейдіть за посиланням нище:')
            backend(call.message,'Back2')
        elif call.data=='Оплата за навчання':
            strily(call.message,call.data)
            cost(call.message)
            backend(call.message, 'Back2')
        elif call.data=='Вартість навчання2':
             strily(call.message,call.data)
             url(call.message, 'https://pnu.edu.ua/wp-content/uploads/2020/05/223_28.04.2020.pdf',
                 bulavka+'Вартість навчання 2020-2021', lupa + 'Вартість навчання на 2020-2021рp можна знайти за посиланням:')
             backend(call.message,'Back4.2')
        elif call.data=='Вартість навчання1':
             strily(call.message,call.data)
             url(call.message, 'https://pnu.edu.ua/wp-content/uploads/2019/07/Наказ-391-new.pdf',
                 bulavka+'Вартість навчання 2019-2020','Вартість навчання на 2019-2020pp можна знайти за посиланням:')
             backend(call.message,'Back4.2')
        elif call.data=='Вартість навчання3':
             strily(call.message,call.data)
             url(call.message, 'https://pnu.edu.ua/wp-content/uploads/2019/08/1903_190823130333_001.pdf',
                 bulavka+'Вартість гуртожитків 2019-2020','Вартість проживання у гуртожитках на 2019-2020pp можна знайти за посиланням:')
             backend(call.message,'Back4.2')
        elif call.data=='Довідка':
             strily(call.message,call.data)
             url(call.message, 'http://comp-sc.if.ua/dovidka/', 'Довідка', 'Для того,щоб оформити довідку - перейди за посиланням.'
                                                                           '\nP.S. На жаль, на сьогоднішній момент довідку можуть оформити тільки студенти факультету математики і інформатики')
             backend(call.message,'Back2')
        elif call.data == 'Студенські чати':
            strily(call.message,call.data)
            bot.send_message(call.message.chat.id, 'Telegram: \n@pnutalk \n@pnuchat \n@pnulife \n' )
            url(call.message, 'https://www.facebook.com/groups/pnulife', 'Facebook', 'А також y Facebook:')
            url(call.message, 'https://instagram.com/pnulife/', 'Instagram', 'Не маєш , Facebook, то заходь в Instagram:')
            backend(call.message,'Back2')
        elif call.data == 'Розклад занять':
            strily(call.message,call.data)
            bot.send_message(call.message.chat.id, 'Розклад можна знайти  в телеграм-боті: @std_pnu_bot')
            url(call.message, 'http://asu.pnu.edu.ua/cgi-bin/timetable.cgi', 'Веб-розклад', 'А також на сайті:')
            backend(call.message,'Back2')

        elif call.data == 'Підбір спеціальності':
            pidbirSpez(call.message)

        elif call.data == 'Перелік ЗНО':
            strily(call.message,call.data)
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2019/12/Додаток-4-до-ПП-20201227.pdf',
                'Перелік ЗНО', 'Для того, щоб переглянути список можливих спеціальностей в нашому університеті та ЗНО, '
                'неохідних для поступлення, можеш перейти за посиланням нище: ')
            backend(call.message,'Back3')
        elif call.data == 'Підготовчі курси':
            strily(call.message,call.data)
            smile(call.message)
            backend(call.message,'Back3')
        elif call.data == 'Запитання і відповіді':
            strily(call.message,call.data)
            f8 = open('Information/Студент,Абітурієнт/ЗапитанняВідповіді.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f8.read())
            bot.send_message(call.message.chat.id,
                             ' Якщо ти не знайшов відповідь на свої запитання, то пиши нам на пошту:'
                             '\nadmission@pnu.edu.ua \nМи постараємось відповісти на все, що тебе цікавить.')
            backend(call.message,'Back3')
        elif call.data == 'Кафедра військової підготовки':
            strily(call.message,call.data)
            f8 = open('Information/Студент,Абітурієнт/КафедраВійськ.txt', 'r')
            bot.send_message(chat_id=call.message.chat.id, text=f8.read())
            viskovaKaf(call.message)
            #backend(call.message,'Back3')
        elif call.data=='Перелік документів':
             strily(call.message,call.data)
             f8 = open('Information/Студент,Абітурієнт/ПерелікДокументів.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             backend(call.message,'Back4.6')
        elif call.data=='Строки':
             strily(call.message,call.data)
             f8 = open('Information/Студент,Абітурієнт/Строки.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             backend(call.message,'Back4.6')
        elif call.data == 'Правила прийому':
            strily(call.message, call.data)
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2019/12/Додаток-9-'
                              'правила-прийому-на-кафедру-військової-підготовки-у-2020.pdf', 'Правила прийому',
                            'Правила прийому можна переглянути за посиланням:')
            backend(call.message, 'Back4.6')
        elif call.data == 'Програми вступних випробувань':
            strily(call.message, call.data)
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2020/03/програма-з-ДПЮ-2020.pdf',
                'Допризовна підготовка', 'Програми вступних випробувань.Оцінка рівня допризовної підготовки:')
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2020/03/програма-з-ФІЗО-2020.pdf',
                'Фізична підготовка', 'Програми вступних випробувань.Оцінка рівня фізичної підготовленості:')
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2020/03/програма-проф.pdf',
                'Психологічний відбір', 'Програми вступних випробувань. Професійний психологічний відбір:')
            backend(call.message, 'Back4.6')
        elif call.data == 'Розклад вступних випробувань':
            strily(call.message, call.data)
            url(call.message, 'https://admission.pnu.edu.ua/wp-content/uploads/sites/6/2020/03/І-етап-військова-кафедра.pdf',
                'Розклад', 'Розклад вступних випробувань(перший етап):')
            backend(call.message, 'Back4.6')
        elif call.data == 'Іноземному студенту':
            strily(call.message,call.data)
            inozem(call.message)
        elif call.data=='Порядок прийому':
             strily(call.message,call.data)
             f8 = open('Студент,АбітурієнтПорядок/ПрийомуІноз1.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             f9 = open('Студент,АбітурієнтПорядок/ПрийомуІноз2.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f9.read())
             backend(call.message,'Back4.7')
        elif call.data=='Вартість навчання':
             strily(call.message,call.data)
             f8 = open('Information/Студент,Абітурієнт/ВартістьНавчанняІноз.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             backend(call.message,'Back4.7')

        elif call.data=='Керівництво':
             strily(call.message,call.data)
             f1 = open('Information/Контакти/Керівництво.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f1.read())
             backend(call.message,'Back4.3')
        elif call.data=='Приймальна комісія':
             strily(call.message,call.data)
             f2 = open('Information/Студент,Абітурієнт/ПриймальнаКомісія.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f2.read())
             backend(call.message,'Back4.3')
        elif call.data=='Бухгалтерія':
             strily(call.message,call.data)
             f3 = open('Information/Контакти/Бухгалтерія.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f3.read())
             backend(call.message,'Back4.3')
        elif call.data=='Громадські організації':
             strily(call.message,call.data)
             f4 = open('Information/Контакти/ГромадськіОрганізації.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f4.read())
             backend(call.message,'Back4.3')
        elif call.data=='Музеї':
             strily(call.message,call.data)
             f5 = open('Information/Контакти/Музеї.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f5.read())
             backend(call.message,'Back4.3')
        elif call.data=='Спортивний комплекс':
             strily(call.message,call.data)
             f6 = open('Information/Контакти/СпортивнийКомплекс.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f6.read())
             backend(call.message,'Back4.3')
        elif call.data=='Навчальні корпуси':
             strily(call.message,call.data)
             f6 = open('Information/Контакти/НавчальніКорпуси.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f6.read())
             backend(call.message,'Back4.3')
        elif call.data=='Студенське містечко':
             strily(call.message,call.data)
             f6 = open('Information/Контакти/СтуденськеМістечко.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f6.read())
             backend(call.message,'Back4.3')
        elif call.data=='Наукові підрозділи':
             strily(call.message,call.data)
             f10 = open('Information/Контакти/НавчальніПід1.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f10.read())
             f11 = open('Information/Контакти/НавчальніПід2.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f11.read())
             backend(call.message,'Back4.3')
        elif call.data=='Навчальні центри':
             strily(call.message,call.data)
             f6 = open('Information/Контакти/НавчальніЦентриДист.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f6.read())
             backend(call.message,'Back4.3')

        elif call.data=='Юридичний інститут':
             strily(call.message,call.data)
             f8 = open('Information/Інститути/ЮридичнийІнститут.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             url(call.message, 'https://law.pnu.edu.ua/en/', textInst, message_textFac)
             backend(call.message,'Back4.5')
        elif call.data=='Коломийський інститут':
             strily(call.message,call.data)
             f9 = open('Information/Інститути/КоломийськийІнститут.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f9.read())
             url(call.message, 'https://knni.pnu.edu.ua/en/', textInst, message_textFac)
             backend(call.message,'Back4.5')
        elif call.data=='Інститут післядипломної освіти...':
             strily(call.message,call.data)
             f8 = open('Information/Інститути/Післядипломна.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             url(call.message, 'https://ipodp.pnu.edu.ua/', textInst, message_textFac)
             backend(call.message,'Back4.5')
        elif call.data=='Інститут мистецтв':
             strily(call.message,call.data)

             f8 = open('Information/Інститути/ІнституМистецтв.txt', 'r')
             bot.send_message(chat_id=call.message.chat.id, text=f8.read())
             url(call.message, 'https://art.pnu.edu.ua/en/', textInst, message_textFac)
             backend(call.message,'Back4.5')



        elif call.data=='Back1':
            any_univer(call.message)
        elif call.data=='Back2':
            any_student(call.message)
        elif call.data=='Back3':
            any_abit(call.message)
        elif call.data=='Back4.1':
            any_msg(call.message)
        elif call.data=='Back4.2':
            cost(call.message)
        elif call.data=='Back4.3':
            any_contacts(call.message)
        elif call.data=='Back4.4':
            any_units(call.message)
        elif call.data=='Back4.5':
            any_insityt(call.message)
        elif call.data=='Back4.6':
            viskovaKaf(call.message)
        elif call.data=='Back4.7':
            inozem(call.message)
        elif call.data=='Back4.8':
            pidbirSpez(call.message)

@bot.message_handler(content_types=["text"])
def any_abit(message):
    bot.send_message(message.chat.id, 12 * strilky)
    Atext = 'Інформація для абітурієнта:'
    #bot.send_message(chat_id=message.chat.id, text=('Твій вибір:  ' + Atext))
    keyboard = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text='Підбір спеціальності по ЗНО', callback_data='Підбір спеціальності')
    btn2 = telebot.types.InlineKeyboardButton(text='Перелік ЗНО для вступу', callback_data='Перелік ЗНО')
    #btn3 = telebot.types.InlineKeyboardButton(text='Підготовчі курси', callback_data='Підготовчі курси')
    btn4 = telebot.types.InlineKeyboardButton(text='Приймальна комісія', callback_data='Приймальна комісія')
    btn5 = telebot.types.InlineKeyboardButton(text='Оплата за навчання/гуртожиток', callback_data='Оплата за навчання')
    btn6 = telebot.types.InlineKeyboardButton(text='Контакти', callback_data='Контакти')
    btn9 = telebot.types.InlineKeyboardButton(text='Запитання і відповіді', callback_data='Запитання і відповіді')
    btn8 = telebot.types.InlineKeyboardButton(text='Кафедра військової підготовки', callback_data='Кафедра військової підготовки')
    btn7 = telebot.types.InlineKeyboardButton(text='Іноземному студенту', callback_data='Іноземному студенту')

    keyboard.add(btn1)
    keyboard.add(btn2)
    #keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    keyboard.add(btn6)
    keyboard.add(btn7)
    keyboard.add(btn8)
    keyboard.add(btn9)
    bot.send_message(message.chat.id, text=Atext, reply_markup=keyboard)
def any_univer(message):
    bot.send_message(message.chat.id, 12 * strilky)
    Utext='Інформація про університет:'
    #bot.send_message(chat_id=message.chat.id, text=('Твій вибір:  ' + Utext))
    keyboard = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text='Історія', callback_data='Історія')
    btn2 = telebot.types.InlineKeyboardButton(text='Підрозділи', callback_data='Підрозділи')
    btn3 = telebot.types.InlineKeyboardButton(text='Контакти', callback_data='Контакти')

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    bot.send_message(message.chat.id, text=Utext, reply_markup=keyboard)
def backend(message, text):
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='Back  '+ backs, callback_data=text)
    keyboard.add(btn1)
    bot.send_message(message.chat.id, text='Повернутись?', reply_markup=keyboard)
def strily(message, name):
    bot.send_message(message.chat.id, 12*strilky)
    bot.send_message(chat_id=message.chat.id, text=('Твій вибір:  ' + name))
def cost(message):
      keyboard = telebot.types.InlineKeyboardMarkup()
      btn1 = telebot.types.InlineKeyboardButton(text='Вартість навчання 2019-2020pp', callback_data='Вартість навчання1')
      btn2 = telebot.types.InlineKeyboardButton(text='Вартість навчання 2020-2021pp', callback_data='Вартість навчання2')
      btn3 = telebot.types.InlineKeyboardButton(text='Вартість гуртожитків 2019-2020pp', callback_data='Вартість навчання3')
      keyboard.add(btn1)
      keyboard.add(btn2)
      keyboard.add(btn3)
      bot.send_message(message.chat.id, text='Вартість навчання на 2019-2021рік можна знайти за посиланням:', reply_markup=keyboard)
def any_units(message):
      keyboard = telebot.types.InlineKeyboardMarkup()
      btn1 = telebot.types.InlineKeyboardButton(text='Інститути', callback_data='Інститути')
      btn2 = telebot.types.InlineKeyboardButton(text='Факультети', callback_data='Факультети')
      btn3 = telebot.types.InlineKeyboardButton(text='Івано-Франківський коледж', callback_data='Коледж')
      keyboard.add(btn1)
      keyboard.add(btn2)
      keyboard.add(btn3)
      bot.send_message(message.chat.id, text='Підрозділи:', reply_markup=keyboard)
      backend(message, 'Back1')
def any_student(message):
    bot.send_message(message.chat.id, 12 * strilky)
    Stext='Інформація для студента'
    #bot.send_message(chat_id=message.chat.id, text=('Твій вибір:  ' + Stext))
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='Розклад занять', callback_data='Розклад занять')
    btn2 = telebot.types.InlineKeyboardButton(text='Графік навчального процесу', callback_data='Навчальний процес')
    btn3 = telebot.types.InlineKeyboardButton(text='Наукова бібліотека', callback_data='Наукова бібліотека')
    btn4 = telebot.types.InlineKeyboardButton(text='Дистанційне навчання', callback_data='Дистанційне навчання')
    btn5 = telebot.types.InlineKeyboardButton(text='Оплата за навчання/гуртожиток', callback_data='Оплата за навчання')
    #btn6 = telebot.types.InlineKeyboardButton(text='Сайт кафедри', callback_data='Сайт кафедри')
    btn7 = telebot.types.InlineKeyboardButton(text='Довідка про навчання', callback_data='Довідка')
    btn8 = telebot.types.InlineKeyboardButton(text='Студенські чати', callback_data='Студенські чати')
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    #keyboard.add(btn6)
    keyboard.add(btn7)
    keyboard.add(btn8)

    bot.send_message(message.chat.id, text=Stext, reply_markup=keyboard)
def any_insityt(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    btn1 = telebot.types.InlineKeyboardButton(text='Інститут післядипломної освіти та довузівської підготовки',
                                              callback_data='Інститут післядипломної освіти...')
    btn2 = telebot.types.InlineKeyboardButton(text='Коломийський навчально-науковий Інститут', callback_data='Коломийський інститут')
    btn3 = telebot.types.InlineKeyboardButton(text='Навчально-науковий Інститут мистецтв', callback_data='Інститут мистецтв')
    btn4 = telebot.types.InlineKeyboardButton(text='Навчально-науковий Юридичний інститут', callback_data='Юридичний інститут')

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)

    bot.send_message(message.chat.id, text='Інститути:', reply_markup=keyboard)
    backend(message, 'Back4.4')
def any_contacts(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIKZ17M9gESsdDoOHCPxXsAAaOqdZUUDgAC1wADVp29Cg09r24xpO5XGQQ')
    btn1 = telebot.types.InlineKeyboardButton(text='Керівництво',callback_data='Керівництво')
    btn2 = telebot.types.InlineKeyboardButton(text='Приймальна комісія', callback_data='Приймальна комісія')
    #btn3 = telebot.types.InlineKeyboardButton(text='Відділи університету', callback_data='Відділи університету')
    btn4 = telebot.types.InlineKeyboardButton(text='Бухгалтерія', callback_data='Бухгалтерія')
    btn5 = telebot.types.InlineKeyboardButton(text='Навчальні корпуси', callback_data='Навчальні корпуси')
    btn6 = telebot.types.InlineKeyboardButton(text='Громадські організації', callback_data='Громадські організації')
    btn7 = telebot.types.InlineKeyboardButton(text='Студенське містечко', callback_data='Студенське містечко')
    #btn8 = telebot.types.InlineKeyboardButton(text='Заклади харчування', callback_data='Заклади харчування')
    btn9 = telebot.types.InlineKeyboardButton(text='Спортивний комплекс', callback_data='Спортивний комплекс')
    btn10 = telebot.types.InlineKeyboardButton(text='Навчальні центри дистанційних комунікацій', callback_data='Навчальні центри')
    btn11 = telebot.types.InlineKeyboardButton(text='Навчально-наукові підрозділи', callback_data='Наукові підрозділи')
    btn12 = telebot.types.InlineKeyboardButton(text='Музеї', callback_data='Музеї')
    btn13 = telebot.types.InlineKeyboardButton(text='Інститути', callback_data='Інститути')
    btn14= telebot.types.InlineKeyboardButton(text='Факультети', callback_data='Факультети')
    btn15= telebot.types.InlineKeyboardButton(text='Івано-Франківський коледж', callback_data='Коледж')
    keyboard.add(btn1)
    keyboard.add(btn2)
    #keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    keyboard.add(btn6)
    keyboard.add(btn7)
    #keyboard.add(btn8)
    keyboard.add(btn9)
    keyboard.add(btn10)
    keyboard.add(btn11)
    keyboard.add(btn12)
    keyboard.add(btn13)
    keyboard.add(btn14)
    keyboard.add(btn15)
    bot.send_message(message.chat.id, text='Телефонний довідник:', reply_markup=keyboard)
    #any_msg(message)
    #any_insityt(message)
    #backend(message, 'Back1')
def viskovaKaf(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIKZ17M9gESsdDoOHCPxXsAAaOqdZUUDgAC1wADVp29Cg09r24xpO5XGQQ')
    btn1 = telebot.types.InlineKeyboardButton(text='Перелік документів для вступу',callback_data='Перелік документів')
    btn2 = telebot.types.InlineKeyboardButton(text='Строки подачі заяв, проведення вступних випробувань, зарахування', callback_data='Строки')
    btn3 = telebot.types.InlineKeyboardButton(text='Правила прийому на кафедру військової підготовки', callback_data='Правила прийому')
    btn4 = telebot.types.InlineKeyboardButton(text='Програми вступних випробувань', callback_data='Програми вступних випробувань')
    btn5 = telebot.types.InlineKeyboardButton(text='Розклад вступних випробувань', callback_data='Розклад вступних випробувань')
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)
    bot.send_message(message.chat.id, text='Детальніше:', reply_markup=keyboard)
    backend(message, 'Back3')


def inozem(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='Порядок прийому на навчання', callback_data='Порядок прийому')
    btn2 = telebot.types.InlineKeyboardButton(text='Вартість навчання', callback_data='Вартість навчання')
    keyboard.add(btn1)
    keyboard.add(btn2)
    bot.send_message(message.chat.id, text='Інформація для іноземного студента:',reply_markup=keyboard)
    backend(message, 'Back3')
def pidbirSpez(message):
    bot.send_message(message.chat.id, 12 * strilky)
    Stext = 'Підбір спеціальності'
    bot.send_message(chat_id=message.chat.id, text=('Твій вибір:  ' + Stext))
    f8 = open('ZNO.txt', 'r')
    bot.send_message(chat_id=message.chat.id, text=f8.read())
    backend(message, 'Back3')

def smile(message):
    #bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANwXskTHd5uisB9m9Z5CMe_1Xb0k8AAAloAA2CJbQwxXLT_o2OKHxkE')
    bot.send_message(message.chat.id, 'Нічого нового ')
bot.polling()