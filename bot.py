from flask import Flask
import threading
import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

TOKEN = os.environ.get("BOT_TOKEN")

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot ishlayapti!"
    
ADMIN_ID = 8704037612
CARD_NUMBER = "9860600412437037"
CARD_OWNER = "SABIROV URAL"
TOTAL_ORDERS = 0
TODAY_ORDERS = 0

CHANNEL_USERNAME = "@DaminikShop_uz"

ORDER_ID, ORDER_PRODUCT, ORDER_RECEIPT, BROADCAST = range(4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    member = await context.bot.get_chat_member(
        CHANNEL_USERNAME,
        update.effective_user.id
    )

    if member.status in ["left", "kicked"]:
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📢 Kanalga obuna bo'lish",
                    url="https://t.me/DaminikShop_uz"
                )
            ],
            [
                InlineKeyboardButton(
                    "✅ Tekshirish",
                    callback_data="check_subscription"
                )
            ]
        ])

        await update.message.reply_text(
            "🚫 Botdan to'liq foydalanish uchun avval kanalimizga obuna bo'ling.",
            reply_markup=keyboard
        )

        return

    user_id = update.effective_user.id

    if "users" not in context.bot_data:
        context.bot_data["users"] = set()

    context.bot_data["users"].add(user_id)

    keyboard = [
        ["💎 UC Narxlari"],
        ["⭐️ Prime"],
        ["🌟 Prime Plus"],
        ["🛒 Buyurtma"],
        ["📞 Admin"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_photo(
        photo="AgACAgIAAxkBAAIBv2oqUz5IRpOEwXO4eN_2UiYbVvnZAAK2F2sbvHtYScwW0ifW664yAQADAgADeQADOwQ",
        caption=
        "🔥 DAMINIK PUBG SHOP 🔥\n\n"
        "⚡️ Eng tezkor UC xizmati\n"
        "💎 Ishonchli savdo\n"
        "🛒 24/7 buyurtma qabul qilinadi\n\n"
        "💎 PUBG Mobile UC\n"
        "⭐️ Prime\n"
        "🌟 Prime Plus\n\n"
        "👇 Kerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    if text == "💎 UC Narxlari":
            await update.message.reply_photo(
        photo="AgACAgIAAxkBAAFMOtxqK-YqabLQSUJuUOmhI0UOiIXubQAChB1rG5z9YUkeeYNxkbdPWQEAAwIAA3kAAzwE",
        caption=
        "💎 PUBG MOBILE UC NARXLARI\n\n"
        "60 UC — 13 000 UZS\n"
        "120 UC — 26 000 UZS\n"
        "180 UC — 39 000 UZS\n"
        "240 UC — 52 000 UZS\n"
        "325 UC — 60 000 UZS\n"
        "385 UC — 73 000 UZS\n"
        "445 UC — 86 000 UZS\n"
        "505 UC — 100 000 UZS\n"
        "660 UC — 116 000 UZS\n"
        "720 UC — 130 000 UZS\n"
        "780 UC — 142 000 UZS\n"
        "840 UC — 155 000 UZS\n\n"
        "985 UC — 176 000 UZS\n"
        "1045 UC — 189 000 UZS\n"
        "1105 UC — 202 000 UZS\n"
        "1165 UC — 215 000 UZS\n"
        "1320 UC — 232 000 UZS\n"
        "1380 UC — 245 000 UZS\n"
        "1440 UC — 258 000 UZS\n"
        "1500 UC — 271 000 UZS\n"
        "1800 UC — 305 000 UZS\n\n"
        "2125 UC — 364 000 UZS\n"
        "2460 UC — 421 000 UZS\n"
        "2785 UC — 481 000 UZS\n"
        "3850 UC — 570 000 UZS\n"
        "4510 UC — 687 000 UZS\n"
        "4835 UC — 748 000 UZS\n"
        "5650 UC — 875 000 UZS\n"
        "8100 UC — 1 155 000 UZS\n\n"
        "📩 Admin: @SABIROV_uc_admin\n"
        "📞 +998 99 674 58 91"
    )

    elif text == "⭐️ Prime":
        await update.message.reply_photo(
        photo="AgACAgIAAxkBAAFMO1dqK-73-hwvgp3HQoYreXb3g0zJZgACPRxrG3raYUkHD6hqoJtEBgEAAwIAA3kAAzwE",
        caption=
        "⭐️ PRIME NARXLARI ⭐️\n\n"
        "1 oylik — 14 000 so'm\n"
        "3 oylik — 38 000 so'm\n"
        "6 oylik — 75 000 so'm\n"
        "1 yillik — 150 000 so'm\n\n"
        "📩 Admin: @SABIROV_uc_admin\n"
        "📞 Aloqa: +998 99 674 58 91"
    )

    elif text == "🌟 Prime Plus":
        await update.message.reply_photo(
        photo="AgACAgIAAxkBAAFMO3BqK--v5R0gZV_swG0yQQghTktKwQACRBxrG3raYUkzaYPq9mTG-QEAAwIAA3kAAzwE",
        caption=
        "🌟 PRIME PLUS NARXLARI 🌟\n\n"
        "1 oylik — 125 000 so'm\n"
        "3 oylik — 355 000 so'm\n"
        "6 oylik — 700 000 so'm\n"
        "1 yillik — 1 400 000 so'm\n\n"
        "📩 Admin: @SABIROV_uc_admin\n"
        "📞 Aloqa: +998 99 674 58 91"
    )

    elif text == "📞 Admin":
        await update.message.reply_text(
            "📩 Admin: @SABIROV_uc_admin\n"
            "📞 Aloqa: +998 99 674 58 91"
        )
        
    elif text == "📊 Statistika":
        if update.effective_user.id != ADMIN_ID:
            return

        await update.message.reply_text(
            "📊 STATISTIKA\n\n"
            f"📦 Jami buyurtmalar: {TOTAL_ORDERS} ta\n"
            f"📅 Bugungi buyurtmalar: {TODAY_ORDERS} ta"
        )
        
    elif text == "🏠 Asosiy menyu":
        keyboard = ReplyKeyboardMarkup(
            [
                ["💎 UC Narxlari"],
                ["⭐️ Prime"],
                ["🌟 Prime Plus"],
                ["🛒 Buyurtma"],
                ["📞 Admin"]
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "🏠 Asosiy menyuga qaytdingiz.",
            reply_markup=keyboard
        )
        
async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("approve_"):
        user_id = int(data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "🎉 Buyurtmangiz tasdiqlandi!\n\n"
                "⏳ Tez orada UC hisobingizga tushiriladi.\n"
                "📞 Savollar uchun: @SABIROV_uc_admin"
            )
        )

        await query.edit_message_caption(
            caption=query.message.caption + "\n\n✅ TASDIQLANDI"
        )

    elif data.startswith("cancel_"):
        user_id = int(data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text=(
                "❌ Buyurtmangiz bekor qilindi.\n\n"
                "📞 Batafsil ma'lumot uchun: @SABIROV_uc_admin"
            )
        )

        await query.edit_message_caption(
            caption=query.message.caption + "\n\n❌ BEKOR QILINDI"
        ) 
        
async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    member = await context.bot.get_chat_member(
        CHANNEL_USERNAME,
        query.from_user.id
    )

    print(member.status)

    if member.status not in ["member", "administrator", "creator"]:

        await query.message.reply_text(
            "❌ Siz hali kanalga obuna bo'lmagansiz."
        )

    else:
        await query.message.delete()

        user_id = query.from_user.id

        if "users" not in context.bot_data:
            context.bot_data["users"] = set()

        context.bot_data["users"].add(user_id)

        keyboard = ReplyKeyboardMarkup(
            [
                ["💎 UC Narxlari"],
                ["⭐️ Prime"],
                ["🌟 Prime Plus"],
                ["🛒 Buyurtma"],
                ["📞 Admin"]
            ],
            resize_keyboard=True
        )

        await context.bot.send_photo(
            chat_id=query.from_user.id,
            photo="AgACAgIAAxkBAAIBv2oqUz5IRpOEwXO4eN_2UiYbVvnZAAK2F2sbvHtYScwW0ifW664yAQADAgADeQADOwQ",
            caption=
            "🔥 DAMINIK PUBG SHOP 🔥\n\n"
            "⚡️ Eng tezkor UC xizmati\n"
            "💎 Ishonchli savdo\n"
            "🛒 24/7 buyurtma qabul qilinadi\n\n"
            "👇 Kerakli bo'limni tanlang:",
            reply_markup=keyboard
        )
          
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    keyboard = ReplyKeyboardMarkup(
        [
            ["📊 Statistika"],
            ["📢 Reklama"],
            ["🏠 Asosiy menyu"]
        ],
        resize_keyboard=True
    )
    await update.message.reply_text(
        "👑 ADMIN PANEL",
        reply_markup=keyboard
    )
        
async def start_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return ConversationHandler.END

    await update.message.reply_text(
        "📢 Yubormoqchi bo'lgan reklama xabaringizni kiriting:"
    )

    return BROADCAST
    
async def send_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return ConversationHandler.END

    success = 0

    for user_id in context.bot_data.get("users", set()):
        try:
            if update.message.photo:
                photo = update.message.photo[-1].file_id
                caption = update.message.caption

                await context.bot.send_photo(
                    chat_id=user_id,
                    photo=photo,
                    caption=caption
                )

            else:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=update.message.text
                )

            success += 1

        except:
            pass

    await update.message.reply_text(
        f"✅ Reklama {success} ta foydalanuvchiga yuborildi."
    )
   
    return ConversationHandler.END  
    
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    await update.message.reply_text(
        "📊 STATISTIKA\n\n"
        f"📦 Jami buyurtmalar: {TOTAL_ORDERS} ta\n"
        f"📅 Bugungi buyurtmalar: {TODAY_ORDERS} ta"
    )
    
    def run_web():
    app_web.run(host="0.0.0.0", port=10000)
    
def main():
    threading.Thread(target=run_web).start()
    
    app = Application.builder().token(TOKEN).build()
     
    conv_handler = ConversationHandler(
            allow_reentry=True,
            entry_points=[
                  MessageHandler(
                            filters.Regex("^🛒 Buyurtma$"),
                start_order
                   ),

                   MessageHandler(
                             filters.Regex("^📢 Reklama$"),
                start_broadcast
                   )
        ],
    
    states={
        ORDER_ID: [
            MessageHandler(
    filters.TEXT & ~filters.COMMAND & ~filters.Regex("^🛒 Buyurtma$"),
    get_pubg_id
            )
        ],

        ORDER_PRODUCT: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_product
            )
        ],

        ORDER_RECEIPT: [
    MessageHandler(
        (filters.PHOTO) |
        (filters.TEXT & filters.Regex("^(✅ Tasdiqlash|❌ Bekor qilish)$")),
        get_receipt
    )
],
        
        BROADCAST: [
    MessageHandler(
        (filters.TEXT | filters.PHOTO) & ~filters.COMMAND,
        send_broadcast
    )
],
    },

    fallbacks=[],
)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("admin", admin_panel))

    app.add_handler(conv_handler)

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("Bot ishga tushdi...")

    app.add_handler(
        CallbackQueryHandler(
            check_subscription,
            pattern="^check_subscription$"
        )
    )

    app.add_handler(
        CallbackQueryHandler(
            admin_buttons,
            pattern="^(approve_|cancel_)"
        )
    )

    app.run_polling(
    drop_pending_updates=True
)

