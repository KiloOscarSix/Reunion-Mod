label day_03:
    $ day = "Day 3"
    $ save_name = "Day 3"
    $ clara_late = False
    $ clara_useless = False
    $ changeWallpaper()

label day_03_office_scene:

    scene black with dissolve
    show bg day_03 with dissolve
    $ renpy.pause ()

    scene day_03_john_bedroom_alone_scene_2 with dissolve
    "{color=#81F79F}*I hate to wake up alone. I miss my two beautiful ladies very much.*{/color}"
    "{color=#81F79F}*I wish they were here with me. It would be much easier for me to deal with this mess if they were here.*{/color}"

    scene black with fade

    scene day_03_secretariat_scene_1 with dissolve
    mc "Good morning, Clara."
    c "Good morning, sir."
    mc "I want to see you in my office in 5 minutes."
    $ clara_enabled = True

    scene black with dissolve
    "{color=#D2691E}*45 minutes later.*{/color}"
    $ renpy.pause ()

    scene day_03_office_scene_1 with dissolve
    c "You wanted to see me, boss?"

    menu clara_reply_day_03:

        "{color=#74B2F4}Do you know what time is it?{/color} [ClaraSubmissionPath]":

            mc "Do you know what time is it?"
            c "Oh, I'm sorry."
            mc "You were supposed to be here 40 minutes ago!"
            mc "Why don't you respect me?"
            c "I'm sorry."
            mc "Should I treat you as you treat me?"
            c "It won't happen again."
            $ clara_submission += 1
            $ clara_late = True

        "{color=#74B2F4}Say nothing.{/color}":

            c "Can I do something for you?"

    scene day_03_office_scene_3a with dissolve
    mc "I have a task for you."
    mc "Make a list of all the people working in this company. Take into account the positions they hold in the company and for how long they have worked here."
    mc "I want it on my desk in two hours."

    scene day_03_office_scene_2a with dissolve
    c "Two hours, sir? How am I supposed to do it within two hours? I'm not a hiring manager..."

    if clara_late == True:

        menu clara_late_2:

            "{color=#74B2F4}You're useless.{/color} [ClaraSubmissionPath]":

                mc "You are completely useless."
                mc "Is that so hard to make a damn list?"

                scene day_03_office_scene_4 with dissolve
                mc "Why do I need a secretary who can't do a simple task?"
                c "I'm sorry."
                mc "Two hours, Clara. Not a minute longer."
                mc "Now, get out of my sight."
                $ clara_submission += 1
                $ clara_useless = True
                jump office_day_03

            "{color=#74B2F4}I don't know, Clara.{/color}":

                mc "I don't know, Clara."
                mc "Be innovative and think of something. There aren't a thousand people working in this company so I think you'll cope with this task."

                scene day_03_office_scene_4 with dissolve
                c "Okay..."
                mc "As soon as you're done, bring the list to me immediately."
                jump office_day_03

    else:

        mc "I don't know, Clara."
        mc "Be constructive and think of something. There aren't a thousand people working in this company so I think you'll cope with this task."

        scene day_03_office_scene_4 with dissolve
        c "Okay..."
        mc "As soon as you're done, bring the list to me immediately."

        jump office_day_03


label office_day_03:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_03_office_scene_10_sandra with dissolve
    s "Good morning."
    mc "Good morning."
    s "How are you doing?"

    scene day_03_office_scene_11_sandra with dissolve
    mc "I'm fine, thank you."
    s "You sure?  I feel like something's bothering you."
    mc "Eh...  You're right...  Clara brought me a lot of different documents and I don't know where to start."
    mc "Business management was never one of my favorite jobs."
    s "Well, until you get to know the specifics of the job, get to know people and have a vision of how to continue managing the company, that's how it's going to look."
    s "You'll see that in a few days it will be much easier for you."
    s "Besides, you have me, and I'll be happy to take care of everything."

    scene day_03_office_scene_12_sandra with dissolve
    mc "Thank you."
    mc "I hope we can handle this whole mess together."
    s "We just need some time and a plan of action."
    s "Where would you like to start?"
    mc "I don't know. I'm worried about Clara. I don't know if we can trust her."
    s "You're right. A trusted secretary is a fundamental part of any business."
    mc "So what? Should I fire her?"

    scene day_03_office_scene_11_sandra with dissolve
    s "How long has she been working here? Was she hired by your father or by Linda?"
    mc "I don't know, I didn't have time to check it out."
    s "Well, let's start with this. Ask Human Resources for her files."
    "A few minutes later."
    mc "Looks like she was hired a few months ago by Linda."
    s "That's what I was afraid of."

    menu clara_options:

        "{color=#74B2F4}So what do you suggest I should do?{/color} [SandraLovePath]":

            scene day_03_office_scene_14_sandra with dissolve
            mc "So what do you suggest?"
            s "I think you should hire a new secretary or even better - an assistant."
            mc "Yeah, but it's gonna take a lot of time to find the right candidate."
            s "I know, and we can't afford it."
            s "Actually, there is another solution. I've never practiced this before, but since we're working together, I think I can offer it."
            s "At least until you find a new secretary."
            mc "What do you mean?"

            scene day_03_office_scene_15_sandra with dissolve
            s "If you want, I can recommend someone to you."
            mc "Sure."
            s "I have a friend who recently lost her job, and I think she'll do great."
            mc "Good idea."

            scene day_03_sandra_office_scene_1 with dissolve
            mc "I'll keep Clara away from important things and keep an eye on her."
            s "At this point, firing Clara could cause unnecessary problems."
            mc "There is no time to waste. Call your friend and ask her to come here today."
            $ sandra_love += 1
            jump salary

        "{color=#74B2F4}Well, I guess I have to fire her.{/color}":

            scene day_03_office_scene_14_sandra with dissolve
            mc "Then I think I'll have to fire her and start looking for a new secretary."
            s "I don't think you should fire her right away. It could cause unnecessary problems."
            s "There could be more people like her."
            mc "You're right. I didn't think about it."

            scene day_03_office_scene_15_sandra with dissolve
            s "Until you find a new secretary, I can ask a friend of mine to help us."
            mc "I don't know."
            s "It's just an offer."

            scene day_03_sandra_office_scene_1 with dissolve
            mc "Well, maybe you're right."
            mc "Call her. Maybe she could show up here today."
            jump salary

