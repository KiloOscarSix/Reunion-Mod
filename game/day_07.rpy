label day_07:

    $ day = "Day 7"
    $ save_name = "Day 7"
    $ changeWallpaper()

#####################################################################################################################################################
                                                    #############PROLOGUE - NIGHTMARE##################
#####################################################################################################################################################
label day_07_scene_0:

    scene black with dissolve
    pause 1.0

    show bg day_07 with Dissolve(2)
    $ renpy.pause ()

    scene day_07_scene_0_nightmare_1 with fade
    $ renpy.pause ()

    scene day_07_scene_0_nightmare_2 with fade
    $ renpy.pause ()

    scene day_07_scene_0_nightmare_3 with fade
    $ renpy.pause ()

    scene day_07_scene_0_nightmare_4 with fade
    $ renpy.pause ()

    scene day_07_scene_0_nightmare_5 with fade
    mc "Khloe! Stay with me!"

    scene day_07_scene_0_nightmare_6 with fade
    mc "Over here! Come on, faster!"
    mc "Khloe...? Khloe...!"
    mc "Noooooo!"

    scene black with fade
    $ renpy.pause ()

    scene day_07_scene_0_drink_1 with fade
    "{color=#D2691E}*You wake up in a sweat. You sit on the bed and try to recover.*{/color}"
    mc "When these nightmares are over..."
    mc "It's been going on for so many years."

    scene day_07_scene_0_drink_2 with dissolve
    kh "What's going on, honey?"
    mc "Nothing..."
    kh "Are you having nightmares again?"

    scene day_07_scene_0_drink_3 with dissolve
    mc "Yes..."
    mc "I dreamt you died in my arms again."
    kh "Dear, it was just a bad dream. I'm here with you."

    scene day_07_scene_0_drink_4 with dissolve
    mc "I know, dear. I just don't understand why I keep having these nightmares."
    kh "Maybe you should finally go to our psychologist?"

    scene day_07_scene_0_drink_5 with dissolve
    kh "I'm sure he'll help you."
    mc "I think you're right."

    scene day_07_scene_0_drink_6 with dissolve
    "{color=#D2691E}*Khloe kisses you.*{/color}"

    menu khloe_drink:

        "{color=#4169E1}Let's get some sleep.{/color}":

            scene day_07_scene_0_drink_7 with dissolve
            mc "Thank you, honey."
            kh "I'm glad you feel better now."
            mc "Yes, let's get some sleep."

            scene black with dissolve
            show bg few_hours_later with dissolve
            $ renpy.pause()

            jump day_07_breakfast

        "{color=#4169E1}I need a drink.{/color} [KhloeLovePath]":

            $ khloe_love += 1                   # khloe +1
            $ khloe_drink = True

            scene day_07_scene_0_drink_7 with dissolve
            mc "I need a drink. Let's go to the bar."
            kh "Sure, I'll just put something on."

            scene black with dissolve
            show bg some_time_later with dissolve
            $ renpy.pause ()

            scene day_07_scene_0_drink_8 with dissolve
            mc "Hey, a bottle of whiskey and two glasses, please."
            wa "Of course, right away."

            scene day_07_scene_0_drink_9 with dissolve
            wa "Please."
            mc "Thank you."
            wa "Can I get you anything else?"
            mc "For now, that's all. Thank you."

            scene day_07_scene_0_drink_10 with dissolve
            "{color=#D2691E}*You sit next to Khloe on the couch, filling both glasses half full.*{/color}"
            kh "Can you tell me about this dream?"
            mc "It was no different from the previous ones."

            scene day_07_scene_0_drink_11 with dissolve
            mc "As usual, it starts with the fact that you got shot."
            mc "Then I carry you in my arms across the desert, until I have no more strength to carry you."
            mc "Finally a helicopter arrives, but as usual, you die before it lands."

            scene day_07_scene_0_drink_12 with dissolve
            kh "I don't understand why you keep dreaming about it."
            kh "You managed to save me."
            mc "I don't understand it either. Maybe it has some other meaning or cause."

            scene day_07_scene_0_drink_13 with dissolve
            kh "Do you think that's how your other fears manifest themselves?"
            mc "I don't know, but I think it's possible."
            kh "Are you worried about something?"

            scene day_07_scene_0_drink_14 with dissolve
            mc "I have a lot of things on my mind lately."
            mc "You have no idea how sorry I am that I let Mary talk me into coming here."
            kh "Don't say that. I think you did the right thing, as you now can finally leave the past behind."

            scene day_07_scene_0_drink_15 with dissolve
            mc "You're right, but it's not that simple."
            kh "It's never easy, but I know you can do it."
            mc "I don't know. I feel like it's all falling apart in my head."

            menu khloe_chat:

                "{color=#4169E1}Tell Khloe about your concerns.{/color}" if day_07_concerns == False:

                    scene day_07_scene_0_drink_16 with dissolve
                    mc "All these years I tried to forget about this place and everyone here."
                    mc "I somehow managed to move on in my life."
                    mc "And now all the feelings suppressed over all these years have suddenly come back with a vengance."

                    scene day_07_scene_0_drink_17 with dissolve
                    mc "I'm not sure how to deal with it and I can't show that I don't know what I'm doing."
                    mc "I have to pretend in front of all these people that I can overcome every challenge that stands in my way."

                    scene day_07_scene_0_drink_18 with dissolve
                    "{color=#D2691E}*Khloe looks at you and smiles.*{/color}"
                    kh "You know, I never had family or friends because I was in many foster homes until I joined the Army."
                    kh "That's where I finally met you, the most important person in my life."

                    scene day_07_scene_0_drink_19 with dissolve
                    "{color=#D2691E}*You smile at her.*{/color}"
                    kh "I wish I could say I know how you feel, but that wouldn't be true. However I know you're a good person and I believe you can solve any problems that stand in your way."
                    kh "Besides, you know that you can count on Mary and I to support your decisions no matter what."
                    mc "I know, my love."

                    scene day_07_scene_0_drink_20 with dissolve
                    mc "The problem is, I don't know what I want. On the one hand, I want things to be the way they used to be. You know I was very close with Jennifer, Lisa and Nicole. They were like sisters to me."
                    mc "I'd give alot to bring our relationship back to the way it used to be, but everything has changed and that isn't possible."
                    mc "They are adults and their expectiations are completely different from mine."
                    mc "I am scared to hurt them because they may expect more than I can give."

                    scene day_07_scene_0_drink_21 with dissolve
                    kh "I understand your concerns as this is actually a complicate situation."
                    mc "What would you do in my place?"
                    kh "Hmm, I honestly don't know. I'd probably try to make everyone close to me happy."

                    scene day_07_scene_0_drink_22 with dissolve
                    mc "Yeah, I'm trying to do exactly the same thing, and I'm afraid I'll lose control of it at some point."
                    kh "I don't think you have a choice. "
                    $ day_07_concerns = True
                    jump khloe_chat

                "{color=#4169E1}Tell Khloe about Clara.{/color}" if day_07_clara == False:

                    scene day_07_scene_0_drink_23 with dissolve
                    "{color=#D2691E}*You drink another glass of whiskey.*{/color}"
                    mc "There's something else that's bothering me."
                    kh "Yes?"
                    mc "Linda and Clara."

                    scene day_07_scene_0_drink_24 with dissolve
                    kh "Who's Clara?"
                    mc "She works in the company as my secretary and is a friend of Linda's."
                    kh "What's the problem?"

                    scene day_07_scene_0_drink_25 with dissolve
                    mc "There' s something about her that makes me a different person when she' s around."
                    mc "When I found out she was helping Linda, I confronted her she brazenly lied to me. Something inside me broke and I began to humiliate her."
                    mc "I don't know what got into me. I've never acted like this, but I can't control myself with her."

                    if clara_submission >= 5:

                        scene day_07_scene_0_drink_26 with dissolve
                        kh "And what did you do?"
                        mc "Well, I... "
                        kh "Come on, tell me."
                        mc "I ended up having her panties taken off and gave her some spanking."

                        scene day_07_scene_0_drink_27 with dissolve
                        kh "Oh..."
                        mc "Well, uh..."
                        kh "And what did she do?"
                        mc "Nothing at all, because I threatened to ruin her life if she told someone about it."

                        scene day_07_scene_0_drink_28 with dissolve
                        kh "Did you notice any change in her behavior?"
                        mc "She became more submissive, and I guess she stopped lying to me. She even told me she was helping Linda."
                        kh "I have a strange feeling she liked it."
                        mc "What do you mean?"

                        scene day_07_scene_0_drink_29 with dissolve
                        kh "Well, that you humiliated her. People have different perversions or fetishes. Some women like to be dominated. It excites them."
                        mc "So what am I supposed to do with her now?"
                        kh "Nothing. Keep doing what you started. If she took off her panties after five days and let you spank her, she's definitely into it."

                        scene day_07_scene_0_drink_30 with dissolve
                        kh "It seems you have her in your hands, you may even be able to go a lot further without her protesting."
                        mc "But I don't know if I want to go any further."
                        kh "It's up to you to decide what you want to do."

                        scene day_07_scene_0_drink_31 with dissolve
                        mc "Do you really think she'll submit to me completely?"
                        kh "Yes, try it, and you'll see."
                        mc "I'll think about it."
                        $ day_07_clara = True
                        jump khloe_chat

                    else:

                        scene day_07_scene_0_drink_26 with dissolve
                        kh "And what did you do?"
                        mc "Well, I... "
                        kh "Come on, tell me."
                        mc "I really wanted to slap her but I ended up yelling at her."

                        scene day_07_scene_0_drink_27 with dissolve
                        kh "Oh..."
                        mc "Well, uh..."
                        kh "And what did she do?"
                        mc "Nothing."

                        scene day_07_scene_0_drink_28 with dissolve
                        kh "Did you notice any change in her behavior?"
                        mc "She became more submissive, and I guess she stopped lying to me. She even told me she was helping Linda."

                        scene day_07_scene_0_drink_30 with dissolve
                        kh "I think you can go a lot further, and she won't protest. You've got her in your hand."
                        mc "But I don't know if I want to go any further."
                        kh "And that's a completely different matter. It's up to you."

                        scene day_07_scene_0_drink_31 with dissolve
                        mc "Do you really think she'll submit to me completely?"
                        kh "Yes, try it, and you'll see."
                        mc "I'll think about it."
                        $ day_07_clara = True
                        jump khloe_chat

            if day_07_clara and day_07_concerns == True:
                jump day_07_scene_0_1

label day_07_scene_0_1:

    scene day_07_scene_0_drink_32 with dissolve
    "{color=#D2691E}*You drink another glass of whiskey.*{/color}"
    mc "I see problems wherever I look."
    kh "Listen, perhaps the reason the nightmares started again is because the whole situation is affecting you a great deal."

    scene day_07_scene_0_drink_33 with dissolve
    kh "I'm telling you, make an appointment with our psychologist. I'm sure he'll figure out what's causing these nightmares."
    mc "Thank you, I really needed to talk about this."

    scene day_07_scene_0_drink_34 with dissolve
    kh "Don't worry about it."
    mc "The sun is coming up, lets get back to bed."

    jump day_07_scene_1

#####################################################################################################################################################
                                                    #############SCENE 01 - Water park#############
#####################################################################################################################################################
label day_07_scene_1:

    scene black with dissolve
    show few_hours_later with dissolve
    $ renpy.pause ()
    hide few_hours_later

    if khloe_drink == True:

        scene day_07_scene_1_khloe_mary_scene_1 with dissolve
        "{color=#D2691E}*You open your eyes. You feel tired like you haven't slept at all, and you're hung over.*{/color}"
        "{color=#81F79F}*Drinking whiskey in the middle of the night was not a good idea.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_2 with dissolve
        "{color=#D2691E}*You sit up and look around the room.*{/color}"
        "{color=#D2691E}*You see Marry sitting on the couch watching TV, but you don't see Khloe anywhere.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_3 with dissolve
        "{color=#D2691E}*Slowly you get out of bed moaning loudly.*{/color}"
        mc "Fucking headache!"

        scene day_07_scene_1_khloe_mary_scene_5 with dissolve
        "{color=#D2691E}*Mary turns to you.*{/color}"
        mary "That's what happens when you drink almost the whole bottle."
        mary "You stink, go take a shower."

        scene day_07_scene_1_khloe_mary_scene_6 with dissolve
        "{color=#D2691E}*Obediently, you go to the bathroom.*{/color}"
        "{color=#D2691E}*Khloe is standing in front of the mirror and drying her hair.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_7 with dissolve
        kh "You look like a shit."
        mc "Thanks, you'are too kind."
        kh "A shower will make you feel better."

        scene day_07_scene_1_khloe_mary_scene_8 with dissolve
        "{color=#D2691E}*You get in the shower.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_8a with dissolve
        "{color=#D2691E}*You feel the water running down your body and the feeling of tiredness disappear.*{/color}"
        "{color=#D2691E}*You feel your strength coming back.*{/color}"
        kh "Are you okay?"

        menu shower_day_7:

            "{color=#4169E1}Yes, much better.{/color}":

                scene day_07_scene_1_khloe_mary_scene_9 with dissolve
                mc "Yeah, much better."
                kh "Then hurry up, I'm hungry."
                mc "Okay, give me a few minutes."

            "{color=#4169E1}Not really.{/color}":

                scene day_07_scene_1_khloe_mary_scene_9 with dissolve
                mc "Not really."
                kh "Damnit, take your time then."
                kh "We will wait on you for breakfast."
                mc "Thanks."

        scene day_07_scene_1_khloe_mary_scene_10 with dissolve
        "{color=#81F79F}*These goddamn nightmares are going to make me go crazy someday.*{/color}"
        "{color=#81F79F}*Why do I keep having them?*{/color}"
        "{color=#81F79F}*Maybe the doctor will help me?.*{/color}"

    else:

        scene day_07_scene_1_khloe_mary_scene_1 with dissolve
        "{color=#D2691E}*You open your eyes. You feel tired like you haven't slept at all.*{/color}"
        "{color=#81F79F}*Fucking nightmares.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_2 with dissolve
        "{color=#D2691E}*You sit up and look around the room.*{/color}"
        "{color=#D2691E}*You see Marry sitting on the couch watching TV, but you don't see Khloe anywhere.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_3 with dissolve
        "{color=#D2691E}*Slowly you get out of bed moaning loudly.*{/color}"
        mc "Fucking headache!"

        scene day_07_scene_1_khloe_mary_scene_5 with dissolve
        "{color=#D2691E}*Mary turns to you.*{/color}"
        mary "Take a shower. It will help you."

        scene day_07_scene_1_khloe_mary_scene_6 with dissolve
        "{color=#D2691E}*Obediently, you go to the bathroom.*{/color}"
        "{color=#D2691E}*Khloe is standing in front of the mirror and drying her hair.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_7 with dissolve
        kh "You look like a shit."
        mc "Thanks, you'are too kind."
        kh "A shower will make you feel better."

        scene day_07_scene_1_khloe_mary_scene_8 with dissolve
        "{color=#D2691E}*You get in the shower.*{/color}"

        scene day_07_scene_1_khloe_mary_scene_8a with dissolve
        "{color=#D2691E}*You feel the water running down your body and the feeling of tiredness disappear.*{/color}"
        "{color=#D2691E}*You feel your strength coming back.*{/color}"
        kh "Are you okay?"

        menu shower_day_7_1:

            "{color=#4169E1}Yes, much better.{/color}":

                scene day_07_scene_1_khloe_mary_scene_9 with dissolve
                mc "Yeah, much better."
                kh "Then hurry up, I'm hungry."
                mc "Okay, give me a few minutes."

            "{color=#4169E1}Not really.{/color}":

                scene day_07_scene_1_khloe_mary_scene_9 with dissolve
                mc "Not really."
                kh "Damnit, take your time then."
                kh "We will wait on you for breakfast."
                mc "Thanks."

        scene day_07_scene_1_khloe_mary_scene_10 with dissolve
        "{color=#81F79F}*These goddamn nightmares are going to make me go crazy someday.*{/color}"
        "{color=#81F79F}*Why do I keep having them?*{/color}"
        "{color=#81F79F}*I have to finally go to the doctor.*{/color}"

    scene day_07_scene_1_khloe_mary_scene_11 with dissolve
    "{color=#81F79F}*I will call our psychologist.*{/color}"
    "{color=#81F79F}*He did pretty good job with Mary.*{/color}"

    scene day_07_scene_1_khloe_mary_scene_13 with dissolve
    "{color=#D2691E}*As you are leaving the bathroom, the girls are waiting there.*{/color}"
    mary "We're going to breakfast, get dressed and join us."
    mc "Okay."

    jump day_07_breakfast

