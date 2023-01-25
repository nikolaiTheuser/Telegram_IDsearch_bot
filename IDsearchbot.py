import telebot

bot = telebot.TeleBot("5864046084:AAEU72GwWKxHptUYWZbLSZZUCiNMBjfqkfA")

@bot.message_handler(commands=['find'])
def find_user(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Please provide a user ID.")
        return
    user_id = message.text.split()[1]
    try:
        user = bot.get_chat_member(chat_id=user_id, user_id=user_id)
        bot.reply_to(message, f'User found: {user.user.first_name} {user.user.last_name}')
    except:
        bot.reply_to(message, "User not found.")

bot.polling()