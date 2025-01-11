import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gates import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
import telebot
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


import threading
import time
from telebot import types

stopuser = {}
token = "7923595557:AAHtTNKWDqGFFsjCUq3XHV2IGaxnSBUn-gY"
bot=telebot.TeleBot(token,parse_mode="HTML")


admin=5983253591

myid = ['5983253591']

admins = ['5983253591']


content = [
    "┏━━━━━━━━━━━━━━━━━⍟			\n┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 -> ⚆\n┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲  🎉🎉🎉🎉🎉🎉 \n┃⚆ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗝𝗼𝗶𝗻 @aaka8h\n┃⌧ 𝗗𝗘𝗩 @aaka8h 『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』 🇲🇲  \n┗━━━━━━━━/━━━━━━━━⍟",
    "• Bot Subscription Prices - Bot Prices •\n⬅️ Combo CC Checker Bot 🛒👑\n- (4 Gates, 4 Gates) ⭐️\n- (Manual Check, Combo Check) ⭐️\n1- One Day •💷Day -> 3 ⚡️\n1- Week •💷 Week -> 10 ⚡️\n1- Half Month •💷Half Month -> 20 ⚡️\n1- Month •💷Month -> 25 ⚡️\n• We accept all types of international payment ✅\n• We Accept All Payment Methods in World ✅\n• (💴💷🌐👛💀..........🌎🌎)\n• For Subscribe & Inquiry - For Communication and Inquiry •  🛩 🖱👼@aaka8h👼&👼 @aaka8h 👼",
    "Admin Command\n COMBO /set_limit\n\nOFF GATE /offb1 ON GATE /onb1\nOFF GATE /offb2 ON GATE /onb2\nOFF GATE /offb3 ON GATE /onb3\nOFF GATE /offb4 ON GATE /onb4\nOFF GATE /offch1 ON GATE /onch1\nAdmin CMDS /menu",
    "- Welcome My Boss ♡\n- Start Check Bot ¦ /start\n- Add New Subscriber ¦ /add + ID\n- Total Bot Users ¦ /tot\n- Send Msg Forr All ¦ /sendall + msg\n- Delete A Subsc ¦ /dele + ID\n- Show Sub's ID's ¦ /sh\n- Stop And Start The Gate's /gate\n------------------------------------\n• Programmer ¦ @aaka8h\n• Channel ¦ @aaka8h",
    "┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1\n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /chk 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃     \n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅                   \n┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿\n┗━━━━━━━━/━━━━━━━━⍟\n┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛\n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /cc 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃\n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅\n┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿\n┗━━━━━━━━/━━━━━━━━⍟\n┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 3\n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /sx 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃\n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅\n┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿\n┗━━━━━━━━/━━━━━━━━⍟\n┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4\n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /sa 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃\n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅\n┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿\n┗━━━━━━━━/━━━━━━━━⍟\n┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 \n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /ba 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃\n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅\n┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿\n┗━━━━━━━━/━━━━━━━━⍟\n┏━━━━━━━━━━━━━━━━━⍟\n┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 𝗟𝗼𝗼𝗸𝘂𝗽\n┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /bin 𝗕𝗜𝗡\n┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅\n┃⌧ 𝗧𝘆𝗽𝗲: 𝗙𝗿𝗲𝗲 𝗙𝗼𝗿 𝗔𝗹𝗹 ✅\n┗━━━━━━━━/━━━━━━━━⍟\n⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /prices \n⚆ 𝗠𝗮𝘀𝘀 𝗖𝗖 𝗖𝗼𝗺𝗯𝗼.𝘁𝘅𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗕𝗼𝘁\n⌧ 𝗪𝗲 𝘄𝗶𝗹𝗹 𝗮𝗱𝗱𝗶𝗻𝗴 𝗠𝗼𝗿𝗲 𝗚𝗮𝘁𝗲𝘀...."  # New page added
]

# Create a dictionary to track the current page for each user
user_pages = {}

def generate_keyboard(page_number):
    """Create navigation buttons with 'Next', 'Back', 'Menu', 'Owner', and 'New Page'."""
    markup = InlineKeyboardMarkup(row_width=3)  # Set row width for buttons

    # Create the buttons
    back_button = InlineKeyboardButton("𝗡𝗘𝗫𝗧", callback_data="back")
    next_button = InlineKeyboardButton("𝗧𝗢𝗢𝗟", callback_data="next")
    menu_button = InlineKeyboardButton("𝗠𝗘𝗡𝗨", callback_data="menu")
    if page_number < len(content) - 1: # The last page before the new page (Page 4)
        new_page_button = InlineKeyboardButton("𝗖𝗛𝗘𝗖𝗞 𝗖𝗠𝗗𝗦", callback_data="new_page")
        markup.add(new_page_button)
    
    # Add the "Owner" button if not on the last page
    if page_number < len(content) - 1:
        owner_button = InlineKeyboardButton("𝗕𝗢𝗧 𝗣𝗥𝗜𝗖𝗘 ", callback_data="Owner")
        markup.add(owner_button)

    # Add the "New Page" button if not on the last page
    

    # Add buttons based on the current page
    if page_number == 0:
        # First page: no 'Back' button, just 'Next' and 'Menu'
        markup.add(next_button, menu_button)
    elif page_number == len(content) - 1:
        # Last page: no 'Next' button, just 'Back' and 'Menu'
        markup.add(back_button, menu_button)
    else:
        # Middle pages: show 'Back', 'Next', and 'Menu' side by side
        markup.add(back_button, next_button, menu_button)

    return markup

@bot.message_handler(commands=['info'])
def start_message(message):
    """Handle the /start command to initialize pagination."""
    chat_id = message.chat.id
    user_pages[chat_id] = 0  # Set the initial page to 0
    bot.send_message(chat_id, content[0], reply_markup=generate_keyboard(0))

@bot.callback_query_handler(func=lambda call: call.data in ['next', 'back', 'menu', 'Owner', 'new_page'])
def handle_pagination(call):
    """Handle button clicks for pagination, menu, owner, and new page."""
    chat_id = call.message.chat.id
    current_page = user_pages.get(chat_id, 0)

    # Determine the next page based on button clicked
    if call.data == 'next' and current_page < len(content) - 1:
        current_page += 1
    elif call.data == 'back' and current_page > 0:
        current_page -= 1
    elif call.data == 'menu':
        # Reset the user back to the main menu
        bot.edit_message_text("You are back at the menu. Choose a page to navigate:", chat_id, call.message.message_id)
        bot.send_message(chat_id, content[0], reply_markup=generate_keyboard(0))
        return
    elif call.data == 'Owner':
        # Respond to the "Owner" button click
        bot.answer_callback_query(call.id, "You clicked the Owner button!")
        bot.send_message(chat_id, "• Bot Subscription Prices - Bot Prices •\n⬅️ Combo CC Checker Bot 🛒👑\n- (4 Gates, 4 Gates) ⭐️\n- (Manual Check, Combo Check) ⭐️\n1- One Day •💷Day -> 3 ⚡️\n1- Week •💷 Week -> 10 ⚡️\n1- Half Month •💷Half Month -> 20 ⚡️\n1- Month •💷Month -> 25 ⚡️\n• We Accept All Payment Methods in USDT BTX BTC TRC EHT BNB ✅\n• (💴💷🌐👛💀..........🌎🌎)\n• For Subscribe & Inquiry - For Communication and Inquiry •  🛩 🖱👼@aaka8h👼&👼 @aaka8h 👼\nBot Buy @aaka8h \n\n\nChannel 2 https://t.me/+cTzbkXe7FLwwY2Jk \nCHECK CMDS /info")
        return  # Skip editing message if Owner button is clicked
    elif call.data == 'new_page':
        # Handle the new page button click
        current_page = len(content) - 1  # Go to the last page (new page)
    
    # Check if the content is the same before editing
    new_content = content[current_page]
    new_markup = generate_keyboard(current_page)

    if call.message.text != new_content or call.message.reply_markup != new_markup:
        # Edit the message with the new content and update the buttons
        bot.edit_message_text(new_content, chat_id, call.message.message_id, reply_markup=new_markup)

    # Update the current page number
    user_pages[chat_id] = current_page