label day_07_breakfast:

    scene day_07_scene_1_breakfast_1 with fade
    waiter "Good morning, can I take your order?"
    mary "Yes. I'll have some toast with ham and scrambled eggs."
    kh "For me, salmon toast and two sausages."

    scene day_07_scene_1_breakfast_2 with dissolve
    waiter "And what would you like to drink?"
    mary "Big black coffee."
    kh "Double expresso for me."

    scene day_07_scene_1_breakfast_3 with dissolve
    kh "I'm worried about [player_name]."
    mary "Why? What's wrong?"
    kh "His nightmares are back."

    scene day_07_scene_1_breakfast_4 with dissolve
    mary "Fuck! Not again. He's suffered enough from them."
    kh "I know..."
    kh "He's gonna have to go to the psychologist."

    scene day_07_scene_1_breakfast_5 with dissolve
    kh "These nightmares are definitely based on the mental stress he is under."
    mary "Maybe you're right."
    kh "Do you remember what happened to you right after we saved you?"

    scene day_07_scene_1_breakfast_6 with dissolve
    mary "I remember..."
    kh "Right. You suffered from them until you were referred to a psychologist."
    kh "He helped you deal with the trauma and the nightmares disappeared after a few months."

    scene day_07_scene_1_breakfast_7 with dissolve
    "{color=#D2691E}*The waiter brings their order.*{/color}"
    kh "I think that coming back to his hometown has woken up the sleeping demons in him and now it's all slowly getting worse."
    kh "The sooner we deal with his past, the sooner everything will return to normal."

    scene day_07_scene_1_breakfast_8 with dissolve
    "{color=#D2691E}*Mary's taking a sip of hot coffee.*{/color}"

    if khloe_drink == True:

        mary "Did he tell you what bothers him most?"

        menu mc_concerns:

            "{color=#4169E1}Linda's daughters.{/color}" if concern_a == False:

                scene day_07_scene_1_breakfast_9 with dissolve
                kh "We talked about a lot of things. He mentioned his concerns about Linda's daughters in particular."
                kh "On the one hand, he wants to rebuild the relationship with them that they once had, but on the other hand, they're already adults and he feels like they expect something completely different from him."
                kh "He also complained that he has too many things and problems on his mind."
                mary "I have told him so many times that he cannot get so involved in all the problems, because it will kill him one day."

                scene day_07_scene_1_breakfast_10 with dissolve
                kh "He is already like that and we won't change that. All we can do now is stay with him and help him deal with it as best as we can."
                mary "You're right."
                $ concern_a = True
                jump mc_concerns

            "{color=#4169E1}Clara.{/color}" if concern_b == False:

                scene day_07_scene_1_breakfast_11 with dissolve
                kh "He mentioned someone named Clara. "
                mary "What about her?"
                kh "Well, he told me that she was pissing off because she lied about helping Linda steal from the company."

                if clara_submission >= 5:

                    scene day_07_scene_1_breakfast_12 with dissolve
                    kh "Eventually, he caught her lying to him again and he couldn't stand it."
                    kh "He told her to take off her panties and gave her some spanking."
                    mary "Oh..."

                    scene day_07_scene_1_breakfast_13 with dissolve
                    kh "Now he's worried that he overreacted, that he doesn't know what got into him."
                    kh "So I explained to him that since she's still working there and hasn't reported it anywhere, she probably likes to play games like that."
                    mary "It's possible."

                    scene day_07_scene_1_breakfast_14 with dissolve
                    kh "I told him not to worry about it, and keep doing his job. It is possible she'll probably let him do a lot more if she keeps doing these things."
                    kh "But he has to make his own decision."
                    $ concern_b = True
                    jump mc_concerns

                else:

                    scene day_07_scene_1_breakfast_12 with dissolve
                    kh "Eventually, he caught her lying to him again and he couldn't stand it."
                    kh "He wanted to slap her but he only yelled at her."
                    mary "Oh..."

                    scene day_07_scene_1_breakfast_13 with dissolve
                    kh "Now he's worried that he overreacted, that he doesn't know what got into him."
                    kh "So I explained to him that since she's still working there and hasn't reported it anywhere, she probably likes to play games like that."
                    mary "It's possible."

                    scene day_07_scene_1_breakfast_14 with dissolve
                    kh "I told him not to worry about it, and keep doing his job. It is possible she'll probably let him do a lot more if she keeps doing these things."
                    kh "But he has to make his own decision."
                    $ concern_b = True
                    jump mc_concerns

        if concern_a and concern_b == True:
            jump day_07_breakfast_a

    else:

        mary "Yes, you are right. I will make sure he visits some specialist."

label day_07_breakfast_a:

    scene day_07_scene_1_breakfast_15 with dissolve
    mary "Finally. What took you so long?"
    mc "I had to make a phonecall."
    mary "What do you want for breakfast?"

    scene day_07_scene_1_breakfast_16 with dissolve
    mc "Nothing, I'm not hungry."
    mc "What were you talking about?"
    kh "You and your nightmares."

    scene day_07_scene_1_breakfast_17 with dissolve
    mc "I called our psychologist and I made an appointment for Thursday."
    mc "So I'm flying to Los Angeles on Wednesday."

    scene day_07_scene_1_breakfast_18 with dissolve
    kh "That's good, you're gonna have to deal with it eventually, because you don't know how it's gonna end this time."
    mc "I know, but I don't want to talk about it anymore."

    scene day_07_scene_1_breakfast_19 with dissolve
    kh "So...What are we going to do today?"
    mc "I didn't plan anything other than meeting with Lisa nad her sisters to tell them about the letter which will probably take me about two hours."
    mc "Other than that, we can do what ever you want."

    scene day_07_scene_1_breakfast_20 with dissolve
    kh "The weather is going to be beautiful today. Why don't we go to the water park or the lake? I feel like sunbathing and swimming."
    mary "Sounds great."
    kh "Lets go now and you can go to Lisa in the afternoon."

    scene day_07_scene_1_breakfast_21 with dissolve
    mc "Okay, where?"
    mary "The Water Park."

    scene day_07_scene_1_breakfast_22 with dissolve
    kh "I agree."
    mc "Let's go get ready then."

    jump waterpark

label waterpark:

    scene black with fade
    show some_time_later with dissolve
    $ renpy.pause ()
    hide some_time_later

    scene day_07_scene_1_waterpark_1 with dissolve
    kh "I'm so happy that we decided to spend some time together. I was starting to miss this."
    kh "It's been all work and no pleasure lately!"
    mc "You're right, the last week has been a nightmare! Nothing but trouble."

    scene day_07_scene_1_waterpark_2 with dissolve
    "{color=#D2691E}*You find your seats and strip to your swim suits.*{/color}"
    mary "Who wants to swim?"
    kh "I do."

    scene day_07_scene_1_waterpark_3 with dissolve
    mc "I'll lie down for now, but you guys go."

    scene day_07_scene_1_waterpark_4 with dissolve
    "{color=#D2691E}*The girls don't think long and splash water all over you as they jump in the pool.*{/color}"

    scene day_07_scene_1_waterpark_5 with dissolve
    "{color=#D2691E}*You watch them swim from the deckchair.*{/color}"

    scene day_07_scene_1_waterpark_6 with dissolve
    "{color=#D2691E}*After a few minutes, Mary calls you.*{/color}"
    mary "Come on, don't let me beg you."

    scene day_07_scene_1_waterpark_7 with dissolve
    "{color=#D2691E}*You get up and diven into the water.*{/color}"

    scene day_07_scene_1_waterpark_8 with dissolve
    "{color=#D2691E}*When you resurface, both girls attack and try to pull you back underwater.*{/color}"

    scene day_07_scene_1_waterpark_9 with dissolve
    "{color=#D2691E}*You break free and rush to the other end of the pool.*{/color}"
    "{color=#D2691E}*The girls rush after you.*{/color}"

    scene day_07_scene_1_waterpark_10 with dissolve
    "{color=#D2691E}*For the next few minutes, you're fooling around like little children laughing loudly.*{/color}"

    scene day_07_scene_1_waterpark_11 with dissolve
    $ renpy.pause ()

    scene day_07_scene_1_waterpark_12 with dissolve
    $ renpy.pause ()

    scene day_07_scene_1_waterpark_13 with dissolve
    $ renpy.pause ()

    scene day_07_scene_1_waterpark_14 with dissolve
    "{color=#D2691E}*Finally, you swim to the side to get some rest.*{/color}"

    scene day_07_scene_1_waterpark_15 with dissolve
    "{color=#D2691E}*After a while, Mary and Khloe join you.*{/color}"
    kh "What's up?"
    mc "Nothing, I got tired."

    scene day_07_scene_1_waterpark_16 with dissolve
    kh "Seriously? HAHA. We're going to the slide."
    mc "Have fun."

    scene day_07_scene_1_waterpark_17 with dissolve
    "{color=#D2691E}*You sit on the deckchair and watch the girls climb the stairs to the top of the slide.*{/color}"

    scene day_07_scene_1_waterpark_17a with dissolve
    "{color=#D2691E}*The girls laugh loudly as they slide down to the pool.*{/color}"

    scene day_07_scene_1_waterpark_18 with dissolve
    "{color=#D2691E}*Time goes by slowly. You watch the girls for a few more minutes until you finally get up and go to the bar.*{/color}"

    if persistent.smoke == True:

        scene day_07_scene_1_waterpark_18a with dissolve
        "{color=#D2691E}*you sit down at the bar and the barmaid comes over to you.*{/color}"
        barmaid "Hello there, what can I get for you?"
        mc "Double whiskey with ice, please."

        scene day_07_scene_1_waterpark_18b with dissolve
        "{color=#D2691E}*The barmaid pours a large amount of golden liquor into the glass. She looks at you, smiles a little, and then leaves to serve the next customer.*{/color}"

        scene day_07_scene_1_waterpark_19 with dissolve
        "{color=#D2691E}*You take a solid sip of whiskey and let your thoughts drift.*{/color}"
        "{color=#81F79F}*I really need to move on with this mess.*{/color}"
        "{color=#81F79F}*I'm slowly starting to lose patience. Nothing has gone right. It looks like I'll spend the next year here confronting the demons of the past at this rate.*{/color}"

        scene day_07_scene_1_waterpark_20 with dissolve
        "{color=#81F79F}*I have to get my hands on it and start to solve problems successively and avoid new ones at all costs.*{/color}"
        "{color=#81F79F}*First of all, I have to deal with Linda. If everything went according to plan, in two days' time she will be in my hands and I have to do everything to teach her a lesson.*{/color}"

        if lisa_proposal == True:

            scene day_07_scene_1_waterpark_22 with dissolve
            "{color=#D2691E}*You take another solid sip of whiskey.*{/color}"

        else:

            scene day_07_scene_1_waterpark_21 with dissolve
            "{color=#81F79F}*The next thing is Lisa and Jennifer. Lisa will certainly not give up so easily, so I have to decide whether to get into this relationship no matter what, or to let her know gently that it is not the best idea to get involved.*{/color}"
            "{color=#81F79F}*I just don't know if it will be possible at all after our last conversation. I don't want to make her hate me and suffer again because of me.*{/color}"

            scene day_07_scene_1_waterpark_22 with dissolve
            "{color=#D2691E}*You take another solid sip of whiskey.*{/color}"

        if jennifer_kiss_day_06 == True:

            "{color=#81F79F}*Another thing is Jennifer. I don't know what to think after yesterday's dinner. I'm glad we're getting close again, but that kiss surprised me.*{/color}"

        else:

            "{color=#81F79F}*Another thing is Jennifer. I don't know what to think after yesterday's dinner. I'm glad we're getting close again, but that hug surprised me.*{/color}"

        scene day_07_scene_1_waterpark_23 with dissolve
        "{color=#D2691E}*Khloe's loud laughing tears you out of your mind.*{/color}"
        mc "How are you doing? Having a good time?"
        mary "Yeah, I wish you had joined us."

    else:

        scene day_07_scene_1_waterpark_18a_sm with dissolve
        "{color=#D2691E}*you sit down at the bar and the barmaid comes over to you.*{/color}"
        barmaid "Hello there, what can I get for you?"
        mc "Double whiskey with ice, please."

        scene day_07_scene_1_waterpark_18b_sm with dissolve
        "{color=#D2691E}*The barmaid pours a large amount of golden liquor into the glass. She looks at you, smiles a little, and then leaves to serve the next customer.*{/color}"

        scene day_07_scene_1_waterpark_19_sm with dissolve
        "{color=#D2691E}*You take a solid sip of whiskey and let your thoughts drift.*{/color}"
        "{color=#81F79F}*I really need to move on with this mess.*{/color}"
        "{color=#81F79F}*I'm slowly starting to lose patience. Nothing has gone right. It looks like I'll spend the next year here confronting the demons of the past at this rate.*{/color}"

        scene day_07_scene_1_waterpark_20_sm with dissolve
        "{color=#81F79F}*I have to get my hands on it and start to solve problems successively and avoid new ones at all costs.*{/color}"
        "{color=#81F79F}*First of all, I have to deal with Linda. If everything went according to plan, in two days' time she will be in my hands and I have to do everything to teach her a lesson.*{/color}"

        if lisa_proposal == True:

            scene day_07_scene_1_waterpark_22 with dissolve
            "{color=#D2691E}*You take another solid sip of whiskey.*{/color}"

        else:

            scene day_07_scene_1_waterpark_21 with dissolve
            "{color=#81F79F}*The next thing is Lisa and Jennifer. Lisa will certainly not give up so easily, so I have to decide whether to get into this relationship no matter what, or to let her know gently that it is not the best idea to get involved.*{/color}"
            "{color=#81F79F}*I just don't know if it will be possible at all after our last conversation. I don't want to make her hate me and suffer again because of me.*{/color}"

            scene day_07_scene_1_waterpark_22 with dissolve
            "{color=#D2691E}*You take another solid sip of whiskey.*{/color}"

        if jennifer_kiss_day_06 == True:

            "{color=#81F79F}*Another thing is Jennifer. I don't know what to think after yesterday's dinner. I'm glad we're getting close again, but that kiss surprised me.*{/color}"

        else:

            "{color=#81F79F}*Another thing is Jennifer. I don't know what to think after yesterday's dinner. I'm glad we're getting close again, but that hug surprised me.*{/color}"

            scene day_07_scene_1_waterpark_23_sm with dissolve
            "{color=#D2691E}*Khloe's loud laughing tears you out of your mind.*{/color}"
            mc "How are you doing? Having a good time?"
            mary "Yeah, I wish you had joined us."

    scene day_07_scene_1_waterpark_24 with dissolve
    mc "I just needed a moment alone to get my mind in thoughts."
    kh "Eh... Are you worried about something again?"
    mc "No, it's not that. I've got too many things on my mind, and I need to sort it all out in some sensible way to move on. Standing still is starting to annoy me."

    scene day_07_scene_1_waterpark_25 with dissolve
    barmaid "Can I get you ladies something?"
    mary "Hmm. What would you recommend?"
    barmaid "I think a coconut milk drink would be best for you, ladies."

    scene day_07_scene_1_waterpark_26 with dissolve
    mary "Sounds lovely."
    mary "Two, please."
    mc "And for me, one more double Whiskey."
    barmaid "Right away."

    scene day_07_scene_1_waterpark_27 with dissolve
    "{color=#D2691E}*You go back to the deckchairs and relax.*{/color}"
    kh "Okay. Now tell us what's on your mind. Maybe we can work out a solution together."
    mary "Before we start discussing this, I'll tell you that I've been thinking about it too. You know I like to have everything organized and planned."

    scene day_07_scene_1_waterpark_28 with dissolve
    mary "I think there are three main topics we should discuss, and that would allow us to plan our next steps."
    mary "First of all, we need to make some decisions about the company. I've had to reject some contracts and we're losing customers."
    mary "Secondly, we should establish a plan of action, because I feel like we're wandering around in the fog and not moving forward at all."
    mary "Thirdly, we need to discuss the women around you. I would like to know what your plans for them are."

    scene day_07_scene_1_waterpark_29 with dissolve
    mary "First, we had three contracts in the last week and we could only work on one of them."
    mary "If we don't want to lose the last few years of our hard work, it can't happen again."
    kh "I agree. I understand that things here are important to you, but I don't think we should sacrifice our company to deal with your private affairs."

    scene day_07_scene_1_waterpark_30 with dissolve
    kh "I'll do anything to help you, you know that, but I won't let us destroy the company at the same time."
    mc "Okay, good that you tell me about it. To be honest, I've completely forgotten about other things. It won't happen again."
    mc "Do you have any suggestions as to how to deal with this?"

    scene day_07_scene_1_waterpark_31 with dissolve
    mary "It all depends on how long you're going to spend here."
    mc "You know damn well I have no idea."
    mc "Every day new things come up and the whole situation gets more and more complicated."

    scene day_07_scene_1_waterpark_32 with dissolve
    mc "I want to bring it to an end no matter how long it takes."
    mc "If you want to go back to Los Angeles I won't blame you."
    mary "That's not the point. We'll stay with you till the end, but I suggest we open a branch office here. Some people would stay in Los Angeles and some would move here."

    scene day_07_scene_1_waterpark_33 with dissolve
    mary "We' d have to hire new people but that's not a problem."
    kh "We can also go one step further and merge the two companies."
    mary "Yes, I agree. That would be a good move but it's too soon for that."

    scene day_07_scene_1_waterpark_34 with dissolve
    mc "Opening a branch office is a good idea but I agree with Mary that merging our companies would be too soon. Let's give it some time and see how it works and then we can merge them."
    mary "Exactly."
    kh "Okay, let's do that."

    scene day_07_scene_1_waterpark_35 with dissolve
    mc "I'm flying to Los Angeles on Wednesday, one of you could come with me and we could get everything ready to move here."
    mary "This is a good idea. I think Khloe should go with you. What do you think Khloe?"
    kh "Sure."

    scene day_07_scene_1_waterpark_36 with dissolve
    mary "Great, we are already moving forward."
    mc "I'll start preparations at the company tomorrow morning so that everything is ready by Friday."
    mary "Okay."

    menu mary_topics:

        "{color=#4169E1}The plan.{/color}" if plan == False:

            scene day_07_scene_1_waterpark_37 with dissolve
            mc "Let's talk about the plan of action."
            mary "Well, you know I like to have everything arranged and planned. So far, I feel like neither of us knows what we' re doing."
            mary "We're wandering in the dark without a specific goal we want to achieve."

            scene day_07_scene_1_waterpark_38 with dissolve
            mary "This applies both to your private affairs and who we help and why."
            mary "I know you're a good man but you can't loose yourself by your want to help those around you in their time of need."
            mary "Every now and then a new person appears with a new problem that needs to be solved urgently. This is how we lose sight of our primary objective."

            scene day_07_scene_1_waterpark_39 with dissolve
            mc "You're right, Mary. I get lost in these things."
            mary "What is your main objective?"
            mc "I want to find out what happened to my father, why the letters I wrote were kept by him."
            mc "I want to know what Linda's part in all this was."

            scene day_07_scene_1_waterpark_40 with dissolve
            mary "So everything else is not so important?"
            mc "No, if we can solve a few other things by the way, or help a few people, that's great, but from now on I want to focus on these three things first."
            mary "All right. I think it's very good to handle these things this way."

            scene day_07_scene_1_waterpark_41 with dissolve
            mc "Khloe, what is your opinion on this?"
            kh "Well, I think by focusing on one goal we'll achieve a lot more than trying to solve all things at once."
            kh "Besides, I think that once we know what we're gonna do, we should share the tasks so that everyone can do something."

            scene day_07_scene_1_waterpark_42 with dissolve
            mary "I agree. The division of roles will help us reach our goal faster."
            mary "Besides, each of us has different skills that we should make the most of."
            kh "Let's treat this as a simple assignment. Analysis, reconnaissance, tactical preparation, execution."

            scene day_07_scene_1_waterpark_43 with dissolve
            mary "Exactly. We can do it and we know how to do it."
            mary "Let us use our skills and abilities. Let this be a team effort, not your lonely vendetta against the whole city."
            mc "Can't disagree with that."

            $ plan = True

            jump mary_topics

        "{color=#4169E1}The girls.{/color}" if girls == False:

            scene day_07_scene_1_waterpark_44 with dissolve
            mc "You said we should talk about women around me. Which ones did you mean?"
            mary "All of them."
            mc "Eh..."

            scene day_07_scene_1_waterpark_45 with dissolve
            kh "There are so many of them?"
            mc "No, don't exaggerate."
            mary "Well, then, one at a time."

            scene day_07_scene_1_waterpark_46 with dissolve
            mc "Okay, then. Let's start with Lisa."
            mc "She is Linda's youngest daughter. She already told me that she is in love with me."
            mc "I explained our situation even though it could have broken her heart, I just couldn't lie to her."

            scene day_07_scene_1_waterpark_47 with dissolve
            kh "What was her reaction after you told her you are with us?"
            mc "Well... I'm sure that's not what she expected, she was disappointed, upset, I don't know."
            kh "So she didn't give you any clear answer to what you told her? Because as I understand it, you asked her to join us."

            scene day_07_scene_1_waterpark_48 with dissolve
            mc "Exactly."
            mary "Are you planning on doing something more to convince her?"
            mc "No. I told her everything and now she has to make a choice."

            scene day_07_scene_1_waterpark_49 with dissolve
            mc "Next one is Nicole, second Linda's daughter. I don't know what to think about her. She was mad at me, and now she needs my help to deal with the blackmailer."
            mc "So she changed her attitude towards me, but I don't know if it's just a sham or if she really understood that she made a mistake."
            mc "Time will show what her real purpose is."

            scene day_07_scene_1_waterpark_50 with dissolve
            mary "So you have nothing in common?"
            mc "Absolutely nothing."
            kh "Is there anyone else?"

            scene day_07_scene_1_waterpark_51 with dissolve
            mc "Yes, Jennifer, the oldest Linda's daughter. I'm not sure what to think about her. Her behavior was similar to Nicole's, but suddenly it changed."
            mc "She invited me to dinner and we had a long talk about us, about our past, about what happened in our lives."
            mc "I didn't mention anything about you because there was no need for it at this point."
            mc "When I walked her home she kissed me and that has me confused."

            scene day_07_scene_1_waterpark_52 with dissolve
            mary "It seems like she doesn't know what she wants. You have to give her some time to understand her feelings for you."
            kh "And you have feelings for her?"
            mc "I don't know. I love her and I like being with her and we always had a lot in common."
            mc "If she wanted to be with me, I'd be happy, but I'm not gonna make her do it."

            scene day_07_scene_1_waterpark_53 with dissolve
            kh "Fair enough."
            mc "There is also Emily and Sandra."
            mc "Sandra is a lawyer I hired recently. We went on one date so far."

            scene day_07_scene_1_waterpark_54 with dissolve
            kh "Do you feel anything for her?"
            mc "I am not sure, but I know I like her.  She's pretty and very intelligent, but I don't know her enough to say anything more yet."
            mc "Besides, she's had a hard time in the past, and I don't know how that affects her."
            mc "Time will tell if anything more will come of it."

            scene day_07_scene_1_waterpark_55 with dissolve
            mc "Last one is Emily. We went to school together. I met her once at Sandra's, and then at the lingerie shop. We had a drink."
            mc "It turned out then, that she was secretly in love with me since school, and now these feelings are back."
            mc "Like Lisa, I told her everything and, contrary to my expectations, she was ready to join us."
            mc "But it turns out she doesn't want to hurt Sandra, who's been her best friend for years."

            scene day_07_scene_1_waterpark_56 with dissolve
            mc "And that's it."
            mary "A lot of information, but we finally know what's going on around you."
            mary "We're a family in an open relationship and you never have to confess to us who you're sleeping with, but we would like to know if there's anything more than sex at any time."

            scene day_07_scene_1_waterpark_57 with dissolve
            mc "Of course, the last thing I want to do is hurt you."
            mc "You two are and always will be most important to me and I will never do anything to hurt you."
            mary "We know this, and we love you too."

            scene day_07_scene_1_waterpark_58 with dissolve
            mary "Okay, so we've talked about this before and we'd like to assure you we're open to new challenges."
            kh "We don't mind if there's a new person or even a few new people in our family."

            scene day_07_scene_1_waterpark_59 with dissolve
            mary "But before you decide to take the next step with any of them, be sure you truly trust them."
            mary "We don't want any surprises."
            mc "I promise and thank you for everything."

            scene day_07_scene_1_waterpark_60 with dissolve
            kh "Let's meet them as we would like to know them before you make any decisions."
            mc "Sure, I will do that."
            $ girls = True
            jump mary_topics

    if plan == True and girls == True:

        jump mary_after_topics

label mary_after_topics:

    scene day_07_scene_1_waterpark_61 with dissolve
    mary "One more thing, what do we do with the hotel? Are we extending our stay there or are we looking for something else?"
    mc "I really want to get out of there. Please, find us something to rent."
    mc "A small house would be great, or some kind of an apartment."

    scene day_07_scene_1_waterpark_62 with dissolve
    mary "Okay. I'll check the websites and see if there is something interesting for us."
    kh "It would be great if we could finally leave this so-called hotel."
    mary "Don't worry, I will find something great for us."

    scene day_07_scene_1_waterpark_63 with dissolve
    mc "I think we discussed everything. It's getting late, lets get back to the hotel."

    jump day_07_scene_2

#####################################################################################################################################################
                                                    #############SCENE 02 - At the lake#############
