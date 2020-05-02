from kivy.app import App
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest

class TestApp(App):
    def build(self):
        button = Button(text='Hello from Kivy')
                        
        button.bind(on_press=self.on_press_button)
 
        return button

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')
        f = open("test.txt", "w")
        f.write("hello")
        

TestApp().run()