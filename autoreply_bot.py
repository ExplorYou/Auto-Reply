from telethon.sync import TelegramClient, events
import asyncio
import re

# Bhai, yeh tera VIP ticket – apne details daal, warna entry nahi! 😏
api_id = 'YOUR_API_ID_HERE'  # Yeh nahi toh bhai ka swag adhoora hai! 😎
api_hash = 'YOUR_API_HASH_HERE'  # Secret code, chhupa ke rakhna, bhai! 🌶️
phone = 'YOUR_PHONE_NUMBER_HERE'  # +91 wala number daal, nahi toh bhool ja maza! 📱

# Telegram ka darwaza kholte hain – bhai ka bot shuru! 🚪
client = TelegramClient('session_name', api_id, api_hash)

# Replies with full swag – HTML mein bold, italic, aur emoji! 😍
hindi_reply = "<b>Bhai/Bahen</b> 😍<br><i>Yahan Aapko Saari Movies, Web Series Aur Anime Mil Jayengi!</i><br><b>Direct File Format:</b> @ChanelUsername (Mkv, Mp4, Avi, Mov, Wmv, Aur Bhi)<br><b>Terabox Link:</b> @ChanelUsername (Sirf Link, Turant Milega)"
english_reply = "<b>Brother/Sister</b> 😍<br><i>You’ll Find All Movies, Web Series, And Anime Right Here!</i><br><b>Direct File Format:</b> @ChanelUsername (Mkv, Mp4, Avi, Mov, Wmv, And More)<br><b>Terabox Link:</b> @ChanelUsername (Just The Link, Delivered Instantly)"

# Target link – yahan apni link daal do, bhai log! 🎯
target_link = "Group Link Here"  # Apna target daal, jahan se shuru karna hai!

# Ignore list – inko chhod do, yeh spammer ya bot hain! 🚫
ignored_users = ["ignored_users", "ignored_bot", "ignored_users"]  # Bots ya nakli log yahan daal do!

# Chat aur message ID nikalne ka filmy style function! 🕵️‍♂️
def get_chat_and_message_id_from_link(link):
    print(f"Bhai, {link} se chat aur ID nikal raha hoon – ekdum detective mode!")
    match = re.search(r't.me/([^/]+)/(\d+)', link)
    if match:
        chat = match.group(1)  # Group ka naam ya ID
        message_id = int(match.group(2))  # Message ka number
        print(f"Chat: {chat}, Message ID: {message_id} – mil gaya, bhai!")
        return chat, message_id
    print("Arre, link mein kuch gadbad hai, bhai! Dobara check kar!")
    return None, None

# Global variables – bhai ka game plan! 🌟
target_chat, target_message_id = get_chat_and_message_id_from_link(target_link)
running = True

# Target message pe reply – shaan se shuru karo! 🔥
async def reply_to_target_message():
    if target_chat and target_message_id:
        try:
            await client.send_message(
                target_chat,
                f"{hindi_reply}\n\n{english_reply}",
                reply_to=target_message_id,
                parse_mode='html'
            )
            print(f"Target message ID: {target_message_id} pe reply daal diya – bhai ka swag dikh gaya!")
        except Exception as e:
            print(f"Target pe reply mein gadbad – {e}! Thodi thandi lete hain!")

# Target ke baad wale messages pe reply – ekdum auto dhamaka! 💪
async def reply_to_messages_after_target():
    if target_chat and target_message_id:
        try:
            print(f"Bhai, {target_chat} mein target ke baad ka tamasha shuru!")
            async for message in client.iter_messages(target_chat, min_id=target_message_id):
                sender = await message.get_sender()
                sender_username = sender.username if sender and hasattr(sender, 'username') else None
                if sender_username in ignored_users or (sender and hasattr(sender, 'bot') and sender.bot):
                    print(f"{sender_username or 'ek bot'} (ID: {message.id}) ko ignore kiya – spammer ko chhodo!")
                    continue
                await message.reply(f"{hindi_reply}\n\n{english_reply}", parse_mode='html')
                print(f"Message ID: {message.id} pe reply daal diya – ekdum mast!")
                await asyncio.sleep(1)  # Rate limit se bacho, bhai!
        except Exception as e:
            print(f"Messages reply mein problem – {e}! Thodi der thandi!")

# Naye messages pe reply – live action, bhai log! 🎬
@client.on(events.NewMessage(chats=target_chat))
async def handler(event):
    global running
    if not running:
        print("Bhai, ruk gaya hoon – koi kaam nahi!")
        return
    
    sender = await event.get_sender()
    if sender and (hasattr(sender, 'username') and sender.username in ignored_users) or (hasattr(sender, 'bot') and sender.bot):
        print(f"Naya message {event.message.id} ignore kiya – {sender.username or 'bot'} se aaya tha!")
        return
    
    await event.reply(f"{hindi_reply}\n\n{english_reply}", parse_mode='html')
    print(f"Naye message ID: {event.message.id} pe reply daal diya – bhai ka jadoo chal gaya!")

# Main tamasha shuru – bhai ka bot ka time! 🎉
async def main():
    await client.start(phone)
    print(f"Bhai ka bot shuru – {target_chat} pe nazar rakhega! Link: {target_link} 🔥")
    
    # Target pe pehla dhamaka
    await reply_to_target_message()
    # Target ke baad ka hungama
    await reply_to_messages_after_target()
    
    # Live action ke liye wait – @sup_toon_1 ka swag!
    print("Ab naye messages ka intezaar – bhai ka bot hamesha taiyar!")
    while running:
        await asyncio.sleep(1)

# Script ko dance floor pe bhejo! 💃🕺
with client:
    print("Bhai ka AutoReply Bot shuru – @sup_toon_1 ki shaan! Ctrl+C se rok sakte ho! 😎")
    try:
        client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Arre bhai, tune rok diya? Thik hai, @sup_toon_1 pe milte hain! 🔥")
