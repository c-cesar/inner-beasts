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
#                                                                   #
#####################################################################

# Here we define the backgrounds that are used.
image bg report = "bgs/imigration.jpg"
image bg hospital = "bgs/hosp.png"
image bg lipa_room = "bgs/lipa_room.jpg"
image bg lake = "bgs/lake.jpg"
image bg infirmary = "bgs/infirmary.jpg"
image bg pub = "bgs/pub.jpg"
image bg snow_street = "bgs/snow_street.jpg"
image bg snow_street_back = "bgs/snow_street_back.jpg"
image bg factory_skyline = "bgs/factory_skyline.jpg"
image bg inner_hospital = "bgs/inner_hospital.jpg"
image bg pavel_office = "bgs/mesa_placeholder.jpg"
image bg white = "#ffffff"

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define fsb = Character(None, kind=nvl, what_color="#000000")
define pavel = Character("Pavel")
define strange = Character("Stranger")
define lipa = Character("Lipa")
define uchastkovyi = Character("Uchastkovyi Vasilii")
# NPCs
define nurse = Character("Nurse")
define paramedic = Character("Paramedic")
# Workers
define oleg = Character("Oleg")
define fedot = Character("Fedot")
define nikolai = Character("Nikolai")

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
    strange "Take a cigarette."
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
    pavel "I'm... the damn whole day... he don't listen. Don't listen understood!?"
    strange "Came back!"
    
label lipa_room:
    scene bg lipa_room
    pavel "Snowed when the bomb exploded."
    lipa "Brings you bad memories?"
    pavel "Always."
    lipa "Then, why in hell come you here? Snow every damn day."
    pavel "I don't know, Lipa. I guess... I don't want to forget."
    lipa "You already had someone since?... Not like me, I mean."
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
    "The sun pretends to down at the frozen lake. It will linger for hours before to really reach the horizon. The image comes back."
    "Always comes back."
    "Lipa will not understand. Nobody will understand."
    "It's not pain, or hate, that can't throw in some god. The shame."
    "Between the chaos of victims and medics of the decadent hospital, was bagged, promised all kind of nonsense."
    "Renounced all dignity for Marfa. The guilt."
    "Like matryoshkas, a thing inside other. Other people would be proud, but all that come is guilt."
    "Renounced everything for a illusion. The impotence."
    "Couldn't save Marfa, but could save some dignity, your principles."
    "Impotent."
    "Ashamed of impotence."
    "Guilty."
    "Ashamed of guilt."
    "And no one but himself to hate."
    "Breath needles of cold."
    "Maybe, it's really a self punishment."
    "The dull light of sun comes red after cross the eyelids."
    pavel "I sill wanting it would have worked."
    "Something colder than ice downs the spine. Eyes open. All are here. All still here. But not. Are more. And not are."
    "The wind crosses the whole world to reach your lungs. Breathed the air of millions of breaths, under the Sun that holds all the world."
    pavel "Marfa..."
    "She... are. Not like always. In everything. In nothing. Nothing really go away, but not stay. Not like was. All. One. But not a sum. None of them interact, compartmented."
    pavel "Marfa, I..."
    "The sun, the sky, the wind, the snow. All in a motionless explosion."
    pavel "I forgive me."
    
label hospital_inside:
    scene bg infirmary
    pavel "Who?..."
    nurse "Finally you awake."
    pavel "I?..."
    nurse "Try don't strain yourself. You are at hospital. I'm the Nurse Radko. You was found almost frozen at the lake."
    nurse "You was sleeping for three days. Now, you are awake, I'm call the doctor."
    
label pub:
    scene bg pub
    oleg "Cheers to the Ice Men!"
    fedot "What cheers? When he back to construction we will need to back to work!"
    pavel "I was worried about you too, Fedot."
    fedot "Woried? When you was taking your time as ice block I was keeping the chicks warm. You don't need to worry about me."
    nikolai "Speaking of heat, Lipa was walking around your bed to warm you."
    oleg "Ha! The Ice Men turn fire even in the whores of the city."
    pavel "She went to hospital?"
    nikolai "More times then you complain about my work."
    fedot "Then she never go out. Your service is worse then your face, Nikolai!"
    nikolai "But, how to die, boss? One bikini angel come to catch you?"
    pavel "Don't know. In fact... I think I saw my wife."
    "..."
    "......"
    pavel "I'm going home. See you at work tomorrow, guys."
    
label back_house:
    scene bg snow_street
    pavel "'After all, what I saw?'"
    "The snow grates at each step. Don't remember when heard this last time. Maybe at Saint Petesbugh."
    "Some things, always here, are vanished from our mind. Other, are like a callus. Impossible to forgot."
    "Was not able to forgot Marfa."
    "That... thing at the lake. Something happened."
    "Arrived. Key on hand. Almost at home. But will not sleep tonight. No way to sleep tonight."
    "what I should do?"
    menu:
        "Go to Lipa home.":
            $ social = 1
            jump lipa_night1
        "Think at the roof.":
            $ introvert = 1
            jump roof
    
