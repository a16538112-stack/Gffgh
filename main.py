import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن ومعرف الأدمن الخاص بك
TOKEN = "8848485695:AAHaE3adR_XFhEHehHKjck2U3gjvFZRWMdY"
ADMIN_ID = 7713496654

bot = telebot.TeleBot(TOKEN)

# رسالة البداية والأوامر الرئيسية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("📱 الأرقام المتاحة", callback_data="get_numbers"))
    markup.row(InlineKeyboardButton("💰 رصيدي", callback_data="my_balance"),
               InlineKeyboardButton("⚙️ دعم العملاء", callback_data="support"))
    
    if message.from_user.id == ADMIN_ID:
        markup.row(InlineKeyboardButton("🛠 لوحة تحكم الأدمن", callback_data="admin_panel"))

    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت الأرقام الوهمية واستلام الـ OTP.\n"
        "اختر أحد الخيارات أدناه للبدء:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# التعامل مع الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "get_numbers":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "قائمة الدول والأرقام ستظهر هنا قريباً...")
    
    elif call.data == "my_balance":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "رصيدك الحالي: 0 نقطة / جنيه.")
        
    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "للتواصل مع الدعم الفني: @YourUsername")
        
    elif call.data == "admin_panel" and call.from_user.id == ADMIN_ID:
        bot.answer_callback_query(call.id)
        admin_markup = InlineKeyboardMarkup()
        admin_markup.row(InlineKeyboardButton("➕ إضافة دولة/رقم", callback_data="add_number"))
        admin_markup.row(InlineKeyboardButton("📊 إحصائيات البوت", callback_data="bot_stats"))
        bot.send_message(call.message.chat.id, "مرحباً بك في لوحة تحكم الأدمن:", reply_markup=admin_markup)

# تشغيل البوت
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
