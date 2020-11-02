label day_01:
    $ day = "Day 1"
    $ save_name = "Day 1"
    $ k_sex = False

label day_01_office_scene:

    scene black with dissolve

    show bg day_01 with fade
    $ renpy.pause (2)

    scene day_01_entrance_scene_1f with fade
    show screen map_button

    scene day_01_entrance_scene_1f with dissolve
    "{color=#D2691E}*You get off the train and head for the exit. A young woman is walking right next to you and starring at you.*{/color}"
    "{color=#D2691E}*Finally she comes up to you and asks.*{/color}"

    scene day_01_entrance_scene_1a with dissolve
    wo1 "[player_name]? [player_name] [player_surname]? Is that really you?"
    mc "Yes."
    "{color=#D2691E}*You are looking at the girl trying to remember who she was.*{/color}"
    wo1 "You don't recognize me, do you?"
    mc "I'm very sorry."
    wo1 "It's me, Becky!"

    scene day_01_entrance_scene_1b with dissolve
    mc "Jesus Christ, Becky, nice to see you again."
    be "Hehe. It's hard to recognize me without braces and the big glasses, isn't it?"
    mc "Yeah, you've changed a lot."
    be "And you've changed almost nothing. Haha."
    mc "Hehe, yeah."

    scene day_01_entrance_scene_1c with dissolve
    be "By the way, do you remember that you lost the bet and you owe me something?"
    mc "Oh, yeah, I totally forgot about that."
    be "Why don't you come and pay your debts before you disappear again for another ten years."
    mc "I'll do my best."

    scene day_01_entrance_scene_1d with dissolve
    mc "How's your brother?"
    be "Jimmy left for Chicago about five years ago. He got married and had two kids."
    mc "Wow! Jimmy's settled down. We are doomed."
    be "Haha."
    be "How long are you staying in town?"
    mc "I don't know. A few days, maybe longer as I have some family business to attend to."

    scene day_01_entrance_scene_1e with dissolve
    be "I see. If you want to talk about old times or pay your debts, you know where to find me."
    mc "Yes, I remember. It was nice seeing you again."
    be "It was nice to see you, too."
    mc "Say hi to your brother for me."
    be "I will."
    mc "Bye."
    $ becky_enabled = True

    if persistent.smoke == True:

        scene day_01_entrance_scene_2 with dissolve
        "{color=#D2691E}*You look at the watch. It's almost 9 am.*{/color}"
        "{color=#81F79F}*Fuck, I'm already late.*{/color}"
        "{color=#D2691E}*After a few minutes you're standing in front of the building a little breathless.*{/color}"
        "{color=#D2691E}*You're getting more and more nervous.*{/color}"
        "{color=#81F79F}*I have to smoke, or I'll loose my mind.*{/color}"

        scene day_01_entrance_scene_3 with dissolve
        "{color=#D2691E}*You sit on a bench and smoke a cigarette.*{/color}"
        "{color=#81F79F}*I have a bad feeling about this meeting.*{/color}"
        "{color=#81F79F}*I'll see Jennifer, Nicole and Lisa again after all these years. How am I supposed to act?*{/color}"
        "{color=#81F79F}*I'm sure Linda did everything she could to make the girls hate me. Should I talk to them? Explain to them what happened then?*{/color}"
        "{color=#81F79F}*But will they even want to talk to me?*{/color}"

        scene day_01_entrance_scene_3a with dissolve
        "{color=#81F79F}*I hope this meeting won't take too long. I don't know for how long I'll be able to stand to be in the same room as Linda.*{/color}"

    else:

        scene day_01_entrance_scene_2 with dissolve
        "{color=#D2691E}*You look at the watch. It's almost 9 am.*{/color}"
        "{color=#81F79F}*Fuck, I'm already late.*{/color}"
        "{color=#D2691E}*You're getting more and more nervous.*{/color}"

        scene day_01_entrance_scene_3a with dissolve
        "{color=#81F79F}*I'll see Jennifer, Nicole and Lisa again after all these years. How am I supposed to act?*{/color}"
        "{color=#81F79F}*I'm sure Linda did everything she could to make the girls hate me. Should I talk to them? Explain to them what happened then?*{/color}"
        "{color=#81F79F}*But will they even want to talk to me?*{/color}"

    scene day_01_entrance_scene_4 with dissolve
    sec "Good day, sir. How can I help you?"
    mc "Good morning."
    mc "I have an appointment at 10. My name is [player_name] [player_surname]."

    scene day_01_entrance_scene_5 with dissolve
    sec "Of course. Everyone is already waiting."

    scene day_01_entrance_scene_6 with dissolve
    sec "Please, Mr. [player_surname], this way."
    $ holy_enabled = True

    scene day_01_lawyer_office_scene_2
    law "Since everyone is here, I think we can start."
    "{color=#D2691E}*The lawyer sits down at the head of the table and opens the folder with documents.*{/color}"
    law "May I have your attention now?"
    "{color=#D2691E}*But you don't care what the lawyer is saying.*{/color}"
    $ sandra_enabled = True
    $ changeWallpaper()

    scene day_01_lawyer_office_scene_4 with dissolve
    "{color=#D2691E}*You focus your attention on Linda.*{/color}"
    "{color=#81F79F}*I'll humiliate you, bitch.*{/color}"
    "{color=#81F79F}*You'll be begging me to end your miserable life.{/color}"
    "{color=#81F79F}*Then I'll humiliate you even more.*{/color}"
    "{color=#81F79F}*I swear on my mother's soul, you'll pay for everything tenfold.*{/color}"
    "{color=#D2691E}*Out of the corner of your eye, you notice that one of the girls is smiling at you.*{/color}"

    scene day_01_lawyer_office_scene_3 with dissolve
    "{color=#81F79F}*Is that Lisa?*{/color}"
    "{color=#81F79F}*I haven't seen her for so many years, she is not a child anymore.*{/color}"
    "{color=#D2691E}*You smile back at her.*{/color}"

    scene day_01_lawyer_office_scene_5 with dissolve
    "{color=#D2691E}*You turn your head a bit more and you see the other two girls, Lisa's older sisters, Jennifer and Nicole.*{/color}"
    "{color=#81F79F}*Damnit... It's only now that I realize how much I've missed them over the last ten years....*{/color}"
    "{color=#D2681E}*You smile at them too, but Jennifer is ignoring you and Nicole sends you a look full of hatred.*{/color}"
    "{color=#81F79F}*Looks like Lisa's the only one who's happy to see me. Well, there's not much I can do about it.*{/color}"
    "{color=#D2691E}*Suddenly you hear the lawyer say your name and you start to listen to her more carefully.*{/color}"

    scene day_01_lawyer_office_scene_6 with dissolve
    law "...I bequeath my house and my car to my son, [player_name] [player_surname]..."
    law "...After my death, my son becomes the sole owner of my company and its President..."
    law "...Nicole, Lisa and Jennifer will get $5,000 each as a study fund..."
    law "...Linda, my dear friend, will get my collection of butterflies which she loved so much..."
    law "...Linda and her daughters are to leave my home within 7 days of the reading of my Will."

    scene day_01_lawyer_office_scene_7 with dissolve
    li "This is fucking BULLSHIT! ...This can't be true..."
    "{color=#81F79F}*Hehe. My old man gave you a good lesson, bitch.*{/color}"
    law "Please, calm down Mrs. Brown or I will have to ask you to leave the office!"
    $ linda_enabled = True
    $ changeWallpaper()

    scene day_01_lawyer_office_scene_8 with dissolve
    li "I'll never let him take over MY HOUSE and MY COMPANY!"
    li "Do you hear me, [player_name]? This isn't over yet!"

    menu linda_reply:

        "{color=#74B2F4}Just shut the fuck up!{/color} [LindaSubmissionPath]":

            mc "Just shut the fuck up, Linda!"
            mc "I'm not afraid of you, anymore."
            li "You will pay me for everything."
            mc "This time it's your turn and you are the one who will pay me for everything."
            li "You will regret that I promise you!"
            $ linda_submission += 1

        "{color=#74B2F4}Stay quiet.{/color}":

            law "I'm sorry, but this is expressly stated in the will. There's nothing you can do."

    scene day_01_lawyer_office_scene_9 with dissolve
    "{color=#D2691E}*Linda rushes out of the office and slams the door.*{/color}"
    "{color=#D2691E}*The meeting ends soon, and you leave the office with a big smile on your face.*{/color}"

    scene day_01_hallway_scene_1 with dissolve
    l "[player_name], wait!"
    "{color=#81F79F}*In all the commotion, I totally forgot about the girls.*{/color}"
    $ lisa_enabled = True

    scene day_01_hallway_scene_3 with dissolve
    mc "Hey, Lisa."
    "{color=#D2691E}*Lisa runs up to you and throws herself around your neck.*{/color}"
    l "I missed you so much!"
    mc "I missed you, too!"
    l "I'm so happy to see you again!"
    l "I always knew I'd see you again one day."
    $ jennifer_enabled = True
    $ changeWallpaper()

    scene day_01_hallway_scene_6 with dissolve
    mc "Hello, Jennifer."
    mc "Hello, Nicole."
    mc "It's good to see you again after all these years."
    j "Seriously, [player_name]."
    j "You must have a lot of nerve to just show up here after all these years."
    j "You want to turn our lives upside down again? Don’t you get tired of hurting us?"

    $ nicole_enabled = True


    menu jennifer_reply:

        "{color=#74B2F4}Jennifer...{/color} [JenniferPath]":

            scene day_01_hallway_scene_7 with dissolve
            mc "Jennifer..."
            j "I don’t want to hear any excuses from you."
            j "I just want to know what are you going to do with us now?"

            scene day_01_hallway_scene_8 with dissolve
            mc "What do you mean?"
            j "Are you stupid or you’re just pretending?"
            mc "Come on, Jennifer. Why are you so mad at me?"
            $ jennifer_love += 1

        "{color=#74B2F4}The hell you want from me?{/color}":

            scene day_01_hallway_scene_8 with dissolve
            mc "The hell you want from me?"
            j "I've just told you what I want to know. Are you deaf?"
            mc "Don't talk to me like that!"

    scene day_01_hallway_scene_9 with dissolve
    l "Seriously, Jennifer. What the heck is wrong with you?"

    scene day_01_hallway_scene_10 with dissolve
    j "Stop interrupting me, Lisa."
    mc "If you're talking about the house, well...it's mine now. I should be living there. Not you and your stupid mother."
    mc "I didn’t want to tear you out of your life but this kind of attitude makes me rethink my decision."

    scene day_01_hallway_scene_11 with dissolve
    n "Leave my mother alone. She’s not as bad as you think!"

    menu nicole_reply:

        "{color=#74B2F4}You have to be joking!{/color} [NicoleSubmissionPath]":
            mc "You have to be joking! The bitch destroyed my life."
            mc "Are you seriously going to tell me that she’s not that bad?"

            scene day_01_hallway_scene_12 with dissolve
            n "So many years have passed, and you continue to accuse her of all kinds of disgusting things."
            n "Stop insulting her finally. This is all your fault, not hers, so be a man for once and admit that it was you who made us suffer for so many years..."
            n "..."
            n "You have no idea what we were going through when you left home!"
            $ nicole_submission += 1

        "{color=#74B2F4}Stop defending her.{/color} [NicoleLovePath]":
            mc "Why it is so hard for you to understand that your beloved mother destroyed my life?"

            scene day_01_hallway_scene_12 with dissolve
            n "I don't want to hear that crap."
            n "You've always hated her."
            mc "That's not true! How can you say that?"
            $ nicole_love += 1

    scene day_01_hallway_scene_13 with dissolve
    l "Nicole, seriously! I love our mother too, but you know perfectly well that she isn’t a saint."
    l "For once, try to be objective. [player_name] has always been like an older brother to all of us and I don't believe that he left without reason."

    scene day_01_hallway_scene_14 with dissolve
    n "I don't care. The truth is that [player_name] was not with us for ten years. Now he appears out of nowhere and wants to turn our lives upside down."
    n "He gets the house, the car and the company. Lisa, instead of defending him, think for a moment what will happen to us now."
    mc "Everything you named belonged to my family, not yours and now it’s officially mine. Is this kind of greed that deep-seated in your family?"

    scene day_01_hallway_scene_15_blink with dissolve
    n "I’m greedy? Are you out of your mind? You don’t deserve any of these things. I can’t believe that your father made you his heir."
    mc "Enough is enough. I don’t have to listen to all this bullshit. I could expect such a reaction from Linda but you?
    It's not enough that your mother took my home, ran my father's company, and destroyed my life? Are you so damn blind? Maybe someday you’ll learn the truth about your beloved mother."

    scene day_01_hallway_scene_16_blink with dissolve
    j "Really [player_name]...what did you expect from us?"
    mc "Not much to be honest. I just thought we’d act like adults and not like spoiled kids. I didn’t want any of those things. I just came here to finally close this chapter of my life."
    mc "But it looks like I was wrong. I have to think about what to do next. I'll see you again soon."

    scene day_01_hallway_scene_17 with dissolve
    l "[player_name], don’t go please…!"

    menu:
        "{color=#74B2F4}I would love to stay with you, but I'm not welcome here anymore.{/color} [LisaLovePath]":
            mc "I would love to stay with you, but I'm not welcome here anymore."
            "{color=#D2691E}*You see tears rolling down her cheeks. You feel sorry, but you're helpless.*{/color}"
            mc "I'm really sorry..."
            $ lisa_love += 1
            jump day_01_girls_fight

        "{color=#74B2F4}I don't think it's a good idea.{/color} [_LisaLovePath]":
            mc "I don't think it's a good idea."
            "{color=#D2691E}*You see tears rolling down her cheeks. You feel sorry, but you're helpless.*{/color}"
            "{color=#D2691E}*There is so much hate in Jennifer and Nicole look so you decide to turn around and leave the office.*{/color}"
            $ lisa_love -= 1
            jump day_01_girls_fight

        "{color=#74B2F4}Leave me alone.{/color} [GameOver]":
            mc "Just leave me alone!"
            jump game_over

