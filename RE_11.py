# -*- coding: utf-8 -*-

import telebot
from telebot import apihelper, types
from datetime import datetime

import os
import time
import sys


bot = telebot.TeleBot(API)
#proxy: 'http://IP:PORT'.
apihelper.proxy = {'http':PROXY}
Zn = False
changep = False
cp = False
#hideBoard = types.ReplyKeyboardRemove(selective = False)
pok = False
while True:
    def check():
        global Zn, pok
        wd = datetime.today().weekday()
    #    ths = datetime.strftime(datetime.now(), "%H")
    #    tms = datetime.strftime(datetime.now(), "%M")
    #    th = int(ths)
    #    tm = int(tms)
    #    t = (th - 1) * 3600000 + tm * 60000
        if Zn == False:
            if wd == 4:
                pok = True
            else:
                pass
        elif Zn == True:
            if wd == 4:
                pok = False
            else:
                pass
        if pok == False:
            if wd == 5:
                Zn = False
            else:
                pass
        elif pok == True:
            if wd == 5:
                Zn == True
            else:
                pass


    check()
    #@bot.message_handler(commands=['exit'])
    #def exit_message(message):
    #    bot.send_message(message.chat.id,
    #                     'Artem, esli ti uvidish eto soobshenie, to znay:')
    #    bot.send_message(message.chat.id,
    #                     'Ti leniviy debil.')
    #    sys.exit(1)
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,
                         'Я - бот группы РЕ-11.\nНа данный момент, я многого не умею.\nМогу рассказать о своём функционале командой "/help"\nИли просто нажми на "/", чтобы увидеть список команд.',
                         )#reply_markup=keyboard0
        check()

    @bot.message_handler(commands=['help'])
    def help_message(message):
        #bot.send_message(message.chat.id,
       #                  '"/help" - Отобразить все доступные команды.\n"/next" - Какая пара следующая?\n"/today" - Расписание на сегодня.\n"/tm" - Расписание на завтра.\n"/ph" - Номера телефонов преподов.\n"/book" - Ссылка на книги.'
       #                  )#reply_markup=keyboard0
                bot.send_message(message.chat.id,
                                 '"/help" - Отобразить все доступные команды.\n"/next" - Какой ближайший экзамен?\n"/exams" - Список экзаменов.\n"/ph" - Номера телефонов преподов.\n"/book" - Ссылка на книги.\n'
                         )#reply_markup=keyboard0


    @bot.message_handler(commands=['exams'])
    def exams_message(message):
        bot.send_message(message.chat.id,
       #                   '23 Декабря - Биология, в аудитории 2-16. ✅')
                         '13 Июня в 8:30 - МБД в Скайпе. ✅')
    
        bot.send_message(message.chat.id,
       #                   '27 Декабря - Физика, в аудитории 3-2.✅')
                            '19 Июня в 8:30 - Анатомия в Скайпе. ✅')
        bot.send_message(message.chat.id,
        #                 '2 Января - Выш. мат, в аудитории 8-11.✅')
                            '22 Июня в 8:30 - Физика в Zoom. ✅')
        bot.send_message(message.chat.id,
       #                  '10 Января - История Украины, в аудитории 3-9.')
                         '26 Июня в 8:30 - Выш. мат в Скайпе. ✅')
    #@bot.message_handler(commands=['tm'])
    #def tm_mess(message):
    #   global Zn
    #   global firn
    #   firn = message.from_user.first_name
    #   wd = datetime.today().weekday()
    #   bot.send_message(message.chat.id,
    #                    firn + ", Карантин до 24 апреля.")
       # if Zn == True:
       #     if wd == 6:
       #         bot.send_message(message.chat.id,
       #                          'Понедельник:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Англ. Яз(Аудитория 3-2).\n3 Пара - Программирование(Аудитория 281).')
       #     elif wd == 0:
       #         bot.send_message(message.chat.id,
       #                          'Вторник:\n1 Пара - Выш. мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 7-40).\n3 Пара - Программирование(Аудитория 281).\n4 Пара - Программирование(Аудитория 281).')
       #     elif wd == 1:
       #         bot.send_message(message.chat.id,
       #                          'Среда:\n1 Пара - Анатомия человека(Аудитория 2-16).\n2 Пара - Физика(Аудитория 3-81).\n3 Пара - Физика(Аудитория 3-81).\n4 Пара - Кураторский час(Аудитория 281).')
       #     elif wd == 2:
       #         bot.send_message(message.chat.id,
       #                          'Четверг:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 3-79).')
       #     elif wd == 3:
       #         bot.send_message(message.chat.id,
       #                          'Пятница:\n1 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n2 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n3 Пара - Мед.-Биол. Досл.(Аудитория 284).')
       #     else:
       #         bot.send_message(message.chat.id,
       #                          'Завтра пар не должно быть.')
       # else:
       #     if wd == 6:
       #         bot.send_message(message.chat.id,
       #                          'Понедельник:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Англ. Яз(Аудитория 3-2).\n3 Пара - Программирование(Аудитория 281).')
       #     elif wd == 0:
       #         bot.send_message(message.chat.id,
       #                          'Вторник:\n1 Пара - Выш. мат(Аудитория 8-11).\n2 Пара - Выш. Мат(Аудитория 8-11).\n3 Пара - Физика(Аудитория 7-54).\n4 Пара - Программирование(Аудитория 281).')
       #     elif wd == 1:
       #         bot.send_message(message.chat.id,
       #                          'Среда:\n1 Пара - Анатомия человека(Аудитория 2-16).\n2 Пара - Анатомия человека(Аудитория 2-16).\n3 Пара - Физика(Аудитория 3-81).\n4 Пара - Кураторский час(Аудитория 281).')
       #     elif wd == 2:
       #         bot.send_message(message.chat.id,
       #                          'Четверг:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 3-79).')
       #     elif wd == 3:
       #         bot.send_message(message.chat.id,
       #                          'Пятница:\n1 Пара - Мед.-Биол. Досл.(Аудитория 284).\n2 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n3 Пара - Мед.-Биол. Досл.(Аудитория 284).')
       #     else:
       #         bot.send_message(message.chat.id,
       #                          'Завтра пар не должно быть.')
     #  check()

    #@bot.message_handler(commands=['week'])
    #def week(message):
   #     global Zn
   #     global firn
    #    firn = message.from_user.first_name
  #      wd = datetime.today().weekday()
     #   bot.send_message(message.chat.id,
     #                   firn + ", Карантин до 24 апреля.")
        # if Zn == True:
        #     bot.send_message(message.chat.id,
        #                      'Понедельник:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Англ. Яз(Аудитория 3-2).\n3 Пара: Програмирование(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Вторник:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Физика(Аудитория 7-40).\n3 Пара: Програмирование(Аудитория 281).\n4 Пара: Програмирование(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Среда:\n1Пара: Анатомия(Аудитория 2-16).\n2 Пара: Физика(Аудитория 3-81).\n3 Пара: Физика(Аудитория 3-81).\n4 Пара: Кур. Час(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Четверг:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Физика(Аудитория 3-79).')
        #     bot.send_message(message.chat.id,
        #                      'Пятница:\n1Пара: Лабы физика(Аудитория 3-35 3-36).\n2 Пара: Лабы физика(Аудитория 3-35 3-36).\n3 Пара: Мед. Биол. Досл.(Аудитория 284).')
        # else:
        #     bot.send_message(message.chat.id,
        #                      'Понедельник:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Англ. Яз(Аудитория 3-2).\n3 Пара: Програмирование(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Вторник:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Выш. Мат(Аудитория 8-11).\n3 Пара: Физика(Аудитория 7-54).\n4 Пара: Програмирование(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Среда:\n1Пара: Анатомия(Аудитория 2-16).\n2 Пара: Анатомия(Аудитория 2-16).\n3 Пара: Физика(Аудитория 3-81).\n4 Пара: Кур. Час(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Четверг:\n1Пара: Выш. Мат(Аудитория 8-11).\n2 Пара: Англ. Яз(Аудитория 3-2).\n3 Пара: Програмирование(Аудитория 281).')
        #     bot.send_message(message.chat.id,
        #                      'Пятница:\n1Пара: Мед. Биол. Досл.(Аудитория 284).\n2 Пара: Лабы физика(Аудитория 3-35 3-36).\n3 Пара: Мед. Биол. Досл.(Аудитория 284).')
    #    check()
    #@bot.message_handler(commands=['change'])
    #def change_para(message):
    #    global changep, cp
    #    changep = True
    #    cp = True
    #    change_text(message)
    #    check()

    #@bot.message_handler(commands=['back'])
    #def back(message):
    #    global cp
    #    cp = False
    #    bot.send_message(message.chat.id,
    #                     'Возвращаюсь.',
    #                     reply_markup = hideBoard)
    #    check()


   # @bot.message_handler(commands=['today'])
   # def today(message):
   #    global Zn
   #    global firn
   #    firn = message.from_user.first_name
    #   wd = datetime.today().weekday()
    #   bot.send_message(message.chat.id,
     #                   firn + ", Карантин до 24 апреля.")
       # if Zn == True:
       #     if wd == 0:
       #         bot.send_message(message.chat.id,
       #                          'Понедельник:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Англ. Яз(Аудитория 3-2).\n3 Пара - Программирование(Аудитория 281).')
       #     elif wd == 1:
       #         bot.send_message(message.chat.id,
       #                          'Вторник:\n1 Пара - Выш. мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 7-40).\n3 Пара - Программирование(Аудитория 281).\n4 Пара - Программирование(Аудитория 281).')
       #     elif wd == 2:
       #        bot.send_message(message.chat.id,
       #                          'Среда:\n1 Пара - Анатомия человека(Аудитория 2-16).\n2 Пара - Физика(Аудитория 3-81).\n3 Пара - Физика(Аудитория 3-81).\n4 Пара - Кураторский час(Аудитория 281).')
       #     elif wd == 3:
       #         bot.send_message(message.chat.id,
       #                          'Четверг:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 3-79).')
       #     elif wd == 4:
       #         bot.send_message(message.chat.id,
       #                          'Пятница:\n1 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n2 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n3 Пара - Мед.-Биол. Досл.(Аудитория 284).')
       #     else:
       #         bot.send_message(message.chat.id,
       #                          'Сегодня пар не должно быть.')
       # else:
       #     if wd == 0:
       #         bot.send_message(message.chat.id,
       #                          'Понедельник:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Англ. Яз(Аудитория 3-2).\n3 Пара - Программирование(Аудитория 281).')
       #     elif wd == 1:
       #         bot.send_message(message.chat.id,
       #                          'Вторник:\n1 Пара - Выш. мат(Аудитория 8-11).\n2 Пара - Выш. Мат(Аудитория 8-11).\n3 Пара - Физика(Аудитория 7-54).\n4 Пара - Программирование(Аудитория 281).')
       #     elif wd == 2:
       #         bot.send_message(message.chat.id,
       #                          'Среда:\n1 Пара - Анатомия человека(Аудитория 2-16).\n2 Пара - Анатомия человека(Аудитория 2-16).\n3 Пара - Физика(Аудитория 3-81).\n4 Пара - Кураторский час(Аудитория 281).')
       #     elif wd == 3:
       #         bot.send_message(message.chat.id,
       #                          'Четверг:\n1 Пара - Выш. Мат(Аудитория 8-11).\n2 Пара - Физика(Аудитория 3-79).')
       #     elif wd == 4:
       #         bot.send_message(message.chat.id,
       #                          'Пятница:\n1 Пара - Мед.-Биол. Досл.(Аудитория 284).\n2 Пара - Лабы по физике(Аудитория 3-35, 3-36).\n3 Пара - Мед.-Биол. Досл.(Аудитория 284).')
       #     else:
       #         bot.send_message(message.chat.id,
       #                          'Сегодня пар не должно быть.')
       # check()
    @bot.message_handler(commands=['ph'])
    def phone(message):
        bot.send_message(message.chat.id,
                         "Номера телефонов пока собираются старостой.")
        check()
    @bot.message_handler(commands=['rep'])
    def rep(message):
            global Zn
            global pok
            ban = message.from_user.id
            banan = message.text.split(' ')
            if ban == 481541926:
                try:
                    if banan[1] == 'zn.':
                        if Zn == True:
                            bot.send_message(message.chat.id,
                                             'Переменная Zn была равна True.')
                        else:
                            bot.send_message(message.chat.id,
                                             'Переменная Zn была равна False.')
                        Zn = True
                        pok = True
                        bot.send_message(message.chat.id,
                                         'Меняю, ваше высочество.')
                        bot.send_message(message.chat.id,
                                         'Переменная Zn теперь равна True.')
                    elif banan[1] == 'ch.':
                        if Zn == True:
                            bot.send_message(message.chat.id,
                                             'Переменная Zn была равна True.')
                        else:
                            bot.send_message(message.chat.id,
                                             'Переменная Zn была равна False.')
                        Zn = False
                        pok = False
                        bot.send_message(message.chat.id,
                                         'Меняю, ваше высочество.')
                        bot.send_message(message.chat.id,
                                         'Переменная Zn теперь равна False.')
                    elif banan[1] == 'exit.':
                        bot.send_message(message.chat.id,
                                         'Бот наелся и спит. Бот умер.')
                        os._exit()
                except IndexError:
                    bot.send_message(message.chat.id,
                                     'Вот форма: "/rep ch." или "/rep zn.".\nДля завершения работы бота: "/rep exit.".')
            else:
                bot.send_message(message.chat.id,
                                 'У вас недостаточно прав для использования этой команды.')
    @bot.message_handler(commands=['book'])
    def book(message):
        bot.send_message(message.chat.id,
                         "https://drive.google.com/folderview?id=175giAWQJsAa7fKW_kiKpzt8VwM18AUul")
        check()
    @bot.message_handler(commands=['next'])
    def next_para(message):
        bot.send_message(message.chat.id,
                         'Поздравляю с успешной сдачей экзаменов!')
    #   global Zn, change, changep, pok, firn
    #    firn = message.from_user.first_name
    #    now = datetime.now()
   #     wd = datetime.today().weekday()
  #      ths = datetime.strftime(datetime.now(), "%H")
  #      tms = datetime.strftime(datetime.now(), "%M")
  #      fp = 30*60000+8*3600000
  #      ffp = 9*3600000+50*60000
  #      sp = 10*60000+10*3600000
  #      ssp = 11*3600000 + 30*60000
   #     tp = 12*3600000
   #     ttp = 13*3600000 + 20*60000
  #      fop = 13*3600000+40*60000
   #     end = 15*3600000
  #      th = int(ths)
  #      tm = int(tms)
   #     t = tm*60000+(th - 1)*3600000
  #      bot.send_message(message.chat.id,
   #                     firn + ", Карантин до 24 апреля.")
        # if changep == False:
        #     if Zn == True:
        #         if wd == 0:
        #             if t <= fp:
        #                 pon111 = bot.send_message(message.chat.id,
        #                                         firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11).')
        #             elif t > fp:
        #                 if t <= ffp:
        #                     pon1111 = bot.send_message(message.chat.id,
        #                                                firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Англ. Яз в 10:10(Аудитория 3-2).')
        #                 elif t > ffp:
        #                     if t <= sp:
        #                         pon112 = bot.send_message(message.chat.id,
        #                                                  firn + ', в 10:10 будет Англ. Яз(Аудитория 3-2).')
        #                     elif t > sp:
        #                         if t <= ssp:
        #                             pon1122 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идёт Англ. Яз(Аудитория 3-2).\nСледующая пара - Программирование в 12:00(Аудитория 281).')
        #                         elif t >ssp:
        #                             if t <= tp:
        #                                 pon113 = bot.send_message(message.chat.id,
        #                                                          firn + ', в 12:00 будет Программирование(Аудитория 281).')
        #                             elif t > tp:
        #                                 if t <= fop:
        #                                     pon114 = bot.send_message(message.chat.id,
        #                                                              firn + ', Идёт последняя пара(Программирование в 281).')
        #                                 else:
        #                                     pon11e = bot.send_message(message.chat.id,
        #                                                             firn + ', пары кончились.')
        #         elif wd == 1:
        #             if t <= fp:
        #                 pon121 = bot.send_message(message.chat.id,
        #                                 firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11.')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             pon1111 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Физика в 10:10(Аудитория 7-40).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             pon122 = bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет Физика(Аудитория 7-40).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 pon1222 = bot.send_message(message.chat.id,
        #                                                            firn + ', сейчас идёт Физика(Аудитория 7-40).\nСледующая пара - Программирование в 12:00(Аудитория 281).')
        #                             elif t > ssp:
        #                                 if t <= tp:
        #                                     pon123 = bot.send_message(message.chat.id,
        #                                                      firn + ', в 12:00 будет Программирование(Аудитория 281).')
        #                                 elif t > tp:
        #                                     if t <= ttp:
        #                                         pon1233 = bot.send_message(message.chat.id,
        #                                                                    firn + ', сейчас идёт Программирование(Аудитория 281).\nСледующая пара - Программирование в 13:40(Аудитория 281).')
        #                                     elif t > ttp:
        #                                         if t <= fop:
        #                                             pon124 = bot.send_message(message.chat.id,
        #                                                               firn + ', в 13:40 будет Программирование(Аудитория 281).')
        #                                         elif t > fop:
        #                                             if t <= end:
        #                                                 pon124g = bot.send_message(message.chat.id,
        #                                                                  firn + ', идёт последняя пара(Программирование в 281).')
        #                                             elif t > end:
        #                                                 pon12e = bot.send_message(message.chat.id,
        #                                                                  firn + ', пары кончились.')
        #
        #         elif wd == 2:
        #             if t <= fp:
        #                 pon131 = bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Анатомия человека(Аудитория 2-16).')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             pon1111 = bot.send_message(message.chat.id,
        #                                                     firn + ', сейчас идёт Анатомия человека(Аудитория 2-16).\nСледующая пара - Физика в 10:10(Аудитория 3-81).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             pon132 = bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет физика(Аудитория 3-81).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 pon1322 = bot.send_message(message.chat.id,
        #                                                            firn + ', сейчас идёт физика(Аудитория 3-81).\nСледующая пара - Физика в 12:00(Аудитория 3-81).')
        #                             elif t > ssp:
        #                                 if t <= tp:
        #                                     pon133 = bot.send_message(message.chat.id,
        #                                                      firn + ', в 12:00 будет Физика(Аудитория 3-81).')
        #                                 elif t > tp:
        #                                     if t <= ttp:
        #                                         pon1333 = bot.send_message(message.chat.id,
        #                                                                    firn + ', сейчас идёт Физика(Аудитория 3-81).\nСледующая пара - кураторский час(Аудитория 281).')
        #                                     elif t >ttp:
        #                                         if t <= fop:
        #                                             pon134 = bot.send_message(message.chat.id,
        #                                                              firn + ', в 13:40 будет кураторский час(Аудитория 281).')
        #                                         elif t > fop:
        #                                             if t <= end:
        #                                                 pon134g = bot.send_message(message.chat.id,
        #                                                                  firn + ', идёт последняя пара(Кураторский час в ауд. 281).')
        #                                             elif t > end:
        #                                                 pon13e = bot.send_message(message.chat.id,
        #                                                                  firn + ', пары кончились.')
        #         elif wd == 3:
        #             if t <= fp:
        #                 bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11).')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             bot.send_message(message.chat.id,
        #                                             firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Физика в 10:10(Аудитория 3-79).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет физика(Аудитория 3-79).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 bot.send_message(message.chat.id,
        #                                             firn + ', сейчас идёт физика(Аудитория 3-79).\nЭто последняя пара.')
        #                             elif t > ssp:
        #                                     bot.send_message(message.chat.id,
        #                                                      firn + ', пары кончились.')
        #         elif wd == 4:
        #             if t <= fp:
        #                 pon151 = bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Лабы по физике(Аудитория 3-35, 3-36).')
        #             elif t > fp:
        #                 if t <= ffp:
        #                     pon1511 = bot.send_message(message.chat.id,
        #                                                firn + ', сейчас идут лабы по физике(Аудитория 3-35, 3-36).\nДальше будут Лабы по физике в 10:10(Аудитория 3-35, 3-36).')
        #                 elif t >ffp:
        #                     if t <= sp:
        #                         pon152 = bot.send_message(message.chat.id,
        #                                          firn + ', в 10:10 будут лабы по физике(Аудитория 3-35, 3-36).')
        #                     elif t > sp:
        #                         if t <= ssp:
        #                             pon1522 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идут лабы по физике(Аудитория 3-35, 3-36).\nДальше будут Мед.-Биол. Досл. в 12:00(Аудитория 284).')
        #                         elif t > ssp:
        #                             if t <= tp:
        #                                 pon153 = bot.send_message(message.chat.id,
        #                                                  firn + ', в 12:00 будет Мед.-Биол. Досл.(Аудитория 284).')
        #                             elif t > tp:
        #                                 if t <= fop:
        #                                     pon154 = bot.send_message(message.chat.id,
        #                                                      firn + ', идёт последняя пара(Мед.-Биол. Досл. в 284).')
        #                                 elif t > fop:
        #                                     if t <= end:
        #                                         pon154g = bot.send_message(message.chat.id,
        #                                                          firn + ', четвёртой пары у вас нет.')
        #                                     elif t > end:
        #                                         pon15e = bot.send_message(message.chat.id,
        #                                                          firn + ', пары кончились.')
        #
        #         elif wd == 5:
        #             pon16 = bot.send_message(message.chat.id,
        #                              firn + ', сегодня суббота(выходной).')
        #
        #         elif wd == 6:
        #             pon17 = bot.send_message(message.chat.id,
        #                              firn + ', сегодня воскресенье(выходной).')
        #     else:
        #         if wd == 0:
        #             if t <= fp:
        #                 pon111 = bot.send_message(message.chat.id,
        #                                         firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11).')
        #             elif t > fp:
        #                 if t <= ffp:
        #                     pon1111 = bot.send_message(message.chat.id,
        #                                                firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Англ. Яз в 10:10(Аудитория 3-2).')
        #                 elif t > ffp:
        #                     if t <= sp:
        #                         pon112 = bot.send_message(message.chat.id,
        #                                                  firn + ', в 10:10 будет Англ. Яз(Аудитория 3-2).')
        #                     elif t > sp:
        #                         if t <= ssp:
        #                             pon1122 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идёт Англ. Яз(Аудитория 3-2).\nСледующая пара - Программирование в 12:00(Аудитория 281).')
        #                         elif t >ssp:
        #                             if t <= tp:
        #                                 pon113 = bot.send_message(message.chat.id,
        #                                                          firn + ', в 12:00 будет Программирование(Аудитория 281).')
        #                             elif t > tp:
        #                                 if t <= fop:
        #                                     pon114 = bot.send_message(message.chat.id,
        #                                                              firn + ', Идёт последняя пара(Программирование в 281).')
        #                                 else:
        #                                     pon11e = bot.send_message(message.chat.id,
        #                                                             firn + ', пары кончились.')
        #         elif wd == 1:
        #             if t <= fp:
        #                 pon121 = bot.send_message(message.chat.id,
        #                                 firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11.')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             pon1111 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Выш. Мат в 10:10(Аудитория 8-11).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             pon122 = bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет Выш. Мат(Аудитория 8-11).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 pon1222 = bot.send_message(message.chat.id,
        #                                                            firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Физика в 12:00(Аудитория 7-54).')
        #                             elif t > ssp:
        #                                 if t <= tp:
        #                                     pon123 = bot.send_message(message.chat.id,
        #                                                      firn + ', в 12:00 будет Физика(Аудитория 7-54).')
        #                                 elif t > tp:
        #                                     if t <= ttp:
        #                                         pon1233 = bot.send_message(message.chat.id,
        #                                                                    firn + ', сейчас идёт Физика(Аудитория 7-54).\nСледующая пара - Программирование в 13:40(Аудитория 281).')
        #                                     elif t > ttp:
        #                                         if t <= fop:
        #                                             pon124 = bot.send_message(message.chat.id,
        #                                                               firn + ', в 13:40 будет Программирование(Аудитория 281).')
        #                                         elif t > fop:
        #                                             if t <= end:
        #                                                 pon124g = bot.send_message(message.chat.id,
        #                                                                  firn + ', идёт последняя пара(Программирование в 281).')
        #                                             elif t > end:
        #                                                 pon12e = bot.send_message(message.chat.id,
        #                                                                  firn + ', пары кончились.')
        #
        #         elif wd == 2:
        #             if t <= fp:
        #                 pon131 = bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Анатомия человека(Аудитория 2-16).')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             pon1111 = bot.send_message(message.chat.id,
        #                                                     firn + ', сейчас идёт Анатомия человека(Аудитория 2-16).\nСледующая пара - Анатомия человека в 10:10(Аудитория 2-16).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             pon132 = bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет Анатомия человека(Аудитория 2-16).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 pon1322 = bot.send_message(message.chat.id,
        #                                                            firn + ', сейчас идёт Анатомия человека(Аудитория 2-16).\nСледующая пара - Физика в 12:00(Аудитория 3-81).')
        #                             elif t > ssp:
        #                                 if t <= tp:
        #                                     pon133 = bot.send_message(message.chat.id,
        #                                                      firn + ', в 12:00 будет Физика(Аудитория 3-81).')
        #                                 elif t > tp:
        #                                     if t <= ttp:
        #                                         pon1333 = bot.send_message(message.chat.id,
        #                                                                    firn + ', сейчас идёт Физика(Аудитория 3-81).\nСледующая пара - кураторский час(Аудитория 281).')
        #                                     elif t >ttp:
        #                                         if t <= fop:
        #                                             pon134 = bot.send_message(message.chat.id,
        #                                                              firn + ', в 13:40 будет кураторский час(Аудитория 281).')
        #                                         elif t > fop:
        #                                             if t <= end:
        #                                                 pon134g = bot.send_message(message.chat.id,
        #                                                                  firn + ', идёт последняя пара(Кураторский час в ауд. 281).')
        #                                             elif t > end:
        #                                                 pon13e = bot.send_message(message.chat.id,
        #                                                                  firn + ', пары кончились.')
        #         elif wd == 3:
        #             if t <= fp:
        #                 bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Выш. Мат(Аудитория 8-11).')
        #             elif t > fp:
        #                     if t <= ffp:
        #                             bot.send_message(message.chat.id,
        #                                             firn + ', сейчас идёт Выш. Мат(Аудитория 8-11).\nСледующая пара - Физика в 10:10(Аудитория 3-79).')
        #                     elif t > ffp:
        #                         if t <= sp:
        #                             bot.send_message(message.chat.id,
        #                                              firn + ', в 10:10 будет физика(Аудитория 3-79).')
        #                         elif t > sp:
        #                             if t <= ssp:
        #                                 bot.send_message(message.chat.id,
        #                                             firn + ', сейчас идёт физика(Аудитория 3-79).\nЭто последняя пара.')
        #                             elif t > ssp:
        #                                     bot.send_message(message.chat.id,
        #                                                      firn + ', пары кончились.')
        #         elif wd == 4:
        #             if t <= fp:
        #                 pon151 = bot.send_message(message.chat.id,
        #                                  firn + ', в 8:30 будет Мед.-Биол. Досл.(Аудитория 284).')
        #             elif t > fp:
        #                 if t <= ffp:
        #                     pon1511 = bot.send_message(message.chat.id,
        #                                                firn + ', сейчас идут Мед.-Биол. Досл.(Аудитория 284).\nДальше будут Лабы по физике в 10:10(Аудитория 3-35, 3-36).')
        #                 elif t >ffp:
        #                     if t <= sp:
        #                         pon152 = bot.send_message(message.chat.id,
        #                                          firn + ', в 10:10 будут лабы по физике(Аудитория 3-35, 3-36).')
        #                     elif t > sp:
        #                         if t <= ssp:
        #                             pon1522 = bot.send_message(message.chat.id,
        #                                                        firn + ', сейчас идут лабы по физике(Аудитория 3-35, 3-36).\nДальше будут Мед.-Биол. Досл. в 12:00(Аудитория 284).')
        #                         elif t > ssp:
        #                             if t <= tp:
        #                                 pon153 = bot.send_message(message.chat.id,
        #                                                  firn + ', в 12:00 будет Мед.-Биол. Досл.(Аудитория 284).')
        #                             elif t > tp:
        #                                 if t <= fop:
        #                                     pon154 = bot.send_message(message.chat.id,
        #                                                      firn + ', идёт последняя пара(Мед.-Биол. Досл. в 284).')
        #                                 elif t > fop:
        #                                     if t <= end:
        #                                         pon154g = bot.send_message(message.chat.id,
        #                                                          firn + ', четвёртой пары у вас нет.')
        #                                     elif t > end:
        #                                         pon15e = bot.send_message(message.chat.id,
        #                                                          firn + ', пары кончились.')
        #         elif wd == 5:
        #             pon26 = bot.send_message(message.chat.id,
        #                              firn + ', сегодня суббота(выходной).')
        #         elif wd == 6:
        #             pon27 = bot.send_message(message.chat.id,
        #                              firn + ', сегодня воскресенье(выходной).')
        #
        #
        # check()
    DayOfAWeek = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=7)
    DayOfAWeek.row('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС')
    pair = types.ReplyKeyboardMarkup(True, True)
    pair.row('1', '2', '3', '4')
    @bot.message_handler(content_types=['text'])
    def change_text(message):
        toc = False
        global Zn, cp, changep, pon111, pon112, pon113, pon114, pon11e, pon121, pon122, pon123, pon124, pon124g, pon12e, pon131, pon132, pon133, pon134, pon134g, pon13e, pon141, pon142, pon143, pon144, pon144g, pon14e, pon151, pon152, pon153, pon154, pon154g, pon15e, pon16, pon17, pon211, pon212, pon213, pon214, pon214g, pon21e, pon221, pon222, pon223, pon224, pon224g, pon22e, pon231, pon232, pon233, pon234, pon234g, pon23e, pon241, pon242, pon243, pon244, pon244g, pon24e, pon251, pon252, pon253, pon254, pon254g, pon25e, pon26, pon27
        if cp == True:
            bot.send_message(message.chat.id,
                             'В каком дне недели будут проводится изменения?',
                             reply_markup=DayOfAWeek)
            if Zn == False:
                if message.text.lower() == 'пн':
                    toc = True
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                    if message.text.lower() == '1':
                        print('1')
                elif message.text.lower() == 'вт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'ср':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'чт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'пт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'сб':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'вс':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
            else:
                if message.text.lower() == 'пн':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'вт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'ср':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'чт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'пт':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'сб':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
                elif message.text.lower() == 'вс':
                    bot.send_message(message.chat.id,
                                     'Какую пару меняем?',
                                     reply_markup=pair)
        else:
            pass
        check()



    #keyboard0 = telebot.types.ReplyKeyboardMarkup(True, True)
    #keyboard0.row('Добавить.', 'Что купить?')


    #@bot.message_handler(content_types=['text'])

    # def send_text(message):

    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass


