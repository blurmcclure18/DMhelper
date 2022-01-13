from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from nameDict import namesDict
from random import randint
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    HomeScreen
    NPCScreen
    GeneratedNPC
    
<HomeScreen>
    name: 'home'
    MDLabel:
        id: chooseOption
        text: "Choose An Option"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243,160,81,1
    
    MDRaisedButton
        id: generateCharName
        text: "Generate NPC"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press:
            root.generateNPCScreen()


<NPCScreen>
    name: 'npcScreen'

    MDLabel:
        id: generateNPC
        text: "Select NPC Race"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243,160,81,1
    
    MDRaisedButton
        id: generateCharName
        text: "Dwarf"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press:
            root.generateNPCRace('dwarf')

    MDFillRoundFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            app.goHome()

<GeneratedNPC>
    name: 'generatedNPC'

    MDLabel:
        id: generatedNPC
        text: "Your NPC"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H2'
        theme_text_color: "Custom"
        text_color: 243,160,81,1

    MDFillRoundFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            app.goHome()
    

"""

# Create Screen classes (build logic functions for each screen in their class)
class HomeScreen(Screen):
    def generateNPCScreen(self):
        MDApp.get_running_app().root.current = 'npcScreen'

class NPCScreen(Screen):
    def generateNPCRace(self,race):
        if race == 'dwarf':
            firstName = str(namesDict['dwarfNames'][0][randint(0,len(namesDict['dwarfNames'][0]))] + namesDict['dwarfNames'][1][randint(0,len(namesDict['dwarfNames'][1]))])
            lastName = str(namesDict['dwarfNames'][4][randint(0,len(namesDict['dwarfNames'][4]))] + namesDict['dwarfNames'][5][randint(0,len(namesDict['dwarfNames'][5]))])
            name = firstName + ' ' + lastName
            print(name)
        MDApp.get_running_app().root.current = 'generatedNPC'

class GeneratedNPC(Screen):
    pass

# Create App class to build and run
class DMhelperApp(MDApp):
    def goHome(self):
        MDApp.get_running_app().root.current = 'home'
    
    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = 'Dark'
        return screen
    

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(NPCScreen(name='npcScreen'))
sm.add_widget(GeneratedNPC(name='generatedNPC'))

if __name__ == '__main__':
    DMhelperApp().run()