#####################################################################################################################################################
label day_07_scene_2:

    if lisa_masturbate == True:

        scene black with fade
        show in_the_meantime with dissolve
        $ renpy.pause ()
        hide in_the_meantime

        scene expression "day_07_scene_2_lisa_1[hair]" with dissolve
        "{color=#D2691E}*Lisa wakes up first.*{/color}"

        scene expression "day_07_scene_2_lisa_2[hair]" with dissolve
        "{color=#D2691E}*For a long time she lays staring at her sleeping sister.*{/color}"
        "{color=#81F79F}*She is so beautiful. I can't stop looking at her.*{/color}"
        "{color=#81F79F}*But it's strange that I've never looked at her like that before.*{/color}"
        "{color=#81F79F}*It's definitely all because of Rachel and what she told me. And that kiss...*{/color}"

        scene expression "day_07_scene_2_lisa_3[hair]" with dissolve
        "{color=#81F79F}*But can I blame her for that? She's always been open to all sorts of strange relationships and liked to experiment with sex.*{/color}"
        "{color=#81F79F}*I was always the one who was virtuous and afraid of everything. Maybe recent events have changed something inside me?*{/color}"
        "{color=#81F79F}*I never in my life would have thought I could masturbate in front of other people, even if it was Rachel. Not to mention kissing a woman.*{/color}"

        scene expression "day_07_scene_2_lisa_4[hair]" with dissolve
        "{color=#81F79F}*It's true that what happened last night was very weird, but for some reason I damn well liked it.*{/color}"
        "{color=#81F79F}*The feeling of Jennifer's wet pussy rubbing against my thigh and then the feeling of her body trembling in a wave of pleasure was incredible.*{/color}"
        "{color=#81F79F}*It made me so horny. But isn't it weird? After all, she is my sister.*{/color}"


        scene expression "day_07_scene_2_lisa_5[hair]" with dissolve
        "{color=#D2691E}*Jennifer opens her eyes and looks at her sister. A shy smile appears on her face.*{/color}"
        j "Hey."
        l "Hi, Jennifer."

        scene expression "day_07_scene_2_lisa_6[hair]" with dissolve
        "{color=#D2691E}*Girls stare at each other for a while.*{/color}"
        j "You know... what happened yesterday..."

        scene expression "day_07_scene_2_lisa_7[hair]" with dissolve
        l "Don't say anything..."

        scene expression "day_07_scene_2_lisa_8[hair]" with dissolve
        "{color=#D2691E}*Jennifer sits on the bed.*{/color}"
        j "You know that what happened yesterday shouldn't happened, right?"
        l "Yes, I'm aware of that."

        scene expression "day_07_scene_2_lisa_9[hair]" with dissolve
        j "What should we do now?"
        l "I have no idea. Do we really have to do anything?"

        scene expression "day_07_scene_2_lisa_10[hair]" with dissolve
        "{color=#D2691E}*Jennifer looks her sister in the eyes.*{/color}"
        j "We can't let this ever happen again."
        j "We can't... what happened was wrong..."

        scene expression "day_07_scene_2_lisa_11[hair]" with dissolve
        l "Wrong?"
        j "Yes... you're my sister... it... shouldn't have happened."

        scene day_07_scene_2_lisa_12 with dissolve
        j "I’m sorry, Lisa."
        l "You have nothing to apologize for."

        scene expression "day_07_scene_2_lisa_13[hair]" with dissolve
        "{color=#D2691E}*Jennifer gets up. She looks at her sister and wants to say something, but she changes her mind and leaves the room without a word.*{/color}"

        scene expression "day_07_scene_2_lisa_14[hair]" with dissolve
        "{color=#D2691E}*Lisa lies in bed for a few more minutes staring at the ceiling.*{/color}"

        scene expression "day_07_scene_2_lisa_15[hair]" with dissolve
        "{color=#D2691E}*Few minutes later she gets up and goes to the bathroom to take a bath.*{/color}"

        scene expression "day_07_scene_2_lisa_16[hair]" with dissolve
        "{color=#D2691E}*She undresses and goes into a bath filled with hot water.*{/color}"

        scene expression "day_07_scene_2_lisa_17[hair]" with dissolve
        "{color=#D2691E}*She's getting wet up to her neck and closing her eyes.*{/color}"

        jump day_07_lake

    else:

        jump day_07_lake


label day_07_lake:

    if lisa_masturbate == True:

        scene expression "day_07_scene_2_lisa_rachel_amy_scene_1[hair]" with dissolve
        "{color=#D2691E}*Half an hour later, Lisa's phone rings disturbing her from a relaxing bath.*{/color}"
        r "Where the hell are you?"
        r "We have been waiting for you for the last half hour."

    else:

        scene black with dissolve
        show in_the_meantime with dissolve
        $ renpy.pause ()
        hide in_the_meantime

        scene expression "day_07_scene_2_lisa_rachel_amy_scene_1[hair]" with dissolve
        "{color=#D2691E}*Lisa's phone rings disturbing her from a relaxing bath.*{/color}"
        r "Where the hell are you?"
        r "We have been waiting for you for the last half hour."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_2[hair]" with dissolve
    l "Sorry... ...I overslept... I'm about to leave the house..."
    r "Hurry up."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_3[hair]" with dissolve
    "{color=#D2691E}*Lisa quickly finishes her bath and gets dressed.*{/color}"
    "{color=#81F79F}*I completely forgot I planned to go out with them.*{/color}"
    "{color=#81F79F}*Rachel's gonna bitch again...*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_4[hair]" with dissolve
    "{color=#81F79F}*Okay, I think everything's packed.*{/color}"
    "{color=#D2691E}*Lisa looks around nervously.*{/color}"
    "{color=#81F79F}*Where the hell are the keys to the house?*{/color}"
    "{color=#81F79F}*Ah, here they are.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_5[hair]" with dissolve
    "{color=#81F79F}*I'll ride my bike. It will be faster.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_6[hair]" with dissolve
    "{color=#D2691E}*A few minutes later she's in the park.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_6a[hair]" with dissolve
    "{color=#D2691E}*She carefully passes the children playing and reaches the narrow path winding between the trees.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_7[hair]" with dissolve
    "{color=#D2691E}*Few minutes later she finally gets to the clearing.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_8[hair]" with dissolve
    r "Finally."
    l "I'm sorry, but I overslept."
    amy "That's all right."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_9[hair]" with dissolve
    "{color=#D2691E}*Lisa stips off her outer clothes and lays the towel down.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_10[hair]" with dissolve
    amy "We were just about to go swimming, will you join us?"
    l "Sure."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_11[hair]" with dissolve
    "{color=#D2691E}*The girls get up from their towels and slowly enter the water.*{/color}"
    "{color=#D2691E}*The water is cool and the air is already warmed up by the sun.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_12[hair]" with dissolve
    "{color=#D2691E}*She swims to the middle of the lake and then decides to float on her back.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_13[hair]" with dissolve
    "{color=#81F79F}*[player_name]... what shall I do now?*{/color}"
    "{color=#81F79F}*Why can't we be together?*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_14[hair]" with dissolve
    "{color=#81F79F}*Do I have to share you with other women to be with you?*{/color}"
    "{color=#81F79F}*Rachel was right... I shouldn't have been convinced that you felt the same way about me as I did about you.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_15[hair]" with dissolve
    "{color=#81F79F}*Jesus... why must life be so unfair?*{/color}"
    "{color=#81F79F}*I've waited so long for you, and now that you're finally with me, you can't just be mine.*{/color}"
    "{color=#81F79F}*What am I supposed to do now?*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_16[hair]" with dissolve
    "{color=#D2691E}*Amy's screaming rips her out of her thoughts.*{/color}"
    "{color=#D2691E}*Lisa looks in her direction and sees the girls waving at her to come back.*{/color}"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_17[hair]" with dissolve
    amy "What had you deep in thought that you didn't hear us?"
    l "Nothing..."
    amy "We've been calling you for a few minutes."
    l "No way. I didn't hear anything."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_25[hair]" with dissolve
    "{color=#D2691E}*Lisa sits on the blanket next to Rachel and Amy.*{/color}"
    "{color=#D2691E}*Rachel looks at her.*{/color}"
    r "What's bothering you, because I can't keep looking at that sad face of yours."
    l "I met with [player_name] yesterday."
    r "And?"

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_26[hair]" with dissolve
    l "I finally told him how I feel about him."
    amy "Then why are you so sad?"
    l "Because I don't know what to do."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_27[hair]" with dissolve
    r "Why?"
    l "After I confessed my feelings for him, he told me a strange story about two women."
    l "Then he told me that he loves them and that they've been in an open relationship for several years."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_28[hair]" with dissolve
    "{color=#D2691E}*Rachel's starting to laugh.*{/color}"
    l "Could you be serious for once?"
    r "I'm sorry."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_29[hair]" with dissolve
    l "In the end, he told me he loves me too, and if I want to, we can be together, but he won't break up with those girls, so I would have to accept that."
    r "Well, I guess that's good? I don't understand why you're so sad."
    l "Because that's not what I expected!"

    scene day_07_scene_2_lisa_rachel_amy_scene_30 with dissolve
    r "I think you're overreacting as usual."
    r "First, he was honest with you and told you the truth. That means he trusts you and respects you."
    r "Secondly, such relationships are increasingly popular nowadays and there is nothing wrong with them."

    scene day_07_scene_2_lisa_rachel_amy_scene_31 with dissolve
    r "And thirdly, if he's not alone and you want to be with him, this is your chance to make your dreams come true."
    amy "Otherwise, you can forget about him because, as he told you, he won't end his relationship for you."
    amy "I know it sounds weird, but in that case, his proposition is an opportunity for you."

    scene day_07_scene_2_lisa_rachel_amy_scene_32 with dissolve
    amy "Open relationships are not the end of the world. If you love each other and trust each other, only something good can come out of it."
    r "I've long dreamed of such a relationship. Only like Amy said, a relationship must be based on mutual trust and honesty."
    r "Otherwise, it won't work."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_33[hair]" with dissolve
    l "You think I should try?"
    amy "Of course."
    r "You have nothing to lose."

    scene day_07_scene_2_lisa_rachel_amy_scene_34 with dissolve
    amy "Exactly. I think you can only take advantage of that, and who knows what's going to come of it. How about something cool?"
    r "At worst, you'll go back to the starting point and be sad like this."
    amy "If I were you, I wouldn't hesitate to accept his proposal."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_35[hair]" with dissolve
    l "I guess you're right."
    l "Thank you."
    l "Do you really think I should try?"

    scene day_07_scene_2_lisa_rachel_amy_scene_36 with dissolve
    r "Eh... Lisa, honey, what do you have to lose? Look at it from this side. If you reject his offer, you'll be on your own and you'll wonder what would happen if you did accept his offer."
    r "After a while, it will become your obsession and who knows how it will end."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_37[hair]" with dissolve
    r "But if you give it a chance, if nothing comes out of it, you'll be aware that you've done everything you can and with time the pain will disappear and you'll be able to live normally."
    r "In this situation, you just have no other choice. I told you that your perception of him and your relationship could be very different from reality."
    r "And I'm sorry to say I was right."

    scene day_07_scene_2_lisa_rachel_amy_scene_38 with dissolve
    amy "Rachel is absolutely right. We won't convince you to do anything, but look at it the way Rachel described it to you."
    amy "If you still think you can somehow overcome your pain and move forward leaving [player_name] behind, don't get involved in this open relationship, but if you already have a shadow of doubt, try."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_39[hair]" with dissolve
    amy "It can happen that he's right, and this relationship is perfect for you, and these two girls will be like friends or sisters to you."
    r "Or lovers. HAHA."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_40[hair]" with dissolve
    "{color=#D2691E}*Lisa looks at Rachel with daggers in her eyes.*{/color}"
    r "Sorry, I couldn't resist."
    l "Thanks, I have to think it over. That does make a sort of sense and I see the logic in that. I'll honestly say I did not look at it like that, thank you."

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause()

    scene day_07_scene_2_lisa_rachel_amy_scene_19 with dissolve
    "{color=#D2691E}*Lisa starts eating.*{/color}"
    "{color=#D2691E}*After few minutes Rachel says.*{/color}"
    r "We were at the club yesterday."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_20[hair]" with dissolve
    r "We were sitting at the table when two drunken jackasses started hitting on us."
    r "They didn't want to leave us alone."
    r "Suddenly a guy came up to them and politely asked them to leave us alone."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_21[hair]" with dissolve
    r "But they wanted to beat him up."
    r "However, he dealt with them in seconds."
    amy "When we left the club, we saw him fighting with another guy in the parking lot."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_22[hair]" with dissolve
    r "The guy was about twice his size, but he dealt with him quickly."
    r "Too bad you didn't see him move, literally like a cat."
    amy "When the fight was over we came up to him to say thank you."

    scene day_07_scene_2_lisa_rachel_amy_scene_23 with dissolve
    amy "It turned out that our savior was [player_name]."
    l "Oh?!"
    r "Damn, you are lucky Lisa. He is awesome."

    scene day_07_scene_2_lisa_rachel_amy_scene_24 with dissolve
    amy "He drove us home afterwards."
    amy "We want to invite him for a drink and thank him for his help. I hope you don't mind."
    r "It would be great if you came too. We would have a small party."

    menu amy_rachel_party_invitation:

        "{color=#74B2F4}Accept the invitation.{/color} [LisaPath]":

            scene expression "day_07_scene_2_lisa_rachel_amy_scene_24a[hair]" with dissolve
            l "Hmm... Maybe it's not such a bad idea."
            r "Of course it's not."
            $ lisa_invitation = True

        "{color=#74B2F4}Decline the invitation.{/color}":

            scene expression "day_07_scene_2_lisa_rachel_amy_scene_24a[hair]" with dissolve
            l "I'm sorry Rachel, but it is a bad idea."
            r "Okay, as you wish, but if you change your mind you are always welcome."
            l "Thanks."

    scene expression "day_07_scene_2_lisa_rachel_amy_scene_41[hair]" with dissolve
    l "It's getting late. I gotta get going."
    r "Let us know how it goes with [player_name]."
    l "I will, bye."

    jump day_07_scene_3