async def start_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "🎮 PUBG ID raqamingizni yuboring:"
    )
    return ORDER_ID

async def get_pubg_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in [
        "📞 Admin",
        "💎 UC Narxlari",
        "⭐️ Prime",
        "🌟 Prime Plus",
        "🛒 Buyurtma",
    ]:
        await handle_message(update, context)
        return ORDER_ID

    context.user_data["pubg_id"] = text

    await update.message.reply_text(
        "📦 Buyurtma qilmoqchi bo'lgan mahsulotni kiriting.\n\n"
        "Masalan:\n"
        "325 UC\n"
        "Prime 1 oy"
    )

    return ORDER_PRODUCT

async def get_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "❌ Bekor qilish":
        context.user_data.clear()

        keyboard = ReplyKeyboardMarkup(
            [
                ["💎 UC Narxlari"],
                ["⭐️ Prime"],
                ["🌟 Prime Plus"],
                ["🛒 Buyurtma"],
                ["📞 Admin"]
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "❌ Buyurtma bekor qilindi.",
            reply_markup=keyboard
        )

        return ConversationHandler.END

    if text in [
        "📞 Admin",
        "💎 UC Narxlari",
        "⭐️ Prime",
        "🌟 Prime Plus",
        "🛒 Buyurtma",
    ]:
        await handle_message(update, context)
        return ORDER_PRODUCT

    context.user_data["product"] = text

    keyboard = ReplyKeyboardMarkup(
        [["✅ Tasdiqlash", "❌ Bekor qilish"]],
        resize_keyboard=True
    )

    await update.message.reply_text(
        f"📋 Buyurtma ma'lumotlari:\n\n"
        f"🎮 PUBG ID: {context.user_data['pubg_id']}\n"
        f"📦 Mahsulot: {text}\n\n"
        f"Buyurtmani tasdiqlaysizmi?",
        reply_markup=keyboard
    )

    return ORDER_RECEIPT

async def get_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text if update.message.text else ""

    if text == "❌ Bekor qilish":
        context.user_data.clear()

        keyboard = ReplyKeyboardMarkup(
            [
                ["💎 UC Narxlari"],
                ["⭐️ Prime"],
                ["🌟 Prime Plus"],
                ["🛒 Buyurtma"],
                ["📞 Admin"]
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "❌ Buyurtma bekor qilindi.",
            reply_markup=keyboard
        )

        return ConversationHandler.END

    if text == "✅ Tasdiqlash":
        keyboard = ReplyKeyboardMarkup(
            [
                ["💎 UC Narxlari"],
                ["⭐️ Prime"],
                ["🌟 Prime Plus"],
                ["🛒 Buyurtma"],
                ["📞 Admin"]
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "💳 To'lov rekvizitlari:\n\n"
            f"💳 Karta: {CARD_NUMBER}\n"
            f"👤 Egasi: {CARD_OWNER}\n\n"
            "📸 To'lov qilgandan so'ng chek rasmini yuboring.",
            reply_markup=keyboard
        )

        return ORDER_RECEIPT

    photo = update.message.photo[-1].file_id

    user = update.effective_user

    caption = (
        "🛒 YANGI BUYURTMA\n\n"
        f"👤 Ism: {user.first_name}\n"
        f"🔗 Username: @{user.username if user.username else 'Mavjud emas'}\n"
        f"🆔 Telegram ID: {user.id}\n"
        f"🎮 PUBG ID: {context.user_data['pubg_id']}\n"
        f"📦 Mahsulot: {context.user_data['product']}\n\n"
        "📞 Admin: @SABIROV_uc_admin"
    )
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ Tasdiqlash",
                
callback_data=f"approve_{user.id}"
            ),
            InlineKeyboardButton(
                "❌ Bekor qilish",  
                callback_data=f"cancel_{user.id}"
            )
        ]
    ])
    
    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=caption,
        reply_markup=keyboard
    )

    global TOTAL_ORDERS, TODAY_ORDERS

    TOTAL_ORDERS += 1
    TODAY_ORDERS += 1

    await update.message.reply_text(
        "✅ Buyurtmangiz qabul qilindi.\n"
        "Admin tez orada siz bilan bog'lanadi.\n\n"
        "📞 Admin: @SABIROV_uc_admin"
    )

    context.user_data.clear()

    return ConversationHandler.END
    
if __name__ == "__main__":
    main()
