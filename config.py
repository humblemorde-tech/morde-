# =========================================
#        MORDE✈️ BOT CONFIGURATION
# =========================================

# Bot Information
BOT_NAME = "Morde✈️"
OWNER_NAME = "Mordecai"
OWNER_NUMBER = "254700000000"

# Command Prefix
PREFIX = "."

# =========================================
#               BOT SETTINGS
# =========================================

AUTO_READ_MESSAGES = True
AUTO_READ_STATUS = True
AUTO_TYPING = True
AUTO_RECORDING = False
AUTO_REACT = True

PUBLIC_MODE = True
WELCOME_MESSAGES = True
GOODBYE_MESSAGES = True

ANTI_LINK = True
ANTI_SPAM = True
ANTI_BAD_WORD = True
ANTI_DELETE = True
ANTI_BOT = True
ANTI_CALL = True

GROUP_PROTECTION = True
ANTI_VIEW_ONCE = False

# =========================================
#              AI SETTINGS
# =========================================

AI_CHAT = True
AI_PREFIX = ".ai"
GPT_MODE = True
SMART_REPLY = True

# =========================================
#             SECURITY SETTINGS
# =========================================

MAX_WARNINGS = 3
AUTO_BLOCK_SPAM = True
AUTO_BLOCK_CALLS = True
AUTO_BAN_LINKS = False

# =========================================
#              DOWNLOAD SETTINGS
# =========================================

ALLOW_YOUTUBE_DOWNLOAD = True
ALLOW_TIKTOK_DOWNLOAD = True
ALLOW_INSTAGRAM_DOWNLOAD = True

MAX_DOWNLOAD_SIZE_MB = 100

# =========================================
#               OWNER SETTINGS
# =========================================

OWNER_COMMANDS = [
    "restart",
    "shutdown",
    "broadcast",
    "block",
    "unblock",
    "setpp",
    "clearchats",
    "ban",
    "unban",
]

# =========================================
#             GROUP SETTINGS
# =========================================

GROUP_COMMANDS = [
    "tagall",
    "hidetag",
    "kick",
    "add",
    "promote",
    "demote",
    "mute",
    "unmute",
    "warn",
    "resetlink",
]

# =========================================
#              FUN COMMANDS
# =========================================

FUN_COMMANDS = [
    "joke",
    "meme",
    "quote",
    "truth",
    "dare",
    "ship",
    "hack",
    "compliment",
]

# =========================================
#             AI COMMANDS
# =========================================

AI_COMMANDS = [
    "ai",
    "gpt",
    "chat",
    "imagine",
    "generate",
]

# =========================================
#          SYSTEM INFORMATION
# =========================================

VERSION = "1.0.0"
BOT_STATUS = "Morde✈️ is Online ⚡"
LANGUAGE = "English"

# =========================================
#             MENU DESIGN
# =========================================

MENU_HEADER = """
╔════════════════════╗
      MORDE✈️ BOT
╚════════════════════╝
"""

MENU_FOOTER = """
╔════════════════════╗
   Powered By Morde✈️
╚════════════════════╝
"""

# =========================================
#             SESSION SETTINGS
# =========================================

SESSION_FOLDER = "sessions"
DATABASE_FOLDER = "database"
LOG_FOLDER = "logs"

# =========================================
#             API PLACEHOLDERS
# =========================================

OPENAI_API_KEY = "PUT_YOUR_OPENAI_KEY"
REMOVE_BG_API = "PUT_REMOVE_BG_KEY"
WEATHER_API = "PUT_WEATHER_KEY"

# =========================================
#             STARTUP MESSAGE
# =========================================

STARTUP_MESSAGE = f"""
╔════════════════════╗
      {BOT_NAME}
╚════════════════════╝

✅ Bot Successfully Started
⚡ Status: ONLINE
👑 Owner: {OWNER_NAME}
🌍 Mode: PUBLIC
🛡️ Security: ACTIVE
🤖 AI: ENABLED

Prefix: {PREFIX}

Morde✈️ Ready To Rule WhatsApp
"""