#####################################################################################################################################################
                                                    #############SCENE 03 - Linda - first lesson#############
#####################################################################################################################################################
label day_07_scene_3:

    scene black with dissolve
    show in_the_meantime with dissolve
    $ renpy.pause ()
    hide in_the_meantime

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_07_scene_03_linda_scene_1 with dissolve
    "{color=#D2691E}*Linda wakes up with a massive headache.*{/color}"
    "{color=#D2691E}*She can hardly open her eyes, but she can't see much, because the room is dark.*{/color}"

    scene day_07_scene_03_linda_scene_2 with dissolve
    li "Where am I?"
    "{color=#D2691E}*Eyes are slowly getting used to the darkness and Linda notices she's in some dirty and damp room.*{/color}"
    "{color=#D2691E}*There are no windows or any furniture except the dirty mattress she's lying on.*{/color}"

    scene day_07_scene_03_linda_scene_3 with dissolve
    li "What's happening to me?"
    "{color=#D2691E}*Linda tries to remember how she got here, but she doesn't remember anything.*{/color}"
    "{color=#D2691E}*With growing horror, Linda tries to get up.*{/color}"

    scene day_07_scene_03_linda_scene_4 with dissolve
    li "Why am I naked?"
    li "What is this all about?"

    scene day_07_scene_03_linda_scene_5 with dissolve
    "{color=#D2691E}*Linda walks up to the door and starts banging her fist on it.*{/color}"
    li "Let me out of here!"
    "{color=#D2691E}*Nothing happens.*{/color}"

    scene day_07_scene_03_linda_scene_6 with dissolve
    li "Help!"
    li "Somebody help me!"

    scene day_07_scene_03_linda_scene_7 with dissolve
    "{color=#D2691E}*After a few minutes Linda hears some noise on the other side of the door and starts screaming even louder.*{/color}"
    "{color=#D2691E}*Someone turns the key in the lock and the door opens.*{/color}"
    "{color=#D2691E}*Ming and a man enters the room.*{/color}"

    scene day_07_scene_03_linda_scene_8 with dissolve
    li "Mrs. Ming! I beg you, give me another chance!"
    "{color=#D2691E}*Linda walks up to Mrs. Ming standing right at the door.*{/color}"
    li "Please!"

    scene day_07_scene_03_linda_scene_9 with dissolve
    ming "Shut up or I'll give you a reason to yell."
    ming "I warned you what happens if you don't pay your debts."
    li "I beg you, don't hurt me!"

    scene day_07_scene_03_linda_scene_10 with dissolve
    li "I'll give it all back. I promise!"
    ming "No, my dear. Now you'll work it all out."
    ming "Unless there's a buyer and I sell you for a profit."

    scene day_07_scene_03_linda_scene_11 with dissolve
    ming "There is no other option."
    ming "If you disobey, Mr. D will punish you."
    ming "And take my word for it, he knows his job."

    scene day_07_scene_03_linda_scene_12 with dissolve
    "{color=#D2691E}*The terrified Linda starts crying.*{/color}"
    li "I beg you, don't do this to me."

    scene day_07_scene_03_linda_scene_13 with dissolve
    ming "Failure to obey will be punished."
    ming "Mr. D is your master from now on and he's responsible for your obedience."
    ming "If you don't submit voluntarily, we will use other methods to force you to obey."

    scene day_07_scene_03_linda_scene_14 with dissolve
    "{color=#D2691E}*Ming and Mr. D leave the cell, closing the door behind them.*{/color}"
    "{color=#D2691E}*Linda's slowly beginning to understand the situation she's in.*{/color}"
    $ renpy.end_replay()

    jump day_07_scene_3a

#####################################################################################################################################################
                                                    #############SCENE 03a - Blackmailer#############
#####################################################################################################################################################
label day_07_scene_3a:

    scene black with dissolve
    show in_the_meantime with dissolve
    $ renpy.pause ()
    hide in_the_meantime

    if nicole_pictures == True:

        scene day_07_scene_3a_khloe_mary_scene_1 with dissolve
        mary "[player_name]! Come here. Check this out."
        mc "What's up?"

        scene day_07_scene_3a_khloe_mary_scene_2 with dissolve
        mary "You wanted me to hack into Karen's phone and email. Yesterday evening she got a dozen or so photos."
        mc "Can you open one?"
        mary "Of course."

        if nicole_helped == True:

            scene day_07_scene_3a_khloe_mary_scene_3 with dissolve
            mc "Goddamnit!"
            mary "Jesus... Is this Nicole?"

            scene day_07_scene_3a_khloe_mary_scene_4 with dissolve
            mc "Yes..."
            kh "Let me see."
            mc "These are Nicole's photos."

            scene day_07_scene_3a_khloe_mary_scene_5 with dissolve
            "{color=#D2691E}*You look at the other photos.*{/color}"
            mc "Now I have the proof, I'll have to pay her a visit."
            mc "Khloe, would you go to this address and look around a little bit?"

        else:

            scene day_07_scene_3a_khloe_mary_scene_3a with dissolve
            mc "Goddamnit!"
            mary "Jesus... Is this Nicole?"

            scene day_07_scene_3a_khloe_mary_scene_4 with dissolve
            mc "Yes..."
            kh "Let me see."
            mc "These are Nicole's photos."

            scene day_07_scene_3a_khloe_mary_scene_5a with dissolve
            "{color=#D2691E}*You look at the other photos.*{/color}"
            mc "Now I have the proof, I'll have to pay her a visit."
            mc "Khloe, would you go to this address and look around a little bit?"

        scene day_07_scene_3a_khloe_mary_scene_6 with dissolve
        kh "Yeah, sure. No problem."
        mc "Thanks. If you notice anything suspicious, please let me know."
        kh "Of course."

        scene day_07_scene_3a_khloe_mary_scene_7 with dissolve
        mc "Did you find anything else?"
        mary "There is more of that. Every two or three weeks Nicole sent Karen a bunch of photos."
        mc "Damnit. Now I know why Nicole is behaving like this and I'm not surprised."

        scene day_07_scene_3a_khloe_mary_scene_8 with dissolve
        mary "She must be going through hell. To be so humiliated..."
        mc "Well, that's right. I wonder how much money she has given her so far."
        mary "I'll check. Maybe there's something in those e-mails."

        scene day_07_scene_3a_khloe_mary_scene_9 with dissolve
        kh "Marry, give me Karen's address."
        mary "I will text it to you."
        kh "Thanks, I'm going. I'll see what's going on there and let you know."

        scene day_07_scene_3a_khloe_mary_scene_10 with dissolve
        mc "Thanks, just be careful and don't do anything hasty."
        mc "I haven't decided how to play it yet."
        kh "Sure. You know me. I never do anything hasty. HAHA"

        scene day_07_scene_3a_khloe_mary_scene_11 with dissolve
        "{color=#D2691E}*Khloe kisses you and leaves.*{/color}"

        scene day_07_scene_3a_khloe_mary_scene_12 with dissolve
        mc "I'm going too. I have to meet Lisa and her sisters."
        mary "Sure."
        mary "Don't make me wait too long for you."
        mc "I'll be back as soon as I can."

        scene day_07_scene_3a_khloe_mary_scene_13 with dissolve
        mc "Let me know if Khloe calls."
        mary "I will, don't worry."
        mc "See you tonight."
        mary "Bye."

        jump day_07_scene_04

    else:

        scene day_07_scene_3a_khloe_mary_scene_2 with dissolve
        mc "I was thinking about Karen and how to deal with her."
        mc "But so far I didn't come up with any plan."
        mc "Khloe, would you go to Karen's place and look around a little bit?"

        scene day_07_scene_3a_khloe_mary_scene_6 with dissolve
        kh "Yeah, sure. No problem."
        mc "Thanks. If you notice anything suspicious, please let me know."
        kh "Of course."

        scene day_07_scene_3a_khloe_mary_scene_9 with dissolve
        kh "Marry, give me Karen's address."
        mary "I will text it to you."
        kh "Thanks, I'm going. I'll see what's going on there and let you know."

        scene day_07_scene_3a_khloe_mary_scene_10 with dissolve
        mc "Thanks, just be careful and don't do anything hasty."
        mc "I haven't decided how to play it yet."
        kh "Sure. You know me. I never do anything hasty. HAHA"

        scene day_07_scene_3a_khloe_mary_scene_11 with dissolve
        "{color=#D2691E}*Khloe kisses you and leaves.*{/color}"
        mc "I'm going too. I have to meet Lisa and her sisters."
        mary "Sure."

        scene day_07_scene_3a_khloe_mary_scene_12 with dissolve
        "{color=#D2691E}*Mary kisses you.*{/color}"
        mary "Don't make me wait too long for you."
        mc "I'll be back as soon as I can."

        scene day_07_scene_3a_khloe_mary_scene_13 with dissolve
        mc "Let me know if Khloe calls."
        mary "I will, don't worry."
        mc "See you tonight."
        mary "Bye."

        jump day_07_scene_04

#####################################################################################################################################################
                                                    #############SCENE 04 - Truth about letters revealed#############
