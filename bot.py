import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN est absente.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = [
        [
            InlineKeyboardButton(
                "🌐 Ouvrir le site",
                url="https://vente-ctv.vercel.app/"
            )
        ]
    ]

    clavier = InlineKeyboardMarkup(bouton)

    await update.message.reply_text(
        "Bienvenue sur ma boutique 👋",
        reply_markup=clavier
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot Telegram lancé")

    app.run_polling()


if __name__ == "__main__":