command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == 'Free - Not Subscribed':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 - CN", url="https://t.me/aaka8h")
			keyboard.add(contact_button)
			random_number = random.randint(2, 7)
			photo_url = f'https://t.me/phtors/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''
┏━━━━━━━━━━━━━━━━━⍟			
┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 -> {name} ⚆
┃⚆ 𝗬𝗼𝘂𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗶𝗻 𝗖𝗵𝗲𝗰𝗸 
┃⚆ 𝗪𝗼𝗿𝗹𝗱 𝗕𝗼𝘁 ⚠️ ⚠️ 🚫
┃⚆ 𝗖𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗦𝗲𝗻𝗱 ! /info
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /info
┃⌧ 𝗗𝗘𝗩 <a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>  
┗━━━━━━━━/━━━━━━━━⍟''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="⚆ Our Channel ⚆", url="https://t.me/+cTzbkXe7FLwwY2Jk")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(2, 7)
		photo_url = f'https://t.me/phtors/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<strong>
┏━━━━━━━━━━━━━━━━━⍟		
┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 -> {name}
┃⚆ 𝗬𝗼𝘂𝗿 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗶𝘀 𝗔𝗰𝘁𝗶𝘃𝗲 ✅
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗖𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗦𝗲𝗻𝗱 ! /info
┃⌧ 𝗧𝗵𝗲 𝗖𝗼𝗺𝗯𝗼 𝗖𝗖 𝗙𝗶𝗹𝗲 𝗦𝗲𝗻𝗱 
┃━━━━━━━━/━━━━━━━⍟
┃⌧ 𝗗𝗘𝗩 <a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>  
┗━━━━━━━━/━━━━━━━━⍟</strong>''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='Free - Not Subscribed'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"⚆ {BL} ⚆",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text='''
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /chk 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃     
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅                   
┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿
┗━━━━━━━━/━━━━━━━━⍟
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 1
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /cc 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅
┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿
┗━━━━━━━━/━━━━━━━━⍟
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 2
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /sx 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅
┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿
┗━━━━━━━━/━━━━━━━━⍟
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /sa 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅
┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿
┗━━━━━━━━/━━━━━━━━⍟
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 3
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /ba 𝗰𝗮𝗿𝗱|𝗺𝗼𝗻𝘁𝗵|𝘆𝗲𝗮𝗿|𝗰𝘃𝘃
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅
┃⌧ 𝗧𝘆𝗽𝗲: 𝗢𝗻𝗹𝘆-𝗩𝗶𝗽-𝗨𝘀𝗲𝗿
┗━━━━━━━━/━━━━━━━━⍟
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗡𝗮𝗺𝗲: 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 𝗟𝗼𝗼𝗸𝘂𝗽
┃⌧ 𝗙𝗼𝗿𝗺𝗮𝘁: /bin 𝗕𝗜𝗡
┃⚆ 𝗖𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻: 𝗢𝗡! ✅
┃⌧ 𝗧𝘆𝗽𝗲: 𝗙𝗿𝗲𝗲 𝗙𝗼𝗿 𝗔𝗹𝗹 ✅
┗━━━━━━━━/━━━━━━━━⍟
⚆ 𝗠𝗮𝘀𝘀 𝗖𝗖 𝗖𝗼𝗺𝗯𝗼.𝘁𝘅𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗕𝗼𝘁
⌧ 𝗪𝗲 𝘄𝗶𝗹𝗹 𝗮𝗱𝗱𝗶𝗻𝗴 𝗠𝗼𝗿𝗲 𝗚𝗮𝘁𝗲𝘀....
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
		if BL == 'Free - Not Subscribed':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 - CN", url="https://t.me/aaka8h")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 -> {name} ⚆
┃⚆ 𝗬𝗼𝘂𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗶𝗻 𝗖𝗵𝗲𝗰𝗸 𝗪𝗼𝗿𝗹𝗱 𝗕𝗼𝘁 ⚠️
┃⚆ 𝗖𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗦𝗲𝗻𝗱 ! /info
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /prices
┃⌧ 𝗗𝗘𝗩 <a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>  
┗━━━━━━━━/━━━━━━━━⍟''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 - CN", url="https://t.me/aaka8h")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''
┏━━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 -> {name} ⚆
┃⚆ 𝗬𝗼𝘂𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗶𝗻 𝗖𝗵𝗲𝗰𝗸 𝗪𝗼𝗿𝗹𝗱 𝗕𝗼𝘁 ⚠️
┃⚆ 𝗖𝗵𝗲𝗰𝗸 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗦𝗲𝗻𝗱 ! /info
┃━━━━━━━━/━━━━━━━━⍟
┃⌧ 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄 𝗕𝗼𝘁 𝗣𝗿𝗶𝗰𝗲𝘀 𝗦𝗲𝗻𝗱 ! /prices
┃⌧ 𝗗𝗘𝗩 <a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>  
┗━━━━━━━━/━━━━━━━━⍟''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 - CN", url="https://t.me/aaka8h")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text='''<b>⚆ 𝗬𝗼𝘂𝗿 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻 𝗵𝗮𝘀 𝗘𝘅𝗽𝗶𝗿𝗲𝗱 •</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = 'Free - Not Subscribed'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"⚆ 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 ⚆",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"⚆ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ⚆️",callback_data='br2')
		b3 = types.InlineKeyboardButton(text=f"⚆ 𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛     ⚆️",callback_data='br3')
		sa = types.InlineKeyboardButton(text=f"⚆ 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 ⚆️",callback_data='br4')
		keyboard.add(contact_button)
		keyboard.add(sw)
		keyboard.add(b3)
		keyboard.add(sa)
		bot.reply_to(message, text=f'⚆ 𝗖𝗵𝗼𝘀𝗲 𝗧𝗵𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝘁𝗼 𝘂𝘀𝗲 𝗳𝗿𝗼𝗺 𝗕𝗲𝗹𝗹𝗼𝘄 ',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
			
			
			
			

	
	
	
	
def dato(zh):
 
 

 
 
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''<a href='t.me/aaka8h'>-</a> 𝐈𝐧𝐟𝐨: <code>{brand} - {card_type} - {level}</code>
<a href='t.me/aaka8h'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank} </code>
<a href='t.me/aaka8h'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country_name} [ {country_flag} ]</code>'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'
	
	





import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  


check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True

check_enabled_ch1 = True






@bot.message_handler(commands=['onb1'])
def enable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['offb1'])
def disable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.  🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')








@bot.message_handler(commands=['onb2'])
def enable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 2 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['offb2'])
def disable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 2 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.  🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')





