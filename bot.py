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
    MessageHandler,
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
# CHAT ID : /id
# =========================================================

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Chat ID : `{update.effective_chat.id}`",
        parse_mode="Markdown"
    )


# =========================================================
# MESSAGE DU CANAL : /publier
# =========================================================

async def publier(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        chat_id=update.effective_chat.id,
        text=(
            "🍌 *BIENVENUE DANS NOTRE CANAL DE VENTE !* 🍌\n\n"
            "👋 *Bonjour et bienvenue à tous !*\n\n"
            "Vous êtes au bon endroit pour découvrir nos "
            "*meilleurs goûts* et passer votre commande "
            "directement depuis notre application Telegram. 🛒✨\n\n"
            "📱 *Envie de découvrir notre boutique ?*\n"
            "Appuyez simplement sur le bouton "
            "« 📱 Demander l’application » ci-dessous.\n\n"
            "🤖 Notre bot vous ouvrira ensuite une conversation "
            "privée et vous donnera accès à notre application "
            "directement dans Telegram. 🚀\n\n"
            "🛍️ *Dans la Mini-App, vous pourrez :*\n"
            "• 🍌 Découvrir nos différents goûts\n"
            "• 🔥 Trouver vos produits préférés\n"
            "• 📦 Consulter les produits disponibles\n"
            "• 🛒 Ajouter vos articles au panier\n"
            "• 💳 Passer votre commande facilement\n"
            "• ⚡ Profiter d’une expérience rapide et simple\n\n"
            "👇 *Alors, prêt à découvrir la boutique ?* 👇\n\n"
            "📱 *Appuie sur « Demander l’application » "
            "et lance ta commande !* 🍌🔥\n\n"
            "✨ *Bonne découverte à tous !* ✨"
        ),
        reply_markup=clavier,
        parse_mode="Markdown",
    )


# =========================================================
# CONFIGURATION DU BOT
# =========================================================

app = Application.builder().token(TOKEN).build()

# /start dans le chat privé
app.add_handler(
    CommandHandler("start", start)
)

# /id dans n'importe quel chat
app.add_handler(
    CommandHandler("id", chat_id)
)

# /publier dans le canal
app.add_handler(
    MessageHandler(
        filters.UpdateType.CHANNEL_POST & filters.COMMAND,
        publier
    )
)


# =========================================================
# LANCEMENT
# =========================================================

if __name__ == "__main__":
    print("✅ Bot lancé")
    app.run_polling()
