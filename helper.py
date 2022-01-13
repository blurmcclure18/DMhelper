screen_helper = """
ScreenManager:
    HomeScreen
    NPCScreen
    GenderSelectNPC
    GeneratedNPC
    
<HomeScreen>
    name: 'home'
    MDLabel:
        id: chooseOption
        text: "Choose An Option"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H2'
    
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

    MDRaisedButton
        id: generateDwarf
        text: "Dwarf"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.70}
        on_press:
            root.generateNPC('Dwarf')
    
    MDRaisedButton
        id: generateElf
        text: "Elf"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.65}
        on_press:
            root.generateNPC('Elf')
    
    MDRaisedButton
        id: generateHuman
        text: "Human"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.60}
        on_press:
            root.generateNPC('Human')
    
    MDRaisedButton
        id: generateGnome
        text: "Gnome"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        on_press:
            root.generateNPC('Gnome')
    
    MDRaisedButton
        id: generateGoliath
        text: "Goliath"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.50}
        on_press:
            root.generateNPC('Goliath')
    
    MDRaisedButton
        id: generateHalfElf
        text: "Half-Elf"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.45}
        on_press:
            root.generateNPC('Half-Elf')

    MDRaisedButton
        id: generateHalfOrc
        text: "Half-Orc"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.40}
        on_press:
            root.generateNPC('Half-Orc')

    MDRaisedButton
        id: generateHalfling
        text: "Halfling"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.35}
        on_press:
            root.generateNPC('Halfling')

    MDRaisedButton
        id: generateTiefling
        text: "Tiefling"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.30}
        on_press:
            root.generateNPC('Tiefling')

    MDRaisedButton
        id: generateRandom
        text: "Random"
        spacing: '15sp'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
        on_press:
            root.generateRandomNPC()

    MDFillRoundFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            app.goHome()

<GenderSelectNPC>
    name: 'genderSelectNPC'

    MDLabel:
        id: generatedNPC
        text: "Select A Gender"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H2'

    MDRaisedButton
        id: genderMale
        text: "Male"
        pos_hint: {'center_x':0.4, 'center_y':0.5}
        on_press:
            root.selectGender('Male')
    
    MDRaisedButton
        id: genderFemale
        text: "Female"
        pos_hint: {'center_x':0.6, 'center_y':0.5}
        on_press:
            root.selectGender('Female')

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
    
    MDLabel:
        id: raceNPC
        text: "NPC Race"
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'H3'

    MDLabel:
        id: genderNPC
        text: "NPC Gender"
        halign: 'center'
        pos_hint: {'center_y':0.7}
        font_style: 'H3'
    
    MDFillRoundFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            app.goHome()

    MDFillRoundFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            app.goHome()
    

"""