label game_over:
    scene black with dissolve
    centered "{b}{size=100}{color=#FF0000}GAME OVER{/color}{/b}{/size=100}"
    return

label day_01_girls_fight:

    scene black with fade
    "{color=#D2691E}*The girls leave the office. Lisa is mad and she argues with her sisters.*{/color}"

    scene day_01_outside_scene_1 with dissolve
    l "Why do you always have to be such a bitch, Nicole? And what the heck is wrong with you, Jennifer?"
    n "Leave me alone."
    l "If I lose him again, you’ll regret it. I swear."
    n "Yeah? And what are you going to do?"
    j "Shut up! Now!"

    scene day_01_outside_scene_1a with dissolve
    l "You shut up!"
    l "Don’t try to be my mother. You suck at it."
    l "All of sudden you pretend to care about me? Where have you been for the last few months when I needed you?"
    j "Watch your mouth!"
    l "And what are you going to do if I don’t? Ignore me even more?"
    j "Enough!"

    scene day_01_outside_scene_2 with dissolve
    j "Taxi!"
    l "I'm not going with you."

    scene day_01_outside_scene_3 with dissolve
    j "Get your ass into the taxi, now!"
    l "NO! I hate you both."

    scene day_01_outside_scene_4 with dissolve
    n "Stupid kid. Leave her alone."
    j "You'll regret it, Lisa."
    l "Whatever..."

    jump phone_call_john_mary

