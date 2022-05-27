from telegram import *
from telegram.ext import *
from requests import *
import os
PORT = int(os.environ.get('PORT', 5000))

TOKEN = '5247703195:AAFhyLY4RD-_a6_xdaWRI3_t_ixMl4LWmp4'

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

ourbookstext = "كتبنا"
ourarticlestext = "مقالاتنا"

books = ["المغني في ابواب التوحيد والعدل","تفسير الكشاف","المعتمد","شرح الأصول الخمسة","رسالة إبليس إلى أخوانه المناحيس"]

book1 = ["رؤية الباري","الفرق غير الإسلامية","التعديل والتجوير","الإرادة","خلق القرآن","المخلوق","التوليد","التكليف","النظر والمعارف","اللطف","الأصلح","التنبؤات و المعجزات","إعجاز القرآن","الشرعيات","في الإمامة"]
def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(ourbookstext)], [KeyboardButton(ourarticlestext)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the bot!", reply_markup=ReplyKeyboardMarkup(buttons))

def messageHandler(update: Update, context: CallbackContext):
    if ourbookstext in update.message.text:
        buttons = [[KeyboardButton(books[0])],
                   [KeyboardButton(books[1])],
                   [KeyboardButton(books[2])],
                   [KeyboardButton(books[3])],
                   [KeyboardButton(books[4])],
        ]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the bot!", reply_markup=ReplyKeyboardMarkup(buttons))
    if books[0] == update.message.text:
        buttons = [[KeyboardButton(book1[0]),KeyboardButton(book1[1]),KeyboardButton(book1[2])],
                   [KeyboardButton(book1[3]),KeyboardButton(book1[4]),KeyboardButton(book1[5])],
                   [KeyboardButton(book1[6]),KeyboardButton(book1[7]),KeyboardButton(book1[8])],
                   [KeyboardButton(book1[9]),KeyboardButton(book1[10]),KeyboardButton(book1[11])],
                   [KeyboardButton(book1[12]),KeyboardButton(book1[13]),KeyboardButton(book1[14])],
        ]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the bot!", reply_markup=ReplyKeyboardMarkup(buttons))
    if book1[0] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='35')
    if book1[1] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='36')
    if book1[2] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='37')
    if book1[3] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='38')
    if book1[4] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='39')
    if book1[5] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='40')
    if book1[6] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='41')
    if book1[7] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='42')
    if book1[8] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='43')
    if book1[9] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='44')
    if book1[10] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='45')
    if book1[11] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='46')
    if book1[12] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='47')
    if book1[13] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='48')
    if book1[14] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='49')
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='50')
    if books[1] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='51')
    if books[2] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='52')
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='53')
    if books[3] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='56')
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='57')
    if books[4] == update.message.text:
        context.bot.forward_message(chat_id='5382369552', from_chat_id='-1001724830195', message_id='55')
dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://oawlahetest.herokuapp.com/' + TOKEN)