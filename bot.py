from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import mysql.connector
from calc import matrix

def message(update: Update, context: CallbackContext) -> None:
#     cnx = mysql.connector.connect(user='num', password='iJ9Xis*jciuH3FN',
#                               host='194.58.104.159',
#                               database='num')
#     cursor = cnx.cursor()
#     query = ("SELECT text FROM info WHERE number = %s")
#     cursor.execute(query, (update.message.text, ))
#     print('message')
#     for (text, ) in cursor:
    matrixData = matrix(update.message.text)
    keyboard = [
        [
            InlineKeyboardButton(matrixData[0], callback_data="1"),
            InlineKeyboardButton(matrixData[3], callback_data="4"),
            InlineKeyboardButton(matrixData[6], callback_data="7"),
        ],
        [
            InlineKeyboardButton(matrixData[1], callback_data="2"),
            InlineKeyboardButton(matrixData[4], callback_data="5"),
            InlineKeyboardButton(matrixData[7], callback_data="8"),
        ],
        [
            InlineKeyboardButton(matrixData[2], callback_data="3"),
            InlineKeyboardButton(matrixData[5], callback_data="6"),
            InlineKeyboardButton(matrixData[8], callback_data="9"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_html('test', reply_markup=reply_markup)
#     cnx.close()

updater = Updater('1095748137:AAHD7bSb_zyOkc04ixncG7h-obsqYhalxSE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.all, message))

updater.start_polling()
updater.idle()
