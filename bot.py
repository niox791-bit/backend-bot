import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("La variable TOKEN est absente de Render.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = [
        [
            InlineKeyboardButton(
                "📱 Ouvrir l’application",
                web_app=WebAppInfo(url="https://vente-ctv.vercel.app/")
            )
        ]
    ]

    clavier = InlineKeyboardMarkup(bouton)

    await update.message.reply_text(
        "Bienvenue sur ma boutique 👋\n\n"
        "Appuie sur le bouton ci-dessous pour ouvrir l’application.",
        reply_markup=clavier
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))


if __name__ == "__main__":
    print("✅ Bot lancé")
    app.run_polling()