label salary:

    scene day_03_sandra_office_scene_2 with dissolve
    mc "By the way. Did you prepare your contract?"

    scene day_03_sandra_office_scene_2a with dissolve
    s "Yes, you have it on your desk. I only had problems with my salary. I didn’t know how to set it up. Feel free to change it if you think it’s too much."

    menu salary_01:

        "{color=#74B2F4}I’m fine with it.{/color} [SandraLovePath]":

            scene day_03_sandra_office_scene_2a with dissolve
            mc "If you think it’s enough then I’m fine with it."
            s "Okay."
            $ sandra_love += 1
            jump safe

        "{color=#74B2F4}It’s way too much.{/color}":

            scene day_03_sandra_office_scene_2a with dissolve
            mc "I’ll agree for the half of your proposition."
            s "Okay. As you wish."
            jump safe

label safe:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_03_sandra_office_scene_3 with dissolve
    "*RING RING RING*"
    s "Hello?"
    "..."
    s "Okay."
    s "She is here."
    mc "Great. Let her come in."

    scene day_03_sandra_office_scene_4 with dissolve
    s "This is Isabella."
    mc "Very nice to meet you."
    i "Nice to meet you too, sir."
    mc "Sit down, please."
    i "Thank you very much for the chance. I'm not gonna let you down."
    mc "I understand you have experience in a similar job?"
    $ isabella_enabled = True

    scene day_03_sandra_office_scene_5 with dissolve
    i "Honestly, I've never worked as a secretary, but I worked as an assistant for a long time, so I think I can handle it."
    mc "That should be enough. I must admit that I'm counting on you. I'm trying to build up a team of skilled and trusted people to run this company."
    mc "You will be my personal assistant and I would like to rely on you as much as I can."
    i "Okay."

    scene day_03_sandra_office_scene_6 with dissolve
    s "I'm sure you'll find out very soon that Isabella is trustworthy."
    i "Thanks, Sandra."
    s "Hehe."
    i "I'm very disciplined and very dedicated to my duties."
    mc "I'm glad to hear that."

    scene day_03_sandra_office_scene_7 with dissolve
    mc "Since there is no office for you at the moment, you can work here with me and Sandra. I will try to find some place for you within next few days."
    i "That's fine. Please, don't worry about that."
    mc "Okay, so please go to the finance department and ask for bank statements for the past year. Oh, find out what kind of authorization system for banking operations is in place in the company."
    i "Of course. I'll get right on it."
    mc "That's good."

    scene day_04_office_sandra_scene_4 with dissolve
    c "Sir, the courier brought a package for you."
    mc "Bring it here and put it on my desk."

    scene day_03_sandra_office_scene_9 with dissolve
    mc "That's weird. Who could have sent me a package? Only a few people know I'm in town."
    s "The sender of the package should be marked on the package."
    s "There is nothing here."

    scene day_03_sandra_office_scene_10 with dissolve
    mc "Nevermind. I don't have time for this now."
    mc "I'll take care of it in my spare time."
    s "I'm sorry [player_name], but I have a lot of stuff to do still."
    mc "That's fine."

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_04_office_sandra_scene_4 with dissolve
    "{color=#D2691E}*You check what time is it. Then you call Clara.*{/color}"

    if clara_useless == True:

        menu clara_late_3:

            "{color=#74B2F4}Are you kidding me?{/color} [ClaraSubmissionPath]":

                scene day_04_office_sandra_scene_4 with dissolve
                mc "Clara, are you kidding me?"
                mc "You are late again."
                c "I'm sorry, five more minutes and you'll have it in your hands."
                mc "I'm waiting."

                scene day_03_office_scene_4 with dissolve
                "{color=#D2691E}*Ten minutes later Clara enters your office.*{/color}"
                mc "I can't believe that you are late again!"
                c "It was a hard task, sir."
                mc "I don't care! You failed me for second time today."
                mc "This is unacceptable."

                scene day_03_office_scene_1 with dissolve
                mc "You don't respect me. You think Linda's still in charge here?"
                mc "I tell you that Linda is the past and will never come back."
                mc "If you want to continue working here, you must follow my instructions."
                c "I get it."

                scene day_03_office_scene_3 with dissolve
                mc "I doubt that very much."
                mc "This is the last time you let me down."
                mc "If you let me down again, we'll talk differently."
                mc "Now, get out of my sight."
                "{color=#D2691E}*Clara leaves the office. She is upset and she doesn't even try to hide it.*{/color}"
                $ clara_submission += 1

            "{color=#74B2F4}This is the last warning.{/color}":

                scene day_03_office_scene_4 with dissolve
                mc "Clara, it's been two hours, and the list I asked you for is still not on my desk."
                c "I'm just finishing up. Literally, five more minutes and you'll have it in your hands."
                mc "Hurry up."
                mc "This is the last warning, Clara."

                scene day_03_office_scene_3 with dissolve
                mc "If you want to continue working here, start following my instructions."
                c "I will, sir."
                "{color=#D2691E}*Clara leaves the office. She is upset and she doesn't even try to hide it.*{/color}"

    else :

        scene day_03_office_scene_4 with dissolve
        mc "Clara, it's been two hours, and the list I asked you for is still not on my desk."
        c "I'm just finishing up. Literally, five more minutes and you'll have it in your hands."
        mc "Hurry up."
        mc "This is the last warning, Clara."
        "{color=#D2691E}*Clara leaves the office. She is upset and she doesn't even try to hide it.*{/color}"

    scene black with dissolve
    $ renpy.pause ()

    scene day_03_sandra_office_scene_11 with dissolve
    s "What did Clara want?"
    mc "She made the list of all people hired in the company with the positions they hold in the company and for how long they work here."
    mc "I have to go to HR and verify this list."
    s "Let me do it."
    "{color=#D2691E}*Sandra comes back after a while.*{/color}"

    scene day_03_office_scene_10_sandra with dissolve
    s "Three people are missing from her list."
    mc "Do you know what kind of employees they are?"
    s "No, but I will go over their files."

    scene day_03_office_scene_14_sandra with dissolve
    mc "I wonder why she didn't include them."
    s "Do you think she did it on purpose to make them suspicious?"

    scene day_03_office_scene_15_sandra with dissolve
    s "Maybe that's how she's trying to distract us from her?"
    mc "It's quite possible."
    s "We have to be careful with her. If she actually did it on purpose and still works for Linda, we might have a lot of problems with her."
    mc "Yes, any employee can be bribed, blackmailed or anything else by Linda and can harm us."
    jump lisa