#####################################################################################################################################################
label day_07_scene_04:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_07_scene_4_truth_scene_1 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{/color}"

    scene day_07_scene_4_truth_scene_2 with dissolve
    j "Oh, hi [player_name]."
    mc "Hello, Jennifer."

    if jennifer_kiss_day_06 == True:

        scene day_07_scene_4_truth_scene_3 with dissolve
        j "I'm sorry about that kiss. I really don't know what's got into me."
        mc "You have nothing to apologize for. Nothing happened."

        scene day_07_scene_4_truth_scene_4 with dissolve
        j "Are you sure? I couldn't sleep all night because of it."
        mc "How could I be angry that a beautiful woman who is close to my heart kissed me goodbye."

        scene day_07_scene_4_truth_scene_5 with dissolve
        "{color=#D2691E}*Jennifer blushes.*{/color}"
        j "Don't make fun of me."
        mc "I'm serious and honest."

        menu compliment_jennifer_day_7:

            "{color=#4169E1}Compliment her.{/color} [JenniferLovePath]": # jennifer +1

                scene day_07_scene_4_truth_scene_6 with dissolve
                "{color=#D2691E}*You approach her closer and gently raise her head so that your eyes meet.*{/color}"
                mc "You're a beautiful woman and only a fool won't see it."

                scene day_07_scene_4_truth_scene_7 with dissolve
                mc "And the fact that I love you is probably obvious to everyone. My feelings for you have not changed in all these years."
                mc "You are an important person in my life."

                scene day_07_scene_4_truth_scene_8 with dissolve
                "{color=#D2691E}*Jennifer hugs you.*{/color}"
                j "Thank you..."
                j "I love you too."
                $ jennifer_love += 1

                scene day_07_scene_4_truth_scene_9 with dissolve
                l "Jennifer, who's here?"
                j "[player_name]."

            "{color=#4169E1}Say nothing.{/color}":

                scene day_07_scene_4_truth_scene_8 with dissolve
                l "Jennifer, who's here?"
                j "[player_name]."

    else:

        scene day_07_scene_4_truth_scene_9 with dissolve
        l "Jennifer, who's here?"
        j "[player_name]."

    scene day_07_scene_4_truth_scene_10 with dissolve
    l "Well, don't stand in the doorway."
    j "Come in, please."

    scene expression "day_07_scene_4_truth_scene_11[hair]" with dissolve
    l "Hello, [player_name]."
    mc "Hi."

    scene expression "day_07_scene_4_truth_scene_12[hair]" with dissolve
    "{color=#D2691E}*You come up to her to say hello, but Lisa turns her head."
    l "We'll talk later."
    mc "Okay."

    scene expression "day_07_scene_4_truth_scene_13[hair]" with dissolve
    "{color=#D2691E}*You enter the living room.*{/color}"
    mc "Is Nicole home?"
    j "I think so."

    scene expression "day_07_scene_4_truth_scene_14[hair]" with dissolve
    l "Do you want me to get her?"
    mc "If you would please, I have to tell you something and it would be good if you all were here."

    scene expression "day_07_scene_4_truth_scene_15[hair]" with dissolve
    l "Okay. I'll be right back."

    scene black with fade

    scene expression "day_07_scene_4_truth_scene_16[hair]" with dissolve
    "{color=#D2691E}*A few moments later, Lisa comes back down.*{/color}"
    l "Nicole's coming right down."
    mc "Thank you."

    scene day_07_scene_4_truth_scene_17 with dissolve
    j "I'm starting to worry. You have a very serious look. Is something wrong?"
    mc "You're about to find out everything. Just a little more patience."

    scene day_07_scene_4_truth_scene_18 with dissolve
    n "What is this about?"
    mc "Hi, Nicole."

    scene day_07_scene_4_truth_scene_19 with dissolve
    j "Is it about our mother?"

    menu truth_about_linda:

        "{color=#4169E1}Tell them whole truth.{/color} [JenniferLovePath] [LisaLovePath] [NicoleLovePath] [LindaSubmissionPath]":

            scene expression "day_07_scene_4_truth_scene_20[hair]" with dissolve
            mc "Yes."
            j "Did something happen to her?"
            l "I haven't seen her in a few days."

            scene expression "day_07_scene_4_truth_scene_21[hair]" with dissolve
            mc "You're about to find out everything."
            mc "So... "
            mc "For all these years, I was convinced that your mother was behind everything bad that happened to me in life."

            scene day_07_scene_4_truth_scene_22 with dissolve
            mc "However, since I came back to town, a lot of strange, sometimes incomprehensible things have happened that have made me think about it again."
            mc "But one at a time."
            mc "I learned some interesting things about your mother."

            scene expression "day_07_scene_4_truth_scene_23[hair]" with dissolve
            mc "What you hear will be difficult for you to accept."
            mc "However, I think you should find out about everything, because this also applies to you."
            mc "Your mother is a bad person."

            scene expression "day_07_scene_4_truth_scene_24[hair]" with dissolve
            mc "She used you, my father, and me to fulfill her desires."
            mc "She got addicted to gambling."
            mc "In the beginning she had access to my father's bank accounts and thus paid for her addiction."
            mc "But my father finally cut her off from the money and Linda was forced to borrow money."

            scene day_07_scene_4_truth_scene_25 with dissolve
            mc "Unfortunately, after my father's death, the situation became even more complicated for her."
            mc "She had no money, and the money for Lisa's studies was already spent."
            mc "So Linda was planning to sell the house to pay off her bookies' debts and get rid of you."
            mc "However, my father did not bequeath the house to her but me and removed her from his company."

            scene expression "day_07_scene_4_truth_scene_26[hair]" with dissolve
            mc "Few days ago she tried to embezzel $50.000 from the company but I stopped her."
            mc "The debts grew, and she had nothing to pay them off."

            scene expression "day_07_scene_4_truth_scene_27[hair]" with dissolve
            mc "The deadline for paying the debts expired yesterday."
            mc "I do not know what the contract was for, but it expired yesterday and as she probably not paid her debts I do not know what has happened to her."

            scene expression "day_07_scene_4_truth_scene_28[hair]" with dissolve
            "{color=#D2691E}*Jennifer and Lisa sit without a word staring at you and Nicole stands up and starts to circle around the room.*{/color}"
            mc "I know this is a shock to you, but unfortunately it is the truth."
            mc "I'm sorry to tell you this, but I thought you deserved the truth."

            scene expression "day_07_scene_4_truth_scene_29[hair]" with dissolve
            j "How could she do such a thing to us..."
            l "I hate her."
            l "She hasn't been interested in us for as long as I can remember."

            scene expression "day_07_scene_4_truth_scene_30[hair]" with dissolve
            l "She deserved that."
            j "Lisa, don't say that, she's our mother after all."
            l "I don't care. She never acted like our mother. She has what she deserves."

            scene day_07_scene_4_truth_scene_31 with dissolve
            n "SHUT UP, Lisa!"
            n "I can't believe all this."
            n "You're lying, [player_name]!"

            scene day_07_scene_4_truth_scene_32 with dissolve
            mc "Am i?"
            mc "It was Linda who blackmailed me, accused me of murdering my friend and forced me to leave."
            mc "It was Linda who that night told me to leave stole my phone and then deleted my email."

            scene expression "day_07_scene_4_truth_scene_33[hair]" with dissolve
            mc "It was Linda who took Jennifer's phone and said I stole it."
            mc "It was Linda, when my father died, who wanted to sell the house to pay off her gambling debts."

            scene expression "day_07_scene_4_truth_scene_34[hair]" with dissolve
            mc "It was Linda who wanted you out by sending you to boarding schools."
            mc "Lisa, that's why she didn't help you find a school, because at the same time she found you a school 2000 miles away from here."
            n "I don't believe you..."

            $ jennifer_love += 1
            $ lisa_love += 1
            $ nicole_love += 1
            $ linda_submission += 2
            $ truth_about_linda = True

        "{color=#4169E1}Tell them only what they need to know.{/color}":

            scene expression "day_07_scene_4_truth_scene_20[hair]" with dissolve
            mc "Yes."
            j "Did something happen to her?"
            l "I haven't seen her in a few days."

            scene expression "day_07_scene_4_truth_scene_27[hair]" with dissolve
            mc "As far as I know, your mother has debts, and the deadline for paying them expired yesterday, and she had no way of repaying them."
            mc "I'm afraid you won't see her for awhile."

            scene expression "day_07_scene_4_truth_scene_28[hair]" with dissolve
            "{color=#D2691E}*Jennifer and Lisa sit without a word staring at you and Nicole stands up and starts to circle around the room.*{/color}"
            mc "I know this is a shock to you, but unfortunately it is the truth."

    scene expression "day_07_scene_4_truth_scene_35[hair]" with dissolve
    mc "But that's not all I wanted to tell you."

    menu truth_about_letters:

        "{color=#4169E1}Tell them whole truth.{/color} [JenniferLovePath] [LisaLovePath] [NicoleLovePath] [LindaSubmissionPath]":

            scene expression "day_07_scene_4_truth_scene_36[hair]" with dissolve
            mc "I'd like to talk to you about what happened ten years ago. All this time you have been living in the conviction that I left you for no reason."
            mc "In addition, over the years your mother has tried to make me look like a monster, who cannot be trusted and who will do anything to hurt you."
            mc "It is time to finally clarify this matter."
            mc "Fortunately, I was able to find something that allowed me to finally explain to you that I did not leave without a reason."

            scene expression "day_07_scene_4_truth_scene_38[hair]" with dissolve
            mc "Here are all the letters I sent you. They haven't even been opened. If you want, you can see for yourselves what I wrote to you."
            j "Jesus. You were telling the truth!"

            scene expression "day_07_scene_4_truth_scene_39[hair]" with dissolve
            l "I told you that something must have happened that we didn't know about, that forced [player_name] to leave."
            j "You were right..."

            scene day_07_scene_4_truth_scene_40 with dissolve
            j "[player_name], I'm so sorry I wrongly accused you of everything."
            mc "I don't blame you at all. You had every right to hate me."
            j "Where did you find them?"

            scene expression "day_07_scene_4_truth_scene_41[hair]" with dissolve
            mc "Two days ago I picked up a package that contained these letters."
            l "Package?"
            mc "Yes, someone sent it after my father died."

            scene expression "day_07_scene_4_truth_scene_42[hair]" with dissolve
            j "Strange. Why would someone keep your letters and why did they send them right now?"
            mc "I don't know that yet."
            l "Don't you know who sent the package?"

            scene expression "day_07_scene_4_truth_scene_43[hair]" with dissolve
            mc "Well... The courier company says the sender was my father."
            mc "And I would have believed it if it hadn't been for the fact that the package was sent after his death."

            scene expression "day_07_scene_4_truth_scene_44[hair]" with dissolve
            j "[player_name], what is this all about?"
            mc "I don't know, but I'll find out."

            scene expression "day_07_scene_4_truth_scene_45[hair]" with dissolve
            j "This is so unrealistic."
            mc "I know, I couldn't believe it either, but the facts speak for themselves."

            scene expression "day_07_scene_4_truth_scene_46[hair]" with dissolve
            j "How do you know about our mother's debts?"
            mc "I learned a lot from her secretary, Clara. Besides your mother tried to transfer $50,000 from my father's company account to one of the casino owners."
            mc "I talked to this person and she confirmed to me that Linda owes her over $100,000."

            scene expression "day_07_scene_4_truth_scene_47[hair]" with dissolve
            mc "I have the impression, however, that this is just the tip of the iceberg and sooner or later we will learn much more about it."
            j "I know you hate her for what she did to you, but maybe you could help her out?"
            mc "I don't know. It sounds brutal, but she has what she deserves."

            scene expression "day_07_scene_4_truth_scene_48[hair]" with dissolve
            j "I know and understand you, but please do it for us."
            j "This is our mother after all, and we can't leave her like this."

            $ jennifer_love += 1
            $ lisa_love += 1
            $ nicole_love += 1
            $ linda_submission += 1
            $ truth_about_letters = True

            menu help_linda:

                "{color=#4169E1}Agree.{/color} [JenniferLovePath] [LisaLovePath] [NicoleLovePath] [LindaSubmissionPath]":

                    scene expression "day_07_scene_4_truth_scene_49[hair]" with dissolve
                    mc "Okay. I will try to do something about it, but I'm only doing it for you three."
                    j "I appreciate that and thank you very much."

                    scene expression "day_07_scene_4_truth_scene_50[hair]" with dissolve
                    mc "I'll do anything for you, you should know that."
                    j "I know, but I also do not know how much it will cost you."

                    $ jennifer_love += 1
                    $ lisa_love += 1
                    $ nicole_love += 1
                    $ linda_submission += 1
                    $ help_linda = True

                "{color=#4169E1}Don't agree.{/color}":

                    scene expression "day_07_scene_4_truth_scene_49[hair]" with dissolve
                    mc "I don't know. Would you do it for me if you were me?"
                    j "I don't know..."
                    mc "So you understand I can't do that."

                    scene expression "day_07_scene_4_truth_scene_50[hair]" with dissolve
                    j "Yes, but I beg you, think about it."
                    mc "Eh... well. I'll think about it."
                    j "Thank you."

        "{color=#4169E1}Tell them only what they need to know.{/color}":

            scene expression "day_07_scene_4_truth_scene_36[hair]" with dissolve
            mc "I'd like to talk to you about what happened ten years ago. All this time you have been living in the conviction that I left you for no reason."
            mc "In addition, over the years your mother has tried to make me look like a monster, who cannot be trusted and who will do anything to hurt you."
            mc "It is time to finally clarify this matter."
            mc "Fortunately, I was able to find something that allowed me to finally explain to you that I did not leave without a reason."

            scene expression "day_07_scene_4_truth_scene_38[hair]" with dissolve
            mc "Here are all the letters I sent you. They haven't even been opened. If you want, you can see for yourselves what I wrote to you."
            j "Jesus. You were telling the truth!"

            scene expression "day_07_scene_4_truth_scene_39[hair]" with dissolve
            l "I told you that something must have happened that we didn't know about, that forced [player_name] to leave."
            j "You were right..."

            scene day_07_scene_4_truth_scene_40 with dissolve
            j "[player_name], I'm so sorry I wrongly accused you of everything."
            mc "I don't blame you at all. You had every right to hate me."
            j "Where did you find them?"

            scene expression "day_07_scene_4_truth_scene_41[hair]" with dissolve
            mc "Two days ago I got a package with these letters in it."
            l "Package?"
            mc "Yes, someone sent it to me after my father died."
            mc "Unfortunately, I don't know anything else."

            scene expression "day_07_scene_4_truth_scene_47[hair]" with dissolve
            j "I know you hate her for what she did to you, but maybe you could help her out?"
            mc "I don't know. It sounds brutal, but she has what she deserves."

            scene expression "day_07_scene_4_truth_scene_48[hair]" with dissolve
            j "I know and understand you, but please do it for us."
            j "This is our mother after all, and we can't leave her like this."

            menu help_linda_1:

                "{color=#4169E1}Agree.{/color} [JenniferLovePath]":

                    scene expression "day_07_scene_4_truth_scene_49[hair]" with dissolve
                    mc "Okay. I will try to do something about it, but I'm only doing it for you."
                    j "I appreciate that and thank you very much."

                    scene expression "day_07_scene_4_truth_scene_50[hair]" with dissolve
                    mc "I'll do anything for you, you should know that."
                    j "I know, I also do not know how much it will cost you."

                    $ jennifer_love += 1
                    $ help_linda = True

                "{color=#4169E1}Don't agree.{/color}":

                    scene expression "day_07_scene_4_truth_scene_49[hair]" with dissolve
                    mc "I don't know. Would you do it for me if you were me?"
                    j "I don't know..."
                    mc "So you understand I can't do that?"

                    scene expression "day_07_scene_4_truth_scene_50[hair]" with dissolve
                    j "Yes, but I beg you, think about it."
                    mc "Eh... well. I'll think about it."
                    j "Thank you."

    scene expression "day_07_scene_4_truth_scene_51[hair]" with dissolve
    "{color=#D2691E}*This is too much for Nicole and she leaves the room with tears in her eyes.*{/color}"
    mc "I'll go to her."
    j "Thank you."

    if nicole_helped == True:

        scene day_07_scene_4_truth_scene_52 with dissolve
        "{color=#D2691E}*You go into her room. Nicole is sitting on the bed and crying.*{/color}"
        n "Leave me alone."

        scene day_07_scene_4_truth_scene_53 with dissolve
        "{color=#D2691E}*You sit next to her.*{/color}"

        scene day_07_scene_4_truth_scene_54 with dissolve
        "{color=#D2691E}*You can't watch her crying. Deep down, you know she's learned her lesson.*{/color}"
        "{color=#D2691E}*You move closer to her and wipe tears from her cheeks.*{/color}"

        scene day_07_scene_4_truth_scene_55 with dissolve
        n "Why are you so kind to me?"
        n "After all I've done to you?"

        menu nicole_chat:

            "{color=#74B2F4}You're my little Nicole.{/color} [NicoleLovePath]":

                scene day_07_scene_4_truth_scene_55 with dissolve
                mc "Because you're my little Nicole..."

                scene day_07_scene_4_truth_scene_56 with dissolve
                "{color=#D2691E}*Nicole cuddles up to you.*{/color}"
                n "I wish everything was as it used to be..."
                mc "It could be. It's up to us."

                $ nicole_love += 1

            "{color=#74B2F4}I'm a good guy.{/color}":

                scene day_07_scene_4_truth_scene_55 with dissolve
                mc "Because I'm a good guy."

        scene day_07_scene_4_truth_scene_57 with dissolve
        n "It's not that simple, [player_name]."
        mc "I realize that, but I think it's worth a try."
        n "Would you be able to forget everything I've done to you?"

        scene day_07_scene_4_truth_scene_58 with dissolve
        mc "I think so, yes."
        n "You know I lied to you...?"
        mc "I know."

        scene day_07_scene_4_truth_scene_59 with dissolve
        n "And you're helping me anyway?"
        mc "Yes."
        n "But why?"

        menu nicole_chat_2:

            "{color=#74B2F4}Because I'd do anything for you.{/color} [NicoleLovePath]":

                scene day_07_scene_4_truth_scene_60 with dissolve
                n "I was acting like a bitch, lying to you, extorting money from you, conspiring with my mother against you, even trying to argue you with my sisters."
                n "And you helped me..."

                scene day_07_scene_4_truth_scene_61 with dissolve
                mc "Because I'd do anything for you. I was hoping it would make you look at me in a different way."
                mc "That all the hatred for me built up over the years will disappear and we will love each other again as we used to."

                scene day_07_scene_4_truth_scene_62 with dissolve
                n "I want to change. I want to be happy again. I want us to be as close to each other as we used to be. I want us to trust each other again."
                n "[player_name], please try to understand me. I live in constant tension. Some time ago I did something stupid and I've been paying for it for a very long time."
                n "I don't have the strength anymore."

                scene day_07_scene_4_truth_scene_63 with dissolve
                n "Besides, for a long time I couldn't accept that you weren't in my life! As time went by, the pain of parting with you turned into anger and hatred."
                n "I am stupid.... Instead of being happy that you came back, I hated you even more. My mother had a big part in this, she told us all the time how terrible you are."
                n "I know that you have no reason to help me, to be interested in my life and my problems at all."

                $ nicole_love += 2

            "{color=#74B2F4}Because I still care about you.{/color}":

                scene day_07_scene_4_truth_scene_60 with dissolve
                n "I was acting like a bitch, lying to you, extorting money from you, conspiring with my mother against you, even trying to argue you with my sisters."
                n "And you helped me..."

                scene day_07_scene_4_truth_scene_61 with dissolve
                mc "Because I still care about you."
                mc "And I have hope that our relationship will change and we will trust eachother again."

                scene day_07_scene_4_truth_scene_62 with dissolve
                n "I want to change. I want to be happy again. I want us to be as close to each other as we used to be. I want us to trust each other again."
                n "[player_name], please try to understand me. I live in constant tension. Some time ago I did something stupid and I've been paying for it for a very long time."
                n "I don't have the strength anymore."

                scene day_07_scene_4_truth_scene_63 with dissolve
                n "Besides, for a long time I couldn't accept that you weren't in my life! As time went by, the pain of parting with you turned into anger and hatred."
                n "I am stupid.... Instead of being happy that you came back, I hated you even more. My mother had a big part in this, she told us all the time how terrible you are."
                n "I know that you have no reason to help me, to be interested in my life and my problems at all."

                $ nicole_love += 1

        scene day_07_scene_4_truth_scene_64 with dissolve
        mc "That's not true. I am very interested in you and your life."
        mc "I thought I'd be able to inspire trust in you in this way."
        n "And you made it. You did even more than you had to do."
        mc "Nicole, I know what's going on. I know what the money was for. I know what you're being forced to do."

        scene day_07_scene_4_truth_scene_65 with dissolve
        "{color=#D2691E}*Nicole opens her eyes wide out of surprise.*{/color}"
        n "What are you talking about?"
        mc "About your secret."

        scene day_07_scene_4_truth_scene_66 with dissolve
        n "..."
        mc "You don't have to keep hiding that you're being blackmailed."

        scene day_07_scene_4_truth_scene_67 with dissolve
        "{color=#D2691E}*Nicole looks at you with disbelief.*{/color}"
        n "How did you find out about this?"

        scene day_07_scene_4_truth_scene_68 with dissolve
        mc "That's not important, but what is important is that I know everything."
        mc "And if you want, I can help you get away from him."

        scene day_07_scene_4_truth_scene_69 with dissolve
        "{color=#D2691E}*Nicole starts sobbing. Her body is trembling. You hold her tightly.*{/color}"
        mc "{color=#AFEEEE}*you're whispering in her ear*{/color=#AFEEEE} It's okay. Calm down. Everything will be all right. I'll take care of him."
        n "Are you really gonna help me?"

        if nicole_pictures == True:

            scene day_07_scene_4_truth_scene_70 with dissolve
            mc "Yeah. I've seen what he's making you do, and I'm not gonna leave it at that."
            n "Have you seen my pictures?"

            scene day_07_scene_4_truth_scene_71 with dissolve
            mc "Yes."
            n "Oh, my God. I'm so ashamed."
            mc "It'll all be over soon enough. Don't worry about it anymore."
            n "How can I thank you?"

            menu nicole_promises:

                "{color=#74B2F4}Be my little Nicole again.{/color} [NicoleLovePath]":

                    scene day_07_scene_4_truth_scene_72 with dissolve
                    mc "Be my little Nicole again, and it'll all work out by itself."
                    n "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} I promise you that you will never be disappointed in me again."
                    n "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} You don't even know how grateful I am to you."

                    scene day_07_scene_4_truth_scene_73 with dissolve
                    "{color=#D2691E}*Nicole gives you a juicy kiss. Relief appears on her face and you notice the first smile on her face in a long time.*{/color}"
                    n "Thank you so much. "
                    mc "Just be that sweet little angel you used to be and that will be more than enough."

                    scene day_07_scene_4_truth_scene_74 with dissolve
                    n "I promise. I won't let you down again."
                    mc "I know."
                    n "Thank you."
                    $ nicole_love += 1

                "{color=#74B2F4}Stop acting like a mean bitch.{/color}":

                    scene day_07_scene_4_truth_scene_72a with dissolve
                    mc "Stop acting like a mean bitch and try to trust me."
                    mc "And if you do that I promise that you will not regret it."
                    n "I promise you that you will never be disappointed in me again."

                    scene day_07_scene_4_truth_scene_73b with dissolve
                    n "I won't let you down."
                    mc "I believe you."

        else:

            scene day_07_scene_4_truth_scene_71 with dissolve
            mc "Yes."
            mc "It'll all be over soon enough. Don't worry about it anymore."
            n "How can I thank you?"

            menu nicole_promises_1:

                "{color=#74B2F4}Be my little Nicole again.{/color} [NicoleLovePath]":

                    scene day_07_scene_4_truth_scene_72 with dissolve
                    mc "Be my little Nicole again, and it'll all work out by itself."
                    n "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} I promise you that you will never be disappointed in me again."
                    n "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} You don't even know how grateful I am to you."

                    scene day_07_scene_4_truth_scene_73 with dissolve
                    "{color=#D2691E}*Nicole gives you a juicy kiss. Relief appears on her face and you notice the first smile on her face in a long time.*{/color}"
                    n "Thank you so much. "
                    mc "Just be that sweet little angel you used to be and that will be more than enough."

                    scene day_07_scene_4_truth_scene_74 with dissolve
                    n "I promise. I won't let you down again."
                    mc "I know."
                    n "Thank you."
                    $ nicole_love += 1

                "{color=#74B2F4}Stop acting like a mean bitch.{/color}":

                    scene day_07_scene_4_truth_scene_72a with dissolve
                    mc "All you have to do is start trusting me again. That's enough to start with."
                    n "I won't let you down."

                    scene day_07_scene_4_truth_scene_73b with dissolve
                    n "Thank you so much for helping me."
                    mc "That's okay. You would do the same for me."

    scene black with fade
    $ renpy.pause (1)

    scene expression "day_07_scene_4_truth_scene_75[hair]" with dissolve
    "{color=#D2691E}*You go down to the living room.*{/color}"
    l "[player_name], could we talk for a second?"
    mc "Yeah, sure."

    scene expression "day_07_scene_4_truth_scene_76[hair]" with dissolve
    l "I still can't believe what you just told us."
    l "But I'm glad I was right. I knew you had a good reason to leave."
    mc "I'm glad you finally found out the truth."

    scene expression "day_07_scene_4_truth_scene_77[hair]" with dissolve
    mc "Unfortunately, this raises more questions and more doubts."
    mc "But sooner or later I will find out what my father and your mother were hiding."
    l "I'm sure you'll find answers to all the questions."

    scene expression "day_07_scene_4_truth_scene_78[hair]" with dissolve
    l "Listen... I apologize for my behavior earlier. I still don't know what to think about what you told me and I don't know what decision to make."
    mc "Nothing happened. I understand that perfectly."
    mc "Take your time. My proposal still stands and always will. When you're ready, you'll let me know."

    scene expression "day_07_scene_4_truth_scene_79[hair]" with dissolve
    l "I'm glad you're not mad at me."
    mc "Mad? At you?"

    scene expression "day_07_scene_4_truth_scene_80[hair]" with dissolve
    "{color=#D2691E}*Lisa embraces you and kisses on the cheek.*{/color}"
    l "See you soon."
    mc "Bye."

    scene black with fade
    $ renpy.pause (1)

    scene day_07_scene_4_truth_scene_81 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{/color}"
    j "Come in."

    scene day_07_scene_4_truth_scene_82 with dissolve
    mc "Am I interrupting?"
    j "No, come in."
    j "I'm reading your letters."

    scene day_07_scene_4_truth_scene_83 with dissolve
    mc "Again?"
    j "What you wrote in those letters is so beautiful."
    mc "Come on, you can't be serious."

    scene day_07_scene_4_truth_scene_84 with dissolve
    j "But I am."
    j "I finally know how you felt that night and I know that what you wrote was sincere."
    j "By the way, thank you again for wonderful time yesterday."

    scene day_07_scene_4_truth_scene_85 with dissolve
    j "I'm glad that our relationship has improved so much."
    mc "I am happy too."
    mc "I couldn't imagine a better start for our reunion."

    scene day_07_scene_4_truth_scene_86 with dissolve
    mc "I wish I could stay with you longer today but it is getting late and I still have some stuff to do."
    j "Will you come by tomorrow?"
    mc "Yes."

    scene day_07_scene_4_truth_scene_87 with dissolve
    j "That's great. Thank you for everything."
    mc "Have a good night."
    j "Bye."

    jump day_07_scene_05

