=====================================================

Morde✈️ Ultimate WhatsApp Style Bot

main.py

Safe educational console version

=====================================================

import datetime import random import os import time

=====================================================

BOT DETAILS

=====================================================

BOT_NAME = "Morde✈️" OWNER_NAME = "Morde✈️" VERSION = "3.0" MODE = "PUBLIC" PREFIX = "."

=====================================================

STARTUP SCREEN

=====================================================

os.system("cls" if os.name == "nt" else "clear")

banner = f""" ███████╗███╗   ███╗ ██████╗ ██████╗ ██████╗ ███████╗ ██╔════╝████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔════╝ █████╗  ██╔████╔██║██║   ██║██████╔╝██║  ██║█████╗ ██╔══╝  ██║╚██╔╝██║██║   ██║██╔══██╗██║  ██║██╔══╝ ███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║██████╔╝███████╗ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝ """

print(banner) print("=" * 60) print(f" BOT NAME   : {BOT_NAME}") print(f" OWNER      : {OWNER_NAME}") print(f" VERSION    : {VERSION}") print(f" STATUS     : ONLINE ✅") print(f" MODE       : {MODE}") print(f" PREFIX     : {PREFIX}") print(f" STARTED AT : {datetime.datetime.now()}") print("=" * 60)

=====================================================

FUNCTIONS

=====================================================

def loading(): print("\nConnecting to Morde servers...") for i in range(3): print("Loading" + "." * (i + 1)) time.sleep(0.5)

def current_time(): return datetime.datetime.now().strftime("%H:%M:%S")

def current_date(): return datetime.date.today().strftime("%d/%m/%Y")

def ai_reply(question): replies = [ "AI thinks that is interesting 🤖", "Morde AI processed your request ⚡", "Prediction complete successfully 🔥", "AI response generated 🚀", "System intelligence activated 🧠", "Morde AI is always learning 💻" ] return random.choice(replies)

def quote(): quotes = [ "Never stop coding 💻", "Discipline creates success 🔥", "Small steps build big dreams 🚀", "Focus beats talent ⚡", "The future belongs to creators 👑" ] return random.choice(quotes)

loading()

=====================================================

MAIN LOOP

=====================================================

while True:

user = input(f"\n{PREFIX} Command : ").lower()

# =====================================================
# GENERAL MENU
# =====================================================

if user == "menu":
    print(f"""

================= {BOT_NAME} MAIN MENU =================

[ GENERAL ] hello hi alive ping runtime owner version date time quote joke status about repo

[ GROUP MENU ] grouplist tagall hidetag groupinfo welcome goodbye antilink antispam antibug warn warnings mute unmute kick ban promote demote admins

[ OWNER MENU ] restart shutdown broadcast setname setbio setprefix public private autoread autostatus backup clearsession ownerinfo

[ SETTINGS MENU ] settings changeprefix setmode setreply setwelcome setgoodbye setpp settheme setbotname

[ AI MENU ] ai chatgpt imagine code explain translate math summary story poem aiimage brain

[ FUN MENU ] truth dare fact meme love ship joke hack roast

[ SYSTEM MENU ] help speed uptime ram storage battery network

[ EXIT ] bye

======================================================== """)

# =====================================================
# GENERAL COMMANDS
# =====================================================

elif user == "hello":
    print(f"{BOT_NAME}: Hello commander 👋")

elif user == "hi":
    print(f"{BOT_NAME}: Hi there 🔥")

elif user == "alive":
    print(f"{BOT_NAME}: Yes, system online ✅")

elif user == "ping":
    print(f"{BOT_NAME}: Pong 🏓")

elif user == "runtime":
    print(f"{BOT_NAME}: Running perfectly 🚀")

elif user == "owner":
    print(f"{BOT_NAME}: My owner is {OWNER_NAME} 👑")

elif user == "version":
    print(f"{BOT_NAME}: Version {VERSION}")

elif user == "date":
    print(f"{BOT_NAME}: {current_date()} 📅")

elif user == "time":
    print(f"{BOT_NAME}: {current_time()} ⏰")

