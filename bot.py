from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import mysql.connector

# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')

def message(update: Update, context: CallbackContext) -> None:
    cnx = mysql.connector.connect(user='num', password='iJ9Xis*jciuH3FN',
                              host='194.58.104.159',
                              database='num')
    cursor = cnx.cursor()
    query = ("SELECT text FROM info WHERE number = %s")
    cursor.execute(query, (update.message.text, ))
    for (text, ) in cursor:
        update.message.reply_html(text)
    cnx.close()

updater = Updater('1095748137:AAHD7bSb_zyOkc04ixncG7h-obsqYhalxSE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.all, message))

updater.start_polling()
updater.idle()
