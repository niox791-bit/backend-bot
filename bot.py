import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("La variable TOKEN est absente.")


# =========================================================
# MESSAGE PRIVÉ : /start
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = [
        [
            InlineKeyboardButton(
                "🛍️ Ouvrir l’application",
                web_app=WebAppInfo(
                    url="https://vente-ctv.vercel.app/"
                ),
            )
        ]
    ]

    clavier = InlineKeyboardMarkup(bouton)

    await update.message.reply_text(
        "Bienvenue 👋\n\n"
        "Clique sur le bouton ci-dessous pour ouvrir l’application.",
        reply_markup=clavier,
    )


# =========================================================
# AFFICHER LE CHAT ID : /id
# =========================================================

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    if chat:
        await update.message.reply_text(
            f"Chat ID : `{chat.id}`",
            parse_mode="Markdown"
        )


# =========================================================
# CONFIGURATION DU BOT
# =========================================================

app = Application.builder().token(TOKEN).build()

# /start
app.add_handler(
    CommandHandler("start", start)
)

# /id
app.add_handler(
    CommandHandler("id", chat_id)
)


# =========================================================
# LANCEMENT
# =========================================================

if __name__ == "__main__":
    print("✅ Bot lancé")
    app.run_polling()
