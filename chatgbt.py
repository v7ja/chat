from telebot import *
from mindai import *
from types import *
bot = TeleBot("6802039492:AAFP9j8wMu2ZqQa5xsj2gc8aGLx654jFyj8")
#توكن بوتك 
@bot.message_handler(commands=['start'])
def start(message):
    userm = message.from_user.username
    ID = message.from_user.id
    name_pro = message.from_user
    key = types.InlineKeyboardMarkup()
    bot1 = types.InlineKeyboardButton('- عَبود يابه؟ ' ,url ='https://t.me/xx_YaBh')
    bot2 = types.InlineKeyboardButton('- aBooD ، هواجيس؟' ,url ='https://t.me/xxYaBh')
    key.add(bot1,bot2)
    p1ng = "https://t.me/xxYaBh/2247"
    bot.send_photo(message.chat.id,p1ng,f"""<strong>
 English :- 
- Welcom  @{userm} .
- Yuor Id {ID}
- Send Yuo And Bot .
- Start Now .
* - - - - - - - - - - - - - - - - -*
Arbic :  
- هلا يابه؟ @{userm}
يابهه احجي وية البوت بس لنگليزي ،
يلاا احجيي ، 
</strong>""",parse_mode="html",reply_markup=key)
@bot.message_handler(func=lambda message: True)
def main(message):
    x = Ai().chat(message=message.text)
    bot.reply_to(message,x['reply'])
bot.infinity_polling()