label phone_call_john_mary:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_01_phone_mary_john_1a with dissolve
    mc "Hey, Mary."
    mary "What’s up, boss?"
    mc "It looks like I'll be spending more time than I expected in this shithole."
    mc "My stupid father made me the President of his company. So, I’m going to check what I can get out of it."
    mary "Do you need our help?"
    mc "No, I’ll handle it on my own. Take care of our businesses, please."
    mary "Don’t worry, boss. If you need any help let me know."
    mc "Sure Mary, thanks. Tell Khloe that she’ll have to do her current assignment alone, but I know she’ll be just fine."
    mary "I’ll do that. Goodbye, boss."
    $ mary_enabled = True
    jump hotel_day_01

label hotel_day_01:

    scene black with dissolve
    show bg one_hour_later with dissolve
    $ renpy.pause ()

    if persistent.smoke == True:

        scene day_01_hotel_entrance_scene_1 with dissolve
        "{color=#81F79F}*I knew coming here would be a mistake and I wasn't wrong.*{/color}"
        "{color=#81F79F}*Now I have an extra problem with my father's company and I have to face Linda and her daughters.*{/color}"
        "{color=#81F79F}*And given their attitude towards me, it's not gonna be a simple and pleasant thing to do.*{/color}"
        "{color=#81F79F}*Linda made sure her daughters hated me. She had enough time to do that.*{/color}"
        "{color=#81F79F}*So I have no choice but to act quickly and get rid of the company and this cursed house. Get out of here and never come back while I still can.*{/color}"
        "{color=#81F79F}*I'd love to get my revenge on Linda, but is it worth digging through the old things and going down to her level?*{/color}"
        "{color=#81F79F}*Nothing can fix what happened ten years ago and give us back those lost years.*{/color}"

    else:

        scene day_01_hotel_entrance_scene_1 with dissolve
        "{color=#81F79F}*I knew coming here would be a mistake and I wasn't wrong.*{/color}"
        "{color=#81F79F}*Now I have an extra problem with my father's company and I have to face Linda and her daughters.*{/color}"
        "{color=#81F79F}*And given their attitude towards me, it's not gonna be a simple and pleasant thing to do.*{/color}"
        "{color=#81F79F}*Linda made sure her daughters hated me. She had enough time to do that.*{/color}"

        scene day_01_hotel_entrance_scene_1a with dissolve
        "{color=#81F79F}*So I have no choice but to act quickly and get rid of the company and this cursed house. Get out of here and never come back while I still can.*{/color}"
        "{color=#81F79F}*I'd love to get my revenge on Linda, but is it worth digging through the old things and going down to her level?*{/color}"
        "{color=#81F79F}*Nothing can fix what happened ten years ago and give us back those lost years.*{/color}"

    scene day_01_hotel_lobby_scene_1 with dissolve
    mc "Good evening. I would like to get a room."
    rec "Of course, sir. How long are you going to stay at our hotel?"
    mc "I believe a week will be enough."
    rec "Would you like to pay with cash or credit card?"

    scene day_01_hotel_lobby_scene_2 with dissolve
    mc "Credit card."
    rec "Here is your key. Third floor, room 313."
    mc "Thank you."

    scene black with fade
    "{color=#D2691E}*Next to the elevator you see a beautiful girl.*{/color}"

    scene day_01_hotel_lobby_scene_3aa:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()

    scene day_01_hotel_lobby_scene_3a with dissolve
    k "Oh, hi."
    mc "Hey there, beautiful."

    scene day_01_hotel_lobby_scene_4 with dissolve
    k "I'm Kelly."
    mc "I'm [player_name]."
    $ kelly_enabled = True
    $ changeWallpaper()

    scene day_01_hotel_lobby_scene_5 with dissolve
    k "Nice to meet you. Which floor?"
    mc "Third."
    k "Hmm. Any chance for a drink together in the bar later on?"
    k "It's my first time in this town and I don't want to spend my whole evening alone."

    scene day_01_hotel_lobby_scene_6 with dissolve

    menu drink:
        "{color=#74B2F4}Agree.{/color} [KellyPath]":
            mc "As if I'd ever refuse a flower such as yourself inviting me for a drink."
            k "Let's say 8 pm?"
            mc "Sounds awesome."
            k "Wonderful, see you later."
            jump hotel_bar

        "{color=#74B2F4}No.{/color}":
            mc "I'm sorry, but I'm a bit tired."
            mc "It was a very exhausting day."
            mc "Maybe some other time."
            k "I understand."
            k "In that case, sleep well."
            jump hotel_room

