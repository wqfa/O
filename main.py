import telebot
import requests
import json
from telebot import types
Owner = '5136116009'
User_Ch = 'fadouabac2024'
headers = {
     'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
     'Connection': 'keep-alive',
     'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
     'Accept': '*/*',
     'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
     'Content-Type': 'application/json',
     'Accept-Language': 'en-GB,en;q=0.9'}
Your_Bot = "5768629238:AAEkGrNPIWlJJqReIy0aUEqYJA68LuHqiUU"
bot = telebot.TeleBot(Your_Bot)

@bot.message_handler(commands=['start'])
def start(message):
    Id_Member = message.from_user.id
    Check_Member = requests.get(f"https://api.telegram.org/bot{Your_Bot}/getchatmember?chat_id=@{User_Ch}&user_id={Id_Member}").text
    
    if Id_Member == Owner or "member" in Check_Member or "creator" in Check_Member or "administrator" in Check_Member:
    	keyboard = types.InlineKeyboardMarkup(row_width=2)
    	button1= types.InlineKeyboardButton("( الرياضيات )", callback_data="math")
    	button2= types.InlineKeyboardButton("( فلسفة )", callback_data="phel")
    	button3 = types.InlineKeyboardButton("( الإجابة عن أي سؤال )", callback_data="ask")
    	button4= types.InlineKeyboardButton("( إختبر نفسك )", callback_data="kss")
    	button5= types.InlineKeyboardButton("( اللغات )", callback_data="lang")
    	keyboard.add(button1, button2, button5,button3,button4)
    	bot.reply_to(message,'''- مرحبا بك في بوت BAC 2024

- البوت يساعدك على الإجابة على جميع الأسئلة التي تريدها

- المبرمج : @WHI3PER

- إختر ما تريد من الخيارات التالية''', reply_markup=keyboard)

    else:
    	For_Channel =types.InlineKeyboardMarkup()
    	CH= types.InlineKeyboardButton('قناة البوت ❕',url="t.me/"+str(User_Ch))
    	For_Channel.add(CH)
    	bot.reply_to(message,
'''🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه''',reply_markup=For_Channel)
    	

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == "kss":
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- إختبر نفسك عبر الإجابة عن الأسئلة العشوائية

- أرسل موضوع السؤال''',reply_markup=B)
        bot.register_next_step_handler(call.message,kss)
        
    elif call.data == "ask":
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- الإجابة الفورية عن جميع الأسئلة

- أرسل السؤال لتتم الإجابة عليه''',reply_markup=B)
        bot.register_next_step_handler(call.message,all)
        
    elif call.data == "lang":
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- ترجمة و إنشاء وضعيات حسب الطلب

- إذا كنت تريد ترجمة جملة أرسل "ترجمة (الكلمة/الجملة) الى (اللغة التي تريدها)"

- إذا كنت تريد مني كتابة وضعية لك أكتب "أكتب لي وضعية عن (الموضوع) باللغة (اللغة التي تريد)"

- أرسل ما تريد هنا''',reply_markup=B)
        bot.register_next_step_handler(call.message,lang)
     
    elif call.data == 'Back':
        
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button1= types.InlineKeyboardButton("( الرياضيات )", callback_data="math")
        button2= types.InlineKeyboardButton("( فلسفة )", callback_data="phel")
        button3 = types.InlineKeyboardButton("( الإجابة عن أي سؤال )", callback_data="ask")
        button4= types.InlineKeyboardButton("( إختبر نفسك )", callback_data="kss")
        button5= types.InlineKeyboardButton("( اللغات )", callback_data="lang")
        keyboard.add(button1, button2, button5,button3,button4)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text='''- مرحبا بك في بوت BAC 2024

- البوت يساعدك على الإجابة على جميع الأسئلة التي تريدها

- المبرمج : @WHI3PER

- إختر ما تريد من الخيارات التالية''', reply_markup=keyboard)
     
    elif call.data == "phel":
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- المادة : فلسفة
        
- أرسل موضوع المقالة التي تريدها''',reply_markup=B)
        bot.register_next_step_handler(call.message,phel)
    elif call.data == "math":
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''- المادة : رياضيات

- أرسل العملية التي تريد حلها''',reply_markup=B)
        bot.register_next_step_handler(call.message,math)
        
def math(message):
    text = message.text
    url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    data = {'data': {'message': f'أريد حل {text} مع شرح طريقة الحل'}}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.send_message(message.chat.id, result,reply_markup=B)
    except:
        bot.send_message(message.chat.id, "لم أفهم السؤال")


def phel(message):
    text = message.text
    url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    data = {'data': {'message': f'أكتب لي مقالا فلسفيا عن {text} مع الاستدلال بأقوال الفلاسفة'}}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.send_message(message.chat.id, result,reply_markup=B)
    except:
        bot.send_message(message.chat.id, "لم أفهم السؤال")
        
def kss(message):
    text = message.text
    url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    data = {'data': {'message': f'إطرح علي سؤال عن {text} دون إجابتي'}}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.send_message(message.chat.id, result,reply_markup=B)
    except:
        bot.send_message(message.chat.id, "لم أفهم السؤال")
        
def all(message):
    text = message.text
    url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    data = {'data': {'message':text}}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.send_message(message.chat.id, result,reply_markup=B)
    except:
        bot.send_message(message.chat.id, "لم أفهم السؤال")
        
def lang(message):
    text = message.text
    url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    data = {'data': {'message':text}}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        B = types.InlineKeyboardMarkup()
        Back = types.InlineKeyboardButton("( رجوع )", callback_data="Back")
        B.add(Back)
        bot.send_message(message.chat.id, result,reply_markup=B)
    except:
        bot.send_message(message.chat.id, "لم أفهم السؤال")
        
bot.polling()
