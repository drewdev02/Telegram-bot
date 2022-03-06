from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, context):
    message = update.effective_message
    message.reply_text('Click abajo para continuar', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="CLICK AQUI", callback_data="test")]]))

def help(Update, context):
    message = update.effective_message
    message.reply_text('Click abajo para continuar', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Help me", callback_data="Help")]]))
    

def test(update, context):
    message = update.effective_message
    query = update.callback_query
    query.answer()
    

    if query.data == 'test':
        message.reply_text(text='SI, lo admito soy fan del chocolate!!')




if __name__ == '__main__':
    updater = Updater(token='5157710415:AAFF7mqTrNzrH-a6JrOWCQQ5NN40JXs9zlM')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(test, pattern='test'))
    
    updater.start_polling()
    print('bot is started')
    updater.idle()