label hotel_room:

    scene room_313 with dissolve
    $ renpy.pause ()

    scene day_01_hotel_room with dissolve
    "{color=#81F79F}*Well, Nicole was right about one thing. I have to be a man, and I can't let an old whore mess with me.*{/color}"
    "{color=#81F79F}*Linda ruined my life and she has to be punished.*{/color}"

    scene day_01_hotel_room_1 with dissolve
    "{color=#81F79F}*I'll humiliate her as she humiliated me. I have to figure out what's most important to her and use it against her.*{/color}"
    "{color=#81F79F}*I'll do whatever it takes to make her finally feel what I felt when she blackmailed me.*{/color}"
    "{color=#81F79F}*When she deprived me of my father, my friends, my girlfriend and my loved ones - Nicole, Jennifer and Lisa.*{/color}"

    scene day_01_hotel_room_2 with dissolve
    "{color=#81F79F}*She will find out what it means to lose everything that you love, that is dear and close to you.*{/color}"
    "{color=#81F79F}*She will know the pain of losing the most important people in her life.*{/color}"
    "{color=#81F79F}*Only when I take my revenge will I be able to close this chapter in my life and return to Mary and Khloe in peace.*{/color}"
    jump lisa_jennifer

label hotel_bar:

    scene black with dissolve
    show bg room_313 with dissolve
    $ renpy.pause ()

    scene day_01_hotel_room with dissolve
    "{color=#81F79F}*Well, Nicole was right about one thing. I have to be a man, and I can't let an old whore mess with me.*{/color}"
    "{color=#81F79F}*Linda ruined my life and she has to be punished.*{/color}"

    scene day_01_hotel_room_1 with dissolve
    "{color=#81F79F}*I'll humiliate her as she humiliated me. I have to figure out what's most important to her and use it against her.*{/color}"
    "{color=#81F79F}*I'll do whatever it takes to make her finally feel what I felt when she blackmailed me.*{/color}"
    "{color=#81F79F}*When she deprived me of my father, my friends, my girlfriend and my loved ones - Nicole, Jennifer and Lisa.*{/color}"

    scene day_01_hotel_room_2 with dissolve
    "{color=#81F79F}*She will find out what it means to lose everything that you love, that is dear and close to you.*{/color}"
    "{color=#81F79F}*She will know the pain of losing the most important people in her life.*{/color}"
    "{color=#81F79F}*Only when I take my revenge will I be able to close this chapter in my life and return to Mary and Khloe in peace.*{/color}"

    scene black with dissolve
    show bg few_hours_later with dissolve
    $ renpy.pause ()

    scene day_01_hotel_bar_scene_0 with dissolve
    "{color=#D2691E}*You enter the hotel bar.*{/color}"
    "{color=#81F79F}*Hmm. She's not here yet.*{/color}"

    scene day_01_hotel_bar_scene_1 with dissolve
    mc "Double whiskey, please."
    bartender "First time in our town?"
    mc "Not really, I lived here when I was a kid. I'm visiting old friends."

    scene day_01_hotel_bar_scene_2 with dissolve
    bartender "Welcome back then."
    bartender "How do you like the town after so many years?"
    mc "To be honest, nothing's changed. I haven't had time to visit all the places I used to know, but so far it seems as dull as ever."

    scene day_01_hotel_bar_scene_3 with dissolve
    bartender "The town is growing up. It's noticeable on the other side of it."
    mc "I have to check it out then."

    scene day_01_hotel_bar_scene_4 with dissolve
    k "There you are."
    mc "Oh, hey. What would you like to drink?"
    k "Whiskey."
    mc "Make that two Whiskeys, please."

    scene day_01_hotel_bar_scene_6 with dissolve
    mc "Let's sit down."

    scene day_01_hotel_bar_scene_7 with dissolve
    mc "So, tell me, what is such a beautiful lady doing in this damned town all by herself?"
    k "Well, my flight was delayed and this hotel was the only place with rooms available. So I didn't get to choose."
    k "But at least I had a chance to meet you."

    scene day_01_hotel_bar_scene_7a with dissolve
    mc "Yeah. I'm glad we met."
    k "So, what are you doing here?"
    mc "I have some family stuff. My father passed away recently, so I came here to hear his last will."
    k "I'm sorry."

    scene black with dissolve
    show bg a_few_drinks_later with dissolve
    $ renpy.pause ()

    scene day_01_hotel_bar_scene_7b with dissolve

    menu sex:
        "{color=#74B2F4}I think you've had too much to drink, you should get some sleep.{/color}":
            mc "I think you've had too much to drink, you should get some sleep."
            k "But I feel great. I want to suck your cock."
            mc "Seriously? Pull yourself together."

            scene day_01_hotel_bar_scene_6a with dissolve
            k "Asshole!"

            jump lisa_jennifer

        "{color=#74B2F4}I don't normally do this, but you're making me falter.{/color} [KellyPath]":

            scene day_01_hotel_bar_scene_8 with dissolve
            k "You know... I never thought I would meet someone that gets me so God damn hot."
            k "If you don't stop looking at me like that, we're going to have to go somewhere private."
            mc "I don't normally do this, but you're making me falter."
            k "You know I'm not wearing panties?"
            mc "Living dangerously! I quite like that!"

            scene day_01_hotel_bar_scene_8a with dissolve
            mc "{color=#7FFFD4}*whispers in her ear*{/color} By God. You're so beautiful. Your pussy just looks perfect, I can barely control the urge to eat you out."
            k "{color=#7FFFD4}*whispers back*{/color} I really want to feel your lips on my wet pussy right now."
            mc "{color=#7FFFD4}*whisper*{/color} Let's go to my room. I want to rip your clothes off and taste your pussy."
            $ k_sex = True
            $ persistent.k_sex = k_sex

            jump hotel_room_01