elif user == "quote":
    print(f"{BOT_NAME}: {quote()}")

elif user == "joke":
    jokes = [
        "Why do programmers hate bugs? 😂",
        "Python developers never sleep 🐍",
        "Error 404: Sleep not found 🤣"
    ]
    print(f"{BOT_NAME}: {random.choice(jokes)}")

elif user == "status":
    print(f"{BOT_NAME}: All systems operational ✅")

elif user == "about":
    print(f"{BOT_NAME}: Advanced multi-feature AI bot ⚡")

elif user == "repo":
    print(f"{BOT_NAME}: GitHub repo connected 🔗")

# =====================================================
# GROUP MENU
# =====================================================

elif user == "grouplist":
    print(f"{BOT_NAME}: Displaying joined groups 📜")

elif user == "tagall":
    print(f"{BOT_NAME}: @everyone 📢")

elif user == "hidetag":
    print(f"{BOT_NAME}: Hidden tag message sent 👀")

elif user == "groupinfo":
    print(f"{BOT_NAME}: Group Name : Morde Community")

elif user == "welcome":
    print(f"{BOT_NAME}: Welcome new member 🎉")

elif user == "goodbye":
    print(f"{BOT_NAME}: Goodbye member 👋")

elif user == "antilink":
    print(f"{BOT_NAME}: Anti-link protection enabled 🔒")

elif user == "antispam":
    print(f"{BOT_NAME}: Spam protection activated 🚫")

elif user == "antibug":
    print(f"{BOT_NAME}: Anti-bug security enabled 🛡️")
    print(f"{BOT_NAME}: Suspicious messages will be ignored safely.")

elif user == "warn":
    print(f"{BOT_NAME}: Warning issued ⚠️")

elif user == "warnings":
    print(f"{BOT_NAME}: User has 1 warning ⚠️")

elif user == "mute":
    print(f"{BOT_NAME}: Group muted 🔇")

elif user == "unmute":
    print(f"{BOT_NAME}: Group unmuted 🔊")

elif user == "kick":
    print(f"{BOT_NAME}: User removed 👢")

elif user == "ban":
    print(f"{BOT_NAME}: User banned 🚫")

elif user == "promote":
    print(f"{BOT_NAME}: User promoted to admin 👑")

elif user == "demote":
    print(f"{BOT_NAME}: Admin removed 📉")

elif user == "admins":
    print(f"{BOT_NAME}: Showing admin list 📋")

# =====================================================
# OWNER MENU
# =====================================================

elif user == "restart":
    print(f"{BOT_NAME}: Restarting systems 🔄")

elif user == "shutdown":
    print(f"{BOT_NAME}: Shutdown denied in demo mode ❌")

elif user == "broadcast":
    print(f"{BOT_NAME}: Broadcasting message 📡")

elif user == "setname":
    print(f"{BOT_NAME}: Bot name updated ✏️")

elif user == "setbio":
    print(f"{BOT_NAME}: Bio updated 📝")

elif user == "setprefix":
    print(f"{BOT_NAME}: Prefix changed ⚡")

elif user == "public":
    MODE = "PUBLIC"
    print(f"{BOT_NAME}: Public mode enabled 🌍")

elif user == "private":
    MODE = "PRIVATE"
    print(f"{BOT_NAME}: Private mode enabled 🔒")

elif user == "autoread":
    print(f"{BOT_NAME}: Auto-read activated 👀")

elif user == "autostatus":
    print(f"{BOT_NAME}: Auto-status view enabled 📱")

elif user == "backup":
    print(f"{BOT_NAME}: Backup created successfully 💾")

elif user == "clearsession":
    print(f"{BOT_NAME}: Old sessions cleared 🧹")

elif user == "ownerinfo":
    print(f"{BOT_NAME}: Owner : {OWNER_NAME} 👑")

# =====================================================
# SETTINGS MENU
# =====================================================

elif user == "settings":
    print(f"""

=========== SETTINGS ===========

Bot Name : {BOT_NAME} Owner    : {OWNER_NAME} Mode     : {MODE} Prefix   : {PREFIX} Version  : {VERSION}

================================ """)

