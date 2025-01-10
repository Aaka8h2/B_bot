import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
stopuser = {}
token = '7886528180:AAFLd7UYfCBDCwHkBOmLewsItCBasnj1was'#token
bot=telebot.TeleBot(token,parse_mode="HTML")
admin= '5983253591'
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
			id=message.from_user.id
			user = message.from_user.username
			keyboard = types.InlineKeyboardMarkup()	
			add_bot_button = types.InlineKeyboardButton(text='Add the bot to your collection ', url=f'https://t.me/W_ILLMbot?startgroup')	
			keyboard.row(add_bot_button)
			photo_url = f'https://t.me/TEMM_123/143'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>Hello @{user}! [<code>{id}</code>]
Operational Bot!
- - - - - - - - - - - - - - - - - - - - - 
Status: Active ✅
- - - - - - - - - - - - - - - - - - - - - 
Use the button below to view commands or use '/cmds' .

Developer: @aaka8h</b>
	''',reply_markup=keyboard)
			return
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	keyboard = types.InlineKeyboardMarkup()
	tool = types.InlineKeyboardButton(text='Tools', callback_data='tool')
	plans = types.InlineKeyboardButton(text='Gateways', callback_data='plans')
	keyboard.row(plans,tool)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
Available Commands:
━━━━━━━━━━━━
Total Gateways: 5
Total Tools: 4
━━━━━━━━━━━━
Developer: @aaka8h</b>
''',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu_callback(call):
	keyboard = types.InlineKeyboardMarkup()
	tool = types.InlineKeyboardButton(text='Tools', callback_data='tool')
	plans = types.InlineKeyboardButton(text='Gateways', callback_data='plans')
	keyboard.row(plans,tool)
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=f'''<b> 
Available Commands:
━━━━━━━━━━━━
Total Gateways: 5
Total Tools: 4
━━━━━━━━━━━━
Developer: @aaka8h</b>
''',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'plans')
def menu_callback(call):
	keyboard = types.InlineKeyboardMarkup()
	back = types.InlineKeyboardButton(text='Back', callback_data='menu')
	keyboard.row(back)
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f""" Gateways:
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: Braintree Auth
𝐒𝐭𝐚𝐭𝐮𝐬: ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/chk</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: Braintree Charge 
𝐒𝐭𝐚𝐭𝐮𝐬: ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/b3</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: Stripe Charge $1
𝐒𝐭𝐚𝐭𝐮𝐬: ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/sc</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: Stripe Charge $17
𝐒𝐭𝐚𝐭𝐮𝐬: ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/str</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: Otp PayPal
𝐒𝐭𝐚𝐭𝐮𝐬: ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/pp</code>
━━━━━━━━━━━━""",reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'tool')
def menu_callback(call):
	keyboard = types.InlineKeyboardMarkup()
	back = types.InlineKeyboardButton(text='Back', callback_data='menu')
	keyboard.row(back)
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""Available Tools:
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐂𝐂 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐀𝐩𝐢 - ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/gen 440393</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐁𝐈𝐍 𝐥𝐨𝐨𝐤𝐮𝐩 𝐀𝐩𝐢 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/bin 440393</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐂𝐨𝐦𝐝𝐨 𝐁𝐢𝐧 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/comdo</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐅𝐚𝐤𝐞 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/fake</code>""",reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free'
		if BL == 'Free':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="Dev", url="https://t.me/aaka8h")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>You can't use the bot because your subscription has expired ❌
</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="Dev", url="https://t.me/aaka8h")
			keyboard.add(ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>You can't use the bot because your subscription has expired ❌</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="Dev", url="https://t.me/aaka8h")
			keyboard.add(ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>You can't use the bot because your subscription has expired ❌</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f" Braintree Auth",callback_data='br')
		brcha = types.InlineKeyboardButton(text=f"Braintree Charge",callback_data='looll')
		paypp = types.InlineKeyboardButton(text=f"Otp paypal",callback_data='payp')
		sw = types.InlineKeyboardButton(text=f"Stripe Charge $17",callback_data='str')
		boon = types.InlineKeyboardButton(text=f"Stripe Charge $1",callback_data='boo')		
		keyboard.add(contact_button)
		keyboard.add(brcha)
		keyboard.add(paypp)
		keyboard.add(sw)
		keyboard.add(boon)
		bot.reply_to(message, text=f'Choose The Gateway You Want To Use 🆑',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'boo')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		user = call.from_user.username
		name = call.from_user.first_name
		gate='Stripe_Chrge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Checking Your Cards...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝐒𝐓𝐎𝐏𝐏𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜@aaka8h')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele7(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Charge ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"•Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• insufficient Funds ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ Stop ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐡𝐢𝐥𝐞 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝𝐬 𝐚𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 @aaka8h''', reply_markup=mes)

					msg=f'''#{gate} ($1) 🔥 [/sc]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @aaka8h 🍀'''
					if "Funds" in last or 'Invalid postal' in last or 'live' in last or 'CHARGED' in last or 'Duplicate' in last or 'Approved' in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝐁𝐄𝐄𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜ @aaka8h ')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		user = call.from_user.username
		name = call.from_user.first_name
		gate='Stripe_Chrge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Checking Your Cards...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝐒𝐓𝐎𝐏𝐏𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜@aaka8h')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(nin(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Charge ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"•Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• insufficient Funds ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ Stop ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐡𝐢𝐥𝐞 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝𝐬 𝐚𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 @aaka8h''', reply_markup=mes)

					msg=f'''#{gate} ($17) 🔥 [/str]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @aaka8h 🍀'''
					if "Funds" in last or 'Invalid postal' in last or 'live' in last or 'CHARGED' in last or 'Duplicate' in last or 'Approved' in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝐁𝐄𝐄𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜ @aaka8h ')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'looll')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		user = call.from_user.username
		name = call.from_user.first_name
		gate='Braintree_Charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Checking Your Cards...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝐒𝐓𝐎𝐏𝐏𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜@aaka8h')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele7(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Charge ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"•Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• insufficient Funds ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ Stop ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐡𝐢𝐥𝐞 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝𝐬 𝐚𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 @aaka8h''', reply_markup=mes)

					msg=f'''#{gate} ❤️ [/b3]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @aaka8h 🍀'''
					if 'Charged' in last or 'CNN' in last or 'Insufficient Funds' in last or 'Funds' in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝐁𝐄𝐄𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜ @aaka8h ')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		user = call.from_user.username
		name = call.from_user.first_name
		gate='Braintree_Auth'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Checking Your Cards...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝐒𝐓𝐎𝐏𝐏𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜@aaka8h')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele7(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"•Approved ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• CCN ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"•Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• insufficient Funds ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ Stop ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐡𝐢𝐥𝐞 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝𝐬 𝐚𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 @aaka8h''', reply_markup=mes)

					msg=f'''#{gate} (0.1) 💕 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @aaka8h 🍀'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝐁𝐄𝐄𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜ @aaka8h ')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		user = call.from_user.username
		name = call.from_user.first_name
		gate='Otp_PayPal'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "Checking Your Cards...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝐒𝐓𝐎𝐏𝐏𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜@aaka8h')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele7(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• Otp PayPal➜ [ {live} ] •", callback_data='x')
			
					cm4 = types.InlineKeyboardButton(f"• Declined ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• Total 👻  ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ Stop ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐰𝐡𝐢𝐥𝐞 𝐲𝐨𝐮𝐫 𝐜𝐚𝐫𝐝𝐬 𝐚𝐫𝐞 𝐁𝐞𝐢𝐧𝐠 𝐂𝐡𝐞𝐜𝐤 𝐚𝐭 𝐓𝐡𝐞 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 {gate}
𝐁𝐨𝐭 𝐁𝐲 @aaka8h''', reply_markup=mes)

					msg=f'''#{gate} 💤 [/pp]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐎𝐭𝐩 𝐏𝐚𝐲𝐏𝐚𝐥 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: @aaka8h 🍀'''
					if "3DS Challenge Required" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝐁𝐄𝐄𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃 ✅ \𝐧𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐁𝐘 ➜ @aaka8h ')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	name = message.from_user.first_name
	user = message.from_user.username
	idt=message.from_user.id
	id=message.chat.id
	gate='Stripe_Charge'
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(nin(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''#{gate} ($17) 🔥 [/str]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	msgd=f'''#{gate} ($17) 🔥 [/str]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ]𝐒𝐭𝐚𝐭𝐮𝐬:𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	if "Funds" in last or 'Invalid postal' in last or 'live' in last or 'CHARGED' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sc') or message.text.lower().startswith('/sc'))
def respond_to_vbv(message):
	name = message.from_user.first_name
	user = message.from_user.username
	idt=message.from_user.id
	id=message.chat.id
	gate='Stripe_Charge'
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(Tele7(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''#{gate} ($1) 🔥 [/sc]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	msgd=f'''#{gate} ($1) 🔥 [/sc]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ]𝐒𝐭𝐚𝐭𝐮𝐬:𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	if "Funds" in last or 'Invalid postal' in last or 'live' in last or 'CHARGED' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.b3') or message.text.lower().startswith('/b3'))
def respond_to_vbv(message):
	name = message.from_user.first_name
	user = message.from_user.username
	idt=message.from_user.id
	id=message.chat.id
	gate='Braintree_Charge'
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(nin(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''#{gate} 💲 [/b3]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 𝐂𝐡𝐚𝐫𝐠𝐞 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	msgd=f'''#{gate} 💲 [/b3]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ]𝐒𝐭𝐚𝐭𝐮𝐬:𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	if 'Charged' in last or 'CNN' in last or 'Insufficient Funds' in last or 'Funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	name = message.from_user.first_name
	user = message.from_user.username
	idt=message.from_user.id
	id=message.chat.id
	gate='Braintree_Auth'
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(nin(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''#{gate} (0.01) 💲 [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	msgd=f'''#{gate} (0.01) ♾️ [/chk]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ]𝐒𝐭𝐚𝐭𝐮𝐬:𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	if 'Charged' in last or 'CNN' in last or 'Insufficient Funds' in last or 'Funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp') or message.text.lower().startswith('/pp'))
def respond_to_vbv(message):
	name = message.from_user.first_name
	user = message.from_user.username
	idt=message.from_user.id
	id=message.chat.id
	gate='Otp_PayPal'
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		last= str(nin(cc))
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''#{gate} 💤 [/pp]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ] 𝐒𝐭𝐚𝐭𝐮𝐬: 𝐎𝐭𝐩 𝐏𝐚𝐲𝐏𝐚𝐥 ✅
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a>'' [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	msgd=f'''#{gate} 💤 [/pp]
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐂𝐚𝐫𝐝:  <code>{cc}</code> 
[ϟ]𝐒𝐭𝐚𝐭𝐮𝐬:𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌
[ϟ] 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {last}
- - - - - - - - - - - - - - - - - - - - - - - -
[ϟ] 𝐈𝐧𝐟𝐨: <code>{card_type} - {brand}</code>
[ϟ] 𝐁𝐚𝐧𝐤: <code>{bank}</code>
[ϟ] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - [{country_flag}]</code>
- - - - - - - - - - - - - - - - - - - - - - - -
[⌥] 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)}</code> 𝐒𝐞𝐜. || 𝐏𝐫𝐨𝐱𝐲: <code>Live</code> ✅
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [֎]<a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a>
[Dev]
- - - - - - - - - - - - - - - - - - - - - - - -
[⌤] 𝐃𝐞𝐯 𝐛𝐲: <code>@aaka8h</code> 🍀'''
	if 'Challenge Required' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>⏤͟͞𝙎𝙉𝙄𝙋𝙀𝙍 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='TEMM-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🌩️
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def generate_credit_card(message, bot, ko):
    try: 
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''BIN not recognized. Please enter a valid BIN ❌''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country', 'Unknown')
                level = data.get('level', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'
                level = 'Unknown'
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"[⌥] 𝐂𝐂 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐀𝐩𝐢\n━━━━━━━━━━━━━━\n[⌬] 𝐁𝐢𝐧: <code>{bin}</code> || 𝐄𝐱𝐩𝐢𝐫𝐞: xx|xx || 𝐂𝐯𝐯: xxx\n[⌬] 𝐀𝐦𝐨𝐮𝐧𝐭: 10\n━━━━━━━━━━━━━━\n[⎐] 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐂𝐚𝐫𝐝𝐬:\n- - - - - - - - - - - - - - - - - - \n{response_message}\n- - - - - - - - - - - - - - - - - - \n[⌬] 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: {brand} - {card_type} - {level}\n[⌬] 𝐁𝐚𝐧𝐤:  {bank}\n[⌬] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country} - [{country_flag}]\n━━━━━━━━━━━━━━\n[≹] 𝐓𝐢𝐦𝐞: 0.00 seconds", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="BIN not recognized. Please enter a valid BIN ❌")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10




def gen(bin):
	remaining_digits = 16 - len(bin)
	card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
	digits = [int(digit) for digit in card_number]
	for i in range(len(digits)):
		if i % 2 == 0:
			digits[i] *= 2
			if digits[i] > 9:
				digits[i] -= 9
	
	checksum = sum(digits)
	checksum %= 10
	checksum = 10 - checksum
	if checksum == 10:
		checksum = 0
	card_number += str(checksum)
	return card_number
import requests

@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
    user = message.from_user.username
    name = message.from_user.first_name
    try:
        bm = message.reply_to_message.text
    except:
        bm = message.text
    regex = r'\d+'
    try:
        matches = re.findall(regex, bm)
    except:
        bot.reply_to(message, '🚫 Incorrect input. Please provide a 6-digit BIN number.', parse_mode="HTML")
        return

    # الحصول على أول 6 أرقام من BIN
    bin = ''.join(matches)[:6]
    ko = bot.reply_to(message, "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗯𝗶𝗻...⌛", parse_mode="HTML").message_id

    # التحقق من أن الـ BIN يتكون من 6 أرقام على الأقل
    if len(bin) >= 6:
        try:
            # طلب معلومات الـ BIN من API
            data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country = data.get('country_name', 'Unknown')
            country_flag = data.get('country_flag', '🏳️')
            bank = data.get('bank', 'Unknown')
            
            # تكوين الرسالة النهائية
            msg = f'''
[⌥] 𝐁𝐈𝐍 𝐥𝐨𝐨𝐤𝐮𝐩 𝐀𝐩𝐢
━━━━━━━━━━━━━━━━━
[⌬] 𝐁𝐈𝐍 ⇢ <code>{bin}</code>
[⌬] 𝐈𝐧𝐟𝐨 ⇢ {card_type} - {brand}  
[⌬] 𝐈𝐬𝐬𝐮𝐞𝐫 ⇢  {bank}
[⌬] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇢ {country} - [{country_flag}]
━━━━━━━━━━━━━━━━━
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a>' [Free user]
 '''
        except:
            # في حال حدوث خطأ أثناء طلب البيانات
            msg = '𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌'
    else:
        msg = '🚫 Incorrect input. Please provide a 6-digit BIN number.'
    
    # تعديل الرسالة الأصلية مع النتيجة
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")
@bot.message_handler(func=lambda message: message.text.lower().startswith('.fake') or message.text.lower().startswith('/fake'))
def respond_to_vbv(message):
	def my_function():
		try:
			try:
				u=message.text.split('fake ')[1]
			except:
				u='US'
			parsed_data = requests.get(f'https://randomuser.me/api/?nat={u}').json()
			results = parsed_data['results']
			result = results[0]
			name = f"{result['name']['title']} {result['name']['first']} {result['name']['last']}"
			street_number = result['location']['street']['number']
			street_name = result['location']['street']['name']
			city = result['location']['city']
			state = result['location']['state']
			country = result['location']['country']
			postcode = result['location']['postcode']
			fake = Faker()
			phone = fake.phone_number()
			email = fake.email()
			user = message.from_user.username
			name = message.from_user.first_name
			formatted_address = f"""<b>
