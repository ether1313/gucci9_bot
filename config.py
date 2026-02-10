import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8032459744:AAHflvcZpKeZhNrTBdM2Nqnv7cNV7g7BeFw")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/gucci9australiaa")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://gucci9au.net/RFGUCCI9BOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://gucci9au.net/RFGUCCI9BOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Gucci9 Promo Bot"
BOT_DESCRIPTION = "Gucci9 Marketing Assistant - Provides latest promotions and event information"