label hotel_room_01:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_01_hotel_bar_scene_11 with dissolve
    k "{color=#7FFFD4}*whispers*{/color} I can't stop thinking about your lips on my pussy."
    k "{color=#7FFFD4}*whispers*{/color} It makes me so damn wet!"
    "{color=#D2691E}*She teases you even more with every step you take.*{/color}"
    "{color=#D2691E}*You can't control your lust anymore.*{/color}"

    scene day_01_hotel_bar_scene_13 with dissolve
    "{color=#D2691E}*You grab her and gently push her against the wall.*{/color}"
    "{color=#D2691E}*Slowly reveal her bosom.*{/color}"
    mc "Oh my God. You look like an angel."

    scene day_01_hotel_bar_scene_14 with dissolve
    k "Kiss me, [player_name]."
    "{color=#D2691E}*You hold her tight and kiss her passionately.*{/color}"

    show kelly_kiss_day_1 with dissolve

    "{color=#D2691E}*While still kissing, you open the door to your room and move in.*{/color}"

    scene day_01_hotel_room_stewardess_scene_14 with dissolve
    "{color=#FF69B4}*She enjoys the touch of your lips as you move your head from her neck to her breasts.*{/color}"

    scene day_01_hotel_room_stewardess_scene_1 with dissolve
    k "Oh, yes. Suck my nipples, [player_name]."
    "{color=#FF69B4}*Slowly, while kissing every inch of her perfect body, you move your head down, to the sweet spot between her legs.*{/color}"
    k "I want to feel your lips on my pussy."

    scene day_01_hotel_room_stewardess_scene_15 with dissolve
    "{color=#FF69B4}*You drop on your knees and open her legs. Now you can finally admire her beautiful pussy.*{/color}"

    scene day_01_hotel_room_stewardess_scene_16 with dissolve
    "{color=#FF69B4}*When your tongue touches her cunt, she lets out a relieved sigh.*{/color}"
    "{color=#FF69B4}*She smells so good. You tease her clitoris with your lips and tongue.*{/color}"
    "{color=#FF69B4}*You start to lap up her juices from her tight, sweet pussy. You don't want to miss even a drop of her sweet nectar.*{/color}"
    mc "Mmmmm. You taste so good."

    scene day_01_hotel_room_stewardess_scene_2 with dissolve
    "{color=#FF69B4}*She trembles as you treat her labia and clitoris to the powerful strokes of your tongue.*{/color}"
    "{color=#FF69B4}*Soon you hear Kelly's lewd moans as your tongue is working on her clitoris and labia*{/color}"
    k "My God, [player_name]. Don't stop."

    scene day_01_hotel_room_stewardess_scene_4 with dissolve
    "{color=#FF69B4}*You keep playing with her pussy. Your tongue is darting all over Kelly's vulva.*{/color}"
    k "You're amazing. Ahhhhhh. Yes. Right there!"
    k "You're so good at licking my tight pussy."

    scene day_01_hotel_room_stewardess_scene_5 with dissolve
    "{color=#FF69B4}*Judging from the lewd noises Kelly is making, she is almost at her climax.*{/color}"
    "{color=#FF69B4}*Alternating between kissing, licking and sucking, you methodically push her to the very limit.*{/color}"
    mc "You're so wet."

    scene day_01_hotel_room_stewardess_scene_6 with dissolve
    k "Don't stop now. Make me cum with your tongue, [player_name]."

    scene day_01_hotel_room_stewardess_scene_3a with dissolve
    "{color=#FF69B4}*You press your tongue against Kelly's pussy and start to stimulate the clitoris directly.*{/color}"
    k "Don't stop!"
    k "Oh my God. I'm cumming!"
    "{color=#FF69B4}*Every muscle in her body taut in anticipation. Kelly presses your face against her cunt.*{/color}"
    "{color=#FF69B4}*She lewdly moans louder and louder. One more moan and the wave of pleasure floods her whole body.*{/color}"
    "{color=#FF69B4}*Her body is trembling with pleasure. Her sweet and hot juices run down her pussy.*{/color}"

    scene day_01_hotel_room_stewardess_scene_3a with flash
    with flash
    with flash
    "{color=#FF69B4}*She barely catches her breath.*{/color}"
    k "{color=#AFEEEE}*whispers*{/color}That was incredible."
    k "Now, my turn. I want to feel your cock twitching in my mouth."

    scene day_01_hotel_room_stewardess_scene_11 with dissolve
    "{color=#FF69B4}*She drops on her knees and slowly takes off your pants.*{/color}"
    k "Wow. What a monster. I'm already in love with your dick, [player_name]!"
    "{color=#FF69B4}*Kelly kisses your shaft until she reaches the tip and touches it with her tongue.*{/color}"

    scene day_01_hotel_room_stewardess_scene_12 with dissolve
    mc "Oh, yes. Just like that."

    scene day_01_hotel_room_stewardess_scene_7 with dissolve
    "{color=#FF69B4}*She jerks your member very slowly, only to put it in her mouth.*{/color}"

    show kelly_blowjob_day_1 with dissolve
    mc "Oh my God, Kelly."

    scene day_01_hotel_room_stewardess_scene_9 with dissolve
    "{color=#FF69B4}*You see a flame of desire in her eyes as she reaches her sweet spot with her hand.*{/color}"

    scene day_01_hotel_room_stewardess_scene_10 with dissolve
    "{color=#FF69B4}*She takes your cock even deeper inside her mouth, while her tongue swirls around the head of it.*{/color}"

    scene day_01_hotel_room_stewardess_scene_8 with dissolve
    "{color=#FF69B4}*You feel Kelly's warm mouth wraps around the head of your shaft.*{/color}"
    "{color=#FF69B4}*She teases the tip of it with her tounge while jerking it faster and faster.*{/color}"

    scene day_01_hotel_room_stewardess_presex_scene_1 with dissolve
    "{color=#FF69B4}*You lie down with her on the bed and you kiss and stroke each other.*{/color}"
    "{color=#FF69B4}*You push the head of your cock against her entrance, her lips already moist from her arousal.*{/color}"

    scene day_01_hotel_room_stewardess_presex_scene_2 with dissolve
    "{color=#FF69B4}*After a gentle start, you start to move more roughly and you penetrate her with the entire length of your shaft.*{/color}"
    "{color=#FF69B4}*In a haze of lust, you greedily touch her all over her body and grab her full breasts.*{/color}"

    scene day_01_hotel_room_stewardess_presex_scene_3 with dissolve
    "{color=#FF69B4}*Her voice is barely audible when she speaks to you.*{/color}"
    k "I want you deeper inside me."

    scene day_01_hotel_room_stewardess_presex_scene_4 with dissolve
    "{color=#FF69B4}*Shifting into a different position, she allows herself to be penetrated even deeper.*{/color}"
    "{color=#FF69B4}*The slap of skin on skin is audible every time your balls hit her wet pussy.*{/color}"

    call screen kelly_day_01_sex

