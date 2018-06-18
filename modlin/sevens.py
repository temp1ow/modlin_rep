
import conf
import telebot
import os, time
import urllib.request
import shutil, glob
import datetime


bot = telebot.TeleBot(conf.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    try:
        bot.send_message(message.chat.id, 'Ваша мастер-ветка') #обработка входящего сообщений
        mess = (str.split(message.text, " ")) #присваивание переменных
        user = mess[0]
        user_project = mess[1]
        print(user, user_project)
        print(str(message.text))
        home_dir=(str("/home/modlin/modlin/"))
        today = str(datetime.datetime.today().strftime("%Y%m%d")) #определение даты сегодня для передачи в имя

        zip_date =home_dir+user+user_project+".zip" #путь к зип репозитория
        filo=os.path.isfile(zip_date)
     
        print(filo)
        page=str("https://codeload.github.com/"+user+"/"+user_project+"/zip/master")    
        if filo == True: # Проверка существования файла, если существует, просто отдаем в сообщении, если нет качаем
            try:
                doc = open(home_dir+user+user_project+".zip",'rb')
                print (doc, 'doc True')
                bot.send_document(message.from_user.id,doc)
            except urllib.error.HTTPError: # проверка существования репозитория
               result = "URL and project not found False"

               bot.send_document(message.from_user.id,result)

        elif filo == False:
            try:
                with urllib.request.urlopen(page) as load, open(zip_date, "wb") as result_load:
                    shutil.copyfileobj(load, result_load)
                    doc = open(zip_date, 'rb')
                    print (doc, 'doc False')
                    bot.send_document(message.from_user.id,doc)
            except urllib.error.HTTPError: 
               result = "URL and project not found False"
               bot.send_document(message.from_user.id,result)
    except  FileNotFoundError: 
            result = "Fila net"
    except urllib.error.HTTPError: 
            result = "URL and project not found False"
            bot.send_document(message.from_user.id,result)
    except IndexError: 
            result = "URL and project not found False"
            bot.send_document(message.from_user.id,result)
    except  UnicodeEncodeError:
            result = "нет такого репозитория"
            bot.send_document(message.from_user.id,result)       
if __name__ == '__main__':
    bot.polling(none_stop=True)