[⌥] 𝐅𝐚𝐤𝐞 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫
━━━━━━━━━━━━
[↯] 𝐍𝐚𝐦𝐞: <code>{name}</code>
[↯] 𝐒𝐭𝐫𝐞𝐞𝐭: <code>{street_number} {street_name}</code>                         
[↯] 𝐂𝐢𝐭𝐲: <code>{city}</code>
[↯] 𝐒𝐭𝐚𝐭𝐞: <code>{state}</code>
[↯] 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country}</code>
[↯] 𝐏𝐨𝐬𝐭𝐚𝐥 𝐂𝐨𝐝𝐞: <code>{postcode}</code>
[↯] 𝐏𝐡𝐨𝐧𝐞 𝐍𝐨.: <code>{phone}</code>
[↯] 𝐄𝐦𝐚𝐢𝐥: <code>{email}</code></b> [Inbox]
━━━━━━━━━━━━
[≹] 𝐓𝐢𝐦𝐞: 0.15 seconds
[⎇] 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://resolve?domain={user}">{name}</a> [Free user]
			"""
			bot.reply_to(message, formatted_address,parse_mode="HTML")
		except:
			bot.reply_to(message, "Country code not found or not available.")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗰𝗮𝗿𝗱𝘀...⌛",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)

@bot.message_handler(func=lambda message:True)
def main_bot(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.add(
       telebot.types.InlineKeyboardButton(
           '𝐒𝐭𝐚𝐫𝐬 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦', url='https://t.me/STARS_TELE_BASHA'
       )
   )
	num='0987654321'
	msg=message.text
	user=message.from_user.username
	user_id=message.from_user.id
	cd_2='/combo '
	if cd_2 in msg:
		try:
			os.mkdir('/storage/emulated/0/cc')
		except:pass
		msg=message.text
		len_bin=len(msg.split(cd_2)[1])
		bin=msg.split(cd_2)[1]
		len_card=16-len_bin
		comb=[]
		v=0
		month=['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12']
		year=['23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
		pp='combo-cc'
		path=random.choice(month)+random.choice(year)+random.choice(pp)+pp+'.txt'
		while True:
			mm=random.choice(month)
			yy=random.choice(year)
			cvv=str(''.join(random.choice(num)for i in range(3)))
			card=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
			comb.append(card)
			cwd = os.getcwd()
			os.chdir(r"/storage/emulated/0/cc")
			l = open(path,'a+')
			l.write(card+"\n")
			v+=1
			l.close()
			if v == 1000:
								time.sleep(6)
								os.chdir(r"/storage/emulated/0/cc")
								xx=open(path,'r')
								with open(path, 'r') as file:
									lines = 0
									for line in file:
									  lines += 1
								   
								bot.send_document(message.chat.id,xx,caption=f'<strong>𝗡𝗘𝗪  𝗖𝗢𝗠𝗕𝗢 🍁\n━━━━━━━━━━━━━━━━\n[↯] 𝗕𝗜𝗡  ⇾ {bin}\n[↯] 𝙏𝙊𝙏𝘼𝙇 ⇾{lines}\n━━━━━━━━━━━━━━━━\n[↯] 𝗨𝘀𝗲𝗿𝘀 ⇾ @aaka8h\n[↯] 𝗡𝗘𝗪⇾ [𝗙𝗥𝗘𝗘]\n━━━━━━━━━━━━━━━\n[↯] 𝗕𝗼𝘁 𝗕𝘆 <a href="tg://resolve?domain=aaka8h">ﺂﻟﹻٰۧﹷﻘﹻٰۧﹷﻧﹻٰۧﹷﺂص ۦٰ۪۫ﮮٰٰ۪۪۫۫ۦٰ۪۫ۦ</a></strong>',parse_mode='html')
								os.system(f'rm -rf {path}')
								break
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'	
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
