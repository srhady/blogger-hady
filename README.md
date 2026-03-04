<div align="center">
  <h1 style="background-color: #008080; color: white; padding: 10px; border-radius: 10px;">
    🌙 কুরআনিক ইনসাইটস (Quranic Insights) - অটোমেটেড ইসলামিক ব্লগ বট
  </h1>
</div>

এই প্রজেক্টটি একটি পাইথন ভিত্তিক অটোমেশন সিস্টেম যা **Gemini AI** ব্যবহার করে প্রতিদিন স্বয়ংক্রিয়ভাবে মানসম্মত ইসলামিক ব্লগ পোস্ট জেনারেট করে এবং **Blogger** প্ল্যাটফর্মে পাবলিশ করে। এটি **GitHub Actions** ব্যবহার করে শিডিউল করা হয়েছে, ফলে আপনার ফোন বা কম্পিউটার বন্ধ থাকলেও এটি নিয়মিত পোস্ট করতে সক্ষম।

### ✨ বৈশিষ্ট্যসমূহ (Features)
* **AI চালিত কনটেন্ট:** Gemini 2.5 Flash মডেল ব্যবহার করে সম্পূর্ণ ইউনিক এবং শিক্ষণীয় পোস্ট তৈরি করা হয়।
* **বৈচিত্র্যময় ক্যাটাগরি:** মহাবিশ্ব, নবীদের জীবনী, বিজ্ঞান এবং ইসলামের ইতিহাসসহ ২৩টি ভিন্ন ভিন্ন ক্যাটাগরিতে পোস্ট জেনারেট হয়।
* **অটো-শিডিউলিং:** GitHub Actions-এর মাধ্যমে প্রতিদিন নির্দিষ্ট সময়ে অটোমেটিক পোস্ট পাবলিশ হয়।
* **ক্লিন ফরম্যাটিং:** ১৬px ফন্ট সাইজ এবং এইচটিএমএল (HTML) ট্যাগ ব্যবহার করে প্রফেশনাল লুক নিশ্চিত করা হয়েছে।
* **নির্ভরযোগ্য তথ্য:** প্রতিটি পোস্টে কোরআন ও হাদিসের রেফারেন্স এবং তাফসিরের সোর্স উল্লেখ করার নির্দেশনা দেওয়া আছে।

---

### 🛠️ সেটআপ গাইড (Setup Guide)

### ১. রিপোজিটরি তৈরি
ফাইলগুলো আপলোড করুন: `blogger_bot.py`, `requirements.txt` ও `.github/workflows/daily_post.yml`।

### ২. এনভায়রনমেন্ট ভেরিয়েবল সেটআপ (GitHub Secrets)
গিটহাবের **Settings > Secrets**-এ নিচের ৪টি তথ্য যোগ করুন:
`GEMINI_API_KEY`, `SENDER_EMAIL`, `SENDER_APP_PASSWORD`, `BLOGGER_EMAIL`।

---

<div align="center" style="background-color: #f0f0f0; padding: 20px; border-radius: 15px; border: 2px solid #008080;">
  <h2 style="color: #008080; margin-top: 0;">👤 Author: HADY</h2>
  <p><b>Project:</b> Quranic Insights Automation</p>
  <a href="https://quranicinsightsbd.blogspot.com">
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEi9ZcFiCf3Rt9j7gCu3FT-RmY0EYLx6vyfDClyuzyLh7p60yFKVI0JY7-MuoSIjNiBF6NKHX_9xHAltLos5TV4AtK9II_QpsYy3YVBVgz6fKKJNW-hE090AMCE3eSUOzqU-D1IexQRJyBgHoe7hjevVISTGPHkbBEnMWksNQKUfB81yRFD5jcT4dobZVeQU=s1408" width="150px" style="border-radius: 50%; border: 3px solid #008080;" alt="Quranic Insights Logo">
  </a>
  <br><br>
  <b>Visit Blog:</b> <a href="https://quranicinsightsbd.blogspot.com" style="color: #008080; text-decoration: none; font-weight: bold;">quranicinsightsbd.blogspot.com</a>
</div>

