#Author: John Miego
#Date: 11/13/2020
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window



Window.size = (300, 500)
end = """
ScreenManager:
    HomeScreen:
    Question1Screen:
    Question2Screen:
    Question3Screen:
    Question4Screen:
    InfoScreen:

<HomeScreen>:
    name: "home"
    Image:
        source: "covidshield.png"
        size_hint_y: None
        height: 620
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {"center_x":0.5, "center_y":0.30}

    MDRectangleFlatButton:
        text: 'Register'
        pos_hint: {"center_x":0.5, "center_y":0.21}

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Symptom Tracker'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Calendar"
                            IconLeftWidget:
                                icon: "calendar-week"
                        OneLineIconListItem:
                            text: "Start Survey"
                            IconLeftWidget:
                                icon: "note-text"
                                on_press: root.manager.current = "Question1"
                        OneLineIconListItem:
                            text: "Testing"
                            IconLeftWidget:
                                icon: "web"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout-variant"

<Question1Screen>:
    name: "Question1"
    MDToolbar:
        title: 'Question 1'
        elevation:10
        pos_hint: {"top": 1}
    MDLabel:
        text: "Have you been exposed to COVID-19 in the last 14 days?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: root.manager.current = "Question2"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: root.manager.current = "Question2"
    
<Question2Screen>:
    name: "Question2"
    MDToolbar:
        title: 'Question 2'
        elevation:10
        pos_hint: {"top": 1}
    MDLabel:
        text: "Have you had any of the following Symptoms(1): Dry Cough, Sore Throat, or Fever?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: root.manager.current = "Question3"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: root.manager.current = "Question3"

<Question3Screen>:
    name: "Question3"
    MDToolbar:
        title: 'Question 3'
        elevation:10
        pos_hint: {"top": 1}
    MDLabel:
        text: "Have you had any of the following Symptoms(2): Shortness of breath, trouble breathing, loss sense of smell?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: root.manager.current = "Question4"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: root.manager.current = "Question4"


<Question4Screen>:
    name: "Question4"
    MDToolbar:
        title: 'Question 4'
        elevation:10
        pos_hint: {"top": 1}
    MDLabel:
        text: "Have you tested for COVID-19 in the last 14 days?"
        halign: "center"
        theme_text_color: "Custom"
        text_color: (66 / 255, 158 / 255, 157 / 255, 1)
        font_style: "Body1"
        font_size: "15sp"
    MDRectangleFlatButton
        text: "Yes"
        pos_hint: {"center_x":0.3,"center_y":0.4}
        on_press: root.manager.current = "info"
    MDRectangleFlatButton
        text: "No"
        pos_hint: {"center_x":0.7,"center_y":0.4}
        on_press: root.manager.current = "info"  
          
<InfoScreen>:   
    name: "info" 
    MDRectangleFlatButton:
        text: "Location"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRectangleFlatButton:
        text: "Contact"
        pos_hint: {"center_x": .5, "center_y": .4}     
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Testing Info'
                        left_action_items: [["dots-vertical", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    
                    
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Home"
                            IconLeftWidget:
                                icon: "home"
                                on_press: root.manager.current = "home"
                        OneLineIconListItem:
                            text: "Calendar"
                            IconLeftWidget:
                                icon: "calendar-week"
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
            
"""


class HomeScreen(Screen):
    pass


class Question1Screen(Screen):
    pass


class Question2Screen(Screen):
    pass


class Question3Screen(Screen):
    pass


class Question4Screen(Screen):
    pass


class InfoScreen(Screen):
    pass





class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        screen = Builder.load_string(end)

        return screen


DemoApp().run()
