#####################################################################
#                                                                   #
# This story was created by Cochise César <cochisecesar@gmail.com>  #
# and is under a Creative Commons Atribuition No-Commercial Share-  #
# Alike 3.0 unported (CC-BY-NC-SA).                                 #
# The images are under theis own, compatible, licenses as listed in #
# the LICENSE.md file.                                              #
#                                                                   #
# This novel uses Ren'py, what is licensed at MIT and LGPL license  #
# as you can see here: http://www.renpy.org/doc/html/license.html   #
#####################################################################

# Here we define the backgrounds that are used.
image bg report = "bgs/imigration.jpg"
image bg hospital = "bgs/hosp.png"
image bg lipa_room = "bgs/lipa_room.jpg"
image bg lake = "bgs/lake.jpg"
image bg infirmary = "bgs/infirmary.jpg"
image bg pub = "bgs/pub.jpg"
image bg white = "#ffffff"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define fsb = Character(None, kind=nvl, what_color="#000000")
define pavel = Character("Pavel")
define strange = Character("Stranger")
define lipa = Character("Lipa")
define nurse = Character("Nurse")

init python: # Language Config
    if persistent.lang is None:
        persistent.lang = "english"
        lang = persistent.lang
        config.main_menu.insert(3, (u'Language', "language_chooser", "True"))
        
label start: # The game starts here.
    init python: # Novel window 
        config.nvl_paged_rollback = True
        config.empty_window = nvl_show_core
        config.window_hide_transition = dissolve
        config.window_show_transition = dissolve
        style.nvl_window.background = "#ffffff00"
        style.nvl_window.ypadding = 220
    scene bg report
    fsb ""
    fsb "{font=resources/rough_typewriter.otf}
    Pavel and Marfa Romidelev, 24 and 25 pleading for subvencioned migration to Grózni, Tchetchénskaya Riespúblika.
    {/font}"
    fsb "{font=resources/rough_typewriter.otf}
    Newly degree at Staint Petesbugh State University in Oil Engineering and Mathematics, respectively. Booth without political hystory. Low earning families. Pavel father dead by hepatic cirrosis three years ago. No family savings.
    {/font}"
    fsb "{font=resources/rough_typewriter.otf}
    Interviews show only financial interset. Booth atheist, helping the politic for ethnic tension reduction.
    {/font}"
    fsb "{font=resources/rough_typewriter.otf}
    Subvencion approved for transport and habitation. Hability tests allow work position for Pavel. There is no position suitable for Marfa besides high theorical hability.
    {/font}"
    fsb "{font=resources/rough_typewriter.otf}
    Seymon Diadov, FSB
    {/font}"
    
label hospital:
    scene bg hospital
    strange "What are you doing here?"
    pavel "Maybe the same as you."
    strange "Who?"
    pavel "My wife."
    strange "She already..."
    pavel "Last night."
    strange "My sons. Both."
    "..."
    strange "You are blue. Are here since yesterday?"
    pavel "Yeah."
    strange "Take a cigarrete."
    pavel "Thanks. Mine are gone."
    strange "Will you really jump?"
    pavel "Don't know. And you?"
    strange "Come for this, but now? Don't know. Don't know if I can with you here."
    pavel "Same."
    strange "Maybe we should go to the chapel."
    pavel "SHUTUP!"
    strange "What?"
    pavel "Shut up! Stupid! There is no point! Does not exist!"
    strange "Release me! Are you mad?"
    pavel "There is no point... He don't listen..."
    strange "Don't cry, man. Here, take a draft."
    pavel "I'm... the damm whole day... he don't listen. Don't listen understood!?"
    strange "Came back!"