label kelly_day_1_anal:

    hide screen kelly_day_01_sex

    scene day_01_hotel_room_stewardess_scene_anal_2 with dissolve
    mc "Kelly... Your ass is so perfect. I love it."
    k "You can fuck my ass if you want."
    "{color=#FF69B4}*The desire in her voice makes your cock even harder.*{/color}"
    "{color=#FF69B4}*Slowly and gently you push your member inch by inch inside her tight asshole.*{/color}"
    "{color=#FF69B4}*She moans with pleasure and opens her legs even further to allow you better access.*{/color}"
    mc "It's so tight."

    scene day_01_hotel_room_stewardess_scene_anal_1 with dissolve
    k "Push it deeper. DEEPER."
    k "Oh yes. Just like that, [player_name]."

    show kelly_anal_day_1 with dissolve

    mc "Are you going to cum for me, sexy?"
    k "Oh my God. YES...I am."

    scene day_01_hotel_room_stewardess_scene_anal_1 with flash
    with flash
    with flash
    "{color=#FF69B4}*Few more thrusts in her convulsing asshole and you're ready to cum too.*{/color}"

    call screen kelly_day_01_cumshot_anal

label kelly_day_1_cowgirl:

    hide screen kelly_day_01_sex

    scene day_01_hotel_room_stewardess_cowgirl_scene_1 with dissolve
    "{color=#FF69B4}*You make Kelly sit on your lap.*{/color}"
    "{color=#FF69B4}*She begins to ride your cock and her breasts bounces with the rhythm of her moves.*{/color}"

    show kelly_cowgirl_day_1 with dissolve
    mc "Are you going to cum for me, sexy?"
    k "Oh my God. YES...I am."

    scene day_01_hotel_room_stewardess_cowgirl_scene_1 with flash
    with flash
    with flash
    "{color=#FF69B4}*Few more thrusts in her convulsing pussy and you're ready to cum too.*{/color}"

    call screen kelly_day_01_cumshot_cowgirl