#####################################################################################################################################################
                                                    #############SCENE 05 - Greetings from Paris#############
#####################################################################################################################################################
label day_07_scene_05:

    scene black with dissolve

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname
        $ k_sex = persistent.k_sex

        show screen endreplay_button

    if k_sex == True:

        scene black with dissolve
        show bg one_hour_later with dissolve
        $ renpy.pause ()

        scene day_07_scene_6_kelly_1 with dissolve
        k "Hi, [player_name]. Have you missed me?"
        mc "Kelly?"
        k "Yes."

        scene day_07_scene_6_kelly_2 with dissolve
        mc "How are you doing?"
        k "I'm fine, thanks."

        scene day_07_scene_6_kelly_3 with dissolve
        k "I've been in Paris for a few hours. I took a shower and now I'm lying on my bed thinking about you."
        mc "I've never been to Europe."
        k "You should come here sometime. Paris is beautiful, especially this time of year."

        scene day_07_scene_6_kelly_4 with dissolve
        k "How's your family stuff? Everything okay?"
        mc "Unfortunately, I haven't managed to get everything done yet, so I'm still in my hometown."
        k "That's good. I have a flight to Portland at the end of the week and I thought I could visit you."

        menu kelly_visit:

            "{color=#4169E1}That would be great.{/color} [KellyLovePath]":

                scene day_07_scene_6_kelly_5 with dissolve
                mc "That would be great."
                k "You know, I often think about you..."
                mc "I often think about you too."

                scene day_07_scene_6_kelly_6 with dissolve
                k "I can't wait to see you again."
                mc "Let me know exactly when you're in Portland and I'll come get you."
                k "Sure. See you soon."
                mc "Bye."

                scene day_07_scene_6_kelly_7 with dissolve
                "{color=#FF69B4}*Kelly's hanging up the phone. She takes the dildo out of her suitcase and smiles at herself.*{/color}"
                k "You're gonna have to be enough for now."

                scene day_07_scene_6_kelly_8 with dissolve
                "{color=#FF69B4}*She brings it up to her mouth and kisses it, then she licks it, taking the head of the dildo into her mouth.*{/color}"

                scene day_07_scene_6_kelly_9 with dissolve
                "{color=#FF69B4}*She laughs as she pushes the rubber cock further into her mouth sliding it in and out.*{/color}"

                scene day_07_scene_6_kelly_10 with dissolve
                "{color=#FF69B4}*Kelly lowers the dildo and brings it up between her legs until she feels the head of the cock start to push against her pussy.*{/color}"

                scene day_07_scene_6_kelly_11 with dissolve
                "{color=#FF69B4}*The lubrication did the trick and the dildo slides easily into her waiting cunt.*{/color}"

                scene day_07_scene_6_kelly_12 with dissolve
                "{color=#FF69B4}*Kelly let out a cry of pleasure as the dildo pushes harder against her swollen clit.*{/color}"
                "{color=#FF69B4}*She takes her firm round breast into her hand and squeeze it firmly.*{/color}"

                scene day_07_scene_6_kelly_13 with dissolve
                "{color=#FF69B4}*Kelly tosses her head back into the pillow and shakes it from side to side, while arching her back and thrusting her hips against the dildo.*{/color}"

                scene day_07_scene_6_kelly_14 with dissolve
                "{color=#FF69B4}*Her eyes are closed tightly as her moans grow louder and she loses herself over and over.*{/color}"
                "{color=#FF69B4}*The dildo is sliding back and forth. Kelly positions the dildo so it is stroking her clitoris in the same time.*{/color}"

                scene day_07_scene_6_kelly_15 with dissolve
                "{color=#FF69B4}*Kelly changes her position and picks up the pace."
                k "Yes, yes, yes."

                scene day_07_scene_6_kelly_16 with dissolve
                "{color=#FF69B4}*Her eyes are open now so is her mouth, whimpering with pleasure of the approaching climax.*{/color}"

                scene day_07_scene_6_kelly_17 with flash
                with flash
                with flash
                "{color=#FF69B4}*Finally, a great crashing wave of orgasm, a yell of relief and the ceiling disappearing in a burst of stars and colours as she comes and comes.*{/color}"

                scene day_07_scene_6_kelly_18 with dissolve
                k "It was intense. Shame it was only the dildo, not his huge member."
                k "But I'll soon feel him inside me again."
                $ renpy.end_replay()

                $ kelly_love += 2
                $ kelly_visit = True

                jump day_07_scene_06

            "{color=#4169E1}Maybe some other time.{/color}":

                scene day_07_scene_6_kelly_5 with dissolve
                mc "I'm sorry, but I'm too busy at the moment."
                mc "Maybe some other time."
                k "Okay, I understand that. Bye."
                $ renpy.end_replay()

                $ kelly_love -= 2

                jump day_07_scene_06

    else:

        jump day_07_scene_06

#####################################################################################################################################################
                                                    #############SCENE 06 - Khloe on the terrace#############