label lipa_room:
    scene bg lipa_room
    pavel "Snowed when the bomb exploded."
    lipa "Brings you bad memories?"
    pavel "Always."
    lipa "Then, why in hell came you here? Snow every damm day."
    pavel "Don't know, Lipa. Guess I don't want to forget."
    lipa "You already had someone since? Not like me, I mean."
    pavel "No. Sometimes..."
    lipa "Sometimes?"
    pavel "Forget this."
    lipa "Even if you pay me three times."
    pavel "I guess... I'm punishing-me."
    lipa "For what?"
    pavel "I wanted the Chechnya. The payment was the double. In my field."
    lipa "You know this is bullshit."
    pavel "I know."
    lipa "But feel nevertheless."
    pavel "Yeah..."
    
label lake:
    scene bg lake
    "The sun pretends to down at the frozen lake. It will linger hours to really reach the horizon. The image comes back"
    "Always comes back."
    "Lipa will not understand. Nobory will understand."
    "It's not pain, or hate, that can't throw in some god. The shame."
    "Between the chaos of victims and medics of the decadent hospital, was bagged, promissed all kind of nonsense."
    "Ronouced all dignity for Marfa. The guilt."
    "Like matryoshkas, a thing inside other. Olher people will be proud, but all that come was guilt."
    "Renounced everything for a ilusion. The impotence."
    "Couldn't save Marfa, but could save your diginity, your principles."
    "Impotent."
    "Ashamed of impotence."
    "Guilty."
    "Ashamed of guilt."
    "And no one but himself to hate."
    "Breat needles of cold."
    "Maybe, it's really a self punishment."
    "The dull light of sun comes red after cross the eyelids. "
    pavel "I sill wanting it wold have worked."
    "Some colder than ice down the spine. Eys open. All was here. All still was here. But not. Was more. And not was."
    "The wind crosses the whole world to reach your lungs. Breathed the air of millions of breaths, under the sun reached all the world."
    pavel "Marfa..."
    "She... was. Not like always. In everything. In nothing. Nothing really go away, but not stay. Not like was. All. One. But not a sum. None of them inteact, compartmented."
    pavel "Marfa, I..."
    "The sun, the sky, the wind, the snow. All in a motionless explosion."
    pavel "I forgive me."
    
label hospital_inside:
    scene bg infirmary
    pavel "Who?..."
    nurse "Finnaly you awake."
    pavel "I?..."
    nurse "Try don't strain yourself. You are at hospital. I'm the Nurse Radko. You was found almost frozen at the lake."
    nurse "You was sleeping for three days. Now, you are awake, I'm call the doctor."
    
label pub:
    scene bg pub
    define oleg = Character("Oleg")
    define fedot = Character("Fedot")
    define nikolai = Character("Nikolai")
    oleg "Cheers to the Ice Men!"
    fedot "What cheers? When he back to construction we will need to work!"
    pavel "I was worried about you too, Fedot."
    fedot "Woried? When you was taking your time as ice block I was keeping the chiks warm. You don't need to worry about me."
    nikolai "Speaking of heat, Lipa was walking around your bed to warm you."
    oleg "Ha! The Ice Men turn fire until in the whores of the city."
    pavel "She went to hospital?"
    nikolai "More times then you complain about my work."
    fedot "Then she never go out. Your service is worse then your face, Nikolai!"
    nikolai "But, how to die, boss? One bikini angel come to catch you?"
    pavel "Don't know. In fact... I think I saw my wife."
    "..."
    "......"
    pavel "I'm going home. See you at work tomorow, guys."
    
label credits:
    scene bg white
    nvl clear
    fsb "Writing:"
    fsb "Cochise César\n\n"
    fsb "Photos:"
    fsb "Hospital Roof View-2: Tim Suess http://www.flickr.com/photos/lord_yo/"
    fsb "One day later bedroom: Bolshakov http://www.flickr.com/photos/bolshakov/"
    nvl clear
    fsb "Cold: NapaneeGal http://www.flickr.com/photos/kingstongal/"
    fsb "Classic Hospital Room, Bright View for Moody Time: cobalt123 http://www.flickr.com/photos/cobalt/"
    fsb "Дума .aG http://www.flickr.com/photos/s7stem/"
    nvl clear
    return