label cumshot_1_facial:

    hide screen kelly_day_01_cumshot_anal

    scene day_01_hotel_room_stewardess_scene_anal_1 with dissolve
    mc "I'm cumming."

    scene day_01_hotel_room_stewardess_scene_facial with dissolve
    "{color=#FF69B4}*Few more strokes. You pull out your cock and you make her sit in front of you.*{/color}"
    "{color=#FF69B4}*The torrent of your warm cum splashed on her breasts and face.*{/color}"
    mc "Oh my God..."
    mc "This was so intense."
    jump bed

label cumshot_1_back:

    hide screen kelly_day_01_cumshot_anal

    scene day_01_hotel_room_stewardess_scene_anal_4_ass_cumshot with dissolve
    "{color=#FF69B4}*You slowly pull out your cock out of Kelly and the warm torrent of your cum splashes on her back and ass.*{/color}"
    mc "Oh my God..."
    mc "This was so intense."
    jump bed

label cumshot_2_facial:

    hide screen kelly_day_01_cumshot_cowgirl

    scene day_01_hotel_room_stewardess_cowgirl_scene_1 with dissolve
    mc "I'm cumming."

    scene day_01_hotel_room_stewardess_scene_facial with dissolve
    "{color=#FF69B4}*You lift Kelly off your cock and you make her sit in front of you.*{/color}"
    "{color=#FF69B4}*The torrent of your warm cum splashes on her breasts and face.*{/color}"
    mc "Oh my God..."
    mc "This was so intense."
    jump bed

