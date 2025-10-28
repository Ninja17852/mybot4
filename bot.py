from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ====== Настройки ======
TOKEN = "8295768483:AAEVvVxwLe00xW3pCz6R6_1nV0_OPuZXu9k"
GROUP_LINK = "https://t.me/+N4PanSH-rkQ5ODMy"  # вставь ссылку на группу

WELCOME_TEXT = """Добро пожаловать в транспортную компанию "СompanyMyk"! 🚚

📍Важно:📍
После подключения к нашему Telegram-каналу обязательно укажите игровой ник в разделе «Игровые никнеймы».

🌸 О нас: 🌸
Рады видеть вас в нашей команде! Компания расположена по GPS-координатам 9 ->13.

❓Если появятся вопросы или нужна помощь, всегда обращайтесь к руководству:
• Глава компании — Morgan Murphy
• Заместители — Lika Eclise и Irina Reger

📍Норматив наката: 📍
🟢 1–5 скилл → 10k 
🔵 5–20 скилл → 15k 
🔴 20+ скилл → 25k 

‼️Длительное отсутствие без предупреждения приводит к кику. Если не сможете накатать в какой-либо день — сообщите об этом в разделе «не кикать».‼️

🧷Команды, которые вам понадобятся:🧷
/Cinfo - просмотр своего наката
/cmenu -> автопарк -> аренда газона/тягача
         -> топливо -> заправка транспорта
/С -> чат тк

Спасибо, что выбрали companyMyk! Желаем удачи и безопасных дорог! 🌟
"""

# ====== Функция для /start ======
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ Ознакомлен", url=GROUP_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# ====== Запуск бота ======
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", send_welcome))
app.run_polling()