label lisa:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_03_office_scene_13_sandra with dissolve
    l "Hey, [player_name]!"
    mc "Hey, Lisa."
    mc "Sandra, I'm going with Lisa for lunch. I'll be back in an hour."
    s "Sure. Have fun."
    jump lisa_compliment_day_03

label lisa_compliment_day_03:

    scene day_03_park_scene_1 with dissolve
    "{color=#D2691E}*You and Lisa leave the building. Lisa is smiling at you.*{/color}"

    menu compliment_lisa_1:

        "{color=#74B2F4}Compliment her.{/color} [LisaLovePath]":

            scene day_03_park_scene_2 with dissolve
            mc "You look like an angel today."
            l "Oh! Thank you. That's so sweet."
            $ lisa_love += 1
            jump street

        "{color=#74B2F4}Praise the weather.{/color}":

            scene day_03_park_scene_2 with dissolve
            mc "Hmm. The weather today is wonderful."
            l "I guess."
            jump street

label street:

    scene day_03_park_scene_1 with dissolve
    mc "So, what do you want to do?"
    l "I don't know."
    mc "Hmm. I'm hungry. Let's find some quiet place with good food."
    l "Sure, I think I know a place like that."
    mc "Great, let's go."
    jump restaurant


label restaurant:

    scene day_03_icecream_entrance_scene_0 with dissolve
    "{color=#D2691E}*You're slowly walking down the street to the nearest restaurant.*{/color}"
    l "I love this place. They have delicious ice cream and shakes here."

    scene day_03_icecream_entrance_scene_1 with dissolve
    "{color=#D2691E}You're going inside. Lisa sits down at the table.{/color}"
    mc "So, what would you like to eat?"
    l "Hmmm. A big chocolate shake for me."
    mc "Same for me."
    waitress "Of course, I'll bring you the order right away."
    mc "Thank you."
    jump table

label table:

    scene day_03_icecream_scene_1b with dissolve
    waitress "Here is your order, sir."
    mc "Thank you."

    scene day_03_icecream_scene_2 with dissolve
    l "It looks delicious."
    mc "And it tastes delicious too."
    l "Hehe."
    jump restaurant_shake

label restaurant_shake:

    menu restaurant_choices_1:

        "{color=#74B2F4}Ask her about her day.{/color}" if day_03 == False:

            scene day_03_icecream_scene_2 with dissolve
            mc "How's your day been?"
            l "So far it's boring. Nothing is happening. I was waiting to see you. I like spending time with you."
            l "It's a pity that we have so little of it for each other."
            l "The weekend is coming up. Maybe we can do something interesting together."

            scene day_03_icecream_scene_1 with dissolve
            mc "That would be great."
            l "Really?"

            scene day_03_icecream_scene_1d with dissolve
            mc "Of course, Lisa."
            mc "What would you like to do?"

            scene day_03_icecream_scene_1 with dissolve
            l "I heard from a friend of mine that there's a great movie in the cinema. Why don't we go?"
            mc "That's a great idea."
            $ day_03 = True
            jump restaurant_choices_1

        "{color=#74B2F4}Ask her about her plans for the day.{/color}" if plans_day_03 == False:

            scene day_03_icecream_scene_2 with dissolve
            mc "What are your plans for today?"
            l "To be honest, I don't have any plans."

            scene day_03_icecream_scene_1 with dissolve
            l "I'll probably meet up with Rachel."
            mc "Who is Rachel?"
            l "She is my best friend. I haven't told you about her before?"

            scene day_03_icecream_scene_1d with dissolve
            mc "Maybe you did."
            mc "What do you usually do when you are with her?"

            scene day_03_icecream_scene_1 with dissolve
            l "Different things. We go to the gym, sometimes to the pool, but mostly we hang out in our secret place."
            mc "It sounds interesting."
            $ plans_day_03 = True
            jump restaurant_choices_1

            if  plans_day_03 == True and day_03 == True:
                jump restaurant_shake_2

label restuarant_shake_2:

    menu restaurant_choices_2:

        "{color=#74B2F4}Ask her about Jennifer.{/color}" if jennifer_day_03 == False:

            scene day_03_icecream_scene_1 with dissolve
            mc "Any news on the Jennifer case?"
            l "Unfortunately not."
            mc "That's a pity. I thought maybe you had time to talk to her."
            l "I wanted to, but she wasn't home all afternoon yesterday. My mother came home and there was no more opportunity after that."
            l "But I'll try to talk to her today."

            scene day_03_icecream_scene_2 with dissolve
            mc "That would be great. Tell her I'd like to meet with her."
            l "This is a good idea. You can see that Jennifer is hesitant about how she should behave towards you."
            mc "That's right. We have to use it to convince her that I have no bad intentions for her or you."
            l "No matter what, I'll talk to her today."
            mc "Thank you."
            $ jennifer_day_03 = True
            jump restaurant_choices_2

        "{color=#74B2F4}Ask her about Nicole.{/color}" if nicole_day_03 == False:

            scene day_03_icecream_scene_1 with dissolve
            mc "How is Nicole doing?"
            l "To be honest, I have no idea. She is a mystery to me."
            l "She's hardly at home, she doesn't talk to any of us. Sometimes she will talk to our mom, but rarely. I don't know what to tell you about her. She has changed a lot since she graduated."
            l "I don't know if she's met a guy and that's why she's acting like one, or if it's the result of hanging out with the worst bunch of morons in town."
            mc "Hmm. Tough stuff. I have no idea what to do with it."

            scene day_03_icecream_scene_2 with dissolve
            l "Neither do I. I doubt she would want to talk to me at all, especially about you."
            mc "Maybe I have to see what kind of people she meets and what she does all day long? Maybe then we can find a way to get her to open up to us."
            l "I don't think you have any other choice."
            $ nicole_day_03 = True
            jump restaurant_choices_2

        "{color=#74B2F4}Ask her about Linda.{/color}" if linda_day_03 == False:

            scene day_03_icecream_scene_1 with dissolve
            mc "What about Linda?"
            l "I don't know. We don't see each other very often. And we hardly talk to each other anymore. Mother is not interested in us at all. She has her affairs and does nothing else."
            l "By the way, tell me, do you know how you will get back at her?"
            mc "No. But I'm still working on it. I'll let you know when I know what I'm going to do."

            if lisa_love >= 4:

                scene day_03_icecream_scene_2 with dissolve
                l "Don't worry about me. After what you told me yesterday, you can do whatever you want with her. I don't care at all."
                mc "Are you sure? After all, she's your mother...."
                l "So what? What is this mother who makes her daughters suffer because of her, and she lies to them all the time and is not interested in them at all?"
                mc "You are right."
                l "She doesn't deserve anything good. If I could, I'd take revenge on her myself."

            else:

                scene day_03_icecream_scene_2 with dissolve
                l "I know you hate her, but please don't hurt her."
                mc "I will try, I promise."
                l "Okay. Thank you."

            $ linda_day_03 = True
            jump restaurant_choices_2

            if linda_day_03 == True and nicole_day_03 == True and jennifer_day_03 == True:
                jump holding_hands_lisa