elif user == "changeprefix":
    print(f"{BOT_NAME}: Prefix customization ready ⚡")

elif user == "setmode":
    print(f"{BOT_NAME}: Mode updated successfully 🔄")

elif user == "setreply":
    print(f"{BOT_NAME}: Auto reply configured 💬")

elif user == "setwelcome":
    print(f"{BOT_NAME}: Welcome message updated 🎉")

elif user == "setgoodbye":
    print(f"{BOT_NAME}: Goodbye message updated 👋")

elif user == "setpp":
    print(f"{BOT_NAME}: Profile picture updated 🖼️")
    print(f"{BOT_NAME}: Use dark futuristic or cyber-style art for best look ⚡")

elif user == "settheme":
    print(f"{BOT_NAME}: Theme changed 🎨")

elif user == "setbotname":
    print(f"{BOT_NAME}: Bot renamed successfully ✏️")

# =====================================================
# AI MENU
# =====================================================

elif user == "ai":
    print(f"{BOT_NAME}: AI mode activated 🤖")

elif user == "chatgpt":
    print(f"{BOT_NAME}: {ai_reply('chat')} ")

elif user == "imagine":
    print(f"{BOT_NAME}: AI image imagination ready 🎨")

elif user == "code":
    print(f"{BOT_NAME}: AI coding assistant enabled 💻")

elif user == "explain":
    print(f"{BOT_NAME}: AI explanation generated 📘")

elif user == "translate":
    print(f"{BOT_NAME}: Translation completed 🌐")

elif user == "math":
    print(f"{BOT_NAME}: Solving mathematics 🧮")

elif user == "summary":
    print(f"{BOT_NAME}: AI summary ready 📄")

elif user == "story":
    print(f"{BOT_NAME}: Once upon a time... 📖")

elif user == "poem":
    print(f"{BOT_NAME}: Roses are red, code is bright 🌹")

elif user == "aiimage":
    print(f"{BOT_NAME}: AI image generated 🖼️")

elif user == "brain":
    print(f"{BOT_NAME}: Neural systems active 🧠")

# =====================================================
# FUN MENU
# =====================================================

elif user == "truth":
    print(f"{BOT_NAME}: Truth question generated 🤫")

elif user == "dare":
    print(f"{BOT_NAME}: Dare challenge activated 😅")

elif user == "fact":
    print(f"{BOT_NAME}: Honey never spoils 🍯")

elif user == "meme":
    print(f"{BOT_NAME}: Meme mode activated 😂")

elif user == "love":
    print(f"{BOT_NAME}: Love percentage 99% ❤️")

elif user == "ship":
    print(f"{BOT_NAME}: Compatibility detected 💞")

elif user == "hack":
    print(f"{BOT_NAME}: Ethical security mode only 🛡️")

elif user == "roast":
    print(f"{BOT_NAME}: System roast loaded 🔥")

# =====================================================
# SYSTEM MENU
# =====================================================

elif user == "help":
    print(f"{BOT_NAME}: Type 'menu' to display all commands 📜")

elif user == "speed":
    print(f"{BOT_NAME}: Speed 0.01ms ⚡")

elif user == "uptime":
    print(f"{BOT_NAME}: Running smoothly for hours 🚀")

elif user == "ram":
    print(f"{BOT_NAME}: RAM usage normal 💾")

elif user == "storage":
    print(f"{BOT_NAME}: Storage healthy 📂")

elif user == "battery":
    print(f"{BOT_NAME}: Battery stable 🔋")

elif user == "network":
    print(f"{BOT_NAME}: Connection stable 🌐")

# =====================================================
# EXIT
# =====================================================

elif user == "bye":
    print(f"{BOT_NAME}: Goodbye commander ✈️")
    break

# =====================================================
# UNKNOWN COMMAND
# =====================================================

else:
    print(f"{BOT_NAME}: Unknown command ❌")
    print(f"{BOT_NAME}: Type 'menu' for all commands 📜")
