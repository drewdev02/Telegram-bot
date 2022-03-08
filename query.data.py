import os
import qrcode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters,MessageHandler
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton

IMPUT_TEXT = 0

def start(update, context):
    update.message.reply_text(
        text='Hola bienvenido!!\n\nUsa "/qr" para generar un qr',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Generar qr', callback_data='qr')],
           # [InlineKeyboardButton(text='Autor', url='@Assange')]
        ])
    )

def help(update, context):
    update.message.reply_text('Este bot fue creado por @Assange escribe para cualquier sugerencia')    

def qr_command_handler(update, context):
    update.message.reply_text('Envia el texto para generar un QR')
    
    return IMPUT_TEXT

def qr_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    
    query.edit_message_text(
        text='Envia el texto para generar un QR'
    )
     
    return IMPUT_TEXT
def generate_qr(text):
    
    filename = text + '.jpg'
    
    img = qrcode.make(text)
    img.save(filename)
    
    return filename

def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)

def imput_text(update, context):
  text = update.message.text
  filename = generate_qr(text)
  chat = update.message.chat
  
  send_qr(filename, chat)
  
  return ConversationHandler.END
  
    


if __name__ == '__main__':
    
    updater = Updater(token='5157710415:AAFF7mqTrNzrH-a6JrOWCQQ5NN40JXs9zlM', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(ConversationHandler(
        entry_points=[
           CommandHandler('qr', qr_command_handler),
           CallbackQueryHandler(pattern='qr', callback =qr_callback_handler)   
            ],
         states={
         IMPUT_TEXT: [MessageHandler(Filters.text, imput_text)]
            
        },
        
        fallbacks=[]
    ))
    
    
    updater.start_polling()
    print('bot is started')
    updater.idle()
