import requests
import random
import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD")
BLOGGER_EMAIL = os.getenv("BLOGGER_EMAIL")

# Telegram Credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

categories = [
    "মহাবিশ্ব, সৃষ্টিতত্ত্ব এবং জ্যোতির্বিজ্ঞান",
    "কোরআনে বর্ণিত নবী-রাসূলদের ঐতিহাসিক ঘটনা ও শিক্ষা",
    "মানব সৃষ্টি, ভ্রূণতত্ত্ব এবং জীববিজ্ঞান",
    "প্রাচীন ধ্বংসপ্রাপ্ত জাতিসমূহ এবং তাদের প্রত্নতাত্ত্বিক প্রমাণ",
    "প্রকৃতি, পর্বত এবং সমুদ্রবিজ্ঞান",
    "কোরআনের নির্দিষ্ট আয়াতের শানে নুযুল এবং ঐতিহাসিক প্রেক্ষাপট",
    "হাদিসের আলোকে স্বাস্থ্যবিজ্ঞান ও চিকিৎসাবিজ্ঞান",
    "রাসূল (সাঃ) ও সাহাবীদের জীবনের শিক্ষণীয় ঘটনা",
    "কিয়ামত, পরকাল এবং জান্নাত-জাহান্নামের বর্ণনা",
    "ফেরেশতা এবং জ্বীন জাতির রহস্য ও কোরআনের ব্যাখ্যা",
    "ইসলামী আখলাক, উত্তম চরিত্র এবং মানবিক মূল্যবোধ",
    "কোরআনে বর্ণিত নারী চরিত্র এবং তাদের শিক্ষণীয় অবদান",
    "দৈনন্দিন জীবনে রাসূল (সাঃ) এর সুন্নাহ এবং এর বৈজ্ঞানিক উপকারিতা",
    "ইবাদতের (নামাজ, রোজা, জাকাত, হজ) দার্শনিক ও বৈজ্ঞানিক তাৎপর্য"
]

def send_telegram_msg(title):
    try:
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            print("Telegram credentials missing!")
            return
            
        message = f"✅ <b>নতুন পোস্ট পাবলিশ হয়েছে!</b>\n\n📌 <b>টাইটেল:</b> {title}\n\n🌐 <a href='https://quranicinsightsbd.blogspot.com'>ব্লগে গিয়ে পড়ুন</a>"
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, json=payload)
        print("✅ টেলিগ্রামে মেসেজ পাঠানো হয়েছে!")
    except Exception as e:
        print(f"❌ Telegram Error: {str(e)}")

def post_to_blogger(title, content):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = BLOGGER_EMAIL
        msg['Subject'] = title
        msg.attach(MIMEText(content, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, BLOGGER_EMAIL, msg.as_string())
        server.quit()
        print(f"✅ পোস্ট সফল: {title}")
        
        # ব্লগারে পোস্ট সফল হলে টেলিগ্রামে মেসেজ পাঠাবে
        send_telegram_msg(title)
        
    except Exception as e:
        print(f"❌ Blogger Error: {str(e)}")

def generate_and_post():
    random.seed(time.time_ns())
    category = random.choice(categories)
    seed = random.randint(1, 999999) 
    
    prompt = f"""
    তুমি একজন বিজ্ঞ ইসলামিক স্কলার। আমি তোমাকে একটি ক্যাটাগরি দিচ্ছি: '{category}'। 
    এই বিষয়ের ওপর ভিত্তি করে সম্পূর্ণ নতুন ও শিক্ষণীয় একটি নির্দিষ্ট টপিক নির্বাচন করো (Random Seed: {seed}) এবং টেলিগ্রাম চ্যানেলের জন্য বাংলায় একটি চমৎকার পোস্ট লেখো।
    
    সহজ কিছু নিয়ম মেনে চলবে:
    ১. আকার ও গঠন: লেখাটি ৪০০ শব্দের মধ্যে রাখবে। শুরুতে একটি সুন্দর শিরোনাম বোল্ড করে দেবে। কোনো সাব-হেডিং বা পয়েন্ট দেওয়ার দরকার নেই, ২-৩টি প্যারায় সাবলীলভাবে লিখবে। প্রতিটি প্যারার শেষে লাইন ব্রেকের জন্য <br><br> ট্যাগ ব্যবহার করবে।
    ২. ফরম্যাটিং: লেখায় কোনো মার্কডাউন (যেমন ** বা #) ব্যবহার করবে না। লেখাকে বোল্ড করতে চাইলে <b>লেখা</b> এবং ইটালিক করতে চাইলে <i>লেখা</i> ট্যাগ ব্যবহার করবে। 
    ৩. কোরআন: কোরআনের রেফারেন্স দিলে প্রথমে <br><br> ট্যাগ দিয়ে তারপর আরবি আয়াতটি (হরকতসহ) লিখবে। এরপর <br><br> ট্যাগ দিয়ে আয়াতের বাংলা অর্থটি <blockquote><i>অর্থ...</i></blockquote> এই ট্যাগে লিখবে। অর্থের নিচেই অবশ্যই <b>(সূরা: নাম, আয়াত: নম্বর)</b> উল্লেখ করবে এবং এর ঠিক নিচে <br><br> ট্যাগ দিয়ে পরবর্তী লেখা শুরু করবে।
    ৪. তাফসির: আয়াতের ব্যাখ্যার জন্য 'তাফসিরে ইবনে কাসীর' বা নির্ভরযোগ্য তাফসিরের রেফারেন্স উল্লেখ করবে।
    ৫. হাদিস: হাদিস ব্যবহার করলে প্রথমে <br><br> ট্যাগ দিয়ে তারপর <blockquote><i>হাদিসের অর্থ...</i></blockquote> এই ট্যাগের ভেতরে লিখবে। নিচেই অবশ্যই <b>(সূত্র: হাদিস গ্রন্থের নাম ও নম্বর)</b> উল্লেখ করবে এবং এর ঠিক নিচে <br><br> ট্যাগ দিয়ে পরবর্তী লেখা শুরু করবে।
    ৬. বিষয়বস্তু: বিজ্ঞান সম্পর্কিত বিষয় হলে আধুনিক বিজ্ঞানের সাথে কোরআনের মিল তুলে ধরবে। আর ইতিহাস বা নবীদের ঘটনা হলে বিজ্ঞানের দরকার নেই, শুধু ঐতিহাসিক প্রেক্ষাপট ও তাফসির নিয়ে লিখবে।
    """
    
    try:
        response = requests.post(GEMINI_URL, json={"contents": [{"parts": [{"text": prompt}]}]})
        data = response.json()
        raw_text = data['candidates'][0]['content']['parts'][0]['text']
        clean_text = raw_text.replace('```html', '').replace('```', '').strip()
        
        lines = clean_text.split('\n')
        # টাইটেল থেকে অপ্রয়োজনীয় ট্যাগ রিমুভ করা হয়েছে
        title = lines[0].replace('<b>', '').replace('</b>', '').replace('<p>', '').replace('</p>', '').replace('<h1>', '').replace('</h1>', '').replace('<br>', '').strip()

        formatted_post = f'<div style="font-size: 16px;">{post_text}</div>'
        post_to_blogger(title, formatted_post)
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == '__main__':
    generate_and_post()
