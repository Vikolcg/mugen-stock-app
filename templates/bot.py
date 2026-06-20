import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Charger les variables d'environnement
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
FLASK_URL = os.getenv('FLASK_URL')

# Commandes du bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛒 Bienvenue dans Mugen Stock Bot!\n\n"
        "Commandes disponibles:\n"
        "/voir - Voir le stock\n"
        "/help - Aide"
    )

async def voir_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(f"{FLASK_URL}/")
        await update.message.reply_text("📊 Stock disponible sur l'app web!")
    except Exception as e:
        await update.message.reply_text(f"❌ Erreur: {e}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commandes:\n"
        "/voir - Affiche le stock"
    )

# Lancer le bot
def main():
    print("🤖 Bot en cours de démarrage...")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Ajouter les commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("voir", voir_stock))
    app.add_handler(CommandHandler("help", help_command))
    
    print("✅ Bot lancé et prêt !")
    # Lancer
    app.run_polling()

if __name__ == "__main__":
    main()