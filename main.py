from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

# Вставь сюда свой токен
TOKEN = '8467643191:AAHh1B3-CX6df73BHMiPgAuOQsBVTVtU9VU'

# Логирование (чтобы видеть ошибки, если что)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/price", "/contact"], ["/stats", "/help"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет, я твой личный ассистент 💅\n\n"
        "Я могу рассказать тебе всё о моих услугах, подписке и контактах. Просто выбери команду ниже:",
        reply_markup=reply_markup
    )

# Help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Команды:\n"
        "/start — начать общение\n"
        "/price — узнать прайс 💸\n"
        "/contact — мои соцсети и ссылки 📲\n"
        "/stats — статистика подписчиков 📊\n"
        "/help — список команд"
    )

# Прайс
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 Прайс:\n"
        "❤ Фото: $10\n"
        "❤ Видео: $25\n"
        "❤ Эксклюзив: $50\n"
        "❤ Персональный контент: от $100\n"
        "❤ Заказы обсуждаются в личке 💌"
    )

# Контакты
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📩 Мои контакты:\n"
        "🤑 Telegram: @darilicious\n"
        "🤑 OnlyFans: onlyfans.com/dasha\n"
        "🤑 Fansly: fansly.com/dasha\n"
        "🤑 Instagram: instagram.com/daria\n"
        "Пиши, не стесняйся 😘"
    )

# Статистика
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subscribers = 300
    price = 15
    income = subscribers * price
    await update.message.reply_text(
        f"📊 Подписчиков: {subscribers}\n"
        f"💰 Подписка: ${price}\n"
        f"💸 Примерный доход: ${income}/мес"
    )

# Автоответы на сообщения
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text("Привет, сладкий 😘")
    elif "прайс" in text:
        await price(update, context)
    elif "контакт" in text or "insta" in text or "of" in text:
        await contact(update, context)
    elif "доход" in text or "статистика" in text:
        await stats(update, context)
    else:
        await update.message.reply_text("Я тебя услышала 😌 Напиши /help, чтобы посмотреть, что я умею.")

# Запуск приложения
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("✅ Бот запущен. Ждёт твоих команд.")
app.run_polling()
