# Auhtor: Miranda Humphreys
# 11/11
# Welcome Page, 1st page brought up when opening the app
#1st Draft from Demo 1

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label

# Creates window and assigns the background color (white)
Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)

Config.set('graphics', 'resizable', True)

# Class for Welcome Page
class WelcomePage(App):

    def build(self):
        #Sets up the
        layout = BoxLayout(orientation="vertical", spacing=10, padding=40)
        #Adds title to the page
        titleLabel = Label(text="Covid Symptom Tracker", color=(0/255, 131/255, 97/255, 1), halign="center", font_size=(30))
        #Adds login and register buttons
        loginButton = Button(text="Login", color=(), background_normal='muchdarker.jpg', size_hint=(None, None),
                             width=100, height=50, pos_hint={"center_x": 0.5})
        registerButton = Button(text="Register", color=(), background_normal='muchdarker.jpg', size_hint=(None, None),
                                width=100, height=50, pos_hint={"center_x": 0.5})
        layout.add_widget(titleLabel)
        layout.add_widget(loginButton)
        layout.add_widget(registerButton)

        return layout
#Runs page
WelcomePage().run()