label holding_hands_lisa:

    scene day_03_icecream_scene_1a with dissolve
    "{color=#D2691E}*Lisa smiles at you flirtatiously and shyly touches your hand.*{/color}"

    menu holding_hands_lisa_01:

        "{color=#74B2F4}Let her hold your hand.{/color} [LisaLovePath]" if lisa_love >= 5:

            scene day_03_icecream_scene_1a with dissolve
            $ renpy.pause ()
            $ lisa_love += 1

            jump goodbye_lisa

        "{color=#74B2F4}Take your hand away.{/color}":

            scene day_03_icecream_scene_3 with dissolve
            $ renpy.pause ()

            jump goodbye_lisa1

label goodbye_lisa:

    scene day_03_icecream_scene_1a with dissolve
    l "Will you come to see us today?"
    mc "Unfortunately, I can’t today. I have a lot of work in the company and I’ll probably finish very late."
    mc "I also have one meeting in the evening and I don't know when it will end."
    l "Sure, [player_name]."

    scene day_03_icecream_scene_4 with dissolve
    mc "See you tomorrow then. Love you."
    l "Love you too. Bye."
    jump sandra_meeting

label goodbye_lisa1:

    scene day_03_icecream_scene_3 with dissolve
    l "Will you come to see us today?"
    mc "Unfortunately, I can’t today. I have a lot of work in the company and I’ll probably finish very late."
    mc "I also have one meeting in the evening and I don't know when it will end."
    l "Sure, [player_name]."
    mc "Bye."
    jump sandra_meeting

label sandra_meeting:

    scene black with dissolve
    show bg one_hour_later with dissolve
    $ renpy.pause ()

    scene day_03_sandra_office_scene_1a with dissolve
    s "How was lunch?"
    mc "Great. Did something happen while I was out?"
    s "Nothing interesting happened. I started to look through the employees' files and made a preliminary plan for the interviews. It will take me a few days."
    mc "Do you need that much time? You know we risk a lot. The longer it lasts, the greater the chance of someone harming us."

    scene day_03_sandra_office_scene_2 with dissolve
    s "I know, but interviews take time. I can't do it in five minutes. I'll try to finish this as soon as possible."
    mc "All right, then. I trust that you know what you are doing."
    s "I hope so."
    s "Isabella was here. She left you some documents on the desk. I told her to go home, because she had something already planned for today, but she will be here tomorrow."
    mc "Okay, that's fine."

    scene day_03_sandra_office_scene_1 with dissolve
    "{color=#D2691E}*You sit at your desk. You notice that Sandra is not happy with the way things are going.*{/color}"

    menu sandra_choice_1:

        "{color=#74B2F4}I see something is bothering you.{/color} [SandraLovePath]":

            mc "I see something is bothering you."
            s "No, everything's all right."
            mc "If you don't want to, I won't fire anyone."
            s "That's not the point."
            mc "So what's going on?"
            $ sandra_love += 1

        "{color=#74B2F4}Say nothing.{/color}":

            mc "..."

    scene day_03_sandra_office_scene_3 with dissolve
    s "I'd like to ask you something, but I don't know if I can."
    mc "You can ask me anything you want."
    s "I know, but it's not that simple."

    scene day_03_sandra_office_scene_11 with dissolve
    "{color=#D2691E}*You get up from behind a desk and walk up to her.*{/color}"
    mc "What's going on?"
    s "I wanted to thank you for letting me work with you. And I thought maybe you'd come to dinner with me tonight?"

    scene day_03_sandra_office_scene_13 with dissolve
    "{color=#D2691E}*Seeing the surprise on your face, Sandra turns around and wants to leave.*{/color}"
    "{color=#D2691E}*You grab her and hold her.*{/color}"
    mc "Please, wait."

    scene day_03_sandra_office_scene_15
    s "I'm sorry, I shouldn't have asked you that. You are my boss."

    menu date_with_sandra_day_03:

        "{color=#74B2F4}Go out to the dinner with her tonight.{/color} [SandraLovePath]":

            scene day_03_sandra_office_scene_11 with dissolve
            mc "Oh, come on. Of course, I'll go to the dinner with you."
            mc "You have nothing to be ashamed of. Does it matter that I'm your boss?"

            scene day_03_sandra_office_scene_14 with dissolve
            s "I guess not."
            mc "What time should I pick you up?"
            s "Around 8:00 p.m.?"
            mc "Perfect. "
            s "Here is my address."

            scene day_03_sandra_office_scene_12 with dissolve
            "{color=#D2691E}*You notice that Sandra regains her self-confidence and a smile appears on her face.*{/color}"
            mc "Well, I guess we have to get going. It is almost 4:00 p.m. already."
            s "Sure. See you in 4 hours."
            $ sandra_love += 1
            $ s_dinner_day_3 = True
            jump park_nicole

        "{color=#74B2F4}Tell her that this is not a good idea.{/color} [EndRelationship]":

            scene day_03_sandra_office_scene_13 with dissolve
            mc "Yes, I'm your boss. You shouldn't have asked me that."
            s "I'm really sorry. I don't know what I was thinking."
            s "Please, forgive me."
            mc "Okay, but let this be the last time you ask me that."
            s "Of course."
            $ sandra_love -= 1
            $ sandra_no_love = True
            jump park_nicole

