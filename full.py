import telebot
import mysql.connector
print('Initializing Service...')
bot=telebot.TeleBot('TELEGRAM API TOKEN FROM BOT FATHER')
connection = mysql.connector.connect( 
    password='2Kv3SdxgkY',
    user='sql12745700',
    host='52.76.27.242',
    database='sql12745700',
    )
mycursor=connection.cursor()

def datalogger(message):
    sql='INSERT INTO telegrambot_tbl (`name`,`username`,`message`) VALUES(%s,%s,%s)'
    val=(message.chat.first_name,message.chat.id,message.text)
    mycursor.execute(sql,val)
    connection.commit()
@bot.message_handler()
def welcome(message):
    bot.reply_to(message,'recived messsage✅')
    #datalogger(message)
    mess="🔴From :"+message.chat.first_name+"\n message :⬇️⬇️⬇️ \n"+message.text
    bot.send_message(6269684719,mess)
    print('New Message From ',message.chat.first_name,"ID:",message.chat.id)
    
print('Normal Status')    
bot.polling()    
