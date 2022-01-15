from kivymd.app import MDApp
from nameDict import namesDict
from tavernsDict import tavernNames
from helper import screen_helper
from wildMagicDict import wildMagic
from random import randint
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create Screen classes (build logic functions for each screen in their class)
class HomeScreen(Screen):
    def generateNPCScreen(self):
        MDApp.get_running_app().root.current = 'genderSelectNPC'
    
    def generateTavern(self):
        tavernName = str(tavernNames[0][randint(0,len(tavernNames[0])-1)] + " " + tavernNames[1][randint(0,len(tavernNames[1])-1)] +" " + tavernNames[2][randint(0,len(tavernNames[2])-1)])
        self.manager.get_screen('generatedTavern').ids.generatedTavernName.text = tavernName
        MDApp.get_running_app().root.current = 'generatedTavern'
    
    def wildMagicScreen(self):
        MDApp.get_running_app().root.current = 'wildmagic'


class GenderSelectNPC(Screen):
    global gender
    gender = ''

    def selectGender(self,selection):
        global gender
        gender = selection
        MDApp.get_running_app().root.current = 'npcScreen'
class NPCScreen(Screen):

    def generateRandomNPC(self):
        race = ['Dwarf','Elf','Gnome','Goliath','Half-Elf','Half-Orc','Halfling','Tiefling','Human']
        randomRace = race[randint(0,len(race) - 1)]
        self.generateNPC(randomRace)

    def generateNPC(self,race):
        global gender
        if race == 'Dwarf':
            firstName = str(namesDict['dwarfNames'][gender][0][randint(0,len(namesDict['dwarfNames'][gender][0])-1)] + namesDict['dwarfNames'][gender][1][randint(0,len(namesDict['dwarfNames'][gender][1])-1)])
            lastName = str(namesDict['dwarfNames']['Last'][0][randint(0,len(namesDict['dwarfNames']['Last'][0])-1)] + namesDict['dwarfNames']['Last'][1][randint(0,len(namesDict['dwarfNames']['Last'][1])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Elf':
            firstName = str(namesDict['elfNames'][gender][0][randint(0,len(namesDict['elfNames'][gender][0])-1)])
            lastName = str(namesDict['elfNames']['Last'][0][randint(0,len(namesDict['elfNames']['Last'][0])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
            
        elif race == 'Gnome':
            firstName = str(namesDict['gnomeNames'][gender][0][randint(0,len(namesDict['gnomeNames'][gender][0])-1)] + namesDict['gnomeNames'][gender][1][randint(0,len(namesDict['gnomeNames'][gender][1])-1)])
            lastName = str(namesDict['gnomeNames']['Last'][0][randint(0,len(namesDict['gnomeNames']['Last'][0])-1)] + namesDict['gnomeNames']['Last'][1][randint(0,len(namesDict['gnomeNames']['Last'][1])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Goliath':
            firstName = str(namesDict['goliathNames'][gender][0][randint(0,len(namesDict['goliathNames'][gender][0])-1)] + namesDict['goliathNames'][gender][1][randint(0,len(namesDict['goliathNames'][gender][1]))])
            lastName = str(namesDict['goliathNames']['Last'][0][randint(0,len(namesDict['goliathNames']['Last'][0])-1)] + namesDict['goliathNames']['Last'][1][randint(0,len(namesDict['goliathNames']['Last'][1])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Half-Elf':
            firstName = str(namesDict['halfElfNames'][gender][0][randint(0,len(namesDict['halfElfNames'][gender][0])-1)] + namesDict['halfElfNames'][gender][1][randint(0,len(namesDict['halfElfNames'][gender][1])-1)])
            lastVar = randint(0,1)
            if lastVar == 0:
                lastName = str(namesDict['halfElfNames']['Last'][0][randint(0,len(namesDict['halfElfNames']['Last'][0])-1)])
            else:
                lastName = str(namesDict['halfElfNames']['Last'][1][randint(0,len(namesDict['halfElfNames']['Last'][1])-1)] + namesDict['halfElfNames']['Last'][2][randint(0,len(namesDict['halfElfNames']['Last'][2])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Half-Orc':
            firstName = str(namesDict['halfOrcNames'][gender][0][randint(0,len(namesDict['halfOrcNames'][gender][0])-1)] + namesDict['halfOrcNames'][gender][1][randint(0,len(namesDict['halfOrcNames'][gender][1])-1)])
            name = str(firstName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Halfling':
            firstName = str(namesDict['halflingNames'][gender][0][randint(0,len(namesDict['halflingNames'][gender][0])-1)] + namesDict['halflingNames'][gender][1][randint(0,len(namesDict['halflingNames'][gender][1])-1)])
            lastName = str(namesDict['halflingNames']['Last'][0][randint(0,len(namesDict['halflingNames']['Last'][0])-1)] + namesDict['halflingNames']['Last'][1][randint(0,len(namesDict['halflingNames']['Last'][1])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Tiefling':
            firstName = str(namesDict['tieflingNames'][gender][0][randint(0,len(namesDict['tieflingNames'][gender][0])-1)] + namesDict['tieflingNames'][gender][1][randint(0,len(namesDict['tieflingNames'][gender][1])-1)])
            name = str(firstName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name
        elif race == 'Human':
            firstName = str(namesDict['humanNames'][gender][0][randint(0,len(namesDict['humanNames'][gender][0])-1)])
            lastName = str(namesDict['humanNames']['Last'][0][randint(0,len(namesDict['humanNames']['Last'][0])-1)] + namesDict['humanNames']['Last'][1][randint(0,len(namesDict['humanNames']['Last'][1])-1)])
            name = str(firstName + ' ' + lastName).title()
            self.manager.get_screen('generatedNPC').ids.generatedNPC.text = name            
        else:
            pass

        self.manager.get_screen('generatedNPC').ids.raceNPC.text = f"Race: {race}"
        self.manager.get_screen('generatedNPC').ids.genderNPC.text = f"Gender: {gender}"

        MDApp.get_running_app().root.current = 'generatedNPC'
class GeneratedNPC(Screen):
    pass

class GeneratedTavern(Screen):
    pass

class WildMagic(Screen):
    def searchWildMagic(self):
        input = round(int(self.manager.get_screen('wildmagic').ids.rollInput.text))

        roll = int(input / 2)

        description = wildMagic[roll]

        self.manager.get_screen('wildmagicdescription').ids.wildmagicdescription.text = description

        MDApp.get_running_app().root.current = 'wildmagicdescription'
    
    def rollWildMagic(self):
        roll = round(randint(1,100) / 2)

        description = wildMagic[roll]

        self.manager.get_screen('wildmagicdescription').ids.wildmagicdescription.text = description

        MDApp.get_running_app().root.current = 'wildmagicdescription'

class WildMagicDescription(Screen):
    pass

# Create App class to build and run
class DMhelperApp(MDApp):
    def goHome(self):
        MDApp.get_running_app().root.current = 'home'
    
    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = 'Dark'
        return screen
    

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(NPCScreen(name='npcScreen'))
sm.add_widget(GenderSelectNPC(name='genderSelectNPC'))
sm.add_widget(GeneratedNPC(name='generatedNPC'))
sm.add_widget(GeneratedTavern(name='generatedTavern'))
sm.add_widget(WildMagic(name='wildmagic'))
sm.add_widget(WildMagicDescription(name='wildmagicdescription'))

if __name__ == '__main__':
    DMhelperApp().run()