label park_nicole:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_03_nicole_park_scene_1 with dissolve
    "{color=#D2691E}*Nicole, as usual, does her exercises in the park at this time of day.*{/color}"

    scene day_03_nicole_park_scene_2 with dissolve
    "{color=#D2691E}*A phone rings.*{/color}"
    n "For fuck sake. Not him again…"

    scene day_03_nicole_park_scene_3 with dissolve
    "{color=#D2691E}*Phone is ringing again.*{/color}"
    n "Leave me alone!"

    scene day_03_nicole_park_scene_4 with dissolve
    sms "Pick up the phone or you’ll regret it."

    scene day_03_nicole_park_scene_5 with dissolve
    "{color=#D2691E}*The phone rings for the third time.*{/color}"
    n "What do you want from me?"
    stranger "Don't you know? Do we have to go through it every single time?"
    n "Fuck you!"
    stranger "Such a language. A young lady like you shouldn’t be using such awful words."
    n "Fuck you!"

    scene day_03_nicole_park_scene_6 with dissolve
    stranger "You have two days to pay me $5,000 or you know what will happen."
    n "Did you lose your mind? $5,000 in two days?"
    stranger "Yep. Same time, the same place."
    n "I need more time!"
    stranger "See you in two days."

    scene day_03_nicole_park_scene_7 with dissolve
    n "FUCK!"
    n "What am I going to do now?"
    n "Where can I borrow $5,000? Goddamnit. Why is this happening to me?"

    scene day_03_nicole_park_scene_8 with dissolve
    n "Why was I so damn stupid…"
    jump hair_salon_day_03

label hair_salon_day_03:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_03_hair_salon_scene_1 with dissolve
    r "You're late!"
    l "Yes, I know, I'm sorry."
    r "Did you decide to change your hairstyle?"
    l "That's why I'm here!"

    scene day_03_hair_salon_scene_3 with dissolve
    r "But you're not convinced?"
    l "Of course, I'm not convinced."

    scene day_03_hair_salon_scene_4 with dissolve
    "{color=#D2691E}*The girls enter the hair salon. The hairdresser greets them and shows Lisa where to sit.*{/color}"
    ha "Did you choose a style yet, miss?"
    l "I was thinking about a pixie cut."

    scene day_03_hair_salon_scene_5 with dissolve
    "{color=#D2691E}*Lisa shows the photo to the hairdresser.*{/color}"
    l "Something like this."
    r "That's a good choice. You'll look beautiful in this hairstyle."

    menu haircut:

        "{color=#74B2F4}I'm sorry, but I can't do this.{/color}":

            "{color=#D2691E}*Lisa looks terrified as the hairdresser prepares to cut her long hair.*{/color}"
            "{color=#D2691E}*She can't stand this any more and she finally breaks off the chair.*{/color}"

            scene day_03_hair_salon_scene_6_lh with dissolve
            l "I'm very sorry, but I can't do that."
            r "Don't worry. If you are not convinced, don't do this."
            l "I thought I wanted it, but I just can't do it."
            r "All right. Let's get out of here."

            scene day_03_hair_salon_scene_9_lh with dissolve
            "{color=#D2691E}*The girls go out of the hair salon.*{/color}"
            r "So, how's [player_name]?"
            l "He is wonderful. We met yesterday at my house and talked for a long time. He explained many things to me. I know why he left 10 years ago."
            r "Well, that's great. So, for now, everything is going your way?"
            l "That's what it looks like. We made a date to go to the cinema on Friday."

            scene day_03_hair_salon_scene_10_lh with dissolve
            r "That's great."
            l "But that's not what I'm worried about."
            r "Of course, you and your fears. Why don't you just say for once that you're not worried about anything..."

            scene day_03_hair_salon_scene_11_lh with dissolve
            "{color=#D2691E}*Lisa looks very worried. Rachel's remarks only deepen her sadness.*{/color}"
            l "Stop it. I'm serious..."
            r "All right, then. What is it this time?"
            l "Because, you know... I'm still a virgin...."
            r "So what?"

            scene day_03_hair_salon_scene_12_lh with dissolve
            l "And I don't know if he's going to want me like that."
            r "God damn it, woman. Pull yourself together. Why would he mind? Do you even know anything about men? They love virgins. They are excited to think that they will be your first lover. That they will make you a woman."
            r "Nowadays, being a virgin is something very rare. It's an asset, not a flaw, so for God's sake stop worrying about it."
            l "All right, then. Maybe you're right."

            scene day_03_hair_salon_scene_13_lh with dissolve
            "{color=#D2691E}*Rachel is already tired of Lisa's whining.*{/color}"
            r "Lisa, I love you, but I'm sick and tired of listening to you whining. You are a beautiful, young woman, for whom many men would kill themselves. And you're still just worried about everything."
            r "I've had enough of this. Your lack of self-confidence will kill you one day."

            scene day_03_hair_salon_scene_15_lh with dissolve
            l "Stop it. You know how much I care about him. And instead of helping me, you're still teasing me! I haven't slept with any guy yet and I don't know what to do."
            l "You've already had several of them and it's easy for you to make fun of me."
            l "Maybe it's because you're jealous?"
            "{color=#D2691E}*Lisa turns around and without a word walks away.*{/color}"

            jump emily_sandra_day_03


        "{color=#74B2F4}Ehh... Let's do this.{/color} [gr]\[Haircut\]":

            scene black with dissolve
            $ hair = ""
            "{color=#D2691E}*Lisa closes her eyes and doesn't watch the hairdresser cut her long hair.*{/color}"
            "{color=#D2691E}*After a while, the hairdresser says.*{/color}"
            ha "Okay. I'm done. You can now open your eyes."

            scene day_03_hair_salon_scene_6 with dissolve
            "{color=#D2691E}*Lisa is slowly opening her eyes. She is terrified. But when she looks in the mirror, a wide smile appears on her face.*{/color}"
            l "Hmm. I like it, I really do."
            l "Rachel, what do you think?"

            scene day_03_hair_salon_scene_7 with dissolve
            r "I like it too. I think you look gorgeous and very sexy."
            l "Really?"
            r "Yes. I like your new look. The hairstyle matches you perfectly."
            scene black with fade
            "{color=#D2691E}*The girls go out of the hair salon.*{/color}"

            scene day_03_hair_salon_scene_9 with dissolve
            r "So, how's [player_name]?"
            l "He is wonderful. We met yesterday at my house and talked for a long time. He explained many things to me. I know why he left 10 years ago."
            r "Well, that's great. So, for now, everything is going your way?"
            l "That's what it looks like. We made a date to go to the cinema on Friday."

            scene day_03_hair_salon_scene_10 with dissolve
            r "That's great."
            l "But that's not what I'm worried about."
            r "Of course, you and your fears. Why don't you just say for once that you're not worried about anything..."

            scene day_03_hair_salon_scene_11 with dissolve
            "{color=#D2691E}*Lisa looks very worried. Rachel's remarks only deepen her sadness.*{/color}"
            l "Stop it. I'm serious..."
            r "All right, then. What is it this time?"
            l "Because, you know... I'm still a virgin...."
            r "So what?"

            scene day_03_hair_salon_scene_12 with dissolve
            l "And I don't know if he's going to want me like that."
            r "God damn it, woman. Pull yourself together. Why would he mind? Do you even know anything about men? They love virgins. They are excited to think that they will be your first lover. That they will make you a woman."
            r "Nowadays, being a virgin is something very rare. It's an asset, not a flaw, so for God's sake stop worrying about it."
            l "All right, then. Maybe you're right."

            scene day_03_hair_salon_scene_13 with dissolve
            "{color=#D2691E}*Rachel is already tired of Lisa's whining.*{/color}"
            r "Lisa, I love you, but I'm sick and tired of listening to you whining. You are a beautiful, young woman, for whom many men would kill themselves. And you're still just worried about everything."
            r "I've had enough of this. Your lack of self-confidence will kill you one day."

            scene day_03_hair_salon_scene_15 with dissolve
            l "Stop it. You know how much I care about him. And instead of helping me, you're still teasing me! I haven't slept with any guy yet and I don't know what to do."
            l "You've already had several of them and it's easy for you to make fun of me."
            l "Maybe it's because you're jealous?"
            "{color=#D2691E}*Lisa turns around and without a word walks away.*{/color}"

            $ haircut = True

            jump emily_sandra_day_03