@bot.message_handler(commands=['onb3'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 3 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['offb3'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 3 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.  🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')
        
        
        

        
        
@bot.message_handler(commands=['onb4'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')
@bot.message_handler(commands=['offb4'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.  🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')
        
        
        
        
        
@bot.message_handler(commands=['onch1'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')
@bot.message_handler(commands=['offch1'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱.  🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')
        
        
        
        
        





from telebot import types


check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True
check_enabled_ch1 = True

MAX_LINES = 1000

@bot.message_handler(commands=['gate'])
def show_menu(message):
    if str(message.from_user.id) in admins:
        markup = types.InlineKeyboardMarkup(row_width=1)
        toggle_br1 = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        toggle_br2 = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        toggle_br3 = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        toggle_br4 = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        toggle_ch1 = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        
        br1_button = types.InlineKeyboardButton(f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 ({toggle_br1})", callback_data='toggle_br1')
        br2_button = types.InlineKeyboardButton(f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ({toggle_br2})", callback_data='toggle_br2')
        br3_button = types.InlineKeyboardButton(f"𝗦𝗧𝗥𝗜𝗣𝗘    𝗔𝗨𝗧𝗛 ({toggle_br3})", callback_data='toggle_br3')
        br4_button = types.InlineKeyboardButton(f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 ({toggle_br4})", callback_data='toggle_br4')
        ch1_button = types.InlineKeyboardButton(f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ({toggle_ch1})", callback_data='toggle_ch1')
        limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
        
        markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿 🤍')

@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_') or call.data == 'set_limits')
def handle_toggle(call):
    global check_enabled_br1, check_enabled_br2, check_enabled_br3, check_enabled_br4, check_enabled_ch1, MAX_LINES
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == 'toggle_br1':
        check_enabled_br1 = not check_enabled_br1
        status = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 is now {status}.")
    elif call.data == 'toggle_br2':
        check_enabled_br2 = not check_enabled_br2
        status = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        bot.answer_callback_query(call.id, f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 is now {status}.")
    elif call.data == 'toggle_br3':
        check_enabled_br3 = not check_enabled_br3
        status = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        bot.answer_callback_query(call.id, f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 is now {status}.")
    elif call.data == 'toggle_br4':
        check_enabled_br4 = not check_enabled_br4
        status = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        bot.answer_callback_query(call.id, f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 is now {status}.")
    elif call.data == 'toggle_ch1':
        check_enabled_ch1 = not check_enabled_ch1
        status = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 is now {status}.")
    elif call.data == 'set_limits':
        # إرسال رسالة للمستخدم لإدخال قيمة جديدة لـ MAX_LINES
        bot.send_message(chat_id, "Please enter the new limit value for Gate limits as /set_limit 1000")

    # تحديث الرسالة لعرض الحالة الجديدة
    markup = types.InlineKeyboardMarkup(row_width=1)
    br1_button = types.InlineKeyboardButton(f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1 ({'Enable✅' if check_enabled_br1 else 'Disable❌'})", callback_data='toggle_br1')
    br2_button = types.InlineKeyboardButton(f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ({'Enable✅' if check_enabled_br2 else 'Disable❌'})", callback_data='toggle_br2')
    br3_button = types.InlineKeyboardButton(f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ({'Enable✅' if check_enabled_br3 else 'Disable❌'})", callback_data='toggle_br3')
    br4_button = types.InlineKeyboardButton(f"𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4 ({'Enable✅' if check_enabled_br4 else 'Disable❌'})", callback_data='toggle_br4')
    ch1_button = types.InlineKeyboardButton(f"𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 ({'Enable✅' if check_enabled_ch1 else 'Disable❌'})", callback_data='toggle_ch1')
    limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
    markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    global MAX_LINES
    try:
        # Extract the new limit value from the command
        if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            new_limit = int(message.text.split()[1])
            MAX_LINES = new_limit
            bot.reply_to(message, f"Gate limit has been set to {MAX_LINES}.")
            
       
            show_menu(message)
        else:
            bot.reply_to(message, "Please use the correct format: /set_limit 1000.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        print(f"Error: {e}")











import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  
check_enabled = True 

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = False
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱. 🔒 𝗡𝗼 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸 𝘂𝗻𝘁𝗶𝗹 𝗶𝘁 𝗶𝘀 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = True
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅ 𝗨𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗻𝗼𝘄 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br1:  
        bot.send_message(chat_id=call.message.chat.id, text="𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ❌.")
        return

   
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="🔍 𝗬𝗼𝘂 𝗔𝗿𝗲 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗔 𝗖𝗼𝗺𝗯𝗼. 🔄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗨𝗻𝘁𝗶𝗹 𝗜𝘁 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝘀 𝗢𝗿 𝗦𝘁𝗼𝗽 𝗜𝘁 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆."
        )
        return  

    def my_function():
        user_name = call.from_user.first_name if call.from_user.first_name else "User"
        user_username = call.from_user.username if call.from_user.username else "unknown"
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("⚆ [ 𝗖𝗔𝗥𝗗 ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"⚆ 𝗦𝘁𝗮𝘁𝘂𝘀 & 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("⚆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        ccn = types.InlineKeyboardButton("⚆ 𝗖𝗩𝗩 & 𝗖𝗖𝗡 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm4 = types.InlineKeyboardButton("⚆ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm5 = types.InlineKeyboardButton("⚆ 𝗧𝗼𝘁𝗮𝗹 ⚡-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        stop = types.InlineKeyboardButton("⚆ 𝗙𝗼𝗿 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚆ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 ..⏳", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

              
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='⚆ 𝗗𝗼𝗻𝗲 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 𝗖𝗮𝗿𝗱𝘀 📣⚡')
                        stopuser[id]['status'] = 'stopped' 
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    if 'Stripe Error: Your card was declined.' in last:
                     	last = 'Your Card Was Declined'   
                    elif 'success' in last:
                     	last='Thank You for your donation.'                                              
                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"⚆ 𝗖𝗖 {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"⚆ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"⌧ 𝗖𝗖𝗡 𝗖𝗛𝗔𝗥𝗚𝗘 ✅ • [ {live} ]", callback_data='x')                    
                    cm4 = types.InlineKeyboardButton(f"⌧ 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • [ {dd} ]", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"⌧ 𝗧𝗢𝗧𝗔𝗟 🔍 [ {total_lines} ] / [ {cm} ]•", callback_data='x')
                    stop = types.InlineKeyboardButton("⌧ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>⚆ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱𝘀 💫
⚆ 𝗚𝗔𝗧𝗘 -> {gate} 💫
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a> </b>''', 
                        reply_markup=mes)

                    msg = f'''
<a href='t.me/aaka8h'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>ST®IPE CHA®GE 1$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: @{user_username}
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

                    if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is incorrect." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)                                     
                    else:
                        dd += 1

                    time.sleep(1)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗗𝗼𝗻𝗲 𝗖𝗵𝗲𝗰𝗸 𝗔𝗹𝗹 𝗖𝗮𝗿𝗱𝘀 ✅\n ⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 • @aaka8h')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗡𝗼 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸 𝘁𝗼 𝘀𝘁𝗼𝗽.')
	
	
	
	
	
	



	

	
	
	
	
	
	
	


import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  
check_enabled = True 

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱. 🔒 𝗡𝗼 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸 𝘂𝗻𝘁𝗶𝗹 𝗶𝘁 𝗶𝘀 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅ 𝗨𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗻𝗼𝘄 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br2:  
        bot.send_message(chat_id=call.message.chat.id, text="𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ❌.")
        return

   
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="🔍 𝗬𝗼𝘂 𝗔𝗿𝗲 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗔 𝗖𝗼𝗺𝗯𝗼. 🔄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗨𝗻𝘁𝗶𝗹 𝗜𝘁 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝘀 𝗢𝗿 𝗦𝘁𝗼𝗽 𝗜𝘁 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆."
        )
        return  

    def my_function():
        user_name = call.from_user.first_name if call.from_user.first_name else "User"
        user_username = call.from_user.username if call.from_user.username else "unknown"
        gate = '𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 2'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("⚆ [ 𝗖𝗔𝗥𝗗 ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"⚆ 𝗦𝘁𝗮𝘁𝘂𝘀 & 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("⚆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        ccn = types.InlineKeyboardButton("⚆ 𝗖𝗩𝗩 & 𝗖𝗖𝗡 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm4 = types.InlineKeyboardButton("⚆ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm5 = types.InlineKeyboardButton("⚆ 𝗧𝗼𝘁𝗮𝗹 ⚡-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        stop = types.InlineKeyboardButton("⚆ 𝗙𝗼𝗿 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚆ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 ..⏳", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

               
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped' 
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='⚆ 𝗗𝗼𝗻𝗲 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 𝗖𝗮𝗿𝗱𝘀 📣⚡')
                        stopuser[id]['status'] = 'stopped' 
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele2(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    if 'Your card was declined.' in last:
                     	last = 'Declined - Call Issuer'   
                    elif 'success' in last:
                     	last='APPROVED ✅'	
                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"⚆ 𝗖𝗖 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"⚆ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"⚆ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • [ {live} ]", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"⚆ 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • [ {dd} ]", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"⌧ 𝗧𝗢𝗧𝗔𝗟 🔍 [ {total_lines} ] / [ {cm} ]•", callback_data='x')
                    stop = types.InlineKeyboardButton("⌧ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>⚆ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱𝘀 💫
⚆ 𝗚𝗔𝗧𝗘 -> {gate} 💫
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a> </b>''', 
                        reply_markup=mes)

                    msg = f'''
<a href='t.me/aaka8h'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲 : <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Approved</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: @{user_username}
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

                    if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is incorrect." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(1)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗗𝗼𝗻𝗲 𝗖𝗵𝗲𝗰𝗸 𝗔𝗹𝗹 𝗖𝗮𝗿𝗱𝘀 ✅\n ⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 • @aaka8h')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗡𝗼 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸 𝘁𝗼 𝘀𝘁𝗼𝗽.')
	
	
	
	
	
	












	






















import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  
check_enabled = True 

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱. 🔒 𝗡𝗼 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸 𝘂𝗻𝘁𝗶𝗹 𝗶𝘁 𝗶𝘀 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅ 𝗨𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗻𝗼𝘄 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br3')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br3:  
        bot.send_message(chat_id=call.message.chat.id, text="𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ❌.")
        return

   
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="🔍 𝗬𝗼𝘂 𝗔𝗿𝗲 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗔 𝗖𝗼𝗺𝗯𝗼. 🔄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗨𝗻𝘁𝗶𝗹 𝗜𝘁 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝘀 𝗢𝗿 𝗦𝘁𝗼𝗽 𝗜𝘁 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆."
        )
        return  

    def my_function():
        user_name = call.from_user.first_name if call.from_user.first_name else "User"
        user_username = call.from_user.username if call.from_user.username else "unknown"
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 3'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("⚆ [ 𝗖𝗔𝗥𝗗 ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"⚆ 𝗦𝘁𝗮𝘁𝘂𝘀 & 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("⚆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        ccn = types.InlineKeyboardButton("⚆ 𝗖𝗩𝗩 & 𝗖𝗖𝗡 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm4 = types.InlineKeyboardButton("⚆ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm5 = types.InlineKeyboardButton("⚆ 𝗧𝗼𝘁𝗮𝗹 ⚡-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        stop = types.InlineKeyboardButton("⚆ 𝗙𝗼𝗿 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚆ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 ..⏳", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

               
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='⚆ 𝗗𝗼𝗻𝗲 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 𝗖𝗮𝗿𝗱𝘀 📣⚡')
                        stopuser[id]['status'] = 'stopped'  
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele3(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    if 'Your card is declined' in last:
                        last='Gateway Rejected: fraud'
                    if 'API failed to fetch' in last:
                    	last='Code 2009. No Such Issuer'
                    if 'Request Timeout' in last:
                    	last='Code 2014. Processor Declined - Fraud Suspectes'
                    if 'Card Expired' in last:
                    	last='Your Card Expired'
                    if 'Live' in last:
                    	last='APPROVED ✅'
                    if 'Unable to authenticate' in last:
                    	last='Declined - Call Issuer'
                    elif 'Proxy error' in last:
                    	last='Call Issuer. Pick Up Card. '

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"⚆ 𝗖𝗖 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"⚆ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"⚆ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • [ {live} ]", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"⚆ 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • [ {dd} ]", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"⌧ 𝗧𝗢𝗧𝗔𝗟 🔍 [ {total_lines} ] / [ {cm} ]•", callback_data='x')
                    stop = types.InlineKeyboardButton("⌧ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>⚆ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱𝘀 💫
⚆ 𝗚𝗔𝗧𝗘 -> {gate} 💫
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a> </b>''', 
                        reply_markup=mes)

                    msg = f'''
<a href='t.me/aaka8h'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲 : STRIPE AUTH
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞:  Approved

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: @{user_username}
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

                    if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗗𝗼𝗻𝗲 𝗖𝗵𝗲𝗰𝗸 𝗔𝗹𝗹 𝗖𝗮𝗿𝗱𝘀 ✅\n ⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 • @aaka8h')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗡𝗼 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸 𝘁𝗼 𝘀𝘁𝗼𝗽.')
	







	
	
	
	
	
	
	
	
	
	
	
import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  
check_enabled = True 

@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = False
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱. 🔒 𝗡𝗼 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸 𝘂𝗻𝘁𝗶𝗹 𝗶𝘁 𝗶𝘀 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗙𝗼𝗰𝘂𝘀𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗿𝗲-𝗲𝗻𝗮𝗯𝗹𝗲𝗱. ✅ 𝗨𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝗻𝗼𝘄 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗰𝗵𝗲𝗰𝗸.')
    else:
        bot.send_message(chat_id=message.chat.id, text='⚆ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘁𝗵𝗲 𝗼𝘄𝗻𝗲𝗿🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br4')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br4:  
        bot.send_message(chat_id=call.message.chat.id, text="𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ❌.")
        return

   
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="🔍 𝗬𝗼𝘂 𝗔𝗿𝗲 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗔 𝗖𝗼𝗺𝗯𝗼. 🔄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗨𝗻𝘁𝗶𝗹 𝗜𝘁 𝗙𝗶𝗻𝗶𝘀𝗵𝗲𝘀 𝗢𝗿 𝗦𝘁𝗼𝗽 𝗜𝘁 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆."
        )
        return  

    def my_function():
        user_name = call.from_user.first_name if call.from_user.first_name else "User"
        user_username = call.from_user.username if call.from_user.username else "unknown"
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("⚆ [ 𝗖𝗔𝗥𝗗 ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"⚆ 𝗦𝘁𝗮𝘁𝘂𝘀 & 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("⚆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        ccn = types.InlineKeyboardButton("⚆ 𝗖𝗩𝗩 & 𝗖𝗖𝗡 ✅-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm4 = types.InlineKeyboardButton("⚆ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        cm5 = types.InlineKeyboardButton("⚆ 𝗧𝗼𝘁𝗮𝗹 ⚡-> 𝗡𝘂𝗺𝗯𝗲𝗿 ", callback_data='x')
        stop = types.InlineKeyboardButton("⚆ 𝗙𝗼𝗿 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="⚆ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐅𝐢𝐥𝐞 ..⏳", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

             
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped' 
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='⚆ 𝗗𝗼𝗻𝗲 𝗦𝘁𝗼𝗽 𝗖𝗵𝗲𝗰𝗸 𝗖𝗮𝗿𝗱𝘀 📣⚡')
                        stopuser[id]['status'] = 'stopped'  
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele4(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    if 'Stripe Error: Your card was declined.' in last:
                     	last = 'Your Card Was Declined'   
                    elif 'Your card does not support this type of purchase.' in last:
                     	last='CVV LIVE ✅'

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"⚆ 𝗖𝗖 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"⚆ 𝗦𝗧𝗔𝗧𝗨𝗦 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"⚆ 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • [ {live} ]", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"⚆ 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • [ {dd} ]", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"⌧ 𝗧𝗢𝗧𝗔𝗟 🔍 [ {total_lines} ] / [ {cm} ]•", callback_data='x')
                    stop = types.InlineKeyboardButton("⌧ 𝗦𝗧𝗢𝗣 𝗖𝗛𝗘𝗖𝗞 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>⚆ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱𝘀 💫
⚆ 𝗚𝗔𝗧𝗘 -> {gate} 💫
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a> </b>''', 
                        reply_markup=mes)

                    msg = f'''
<a href='t.me/aaka8h'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>ST®IPE CHA®GE 2.99$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: @{user_username}
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

                    if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(1)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗗𝗼𝗻𝗲 𝗖𝗵𝗲𝗰𝗸 𝗔𝗹𝗹 𝗖𝗮𝗿𝗱𝘀 ✅\n ⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 • @aaka8h')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)

    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗖𝗵𝗲𝗰𝗸...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='⚆ 𝗡𝗼 𝗼𝗻𝗴𝗼𝗶𝗻𝗴 𝗰𝗵𝗲𝗰𝗸 𝘁𝗼 𝘀𝘁𝗼𝗽.')
	


	






























import json
from datetime import datetime, timedelta


def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)]['plan']
        timer = json_data[str(user_id)]['timer']
        if user_plan != 'Free - Not Subscribed':
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  
                    return True
            except Exception as e:
                return False
    return False










import time
from datetime import datetime, timedelta

# قم بتعريف قاموس لتخزين وقت آخر طلب لكل مستخدم
command_usage = {}

# الحالة الافتراضية لبوابة رقم 1 (مفعلة)
check_enabled_br1 = True

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vhk(message):
    global check_enabled_br1
    user_id = message.chat.id
    user_username = message.chat.username or "Anonymous"
    user_name = message.chat.first_name or "User"
    current_time = datetime.now()

 
    if not check_enabled_br1:
        bot.reply_to(message, "<b>⚆ 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗶𝘀 𝘂𝗻𝗱𝗲𝗿 𝗺𝗮𝗶𝗻𝘁𝗲𝗻𝗮𝗻𝗰𝗲 ❌.</b>", parse_mode="HTML")
        return

  
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
 
        if time_diff < 15:
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    

    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.chk ', '').replace('/chk ', '')
        gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘'
        ko = bot.reply_to(message, '𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛').message_id
        try:
        	cc = message.reply_to_message.text
        except:
        	cc=message.text
        cc=str(reg(cc))
        if cc == 'None':
        	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
    Please ensure you enter the card details in the correct format:
    Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        start_time = time.time()
        try:
            last = str(Tele(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>STRIPE CHARGE 1$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        ok = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>ST®IPE CHARGE 1$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        cvc = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>ST®IPE CHARGE 1$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "success" in last or 'Your card has insufficient funds' in last or 'Your card does not support this type of purchase.' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 ♡!
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗚𝗦𝗜𝗫 𝗕𝗢𝗧 !❌

⚆ 𝗬𝗼𝘂𝗿 𝗜𝗗 : {message.chat.id}
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>''')





















import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br2 = True

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def respond_to_vhk(message):
    global check_enabled_br2
    user_id = message.chat.id
    user_username = message.chat.username or "Anonymous"
    user_name = message.chat.first_name or "User"
    current_time = datetime.now()


    if not check_enabled_br2:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return


    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
   
        if time_diff < 15:
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
 
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.cc ', '').replace('/cc ', '')
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 1'
        ko = bot.reply_to(message, '𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛').message_id
        try:
        	cc = message.reply_to_message.text
        except:
        	cc=message.text
        cc=str(reg(cc))
        if cc == 'None':
        	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
    Please ensure you enter the card details in the correct format:
    Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        start_time = time.time()
        try:
            last = str(Tele2(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Declined - Call Issuer</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        ok = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Approved</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        cvc = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆@𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Approved</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞©𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "success" in last or 'Your card has insufficient funds' in last or 'Your card does not support this type of purchase.' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 ♡!
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗚𝗦𝗜𝗫 𝗕𝗢𝗧 !❌

⚆ 𝗬𝗼𝘂𝗿 𝗜𝗗 : {message.chat.id}
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>''')











import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br3 = True

@bot.message_handler(commands=['offb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.b3') or message.text.lower().startswith('/b3'))
def respond_to_vhk(message):
    global check_enabled_br3
    user_id = message.chat.id
    user_username = message.chat.username or "Anonymous"
    user_name = message.chat.first_name or "User"
    current_time = datetime.now()

 
    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

  
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
     
        if time_diff < 15:
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
 
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.sx ', '').replace('/sx ', '')
        gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 2'
        ko = bot.reply_to(message, '𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛').message_id
        try:
        	cc = message.reply_to_message.text
        except:
        	cc=message.text
        cc=str(reg(cc))
        if cc == 'None':
        	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
    Please ensure you enter the card details in the correct format:
    Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        start_time = time.time()
        try:
            last = str(Tele3(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Declined - Call Issuer </code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        ok = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Approved</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        cvc = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Auth</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Approved</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "success" in last or 'Your card has insufficient funds' in last or 'Your card does not support this type of purchase.' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 ♡!
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗚𝗦𝗜𝗫 𝗕𝗢𝗧 !❌

⚆ 𝗬𝗼𝘂𝗿 𝗜𝗗 : {message.chat.id}
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>''')












import time
from datetime import datetime, timedelta


command_usage = {}


check_enabled_br4 = True

@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = False
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sa') or message.text.lower().startswith('/sa'))
def respond_to_vhk(message):
    global check_enabled_br4
    user_id = message.chat.id
    user_username = message.chat.username or "Anonymous"
    user_name = message.chat.first_name or "User"
    current_time = datetime.now()
    

    if not check_enabled_br4:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

   
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
   
        if time_diff < 15:
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
  
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.sa ', '').replace('/sa ', '')
        gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 3'
        ko = bot.reply_to(message, '𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛').message_id
        try:
        	cc = message.reply_to_message.text
        except:
        	cc=message.text
        cc=str(reg(cc))
        if cc == 'None':
        	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
    Please ensure you enter the card details in the correct format:
    Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        start_time = time.time()
        try:
            last = str(Tele4(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>STRIPE CHARGE 3$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        ok = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>STRIPE CHARGE 3$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        cvc = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>STRIPE CHARGE 3$</code>		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Payment Successful 🎉</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "success" in last or 'Your card has insufficient funds' in last or 'Your card does not support this type of purchase.' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 ♡!
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗚𝗦𝗜𝗫 𝗕𝗢𝗧 !❌

⚆ 𝗬𝗼𝘂𝗿 𝗜𝗗 : {message.chat.id}
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>''')






























































from datetime import datetime, timedelta


last_command_usage = {}


check_enabled_ch1 = True

@bot.message_handler(commands=['offch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = False
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(commands=['onch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = True
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.ba') or message.text.lower().startswith('/ba'))
def respond_to_vhk(message):
    global check_enabled_ch1
    user_id = message.chat.id
    user_username = message.chat.username or "Anonymous"
    user_name = message.chat.first_name or "User"
    current_time = datetime.now()


    if not check_enabled_ch1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return


    if user_id in last_command_usage:
        time_diff = (current_time - last_command_usage[user_id]).seconds
        if time_diff < 15: 
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return

 
    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        cc = message.text.replace('.ba ', '').replace('/ba ', '')
        gate = '𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 4'
        ko = bot.reply_to(message, '𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛').message_id
        try:
        	cc = message.reply_to_message.text
        except:
        	cc=message.text
        cc=str(reg(cc))
        if cc == 'None':
        	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
    Please ensure you enter the card details in the correct format:
    Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
        start_time = time.time()
        try:
            last = str(Tele5(cc))
        except:
            last = 'Error Gateway!'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        ok = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ⤿ 𝘕𝘪𝘤𝘦! 𝘕𝘦𝘸 𝘱𝘢𝘺𝘮𝘦𝘯𝘵 𝘮𝘦𝘵𝘩𝘰𝘥 𝘢𝘥𝘥𝘦𝘥 ✅ ⤾

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        cvc = f'''
<a href='https://images.app.goo.gl/PTiXMpwXXf3DcRSf9'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/aaka8h'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/aaka8h'>┃</a>𝐂𝐂 <code>{cc}</code>
<a href='t.me/aaka8h'>┗━━━━━━━⊛</a>
<a href='t.me/aaka8h'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/aaka8h'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ⤿ 𝘕𝘪𝘤𝘦! 𝘕𝘦𝘸 𝘱𝘢𝘺𝘮𝘦𝘯𝘵 𝘮𝘦𝘵𝘩𝘰𝘥 𝘢𝘥𝘥𝘦𝘥 ✅ ⤾

{str(dato(cc[:6]))}

<a href='t.me/aaka8h'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/aaka8h'>-</a> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲: <a href='t.me/{user_username}'>{user_name}</a>
<a href='t.me/aaka8h'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/aaka8h'>⏤͟͞𝐌𝐚𝐬𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭</a>'''

        if 'success' in last or 'Stripe Error: Your card insufficient funds.' in last or 'Thank you for supporting' in last or 'Your card does not support this type of purchase.' in last or "Your card's security code is invalid." in last or 'Membership confirmation' in last or 'Thank You for your donation' in last or 'Stripe Error: Your card incorrect_cvc' in last or 'The zip code you supplied failed validation.' in last or 'Stripe Error: Your card security code is incorrect' in last or 'stripe_3ds2_fingerprint' in last or 'Your card security code is invalid.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'Your card has insufficient funds.' in last or 'Invalid account.' in last or 'zip code is incorrect' in last or 'three_d_secure' in last or 'security code is incorrect' in last or 'security code is invalid' in last or 'authentication required' in last or "Stripe Error: Your card's security code is invalid." in last or "Your card's security code is invalid." in last or 'Verifying strong customer authentication. Please wait...' in last or 'Thank you for your message. We will get in touch with you shortly' in last or 'APPROVED ✅' in last or '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "success" in last or '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or 'Your card does not support this type of purchase.' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗗𝗲𝗮𝗿 ♡!
𝗬𝗼𝘂 𝗮𝗿𝗲 𝗡𝗼𝘁 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲𝗱 𝗚𝗦𝗜𝗫 𝗕𝗢𝗧 !❌

⚆ 𝗬𝗼𝘂𝗿 𝗜𝗗 : {message.chat.id}
⚆ 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿<a href='t.me/aaka8h'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 🇲🇲</a>''')


















@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>⚆ 𝗕𝗜𝗡 𝗜𝗡𝗙𝗢 𝗟𝗢𝗢𝗞𝗨𝗣  🔍
	
⚆ 𝗕𝗜𝗡 -></b> <code>{cc}</code>

<b>{str(dato(cc[:6]))}</b>''')










import json
import threading
from datetime import datetime
import time




def get_user_info(user_id):
    try:
        chat = bot.get_chat(user_id)
        user_name = chat.first_name
        user_username = chat.username
        return user_name, user_username
    except Exception as e:
        m = (f"𝗘𝗿𝗿𝗼𝗿 𝗿𝗲𝘁𝗿𝗶𝗲𝘃𝗶𝗻𝗴 𝘂𝘀𝗲𝗿 𝗶𝗻𝗳𝗼 𝗳𝗼𝗿 𝗜𝗗 {user_id}: {e}")
        return 'Unknown', 'Unknown'

def notify_admins(user_id, user_data):
    user_name, user_username = get_user_info(user_id)
    message = f'''- Subscription Expired Notification 🕒

• User ID: {user_id}
• User Name: {user_name}
• Username: @{user_username}
• Plan: {user_data.get('plan', 'Free - Not Subscribed')}
• Expiration Date: {user_data.get('timer', 'N/A')}
• Bot Subscription @aaka8h
'''
    for admin_id in myid:
        bot.send_message(admin_id, message)

def notify_user(user_id):
    try:
        bot.send_message(user_id, "𝐘𝐨𝐮𝐫 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐇𝐚𝐬 𝐄𝐱𝐩𝐢𝐫𝐞𝐝..")
    except Exception as e:
        m = (f"Error notifying user {user_id}: {e}")

def update_subscription_status():
    try:
    
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        current_time = datetime.now()
        updated = False  

        for user_id, user_data in json_data.items():
            timer_str = user_data.get('timer', None)
            if timer_str:
                try:
                    expiration_time = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                    
                    if current_time > expiration_time:
                        user_data['plan'] = 'Free - Not Subscribed'
                        del user_data['timer'] 
                        updated = True
                        
                        notify_admins(user_id, user_data)
                       
                        notify_user(user_id)
                except ValueError:
                    m = (f"Date format error for user {user_id} with date {timer_str}")
        
        if updated:
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = ("Subscription status updated.")
    
    except Exception as e:
        mm = (f"Error updating subscription status: {e}")

def schedule_check():
    while True:
        update_subscription_status()
        time.sleep(1)  


check_thread = threading.Thread(target=schedule_check)
check_thread.start()















import json
from datetime import datetime, timedelta


def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)].get('plan', 'Free - Not Subscribed')
        timer = json_data[str(user_id)].get('timer', None)
        if user_plan != 'Free - Not Subscribed' and timer:
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  
                    return True
            except Exception as e:
                print(f"Error parsing date for user {user_id}: {e}")
                return False
    return False
    
    
BOT_OWNER_ID = 5983253591  # Replace with your Telegram ID (no quotes)

@bot.message_handler(commands=['gay'])
def gay_command(message):
    if message.reply_to_message:  # Check if the command is in reply to a message
        target_id = message.reply_to_message.from_user.id
        target_username = message.reply_to_message.from_user.username
        target_first_name = message.reply_to_message.from_user.first_name  # Define target_first_name here

        if target_id == BOT_OWNER_ID:  # If the replied user is the bot owner
            bot.reply_to(message, f"𝖧𝖾𝗅𝗅𝗈!  <a href='t.me/{target_username}'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝙶𝚂𝙸𝚇】ꪜ🇲🇲</a> \n\n𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖧𝖺𝗉𝗉𝗒 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖺𝗍 𝖸𝗈𝗎 𝖠𝗋𝖾 \n0% Gay 😂")
        else:
            percentage = random.randint(0, 100)
            if target_username:
                bot.reply_to(message, f"𝖧𝖾𝗅𝗅𝗈!  <a href='t.me/{target_username}'>{target_first_name}</a> \n\n𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖧𝖺𝗉𝗉𝗒 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖺𝗍 𝖸𝗈𝗎 𝖠𝗋𝖾 \n{percentage}% Gay 😂")
            else:
                bot.reply_to(message, f"𝖧𝖾𝗅𝗅𝗈!  {target_first_name} \n\n𝖸𝗈𝗎 𝖶𝗂𝗅𝗅 𝖡𝖾 𝖧𝖺𝗉𝗉𝗒 𝖳𝗈 𝖪𝗇𝗼𝗐 𝖳𝗁𝖺𝗍 𝖸𝗈𝗎 𝖠𝗋𝖾 \n{percentage}% Gay 😂")
    else:
        # Handle the case where the command is not a reply
        user_first_name = message.from_user.first_name
        user_username = message.from_user.username
        percentage = random.randint(0, 100)
        if user_username:
            bot.reply_to(message, f"𝖧𝖾𝗅𝗅𝗈!  <a href='t.me/{user_username}'>{user_first_name}</a> \n\n𝖸𝗈𝗎 𝖶𝗂𝗅𝗂 𝖡𝖾 𝖧𝖺𝗉𝗉𝗒 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖺𝗍 𝖸𝗈𝗎 𝖠𝗋𝖾 \n{percentage}% Gay 😂")
        else:
            bot.reply_to(message, f"𝖧𝖾𝗅𝗅𝗈!   {user_first_name} \n\n𝖸𝗈𝗎 𝖶𝗂𝗅𝗂 𝖡𝖾 𝖧𝖺𝗉𝗉𝗒 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖺𝗍 𝖸𝗈𝗎 𝖠𝗋𝖾 \n{percentage}% Gay 😂")




import json

@bot.message_handler(commands=['sendall'])
def send_all(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            mes = message.text.replace("/sendall ", "")
            
            # Load user IDs from 'data.json'
            try:
                with open('data.json', 'r') as file:
                    json_data = json.load(file)
            except FileNotFoundError:
                bot.reply_to(message, "Error: 'data.json' not found.")
                return
            except json.JSONDecodeError:
                bot.reply_to(message, "Error: 'data.json' is not properly formatted.")
                return

            # Loop through each user ID and send the message
            for user_id in json_data.keys():
                try:
                    mp += 1
                    bot.send_message(user_id, mes)
                except Exception as e:
                    erop += 1
                    print(f"Error sending message to user {user_id}: {e}")

            bot.reply_to(message, f'''- Message sent to all users:
• Success: {mp}
• Failed: {erop}''')

        except Exception as err:
            bot.reply_to(message, f'- An error occurred: {err}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")




@bot.message_handler(commands=['getdraw'])
def get_draw(message):
    # Extract the text from the message
    text = message.text[len('/getdraw '):]  # Remove the "/getdraw " part from the message
    
    if not text:
        bot.reply_to(message, "Please provide text after the command.")
        return
    
    # Create an image with Pillow
    width, height = 800, 400  # Set the size of the image
    image = Image.new('RGB', (width, height), color=(255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Use a font on your system
    except IOError:
        font = ImageFont.load_default()  # Fallback to default if the specific font isn't found

    # Get the bounding box of the text to calculate its width and height
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to center the text
    position = ((width - text_width) / 2, (height - text_height) / 2)

    # Draw the text on the image
    draw.text(position, text, (0, 0, 0), font=font)  # Black text

    # Save the image to a BytesIO object
    img_bytes = BytesIO()
    image.save(img_bytes, 'PNG')
    img_bytes.seek(0)  # Rewind the BytesIO object to the start

    # Send the image to the user
    bot.send_photo(message.chat.id, img_bytes)
    







myid = ['5983253591']
@bot.message_handler(commands=["tot"])
def adode(message):
    if str(message.from_user.id) in myid:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        vip_count = 0
        total_users = len(json_data)  # Count total users from the data.json
        
        for user_id, details in json_data.items():
            user_plan = details.get('plan', 'Free - Not Subscribed')
            timer = details.get('timer', None)
            if user_plan != 'Free - Not Subscribed' and timer:
                try:
                    # Parse the date from the 'timer' field
                    date_str = timer.split('.')[0]
                    provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    current_time = datetime.now()
                    
                    # Check if the subscription is still valid (example: valid for 30 days)
                    if current_time - provided_time <= timedelta(days=30):  # Modify the timedelta to your needs
                        vip_count += 1
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")

        bot.reply_to(message, f'- Total Users = {total_users} \n- Total VIP Subscribers: {vip_count}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")













import json
from datetime import datetime

@bot.message_handler(commands=['sh'])
def show_vip_subscribers(message):
    if str(message.chat.id) in myid:
        try:
            with open('data.json', 'r') as file:
                json_data = json.load(file)
        except Exception as e:
            bot.send_message(message.chat.id, f'- Error reading data file: {e}')
            return

        total_subscribers = 0
        subscriber_details = []

        for user_id, user_data in json_data.items():
            plan = user_data.get('plan', 'NO PLAN')
            if plan == 'VIP Subscribed':
                timer = user_data.get('timer', 'NO EXPIRATION DATE')
                if timer != 'NO EXPIRATION DATE':
                    try:
                        expiration_date = datetime.strptime(timer, "%Y-%m-%d %H:%M")
                        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M")
                    except ValueError:
                        expiration_date_str = 'INVALID DATE FORMAT'
                else:
                    expiration_date_str = 'NO EXPIRATION DATE'
                
                
                try:
                    chat = bot.get_chat(user_id)
                    user_name = chat.first_name
                    user_username = chat.username
                    if user_name:
                        user_display = f"Name: {user_name}\nUsername: @{user_username}" if user_username else f"Name: {user_name}\nUsername: Not Available"
                    else:
                        # Skip users with no valid name
                        continue
                except Exception as e:
                    # Skip users with errors retrieving data
                    continue
                
                subscriber_details.append(f'''• User ID: {user_id}
{user_display}
• Plan: {plan}
• Expiration Date: {expiration_date_str}
━━━━━━━━━━━━━━━━━━━━━━
''')

                total_subscribers += 1

        if subscriber_details:
            details_message = "\n".join(subscriber_details)
            bot.send_message(message.chat.id, f'''- VIP Subscriber Details ✅💫

{details_message} - Total VIP Subscribers -> {total_subscribers} ✅
''')
        else:
            bot.send_message(message.chat.id, '- No VIP subscribers found.')











import json
from datetime import datetime

def remove_subscription(user_id):
    try:
        
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
          
            json_data[user_id]['plan'] = 'Free - Not Subscribed'
            del json_data[user_id]['timer'] 
            
            
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = (f"Subscription for user {user_id} has been set to FREE.")
        else:
            mm= (f"User ID {user_id} not found in data.json.")
    
    except Exception as e:
        m = (f"Error removing subscription for user {user_id}: {e}")

@bot.message_handler(commands=['dele'])
def qwwem(message):
    if str(message.chat.id) in admins:
        user_id = message.text.replace("/dele ", "")
        
        
        remove_subscription(user_id)
        
        try:
            chat = bot.get_chat(user_id)
            frs = chat.first_name
            use = chat.username
            bot.send_message(message.chat.id, f'''- Done ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}

- IS Removed From Subscribers ✅''')
        except Exception as e:
            bot.send_message(message.chat.id, f'''- UnSuccessful Removal ❌

• User might not have opened your bot.

- Error -> {e}''')
    else:
        bot.send_message(message.chat.id, "You do not have permission to execute this command.")















@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or 'NoUsername'  
    
    response_message = f'''🌟 Welcome » {user_first_name}
🆔 ID » <code>{user_id}</code>
📛 Name » {user_first_name}
🧑 Username » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')



	
	
	







@bot.message_handler(commands=["menu"])
def adodre(message):
	if str(message.chat.id) in myid:
		bot.reply_to(message,'''- Welcome My Boss ♡
- Start Check Bot ¦ /start
- Add New Subscriber ¦ /add + ID
- Total Bot Users ¦ /tot
- Send Msg Forr All ¦ /sendall + msg
- Delete A Subsc ¦ /dele + ID
- Show Sub's ID's ¦ /sh
- Stop And Start The Gate's /gate
------------------------------------
• Programmer ¦ @aaka8h
• Channel ¦ @aaka8h''')





	
	
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.prices') or message.text.lower().startswith('/prices'))
def respondn_to_vhk(message):
 bot.reply_to(message,'''• Bot Subscription Prices - Bot Prices •
⬅️ Combo CC Checker Bot 🛒👑

- (4 Gates, 4 Gates) ⭐️
- (Manual Check, Combo Check) ⭐️
1- One Day •💷Day -> 3 ⚡️
1- Week •💷 Week -> 10 ⚡️
1- Half Month •💷Half Month -> 20 ⚡️
1- Month •💷Month -> 25 ⚡️

• We Accept All Payment Methods in USDT BTX BTC TRC EHT BNB ✅
• (💴💷🌐👛💀..........🌎🌎)

• For Subscribe & Inquiry - For Communication and Inquiry •  🛩 🖱👼@aaka8h👼&👼 @aaka8h 👼''')












import json
import threading
from datetime import datetime, timedelta
import random
import string


@bot.message_handler(commands=["code"])
def generate_code(message):
    def my_function():
        id = message.from_user.id
        if not str(id) in myid:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            
            characters = string.ascii_uppercase + string.digits
            pas = 'GSIXTEAM-' + '2024' +'-' + ''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            expiration_time = current_time + timedelta(hours=h)
            plan = 'VIP Subscribed'
            expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
            
            new_data = {
                pas: {
                    "plan": plan,
                    "timer": expiration_time_str
                }
            }
            
            existing_data.update(new_data)
            
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            
            msg = f'''
┏━━━━━━━━━━━━━━━━⍟
┃⚆ 𝗖𝗖 𝗖𝗛𝗘𝗖𝗞𝗘𝗥 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗕𝗢𝗧
┃⚆ 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {expiration_time_str}
┃⚆ 𝗞𝗘𝗬 ➜ <code>{pas}</code>
┃━━━━━━━━/━━━━━━━⍟            
┃⌧ 𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]
┃⌧ 𝗕𝗢𝗧 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 @Maxs_rbot
┗━━━━━━━━/━━━━━━━⍟'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f'<b>ERROR : {e}</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            
            re = message.text.split(' ')[1]
            
            
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            
            
            if re in json_data:
                timer = json_data[re].get('timer', 'Unknown')
                typ = json_data[re].get('plan', 'Free - Not Subscribed')

                
                json_data[str(message.from_user.id)] = {
                    'timer': timer,
                    'plan': typ
                }
                
                
                del json_data[re]
                
                
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=2, ensure_ascii=False)

                msg = f'''
┏━━━━━━━━━━━━━━━━⍟                
┃⚆ 𝗚𝗦𝗜𝗫 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
┃⚆ 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 
┃⚆ 𝗗𝗔𝗧𝗘 𝗧𝗜𝗠𝗘 {timer}
┃━━━━━━━━/━━━━━━━⍟ 
┃⌧ 𝗖𝗼𝗻𝗴𝗿𝗮𝘁𝘂𝗹𝗮𝘁𝗶𝗼𝗻𝘀! 🎉🎉✅✅
┃⌧ 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗡𝗲𝘄 𝗨𝘀𝗲𝗿 👑💸
┗━━━━━━━━/━━━━━━━⍟'''
                bot.reply_to(message, msg, parse_mode="HTML")
            else:
                bot.reply_to(message, '┏━━━━━━━━━━━━━━━━━⍟\n┃⚆𝗜𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗰𝗼𝗱𝗲 𝗼𝗿 𝗶𝘁 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗯𝗲𝗲𝗻 \n┃⚆𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 \n┃⚆𝗖𝗵𝗲𝗰𝗸 /start 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻  \n┗━━━━━━━━/━━━━━━━━⍟', parse_mode="HTML")

        except KeyError as e:
            print(f'KeyError: {e}')
            bot.reply_to(message, '┏━━━━━━━━━━━━━━━━━⍟\n┃⚆𝗜𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗰𝗼𝗱𝗲 𝗼𝗿 𝗶𝘁 𝗵𝗮𝘀  \n┃⚆𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗯𝗲𝗲𝗻 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱 \n┗━━━━━━━━/━━━━━━━━⍟', parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '┏━━━━━━━━━━━━━━━━━⍟\n┃⚆𝗧𝗵𝗲𝗿𝗲 𝘄𝗮𝘀 𝗮𝗻 𝗲𝗿𝗿𝗼𝗿 𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 \n┃⚆𝗿𝗲𝗾𝘂𝗲𝘀𝘁. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 𝗹𝗮𝘁𝗲𝗿.\n┗━━━━━━━━/━━━━━━━━⍟', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


@bot.message_handler(commands=['add'])
def add_subscription(message):
    def my_function():
        try:
            chid = message.chat.id
            command_text = message.text.replace('/add ', '')
            user_id, duration_hours = command_text.split()
            duration_hours = int(duration_hours)
            
            if str(message.chat.id) in myid:
                current_time = datetime.now()
                expiration_time = current_time + timedelta(hours=duration_hours)
                expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
                plan = 'VIP Subscribed'
                
               
                with open('data.json', 'r') as json_file:
                    existing_data = json.load(json_file)
                
                
                existing_data[user_id] = {
                    'timer': expiration_time_str,
                    'plan': plan
                }
                
                
                with open('data.json', 'w') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                
                
                try:
                    chat = bot.get_chat(user_id)
                    frs = chat.first_name
                    use = chat.username
                    user_display = f"Name: {frs}\nUsername: @{use}" if use else f"Name: {frs}\nUsername: Not Available"
                except Exception as e:
                    user_display = f"Username: Unknown"
                
                bot.send_message(chid, f'''- Done Add -> <code>{user_id}</code> 

• Subscription Duration -> {duration_hours} hours
• {user_display}
- Added to Subscribers List ✅''')
            else:
                bot.send_message(chid, ' - Unauthorized Access !!!!')
        except Exception as e:
            bot.reply_to(message, f'- Was An Error -> {e}')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()











def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("Bot Start Access")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"coding problem: {e}")
		continue