label cumshot_2_belly:

    hide screen kelly_day_01_cumshot_cowgirl

    scene day_01_hotel_room_stewardess_scene_belly_cumshot with dissolve
    "{color=#FF69B4}*You lift Kelly off your cock and the torrent of your warm cum splashed on her breasts and belly.*{/color}"
    mc "Oh my God..."
    mc "This was so intense."
    jump bed

label cumshot_2_creampie:

    hide screen kelly_day_01_cumshot_cowgirl

    scene day_01_hotel_room_stewardess_scene_creampie with dissolve
    "{color=#FF69B4}*Few more bounces. She pushes your cock even deeper inside her sweet pussy and the torrent of warm seed fills her fully.*{/color}"
    "{color=#FF69B4}*You pull out your cock and the seed slowly drips off her on the sheet.*{/color}"
    mc "Oh my God..."
    mc "This was so intense."
    $ kelly_creampie += 1
    jump bed

label bed:

    scene day_01_hotel_room_stewardess_scene_bed_1 with dissolve
    "{color=#D2691E}*She smiles at you with passion in her eyes.*{/color}"
    k "Yeah. Best sex of my life. I'm still trembling."
    k "Hold me tight."
    $ renpy.end_replay()

    scene day_01_hotel_room_stewardess_scene_bed_2 with dissolve
    "{color=#D2691E}*You embrace her tenderly and kiss her neck.*{/color}"
    mc "{color=#AFEEEE}*whisper in her ear*{/color} Stay for the night."
    k "I'm not going anywhere."

    scene day_01_hotel_room_stewardess_scene_bed_3 with dissolve
    "{color=#D2691E}*She cuddles to you even more and moans quietly*.{/color}"
    k "Good night stranger."
    mc "Hehe. Sleep well, sexy."
    "{color=#D2691E}*Wrapped in the scent of her body you fall asleep.*{/color}"
    jump lisa_jennifer

label lisa_jennifer:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_01_corridor_lisa_jennifer_room_scene_1 with dissolve
    "{color=#D2691E}*Lisa is about to open the door to her room when Jennifer spots her.*{/color}"
    j "Where the hell were you all day?"
    l "It's none of your damn business!"
    j "I'm your older sister and you should obey me."

    scene day_01_corridor_lisa_jennifer_room_scene_2 with dissolve
    "{color=#D2691E}*Lisa turns around with anger in her eyes.*{/color}"
    l "Are you kidding me? Obey you?"
    j "Don't cross that line, Lisa."
    l "Whatever... Leave me alone."
    j "I'm not done with you."

    scene day_01_corridor_lisa_jennifer_room_scene_2 with dissolve
    "{color=#D2691E}*With tears in her eyes Lisa yells at Jennifer.*{/color}"
    l "But I'm done with you... I HATE you."

    scene day_01_lisa_room_scene_1 with dissolve
    "{color=#D2691E}*Lisa enters her room and slams the door with anger.*{/color}"
    "{color=#D2691E}*Tears roll down her cheeks. She lies down on the bed.*{/color}"
    "{color=#D2691E}*She hides her head in her arms and she sobs quietly.*{/color}"
    l "Why has Jennifer been acting like a bitch recently?"
    l "She wasn't like that before."
    l "I can't lose [player_name] again. I won't let my stupid sisters make him leave."
    l "I HATE this family..."

    scene day_01_lisa_room_scene_2 with dissolve
    "{color=#D2691E}*She sits on the edge of the bed. She wipes her tears.*{/color}"
    l "I'll fight for him this time. I'll do everything I can, to keep him here with me."

    scene day_01_phone_lisa_rachel_1a with dissolve
    "{color=#D2691E}*She grabs her smartphone and makes a call.*{/color}"
    l "Hey bestie."
    l "I need your help. Could we meet tomorrow at our place?"
    r "Sure. What time?"
    l "10 am."
    r "I'll be there."
    l "Thanks."
    $ rachel_enabled = True
    $ changeWallpaper()

    scene black with dissolve
    show bg end_of_day_01 with dissolve
    $ renpy.pause ()
    jump day_02
