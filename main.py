from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import socket

class ParentControlApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.status = Label(text="جهاز التحكم: جاهز", font_size='20sp')
        layout.add_widget(self.status)
        
        btn = Button(text="إرسال أمر (نقرة)", size_hint=(1, 0.4), background_color=(0.1, 0.6, 0.1, 1))
        btn.bind(on_press=self.send_command)
        layout.add_widget(btn)
        return layout

    def send_command(self, instance):
        target_ip = "192.168.1.10" # عنوان IP هاتف الابن
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((target_ip, 9999))
                s.sendall("500,1000\n".encode())
                self.status.text = "تم الإرسال بنجاح ✅"
        except:
            self.status.text = "فشل الاتصال ❌"

if __name__ == "__main__":
    ParentControlApp().run()
  