label emily_sandra_day_03:

    if sandra_no_love == True:

        jump lisa_room_day_03

    else:

        scene black with dissolve
        show bg in_the_meantime with dissolve
        $ renpy.pause ()

        scene day_03_phone_sandra_emily_1 with dissolve
        s "Hey."
        em "How are you doing?"
        s "I need your help..."
        em "What happened?"
        s "I don't know what to wear to a dinner with [player_name]."
        em "Sure, I'll be right there."
        s "Thanks, I'm waiting."

        scene black with fade
        "{color=#D2691E}*15 minutes later Emily drives up to Sandra's house.*{/color}"

        scene day_03_sandra_bedroom_scene_1 with dissolve
        em "So, [player_name] invited you on a date? Finally!"
        s "This is not a date! And I invited [player_name] to dinner to thank him for hiring me."
        em "HAHA. Sure. You and your excuses."
        s "Seriously, Emily. Do you always have to make fun of me?"
        s "I haven't been anywhere in so many years. I'm stressed enough and I don't need your comments."
        em "All right. Don't get so upset with me."
        em "Let's see what's in your closet."

        scene day_03_sandra_bedroom_scene_1 with dissolve
        "{color=#D2691E}*Emily carefully looks at the clothes in Sandra's closet. She pulls out a few dresses and puts them on the bed.*{/color}"
        em "All right. Try these three dresses on. Let's see which one you look the best in."
        "{color=#D2691E}*Sandra is trying on her first dress.*{/color}"

        scene day_03_sandra_bedroom_scene_2 with dissolve
        s "What do you think?"

        scene day_03_sandra_bedroom_scene_3 with dissolve
        em "Not bad. But try another one."

        scene day_03_sandra_bedroom_scene_4 with dissolve
        "{color=#D2691E}*Sandra is trying on another dress. She looks in the mirror and there is a grimace of dissatisfaction on her face.*{/color}"
        s "I don't know. Don't you think it reveals too much?"

        scene day_03_sandra_bedroom_scene_5 with dissolve
        em "Absolutely not. It could even reveal a little more. Try this one on."

        scene day_03_sandra_bedroom_scene_6 with dissolve
        "{color=#D2691E}*Sandra is trying on the last dress.*{/color}"
        s "There's no way I'm going anywhere in it."
        em "Oh, come on. You look great. I guarantee you that your boss will be delighted."
        s "I have no doubts. But that doesn't change the fact that I'm not going anywhere in this dress."
        em "If you care about him, you will wear it."
        em "You have a beautiful body and you have nothing to be ashamed of. Wear this dress."
        em "He has already managed to appreciate your intellect, now it is time to appreciate your beauty."
        s "All right."

        scene day_03_sandra_bedroom_scene_7 with dissolve
        "{color=#D2691E}*The girls hear a knock on the door.*{/color}"
        s "It's definitely him, and I'm not ready."
        em "Get ready and I will go to him."
        s "Thank you."

        scene day_03_sandra_bedroom_scene_8 with dissolve
        mc "Good evening, is Sandra here?"
        em "Good evening. My name is Emily. I'm a friend of Sandra's. "

        scene day_03_sandra_bedroom_scene_9 with dissolve
        mc "I am [player_name]."
        em "Sandra will be ready soon."

        scene day_03_sandra_bedroom_scene_10 with dissolve
        "{color=#D2691E}*Emily is looking at you closely. After a while, she asks.*{/color}"
        em "Don't we know each other by any chance? [player_name] [player_surname], right?"

        menu emily_first_meet:

            "{color=#74B2F4}I'm sorry, but I don't recall that we'd ever meet.{/color}":

                scene day_03_sandra_bedroom_scene_10 with dissolve
                mc "Yes... I'm sorry, but I don't recall that we'd ever meet."
                em "I remember you. We went to the same school. I think we even had some classes together."
                mc "I'm sorry, but I don't remember you."

            "{color=#74B2F4}Yes, I remember you. We went to the same school.{/color} [EmilyLovePath]":

                scene day_03_sandra_bedroom_scene_10 with dissolve
                mc "I remember you. We went to the same school. I think we even had some classes together."
                em "Yes, you are right."
                mc "It's good to see you again after all these years."
                $ emily_love += 1

                menu emily_compliment:

                    "{color=#74B2F4}You've grown into a beautiful woman.{/color} [EmilyLovePath]":

                        scene day_03_sandra_bedroom_scene_10 with dissolve
                        mc "I wasn't sure it was you for a while."
                        mc "You've grown into a beautiful woman."
                        em "Oh, thank you."
                        $ emily_love += 1

                    "{color=#74B2F4}Say nothing.{/color}":

                        scene day_03_sandra_bedroom_scene_10 with dissolve
                        "{color=#D2691E}*Emily is watching you closely and you feel like she wants to say something.*{/color}"

        scene day_03_sandra_bedroom_scene_11 with dissolve
        "{color=#D2691E}*At that moment Sandra stands in the doorway.*{/color}"
        em "I'm leaving now, have a great evening"

        scene day_03_sandra_home_scene_4 with dissolve
        mc "You look amazing in that dress."
        s "I was hoping you'd like it."

        scene day_03_sandra_home_scene_3 with dissolve
        "{color=#D2691E}*You give Sandra a bouquet of roses.*{/color}"
        s "Oh. They are beautiful. Thank you."
        mc "Beautiful flowers for a beautiful lady."
        mc "There's a cab waiting. If you are ready, we can go."

        scene black with fade
        "{color=#D2691E}*You get in the taxi. Sandra hands the driver a card with the address.*{/color}"
        "{color=#D2691E}*Ten minutes later you are there.*{/color}"
        "{color=#D2691E}*You go inside and the waiter shows you to your seat.*{/color}"

        scene day_03_sandra_restaurant_scene_1 with dissolve
        mc "I must admit that you have chosen an interesting place."
        s "I've never been here before, but Emily recommended this restaurant to me."

        scene day_03_sandra_restaurant_scene_2 with dissolve
        s "I am very happy that you came to dinner with me."
        mc "How could I refuse you?"
        s "You know... I haven't been anywhere in such a long time."
        mc "Why?"

        scene day_03_sandra_restaurant_scene_3 with dissolve
        s "I never had time for private life. Still only work and work. I have no time for anything."
        mc "Such a beautiful woman without a private life? I don't believe it."
        s "Well, my career has always been more important."

        jump questions_day_03

