
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from alphascript import Pusher
from settings import IPs, Paths
import subprocess

class HomePageLayout(GridLayout):
    def __init__(self,**kwargs):
        super(HomePageLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Nazwa użytkownika'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Dyktando'))
        self.dyktando = TextInput(multiline=True)
        self.add_widget(self.dyktando)

        
        self.submit = Button(text='Gotowe!', font_size = 32)
        self.submit.bind(on_press=self.activateScript)
        self.add_widget(self.submit)






    def activateScript(self, instance):
        validation = False
        name = self.username.text
        txt_to_send = self.dyktando.text

        if len(name) == 0:
            self.add_widget(Label(text="Podaj nazwę"))
        elif len(txt_to_send) == 0:
            self.add_widget(Label(text="Napisz dyktando"))
        else:
            push = Pusher(name, txt_to_send)
            push.pushToBravo()
            self.add_widget(Label(text="Dyktando przekazane"))

            self.show = Button(text="Pokaż wyniki",font_size = 32)
            self.show.bind(on_press=self.showSite)
            self.add_widget(self.show)


    def showSite(self,instance):
        self.add_widget(Label(text="Wyniki zostaną wyświetlone w przeglądarce internetowej"))
        bashCommand = 'firefox result/result.html'
        process = subprocess.Popen(bashCommand.split(), stdout = subprocess.PIPE)
        output, error = process.communicate()

class MyApp(App):
    def build(self):
        return HomePageLayout()

if __name__ == '__main__':
    MyApp().run()