label lipa_night1:
    "All I need is a talk. Put the thoughts in order."
    "Almost energetic, not almost depressed as in the travel here, as in work, as in home, as almost always, Lipa's house approaches step by step."
    "The first phrase, and the next, and the following. All in your head. All like a real talk."
    "But..."
    "This is stupid."
    "A cold near-death experience. Only this."
    "Always, every day, the memories of that damn hospital. Obviously they become to the near-death delirium."
    "This is so stupid."
    "You slow down. There are only two blocks. Go?"
    "Will be good talk to someone."
    "But about what? And why?"
    "And why she?"
    "She went to the hospital. Why?"
    "We don't have nothing after all. Only a few conversations after."
    "It's not like we have something."
    "Only the workers don't talk about nothing before one and a half bottle of vodka."
    "Nothing after too."
    "Also, it's already late."
    "How Lipa can help? What kind of help she can give?"
    "I should turn back."
    pavel "Maybe a priest can enlighten me with his bullshit."
    "You laugh loud, hush fast."
    pavel "This was a bit crazy..."
    
label first_victim:
    scene bg snow_street_back
    strange "Help..."
    scene bg snow_street
    "Where?"
    "The voice was low. Where come from?"
    scene bg snow_street_back
    "Behind a car, a red stain in the white snow."
    "Run! Blood? Robbery?"
    "A man. His legs. Like Chechnya."
    strange "Te nenet..."
    pavel "Don't talk. I'll call a ambulance."
    strange "Nga comes to us..."
    pavel "I have a injured man. Ul. Pavlova with Kirova. His legs are almost amputated."
    strange "Beware the nenet..."
    "A tourniquet. Your belt."
    pavel "It's only a block to here. They are coming."
    strange "Nga comes to us"
    "He lost much blood. The other leg. A tourniquet with what? I'm wearing a long sleeve shirt."
    "Remove the coat hurt more then I expected. This buttons. I can't open with gloves."
    pavel "Stay calm. They are coming. I can hear the horn."
    "A strong pull and the buttons fly away. I must wear the coat again."
    strange "Nga comes..."
    "The man stops to breath."
    pavel "Fuck!"
    "The ambulance stops besides you. The man's blood taint your shirt. The paramedics go to his body."
    "You close the zipper. The snow inside of the coat pinches your chest."
    paramedic "He was gone."
    pavel "Fuck!"
    paramedic "It wasn't your fault."
    pavel "I know."
    paramedic "Come here. The ambulance is heated."
    jump uchastkovyi_interview
    
label roof:
    scene bg factory_skyline
    "Most of the people don't go to roof at thirty degrees bellow zero."
    pavel "You are some kind of maniac."
    "The skyline is more brighter at night than at day. Thanks to the factories with metal-halide lamps."
    "Really, why Norilsk? This city is frozen, polluted, and don't have a drop of oil."
    "And why work as foreman?"
    pavel "Mining is mining. Sure I can work on the mines. Also in the smelters."
    "We come to the most remote land to mine and melt our nickel. Hundreds of people in a land where farming is almost impossible."
    "We turn night in day as side effect to our mining business."
    "We are the masters of the world. All that new age bullshit is that."
    pavel "Bullshit! You hear me?"
    "Bellow, in the street, your car's alarm goes crazy."
    pavel "If this is the best you can..."
    "You press the button in the key chain in vain. Too far. All the way in the stairs the loud sound do not stop."
    "This will wake all the neighbours."
    "Finally, at the door the key chain works and the noise stops."
    jump first_victim
    
label uchastkovyi_interview:
    scene bg inner_hospital
    uchastkovyi "Are you ok?"
    pavel "I seem ok?"
    uchastkovyi "Not. But this is good. I don't like a man who are ok after this."
    pavel "Tanks uchastkovyi."
    uchastkovyi "I need to do some questions."
    pavel "Go ahead. I have some time."
    uchastkovyi "You are here for three years now. And I know very few about you."
    pavel "What are you insinuating?"
    uchastkovyi "Only in the army I expect to meet a man who know the right way to make a tourniquet with a belt. To be honest I don't know. The paramedic said me that was right."
    uchastkovyi "And do this instead of scream in panic. Was not a light view."
    pavel "I worked at a oil well. One day a co worker had his hand eaten by a vee-belt."
    pavel "Well... I was completely useless then."
    uchastkovyi "You did a good work today. I can say this."
    pavel "Who was that underdog?"
    uchastkovyi "No idea. But was a nenet."
    pavel "He was talking something about nenet. \"beware the nenet\" or somehing like this."
    uchastkovyi "The people who lived here. Siberian nomads."
    pavel "The acid rain killed what the ice couldn't. What a nomad are doing here?"
    uchastkovyi "Many of them live in cities, but this was a foreigner. Maybe paying a visit. Tomorrow I start to ask if someone saw they before."
    pavel "And what made that?"
    uchastkovyi "Not a vee-belt, I guarantee. I never see something like that. It's like his legs are chewed."
    pavel "I've seen."
    uchastkovyi "Where?"
    pavel "Bomb attack. Chechnya, 95."
    uchastkovyi "Want a coffee?"
    pavel "Anything hot."
    
