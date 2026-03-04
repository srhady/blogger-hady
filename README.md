# <kbd>🌙 কুরআনিক ইনসাইটস (Quranic Insights) - অটোমেটেড ইসলামিক ব্লগ বট</kbd>

এই প্রজেক্টটি একটি পাইথন ভিত্তিক অটোমেশন সিস্টেম যা **Gemini AI** ব্যবহার করে প্রতিদিন স্বয়ংক্রিয়ভাবে মানসম্মত ইসলামিক ব্লগ পোস্ট জেনারেট করে এবং **Blogger** প্ল্যাটফর্মে পাবলিশ করে। এটি **GitHub Actions** ব্যবহার করে শিডিউল করা হয়েছে, ফলে আপনার ফোন বা কম্পিউটার বন্ধ থাকলেও এটি নিয়মিত পোস্ট করতে সক্ষম।

### ✨ বৈশিষ্ট্যসমূহ (Features)
* **AI চালিত কনটেন্ট:** Gemini 2.5 Flash মডেল ব্যবহার করে সম্পূর্ণ ইউনিক এবং শিক্ষণীয় পোস্ট তৈরি করা হয়।
* **বৈচিত্র্যময় ক্যাটাগরি:** মহাবিশ্ব, নবীদের জীবনী, বিজ্ঞান এবং ইসলামের ইতিহাসসহ ২৩টি ভিন্ন ভিন্ন ক্যাটাগরিতে পোস্ট জেনারেট হয়।
* **অটো-শিডিউলিং:** GitHub Actions-এর মাধ্যমে প্রতিদিন নির্দিষ্ট সময়ে অটোমেটিক পোস্ট পাবলিশ হয়।
* **ক্লিন ফরম্যাটিং:** ১৬px ফন্ট সাইজ এবং এইচটিএমএল (HTML) ট্যাগ ব্যবহার করে প্রফেশনাল লুক নিশ্চিত করা হয়েছে।
* **নির্ভরযোগ্য তথ্য:** প্রতিটি পোস্টে কোরআন ও হাদিসের রেফারেন্স এবং তাফসিরের সোর্স উল্লেখ করার নির্দেশনা দেওয়া আছে।

### 🛠️ সেটআপ গাইড (Setup Guide)

### ১. রিপোজিটরি তৈরি
প্রথমে গিটহাবে একটি নতুন রিপোজিটরি তৈরি করুন এবং `blogger_bot.py`, `requirements.txt` ও `.github/workflows/daily_post.yml` ফাইলগুলো আপলোড করুন।

### ২. এনভায়রনমেন্ট ভেরিয়েবল সেটআপ (GitHub Secrets)
আপনার রিপোজিটরির **Settings > Secrets and variables > Actions**-এ গিয়ে নিচের ৪টি Secret যোগ করুন:

| Secret Name | Description |
|---|---|
| `GEMINI_API_KEY` | আপনার Gemini AI-এর API Key |
| `SENDER_EMAIL` | যে জিমেইল থেকে পোস্ট পাঠানো হবে () |
| `SENDER_APP_PASSWORD` | জিমেইল এর ১৬ ডিজিটের App Password () |
| `BLOGGER_EMAIL` | আপনার ব্লগের নির্দিষ্ট পোস্টিং ইমেইল () |

### ৩. সময় পরিবর্তন (Optional)
প্রতিদিন কখন পোস্ট হবে তা পরিবর্তন করতে চাইলে `.github/workflows/daily_post.yml` ফাইলের `cron` টাইম পরিবর্তন করুন। বর্তমানে এটি বাংলাদেশ সময় সকাল ৯টায় (UTC 3:00) সেট করা আছে।

### 🚀 যেভাবে কাজ করে
১. GitHub Actions প্রতিদিন নির্দিষ্ট সময়ে পাইথন স্ক্রিপ্টটি রান করে।
২. স্ক্রিপ্টটি র্যান্ডমলি একটি ক্যাটাগরি সিলেক্ট করে Gemini AI-কে প্রম্পট পাঠায়।
৩. Gemini AI একটি চমৎকার পোস্ট লিখে দেয়।
৪. পাইথন স্ক্রিপ্টটি সেই পোস্টটি ইমেইলের মাধ্যমে সরাসরি আপনার ব্লগারে পাবলিশ করে দেয়।

---
---
### 👤 <kbd>Author: HADY</kbd>
**Project:** Quranic Insights Automation

<div align="center">
  <a href="https://quranicinsightsbd.blogspot.com">
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEi9ZcFiCf3Rt9j7gCu3FT-RmY0EYLx6vyfDClyuzyLh7p60yFKVI0JY7-MuoSIjNiBF6NKHX_9xHAltLos5TV4AtK9II_QpsYy3YVBVgz6fKKJNW-hE090AMCE3eSUOzqU-D1IexQRJyBgHoe7hjevVISTGPHkbBEnMWksNQKUfB81yRFD5jcT4dobZVeQU=s1408" width="150px" style="border-radius: 50%; border: 2px solid #008080;" alt="Quranic Insights Logo">
  </a>
  <br>
  <b>Visit Blog:</b> <a href="https://quranicinsightsbd.blogspot.com">quranicinsightsbd.blogspot.com</a>
</div>

