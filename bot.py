```python
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
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("La variable TOKEN est absente de Render.")


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
        "Bienvenue sur ma boutique 👋\n\n"
        "Clique sur le bouton ci-dessous pour ouvrir l’application.",
        reply_markup=clavier,
    )


# =========================================================
# PUBLICATION DANS LE CANAL
# =========================================================

async def publier(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Cette fonction est déclenchée quand /publier est envoyé
    # dans le canal.

    bouton = [
        [
            InlineKeyboardButton(
                "📱 Demander l’application",
                url="https://t.me/vente_puff_bot?start=ouvrir_app",
            )
        ]
    ]

    clavier = InlineKeyboardMarkup(bouton)

    await context.bot.send_message(
        chat_id=update.channel_post.chat_id,
        text=(
            "🛍️ Bienvenue sur notre boutique !\n\n"
            "Pour accéder à notre application Telegram, "
            "appuie sur le bouton ci-dessous."
        ),
        reply_markup=clavier,
    )


# =========================================================
# CONFIGURATION DU BOT
# =========================================================

app = Application.builder().token(TOKEN).build()

# /start dans une conversation privée
app.add_handler(
    CommandHandler("start", start)
)

# /publier dans un canal
app.add_handler(
    MessageHandler(
        filters.UpdateType.CHANNEL_POST & filters.COMMAND,
        publier,
    )
)


# =========================================================
# LANCEMENT
# =========================================================

if __name__ == "__main__":
    print("✅ Bot lancé")
    app.run_polling()
```