label the_day_after:
    scene bg lipa_room
    lipa "You look really bad."
    pavel "I suppose. It was a bad week."
    lipa "Why you was in the lake?"
    pavel "I like to think alone."
    lipa "Bad thoughts?"
    pavel "Not. Something weird at moments, but not bad."
    lipa "Good. If it isn't' bad Nga is not catching you."
    pavel "Who is catching me?"
    "The window open with rumble. Wind and snow swirl around Lipa."
    lipa "Nga, the lord of underworld, who catch your breath to his caves of ice."
    "She floats. Naked. In the swirl. Is frozen."
    lipa "Nga, the frost god of death, father of all diseases."
    "There is no mist in her breath. No red in her skin."
    scene bg pavel_office
    oleg "Are you ok, boss?"
    pavel "What?"
    oleg "You was grunting. A nightmare?"
    pavel "I suppose. It was a bad week."
    pavel "Wait!"
    oleg "What?"
    pavel "Are you going to be crazy or something?"
    oleg "You are awake?"
    pavel "Ok. Now I'm awake. I guess."
    oleg "Maybe you should go home. You almost died, and then yesterday."
    pavel "I'm OK. Was only a nightmare. I not slept since the hospital. The first time at hospital."
    oleg "Well, I come here because Vasilii want to talk with you."
    pavel "He have a paternity intimation?"
    oleg "No. If was that I'd be saying to flee through the bathroom's window."
    pavel "If you do that you will save my life. Let he come in."
    "'Fucking weird nightmare!'"
    uchastkovyi "Hi Pavel. Something new?"
    pavel "Not really, but I should ask this, not you."
    uchastkovyi "His name was Hek, a shaman. Came here to find a apprentice."
    pavel "And the murderer?"
    uchastkovyi "My work is to know my people."
    pavel "So?"
    uchastkovyi "Only yesterday I discovered most of the things of your past."
    pavel "I lost the point."
    uchastkovyi "And Hek saw many things about you to their people. In fact, he don't know only your name."
    pavel "What?"
    uchastkovyi "He comes because there was a widower who survived a war of south-weast. A brave man who have worked 'stealing Ya-nebya'."
    pavel "Who I stole?"
    uchastkovyi "The 'mother gaia' or something else. Their elders call the mines this way."
    pavel "Then you come to jail me. I confess, I stole the dark milk of mother gaia."
    "This is all nonsense. You two start to laugh"
    pavel "A vodka, uchastkovyi?"
    uchastkovyi "Sure."
    "Vasilii sits when you serves the drink and start to talk."
    uchastkovyi "But I come here because he saw things like 'skilled man in a unqualified job', 'born in the far west' and 'tied to his dead wife'."
    pavel "This is coincidence."
    uchastkovyi "I know. But if you believe. He said you are in danger. 'Nga' chases the chosen."
    "Nga? Again? "
    pavel "Repeat the last sentence."
    uchastkovyi "Nga chases the chosen."
    pavel "He said this word, Nga, before die. I thought this was a moan or something."
    uchastkovyi "Is the bad god of nenets."
    pavel "No way!"
    uchastkovyi "Something like this. A frost bastard who commands blizzards and diseases."
    "..."
    "......"
    uchastkovyi "Are you OK?"
    pavel "I'm OK. Only tired. I hardly slept. Thanks for the advice Vasilii. I'll go home and rest."
    uchastkovyi "You are welcome. See you."
    
label credits:
    scene bg white
    nvl clear
    fsb "Writing:"
    fsb "Cochise César\n\n"
    fsb "Photos:"
    fsb "Hospital Roof View-2: Tim Suess http://www.flickr.com/photos/lord_yo/"
    fsb "One day later bedroom, One Day later, drawing room, hospital: Bolshakov http://www.flickr.com/photos/bolshakov/"
    nvl clear
    fsb "Yesterday: NapaneeGal http://www.flickr.com/photos/kingstongal/"
    fsb "Classic Hospital Room, Bright View for Moody Time: cobalt123 http://www.flickr.com/photos/cobalt/"
    fsb "Дума .aG http://www.flickr.com/photos/s7stem/"
    fsb "Factory view Matti Vinni http://www.flickr.com/photos/matti_vinni/"
    "Après la tempête du 19 mars [two images], abdallahh http://www.flickr.com/photos/husseinabdallah/"
    nvl clear
    return