label questions_day_03:

    menu questions:

        "{color=#74B2F4}Ask her about her business.{/color}" if business == False:

            scene day_03_sandra_restaurant_scene_2 with dissolve
            mc "I wonder why you accepted my offer without hesitation? I thought you'd need some time to think about it."
            s "Well, there was nothing to think about. My business was more loss-making than profit-making. In fact, I had no choice."
            mc "I don't understand. How did you get into financial trouble?"

            scene day_03_sandra_restaurant_scene_3 with dissolve
            s "I never wanted to work for a corporation. My dream was to help the needy, mainly disadvantaged women. Everything was going great."
            s "My law firm was thriving. One day a woman came to me who claimed that a certain company poisons the water that the inhabitants of the town drink."
            s "Toxins in the water caused various diseases, but mainly cancer. Her son fell ill and died."
            s "I took up the case because the woman wanted to get compensation from the corporation for her son's death."
            s "The corporation did not want to agree to any settlement and a trial took place."

            scene day_03_sandra_restaurant_scene_2 with dissolve
            s "During the trial it turned out that people from political circles were involved in the case and that huge amounts of money were involved."
            s "Most likely, witnesses were bribed because one by one they refused to testify, and those who stood before the court did not confirm what they told me before the trial."
            s "The result was that we lost the case. I lost a lot of money and a reputation for which I had worked for so long."
            s "After the trial, the clients stopped coming and I had nothing to pay the bills for. And then you came up with your proposal."
            s "There was nothing to think about. After a few months without customers and money, I had to put my ambitions aside and start earning money again."

            scene day_03_sandra_restaurant_scene_3 with dissolve
            s "Thank you."
            $ business = True
            jump questions_day_03

        "{color=#74B2F4}Ask her about her private life.{/color}" if private_life == False:

            scene day_03_sandra_restaurant_scene_2 with dissolve
            mc "I still can't believe you don't have a private life."
            s "It just so happened. First law studies, then practice in a law firm, and now my own company. I just didn't have time."
            s "Besides, my career was more important. Now I regret it, but unfortunately, I will not get that time back."

            scene day_03_sandra_restaurant_scene_3 with dissolve
            mc "Didn't you miss it?"
            mc "I can't imagine not having a private life."
            s "Of course I did. If I hadn't met Emily, I would have been all alone for the last few years."
            $ private_life = True
            jump questions_day_03

        "{color=#74B2F4}Ask her about men in her life.{/color}" if life == False:

            scene day_03_sandra_restaurant_scene_2 with dissolve
            mc "How come you're not dating anyone?"
            s "Well... I've never been lucky with men."
            mc "Why?"
            s "I don't know if I want to talk about it."
            mc "I'm not pushing you, but if you would like to I will listen."
            "{color=#D2691E}*You notice that Sandra is sad.*{/color}"

            scene day_03_sandra_restaurant_scene_4 with dissolve
            mc "I'm sorry, I didn't mean to upset you."
            s "That's okay. It just brought back some bad memories."
            "{color=#D2691E}*Sandra keeps silent for a while, staring at some point above your head, and then she speaks.*{/color}"

            scene day_03_sandra_restaurant_scene_4 with dissolve
            s "Twelve years ago, right after graduation, I went to a party with my friends. There was this one boy... All the girls were crazy about him."
            s "Somehow it happened that we were having fun together. He complimented me, told me that I was beautiful and such. I was enchanted by him."
            s "I, the least popular girl in school, was having fun with the most popular boy in school, the captain of the football team."
            s "A few drinks later we found ourselves in the men's room. We were kissing when he started undressing me."
            s "I tried to protest, but I was too drunk. He finally gave me a break. He yelled at me, called me a stupid whore and left."
            s "Horror only began on the next day. Someone recorded it all and uploaded the videos to the Internet."
            s "I have become the laughing stock of the whole city. It was a nightmare. I reported the case to the police, but they dropped the investigation for lack of evidence."
            s "I'm sure everything was set up and he did that on purpose to humiliate me."
            s "Since then, I have not been involved with any men. In fact, you're the first one I went out with alone, without Emily."
            "{color=#D2691E}*When Sandra finished talking, tears were running down her cheeks. You approached her. She got up and cuddled up to you.*{/color}"

            scene day_03_sandra_restaurant_scene_5 with dissolve
            mc "I'm very, very sorry."
            mc "I don't even know what to say to comfort you."
            s "You don't have to say anything. It is enough that you are here with me."
            mc "The police didn't find those who did this to you?"
            s "No. The investigation lasted maybe a month and was discontinued. I appealed against this decision but it didn't help."
            mc "Fucking bastards. If only I could get my hands on them."
            s "Oh, come on. It's been so many years. I don't want to go back to that."
            mc "Okay."
            $ life = True
            jump questions_day_03

            if business = True and private_life = True and life = True:
                jump dance

