[app]

# عنوان التطبيق واسمه
title = XO Game
package.name = xogame
package.domain = org.ali

# الملفات المراد تضمينها
source.include_exts = py,png,jpg,kv,atlas,ttf,json,txt

# الملف الرئيسي لتطبيقك
source.main = main.py

# الإصدار والتنظيم
version = 0.1
requirements = python3,pygame,ursina

# إذن الإنترنت والأجهزة (حسب الحاجة)
android.permissions = INTERNET

# توجهات الشاشة
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