#####################################################################################################################################################
label day_07_scene_06:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_07_scene_07_khloe_scene_1 with dissolve
    mary "I'm so tired, but I'm glad we moved out of that hotel."
    mc "It's great that you managed to find this house."
    mary "We were lucky."

    scene day_07_scene_07_khloe_scene_2 with dissolve
    mary "It's nice to finally spend some time outdoors. The last few days have been very difficult for me."
    mc "Yes, it's been a tough week."
    mary "It is good that we went to the water park today. It's been a long time since I've been so happy."

    scene day_07_scene_07_khloe_scene_3 with dissolve
    mary "Besides, we finally managed to discuss important matters."
    mc "You're right. We finally have a plan of action and maybe we can finally move forward a little bit."

    scene day_07_scene_07_khloe_scene_4 with dissolve
    kh "What are you talking about?"
    mary "Nothing important at all."
    kh "That's good, [player_name] come with me."
    mc "I'll be right back."

    scene day_07_scene_07_khloe_scene_5 with dissolve
    mc "What's the matter? "
    kh "Just come with me."

    scene day_07_scene_07_khloe_scene_6 with dissolve
    "{color=#D2691E}*You follow Khloe.*{/color}"
    mc "Where are we going?"

    scene day_07_scene_07_khloe_scene_7 with dissolve
    "{color=#D2691E}*You go out on the terrace. Khloe stops by the railing.*{/color}"

    scene day_07_scene_07_khloe_scene_8 with dissolve
    "{color=#FF69B4}*Without a word, Khloe drops her dress to the floor, exposing her beautifully shaped body.*{/color}"

    scene day_07_scene_07_khloe_scene_9 with dissolve
    "{color=#FF69B4}*The desire in her eyes is clearly visible when she presses her full breasts against your chest.*{/color}"
    "{color=#FF69B4}*Your kiss become more and more passionate as your tongues entangle.*{/color}"

    scene day_07_scene_07_khloe_scene_10 with dissolve
    "{color=#FF69B4}*You are overwhelmed by the scent of her perfumes mixed with her natural musk.*{/color}"
    "{color=#FF69B4}*Her voice becomes a breathless whisper as you bury your face in the luscious flesh of her bosom.*{/color}"

    scene day_07_scene_07_khloe_scene_11 with dissolve
    "{color=#FF69B4}*Khloe tilts her head and starts quietly moaning with delight as you kiss her swollen nipples.*{/color}"

    scene day_07_scene_07_khloe_scene_12 with dissolve
    "{color=#FF69B4}*As you trail your down, you kiss every inch of her divine body.*{/color}"
    "{color=#FF69B4}*Your hands slowly move down along her spine, making her shiver.*{/color}"

    scene day_07_scene_07_khloe_scene_13 with dissolve
    "{color=#FF69B4}*As you reach her firm bottom, you gently squeeze and start to caress her buttocks.*{/color}"
    "{color=#FF69B4}*As you stop kissing her, you run a finger teasingly over the soft flesh between her thighs.*{/color}"

    scene day_07_scene_07_khloe_scene_14 with dissolve
    "{color=#FF69B4}*You open Khloe's legs and admire her perfect pussy as you move your head towards her lips.*{/color}"

    scene day_07_scene_07_khloe_scene_15 with dissolve
    "{color=#FF69B4}*You press your slithering tongue diligently against Khloe's pussy and start to stimulate her clitoris directly.*{/color}"

    scene day_07_scene_07_khloe_scene_16 with dissolve
    "{color=#FF69B4}*You slip two fingers inside Khloe's wet and tight pussy, causing her to hold her breath for a split of the second and releasing it with a loud moan.*{/color}"
    "{color=#FF69B4}*While your fingers caress her labia, you alternate between kissing, licking and sucking her clit.*{/color}"

    scene day_07_scene_07_khloe_scene_17 with dissolve
    "{color=#FF69B4}*Due to your attentions, Khloe's pussy get more and more wet. Her sweet juices flow down her thighs, and you greedily lap them up off her cunt.*{/color}"
    "{color=#FF69B4}*You feel Khloe trembling underneath your hands and you know her orgasm is near, so you caress her sweet clitoris more intensively to help her reach her climax.*{/color}"

    scene day_07_scene_07_khloe_scene_18 with flash
    with flash
    with flash

    scene day_07_scene_07_khloe_scene_19 with dissolve
    "{color=#FF69B4}*Khloe kneels before you and grabs hold of your erect cock.*{/color}"

    scene day_07_scene_07_khloe_scene_20 with dissolve
    "{color=#FF69B4}*She starts slow at first, licking the shaft from your balls to the very tip of your penis.*{/color}"
    "{color=#FF69B4}*Her tongue is everywhere at once, treating you with warm, wet care.*{/color}"

    scene day_07_scene_07_khloe_scene_21 with dissolve
    "{color=#FF69B4}*The precum starts flowing and she laps it up before she takes your entire member into her mouth.*{/color}"

    show khloe_blowjob with dissolve

    mc "Oh my God!"

    scene day_07_scene_07_khloe_scene_22 with dissolve
    "{color=#FF69B4}*Hesitant at first, the jerking becomes increasingly more involved.*{/color}"

    scene day_07_scene_07_khloe_scene_23 with dissolve
    "{color=#FF69B4}*She is sucking your dick with such a passion and you feel your climax approaching, so you pull your cock out of her mouth.*{/color}"

    scene day_07_scene_07_khloe_scene_24 with dissolve
    mc "Show me that beautiful ass of yours."

    scene day_07_scene_07_khloe_scene_25 with dissolve
    "{color=#FF69B4}*She turns around and flirtatiously bends her bottom inviting you to dip your swollen dick deep in her pussy.*{/color}"

    scene day_07_scene_07_khloe_scene_26 with dissolve
    "{color=#FF69B4}*You grab her beautiful ass and push the head of your cock against her pussy.*{/color}"
    "{color=#FF69B4}*The first thrusts are slow, agonizingly slow.*{/color}"

    show khloe_cowgirl with dissolve

    kh "Fuck me [player_name]! Fuck me harder!"

    scene day_07_scene_07_khloe_scene_27 with dissolve
    "{color=#FF69B4}*As she moans quietly, Khloe closes her eyes and bites her lower lip with such desire on her face.*{/color}"
    "{color=#FF69B4}*Her wet pussy feels so tight, stimulating your shaft all over and lubricating it with her juices.*{/color}"

    scene day_07_scene_07_khloe_scene_28 with dissolve
    "{color=#FF69B4}*Your thrusts become faster and faster.*{/color}"
    kh "Push it deeper, [player_name]. DEEPER!"

    scene day_07_scene_07_khloe_scene_29 with dissolve
    kh "Oh yeah... Don't stop!"
    kh "Fuck me harder!"

    scene day_07_scene_07_khloe_scene_30 with dissolve
    "{color=#FF69B4}*You proceed to fuck her slowly, pushing the full length of your dick into the moist depths.*{/color}"
    "{color=#FF69B4}*Khloe angles her body slightly to maximize the pleasure she's receiving from the thrusts of your cock.*{/color}"

    scene day_07_scene_07_khloe_scene_31 with dissolve
    kh "Oh yes! Yes! Oh fuck yes!"

    scene day_07_scene_07_khloe_scene_32 with flash
    with flash
    with flash

    scene day_07_scene_07_khloe_scene_33 with dissolve
    "{color=#FF69B4}*Her orgasm is so potent that you have to hold her tight as to not let her slip of your cock.*{/color}"

    scene day_07_scene_07_khloe_scene_34 with dissolve
    "{color=#FF69B4}*Completing a few more thrusts by yourself in her convulsing pussy, you feel you're ready too.*{/color}"

    call screen khloe_day_07_cumshots

label khloe_day_07_creampie:

    hide screen khloe_day_07_cumshots

    scene day_07_scene_07_khloe_scene_35 with dissolve
    mc "I'm... I'm cumming, Khloe!"

    scene day_07_scene_07_khloe_scene_36 with dissolve
    "{color=#FF69B4}*You keep fucking her until the last burst of seed has entered her vagina.*{/color}"
    "{color=#FF69B4}*Khloe enjoys the feeling of being filled up with your hot semen.*{/color}"

    scene day_07_scene_07_khloe_scene_37 with dissolve
    "{color=#FF69B4}*As you pull out your dick, the semen leaks out of her pussy and covers her thights.*{/color}"
    kh "It was something incredible."
    kh "I barely can stand now."

    scene day_07_scene_07_khloe_scene_38 with dissolve
    mc "Yeah. I'm still trembling. I love you and your gorgeus pussy."
    kh "And I love your huge member!"
    $ khloe_creampie += 1
    $ renpy.end_replay()

    jump after_sex_khloe_day_07

label khloe_day_07_facial:

    hide screen khloe_day_07_cumshots

    scene day_07_scene_07_khloe_scene_35 with dissolve
    mc "I'm... I'm cumming, Khloe!"

    scene day_07_scene_07_khloe_scene_39 with dissolve
    "{color=#FF69B4}*You keep fucking her until the last second.*{/color}"
    "{color=#FF69B4}*Khloe drops on her knees and you spray her beautiful face with warm cum.*{/color}"

    scene day_07_scene_07_khloe_scene_40 with dissolve
    "{color=#FF69B4}*A lot of semen ends up in her open mouth, the rest she scoops up with her fingers and licks them clean.*{/color}"
    kh "It was something incredible."
    kh "I barely can stand now."

    scene day_07_scene_07_khloe_scene_38 with dissolve
    mc "Yeah. I'm still trembling. I love you and your gorgeus pussy."
    kh "And I love your huge member!"
    $ renpy.end_replay()

    jump after_sex_khloe_day_07

label khloe_day_07_body:

    hide screen khloe_day_07_cumshots

    scene day_07_scene_07_khloe_scene_35 with dissolve
    mc "I'm... I'm cumming, Khloe!"

    scene day_07_scene_07_khloe_scene_41 with dissolve
    "{color=#FF69B4}*You keep fucking her until the last second.*{/color}"
    "{color=#FF69B4}*Khloe drops on her knees and you spray her beautiful breasts and belly with warm cum.*{/color}"

    scene day_07_scene_07_khloe_scene_42 with dissolve
    "{color=#FF69B4}*She scoops up some of your semen with her fingers and licks them clean.*{/color}"
    kh "It was something incredible."
    kh "I barely can stand now."

    scene day_07_scene_07_khloe_scene_38 with dissolve
    mc "Yeah. I'm still trembling. I love you and your gorgeus pussy."
    kh "And I love your huge member!"
    $ renpy.end_replay()

    jump after_sex_khloe_day_07

label after_sex_khloe_day_07:

    scene day_07_scene_07_khloe_scene_43 with dissolve
    "{color=#D2691E}*You both go back to Mary.*{/color}"
    mary "Well, you were gone for a long time did you have fun?"

    scene day_07_scene_07_khloe_scene_44 with dissolve
    kh "We had something to discuss and it took a while."
    "{color=#D2691E}*The girls start laughing.*{/color}"

    scene day_07_scene_07_khloe_scene_45 with dissolve
    "{color=#D2691E}*Khloe sits on your lap and hugs you.*{/color}"
    kh "I'm glad we finally got out of that nasty hotel."
    kh "I feel like we're together at last."

    scene day_07_scene_07_khloe_scene_46 with dissolve
    mc "You're right."
    mc "Getting out of the hotel was a great idea."

    scene day_07_scene_07_khloe_scene_47 with dissolve
    mary "Yes, now we can finally feel like being at home."
    mary "You know what? I have the impression that today was a breakthrough day and now everything will go much better and faster."

    scene day_07_scene_07_khloe_scene_48 with dissolve
    kh "I guess you're right. I hope that we can get over all the problems as soon as possible and get back to our old life."

    jump day_07_scene_07

#####################################################################################################################################################
                                                    ############# SCENE 07 - Isabella #############
#####################################################################################################################################################
label day_07_scene_07:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_1 with dissolve
    "{color=#D2691E}*Isabella fell asleep on the couch while watching the movie.*{/color}"

    scene day_07_scene_08_isabella_1a with dissolve
    "{color=#D2691E}*She wakes up after midnight. She feels very tired.*{/color}"

    scene day_07_scene_08_isabella_1b with dissolve
    "{color=#D2691E}*To cleanse the mind and wash away the tiredness she decides to take a shower.*{/color}"

    scene day_07_scene_08_isabella_2 with dissolve
    "{color=#D2691E}*She takes off her clothes and goes to the bathroom.*{/color}"

    scene day_07_scene_08_isabella_3 with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_4 with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_5 with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_6 with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_6a with dissolve
    $ renpy.pause ()

    scene day_07_scene_08_isabella_7 with dissolve
    "{color=#D2691E}*Half an hour later, wrapped only in a towel, she enters the bedroom.*{/color}"
    "{color=#D2691E}*She pours wine into a glass.*{/color}"

    scene day_07_scene_08_isabella_8 with dissolve
    "{color=#D2691E}*She turns on her laptop and plays some music.*{/color}"

    scene day_07_scene_08_isabella_9 with dissolve
    "{color=#D2691E}*She lies down on the bed and closes her eyes.*{/color}"
    "{color=#D2691E}*Suddenly she hears the sound of a new message notification, but ignores it.*{/color}"
    "{color=#D2691E}*After a while, another message and another one.*{/color}"

    scene day_07_scene_08_isabella_10 with dissolve
    "{color=#D2691E}*She takes her laptop and clicks on messenger.*{/color}"

    scene day_07_scene_08_isabella_11 with dissolve
    "{color=#D2691E}*Three messages.*{/color}"
    "{color=#D2691E}*She clicks on the new message icon and starts reading.*{/color}"

    scene day_07_scene_08_isabella_12 with dissolve
    man "Hello."
    man "Remember me?"
    man "I know you are there."

    scene day_07_scene_08_isabella_13 with dissolve
    "{color=#D2691E}*Isabella closes her laptop and puts it away..*{/color}"
    i "It couldn't be him."
    i "Probably a stupid joke..."

    scene day_07_scene_08_isabella_14 with dissolve
    "{color=#D2691E}*Isabella circles around the room cursing badly and trying to gather her thoughts.*{/color}"
    i "What if it's not a joke?"

    scene day_07_scene_08_isabella_15 with dissolve
    i "I can't go through all this again."
    i "What am I supposed to do now? Run away again?"

    scene day_07_scene_08_isabella_16 with dissolve
    "{color=#D2691E}*Tears flow down Isabella's face.*{/color}"
    i "It has to be a joke..."
    $ renpy.end_replay()

    jump end_of_day_7

#####################################################################################################################################################

label end_of_day_7:

    scene black with dissolve
    show end_of_day_07 with dissolve
    $ renpy.pause ()

    jump day_08