label dance:

    scene day_03_sandra_restaurant_scene_9 with dissolve
    s "Let's dance."
    mc "I don't know. I suck at it."
    s "Don't make me beg you."
    mc "All right, then."

    scene black with fade
    "{color=#D2691E}*You're starting to dance to some romantic song.  Sandra is cuddling up to you very tightly.  You can feel the warmth of her body and the scent of her perfume.*{/color}"
    "{color=#D2691E}*You enjoy every moment, but somewhere deep down you can't accept what you heard from Sandra. You decide to act and find those who did it to her.*{/color}"
    jump good_night_day_03


label good_night_day_03:

    scene day_03_sandra_restaurant_scene_5 with dissolve
    s "Thank you so much for a wonderful evening."
    mc "The pleasure is all mine."

    menu goodnight_sandra_1:

        "{color=#74B2F4}Kiss her.{/color} [SandraLovePath]" if sandra_love >= 3: #(+1 LOVE and HAREM)

            scene day_03_sandra_restaurant_scene_7 with dissolve
            "*KISS*"
            "{color=#D2691E}*You're taking a taxi back to Sandra's house. You walk her to the door.*{/color}"

            scene day_03_sandra_home_scene_4 with dissolve
            mc "Good night, sexy."
            s "Sleep tight."
            $ sandra_love += 1
            jump lisa_room_day_03

        "{color=#74B2F4}Hug her.{/color}":

            scene day_03_sandra_restaurant_scene_11 with dissolve
            "*HUG*"
            jump lisa_room_day_03

label lisa_room_day_03:

    scene black with dissolve
    show bg few_hours_later with dissolve
    $ renpy.pause ()

    scene expression "day_03_lisa_room_scene_1[hair]" with dissolve
    "{color=#D2691E}*KNOCK* *KNOCK*{/color}"
    j "Lisa, are you awake?"
    l "Yes."
    j "Can I come in?"
    l "Of course."

    scene day_03_lisa_room_scene_2 with dissolve
    l "Oh my God, Jennifer. What happened? Why are you crying again?"
    j "Don’t worry about it. It’s nothing."
    l "Yeah, nothing. Look at your face, it doesn’t look like it was nothing."
    j "I don’t want to talk about it."

    scene day_03_lisa_room_scene_3 with dissolve
    j "Can I sleep here with you tonight? I don’t want to be alone."
    l "Of course, honey."
    j "Thank you."

    scene expression "day_03_lisa_room_scene_4[hair]" with dissolve
    "{color=#D2691E}*The girls go to bed. It's tight for them, but they cuddle up to each other.*{/color}"
    l "What’s going on, Jennifer?"
    j "Nothing… It’s nothing you should worry about."
    l "If you have any troubles talk to [player_name]. He'll help you, you know that."
    j "Okay. I will remember that. Now stop worrying about me."

    scene expression "day_03_lisa_room_scene_7[hair]" with dissolve
    "{color=#D2691E}*Lisa can't sleep. she rolls over to her other side. Jennifer puts her hand on Lisa's waist and cuddles up to her even more.*{/color}"
    l "Mmmmm. Her body is so warm. I can feel her breasts touching mine. They’re so firm. Her skin is so soft."
    l "She smells wonderful, too. It must be that new lotion. Coconut. Mmmmm."
    l "Oh-my-God. Am I getting wet thinking about my sister? What the hell is wrong with me?"
    l "But I must admit she is really beautiful, but for God's sake, she is my sister. I have to pull myself together."

    scene expression "day_03_lisa_room_scene_6[hair]" with dissolve
    "{color=#D2691E}*Lisa's trying to sleep, but she can't stop thinking about her sister.*{/color}"
    l "I wonder what is going on with her. It’s a shame she didn’t want to tell me."
    l "Maybe [player_name] will find out. I have to tell him about it tomorrow."
    l "I’m so tired. It’s time to catch some sleep. I hope I'll dream about [player_name] like last night."
    l "Good night, [player_name]."

    scene expression "day_03_lisa_room_scene_5[hair]" with dissolve
    "{color=#D2691E}*At the same time, Jennifer's fighting her thoughts, too.*{/color}"
    j "Am I cursed or something?"
    j "Why all bad things must happen to me?"
    j "What have I done to be punished in every possible way?"
    j "Why Eric is acting like this? Why he is so mean to me? Did I do something wrong?"
    j "He was a great guy and all of sudden he treats me like a whore."

    scene expression "day_03_lisa_room_scene_8[hair]" with dissolve
    j "Why I can’t meet a normal guy who would treat me like a woman not like a piece of meat to fuck."
    j "I have to break up with him. I can’t stand it anymore."
    j "Maybe I could ask [player_name] to help me deal with Eric? I don’t know what he is capable of."
    j "What if he beats me next time I’ll refuse to have sex with him?"
    j "[player_name] promised me to give me a hand any time I need help."
    j "He seems to be a great guy, and if it is true I wish I'd have grown up with him! That is the kind of guy I want to meet."

    jump linda_at_night

label linda_at_night:

    scene day_03_linda_slap_scene_1 with dissolve
    "{color=#D2691E}In the middle of the night, Linda is making her way home. She takes a quick step through the dark and empty streets.{/color}"
    "{color=#D2691E}She is furious. Suddenly two men come out of the corner and head straight for Linda.{/color}"

    scene day_03_linda_slap_scene_2 with dissolve
    man "Good evening."
    li "What do you want?"

    scene day_03_linda_slap_scene_3 with dissolve
    man "How did it go today? Any luck?"
    li "None of your fucking business."
    man "Be careful what you say."

    scene day_03_linda_slap_scene_4 with dissolve
    li "What the fuck are you going to do to me?"
    man "For the last time, I ask you to behave yourself."

    scene day_03_linda_slap_scene_5 with dissolve
    li "Fuck off."

    scene day_03_linda_slap_scene_6 with dissolve
    "{color=#D2691E}*The man slaps Linda.*{/color}"
    li "What the fuck are you doing?"

    scene day_03_linda_slap_scene_6 with dissolve
    "{color=#D2691E}*The man slaps her again.*{/color}"
    man "Will you calm down?"

    scene day_03_linda_slap_scene_7 with dissolve
    "{color=#D2691E}*From her face, self-confidence and rage disappear and fear appears. She realizes that these men are not joking.*{/color}"
    man "You have 48 hours to pay off the entire debt. If you don't do it, you know what will happen."
    man "Good night."
    "{color=#D2691E}*The men turn around and disappear into the dark.*{/color}"

    scene black with dissolve
    show bg end_of_day_03 with dissolve
    $ renpy.pause ()
    jump day_04
