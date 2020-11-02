label day_04:

    $ day = "Day 4"
    $ save_name = "Day 4"
    $ changeWallpaper()

    scene black with dissolve
    show bg day_04 with dissolve
    $ renpy.pause ()

    scene day_04_hotel_room with dissolve
    "{color=#81F79F}*Another day in this God-forsaken town.*{/color}"
    "{color=#81F79F}*Things with Linda aren’t going as I expected. At this rate, I'll spend a year here before I achieve my goals.*{/color}"

    scene day_04_hotel_room_1 with dissolve
    "{color=#81F79F}*At least things with the girls are going smoothly. Lisa seems to have a crush on me. I can’t complain. She's gorgeous and I would be stupid to whine about it.*{/color}"
    "{color=#81F79F}*Sandra is amazing too. We had a great night together. Maybe I could develop a deeper relationship with her?*{/color}"

    scene day_04_hotel_room_2 with dissolve
    "{color=#81F79F}*That story she told me won't stop bothering me. I have to do something with it. I think it's time to call Mary.*{/color}"
    jump day_04_phone_mary_john

label day_04_phone_mary_john:

    scene day_04_phone_mary_john_1 with dissolve
    mc "Hi, Mary."
    mary "Hi, boss."
    mc "How are you doing? Is everything all right?"
    mary "Yes. No problems."
    mc "How's Khloe doing?"
    mary "She's mad at you, but she'll get over it."
    mc "I don't blame her at all. The job is difficult and we were supposed to do it together. Do you know how she is doing on her own?"
    mary "Everything is under control. It'll just take her more time."
    mc "All right, then. Listen, do we have any available people? I could use some help here. Things are getting too snappy and it's starting to irritate me."
    mary "Hmm. Everyone is busy, unfortunately. But I can come."
    mc "You're in charge of the whole company."
    mary "That's not a problem. I'll pack what I need and I can manage the company remotely."
    mc "You already have enough things on your mind. I don't want to trouble you with my private matters."
    mary "Boss... This isn't a problem for me. Just send me the address and I'll be with you in a few hours. I'm already starting to pack."
    mc "What would I do without you?"
    mary "Heheh. See you later."

    scene day_04_john_sms_1 with dissolve
    "{color=#D2691E}*You check your phone and see that you have new messages.*{/color}"

    menu messages_day_04:

        "{color=#74B2F4}SMS from Lisa.{/color}" if sms_lisa_day_04 == False:
            sms "We have to meet today. The sooner the better. Something wrong is going on with Jennifer."
            sms "She doesn't want to tell me what, but I think it's something serious. Let me know when you have time."
            $ sms_lisa_day_04 = True
            jump messages_day_04

        "{color=#74B2F4}SMS from Jennifer.{/color}" if sms_jennifer_day_04 == False:
            sms "Could we meet soon, please? I would like to talk to you."
            $ sms_jennifer_day_04 = True
            jump messages_day_04

        "{color=#74B2F4}SMS from Sandra.{/color}" if sms_sandra_day_04 == False and s_dinner_day_3 == True:
            sms "I wanted to thank you again for last night. I had a really great time. Thank you."
            $ sms_sandra_day_04 = True
            jump messages_day_04

            if sms_sandra_day_04 == True and sms_jennifer_day_04 == True and sms_lisa_day_04 == True:
                jump phone_choices_day_04

label phone_choices_day_04:

    scene black with dissolve

    menu call_choices_day_04:

        "{color=#74B2F4}Call Lisa.{/color}" if call_lisa_day_04 == False:

            scene expression "day_04_phone_john_lisa_1[hair]" with dissolve
            $ call_lisa_day_04 = True
            mc "Hi, sweetheart."
            mc "What's going on?"
            l "Hi."
            l "We need to meet and talk about Jennifer."
            mc "Yeah, sure. Where and when?"
            l "Can you come to me? We'll go for a walk."
            mc "Okay. I'll be there soon."

            if call_jennifer_day_04 == False:

                scene black with dissolve
                show bg some_time_later with dissolve
                $ renpy.pause ()

                scene expression "day_04_lisa_infront_house_2[hair]" with dissolve
                "{color=#D2691E}*You're driving up to the house. Lisa is already waiting for you.*{/color}"
                mc "Hi, darling."

                if haircut == True:

                    mc "Oh my God, Lisa. You look amazing."
                    l "Do you like my new hairstyle?"
                    mc "I love it."

                else:

                    mc "You look beautiful."
                    l "Oh... Thank you."

                scene expression "day_04_lisa_infront_house_3[hair]" with dissolve
                l "Let's go. I don't want anyone to hear us."
                mc "What's going on?"

                scene expression "day_04_lisa_infront_house_4[hair]" with dissolve
                l "Jennifer came to me last night. She was very upset and she was crying. I couldn't calm her down."
                l "I asked her what happened, but she wouldn't tell me anything. I suggested that she should ask you for help, but I don't know if she would."
                l "She wasn't sure if it was a good idea."

                scene expression "day_04_lisa_infront_house_5[hair]" with dissolve
                mc "She texted me that she wanted to meet me."
                l "That's good. Please help her. I'm very worried about her. I don't want her to get hurt."
                mc "Of course. I'll do what I can. Don't worry about it."

                scene expression "day_04_lisa_infront_house_6[hair]" with dissolve
                l "Thank you."
                mc "I'll call her later and we'll set up something up."

                scene black with fade
                "{color=#D2691E}*You are driving back to the hotel. After a while, you decide to make a phone call to Jennifer.*{/color}"
                scene black with dissolve
                jump call_choices_day_04

            else:

                scene black with dissolve
                show bg some_time_later with dissolve
                $ renpy.pause ()

                scene expression "day_04_lisa_infront_house_2[hair]" with dissolve
                "{color=#D2691E}*You're driving up to the house. Lisa is already waiting for you.*{/color}"
                mc "Hi, darling."

                if haircut == True:

                    mc "Oh my God, Lisa. You look amazing."
                    l "Do you like my new hairstyle?"
                    mc "I love it."

                else:

                    mc "You look beautiful."
                    l "Oh... Thank you."

                l "Let's go. I don't want anyone to hear us."

                scene expression "day_04_lisa_infront_house_3[hair]" with dissolve
                mc "What did you want to talk about?"
                l "About Jennifer. She has some problems and I'm worried about her."
                mc "I know."

                scene expression "day_04_lisa_infront_house_4[hair]" with dissolve
                mc "I already talked to her today and I know everything."
                mc "You don't have to worry about anything. I'll take care of everything."
                l "Can you tell me what happened?"

                scene expression "day_04_lisa_infront_house_5[hair]" with dissolve
                mc "Jennifer has problems with her boyfriend. He needs to be taught how to talk to women."
                l "Did he hurt her?"
                mc "No, but Jennifer is afraid that he might do something to her."

                scene expression "day_04_lisa_infront_house_6[hair]" with dissolve
                mc "She's not supposed to see him again, and I'll talk to him."
                mc "So don't worry about it anymore."
                l "Okay. Be careful, please."
                mc "I'll be fine."
                scene black with dissolve
                jump call_choices_day_04

        "{color=#74B2F4}Call Jennifer.{/color}" if call_jennifer_day_04 == False:

            scene day_04_phone_john_jennifer_1 with dissolve
            mc "Hey."
            j "Hi. Listen. Could we meet today? I have a problem and I'd like to talk to you about it."
            mc "Of course, Jennifer. I could see you now."
            j "That's great. Where do you want me to go?"
            mc "Where are you now?"
            j "I'm at home, but I'm going to go to city hall."
            mc "Hmm. Okay. Let's meet there. I'll be with you in 30 minutes."
            j "I'll be waiting at the entrance."

            scene black with dissolve
            show bg some_time_later with dissolve
            $ renpy.pause ()

            scene day_04_jennifer_infront_city_hall_1 with dissolve
            "{color=#D2691E}*You're driving up to the city hall. Jennifer is waiting for you.*{/color}"

            scene day_04_jennifer_infront_city_hall_2 with dissolve
            $ renpy.pause ()

            scene day_04_jennifer_infront_city_hall_3 with dissolve
            mc "Hey."
            j "Thank you, and I'm glad you found some time to talk with me."
            mc "No problem. Now tell me, what's the problem?"

            scene day_04_jennifer_infront_city_hall_4 with dissolve
            j "It's about my boyfriend, Eric, we've been dating for several months. Everything was great at first."
            j "He'd buy me flowers, take me to cool places. But something bad has happened to him lately. He became vulgar and aggressive."
            j "I'm afraid he might hurt me."
            mc "Did he hurt you?"
            j "No, thankfully he didn't."
            j "But yesterday we went to the cinema. At some point, Eric ordered me to give him a blowjob. Of course, I refused."

            scene day_04_jennifer_infront_city_hall_5 with dissolve
            j "The way he did it scared me a lot. He had never demanded such things before and he said it with such contempt in his voice."
            j "I still have the creeps when I think about it. But that wasn't the worst thing. I got up and wanted to leave, but he grabbed my hair with one hand and started to take off his pants with the other."
            j "Finally he said to me, 'Suck it, you whore.'"
            j "I started to struggle with him. Luckily, someone noticed what was going on and called security. It ended with him being thrown out of the cinema, and I had to run away through the back door."
            mc "Don't worry about it. I'll take care of him. He'll never bother you again."

            scene day_04_jennifer_infront_city_hall_6 with dissolve
            j "What are you going to do?"
            mc "I'll talk to him about how women should be treated."
            j "Thank you very much."
            mc "Have you done everything you needed to do at City Hall?"
            j "Yes."
            mc "Okay. I will drive you home."

            if call_lisa_day_04 == True:

                jump linda_office

            else:

                scene black with fade
                "{color=#D2691E}*You are driving back to the hotel. After a while, you decide to make a phone call to Lisa.*{/color}"
                scene black with dissolve
                $ call_jennifer_day_04 = True
                jump call_choices_day_04

    if call_jennifer_day_04 == True and call_lisa_day_04 == True:
        jump linda_office

label linda_office:

    scene black with dissolve
    "{color=#D2691E}*You went to the address Jennifer gave you, but Eric wasn't home.*{/color}"
    "{color=#D2691E}*You waited for him for a while, but then you got in the car and drove off. You were on the way back to the office when you received a text message.*{/color}"

    scene black with dissolve
    sms "Hurry up. We have a serious problem here."

    scene day_04_office_sandra_mc_scene_1 with dissolve
    "{color=#D2691E}*Ten minutes later you enter the office. Sandra is standing in the doorway. She is upset.*{/color}"
    mc "What is going on here?"
    s "Linda is in the building. She has been seen on the fourth floor."
    mc "You couldn't throw her out? After all, she's not some bloodthirsty alien. Why didn't you call security?"

    scene day_04_office_sandra_mc_scene_2 with dissolve
    s "I called security, but they didn't find her."
    mc "What's on the fourth floor?"
    s "Financial department."

    scene black with fade
    "{color=#D2691E}*You go up on the fourth floor. You check every room on this floor, but Linda is nowhere to be found.*{/color}"

    scene day_04_office_sandra_mc_scene_3 with dissolve
    mc "She had to leave already. I'm disappointed in you. Instead of panicking as if an ISIS unit attacked you,
    you should find her and politely ask her what the fuck she was doing here."

    scene day_04_office_sandra_mc_scene_4 with dissolve
    c "I'm sorry."
    mc "Sandra, I also expected a lot more from you."
    s "I don't know what to say."
    mc "I'm really disappointed in you, Sandra."

    if clara_submission >= 3:

        menu clara_slap:

            "{color=#74B2F4}Slap Clara.{/color} [ClaraSubmissionPath]":

                mc "Clara, get in my office, now!"

                scene day_4_clara_slap_1_1 with dissolve
                "{color=#D2691E}*Without any warning you raise your hand and slap Clara in the face.*{/color}"
                "{color=#D2691E}*Shocked girl looks at you in amazement.*{/color}"
                mc "Are you that stupid?"
                mc "Are you deliberately provoking me with your stupid behavior?"

                scene day_4_clara_slap_1_2 with dissolve
                "{color=#D2691E}*Clara shakes her head in silence.*{/color}"
                mc "But I think you want to get rid of me."
                mc "You don't respect me from the beginning, you don't follow my orders."

                scene day_4_clara_slap_1_3 with dissolve
                "{color=#D2691E}*You hit her again.*{/color}"
                mc "You think you're dealing with an idiot?"
                mc "Only you could let her in here."

                scene day_4_clara_slap_1_4 with dissolve
                "{color=#D2691E}*You raise your hand to hit her again, but Clara kneels before you.*{/color}"
                c "Please, sir. It's not true. I don't want to get rid of you."
                c "You just have another way of working and I have to get used to it."
                c "I promise it won't happen again."
                mc "Get out of my sight."
                $ clara_slap = True
                $ clara_submission += 2

            "{color=#74B2F4}If you fail me one more time, I will punish you.{/color}":

                mc "Clara, get in my office, now!"

                scene day_04_office_sandra_mc_scene_4 with dissolve
                mc "If you fail me one more time, I will punish you."
                c "I'm sorry, sir."
                mc "Your apology means nothing to me. You have just proved yourself useless."
                mc "Fail me one more time and there won't be mister nice guy anymore."
                c "I promise it won't happen again."
                mc "Get out of my sight."
                $ clara_submission += 1

    else:

        mc "Your apology means nothing to me. You have just proved yourself useless. I can't entrust you with the company in my absence."
        mc "Get out of my sight."

    scene black with fade
    "{color=#D2691E}*A few minutes later you hear a knock on the door.*{/color}"

    scene day_04_office_sandra_mc_scene_7 with dissolve
    amy "Good morning, sir. I'm sorry to interrupt, but I think we should talk."
    mc "Who are you?"
    amy "My name is Amy. I work in the finance department."
    mc "What did you want to talk about?"
    amy "I know you were looking for Linda."


    scene day_04_office_sandra_mc_scene_8 with dissolve
    mc "Yes, I was. Did you see her?"
    amy "Yes. I was photocopying the documents as she passed me."
    mc "Was she alone?"
    amy "No. She was there with your secretary, Clara."
    mc "Are you absolutely sure about that?"

    scene day_04_office_sandra_mc_scene_9 with dissolve
    amy "Yes, I am sure."
    mc "Hmm. That would explain a lot..."
    amy "Excuse me?"
    mc "Do you know what they were doing in your department?"

    scene day_04_office_sandra_mc_scene_10 with dissolve
    amy "Unfortunately, I'm not sure. They both went into room 405. Only one person is working there, Steven. He is responsible for approving all financial operations we do within the company."
    mc "Very interesting. I'm very grateful for your help. Your information is invaluable, especially about Clara."
    mc "If you ever need anything, just let me know."

    scene day_04_office_sandra_mc_scene_11 with dissolve
    amy "Thank you, sir."
    mc "See you soon."

    scene black with fade
    "{color=#D2691E}*After a while, Sandra walks into your office.*{/color}"

    scene day_04_office_sandra_mc_scene_12 with dissolve
    mc "Where have you been?"
    s "I was checking what Linda was doing here."
    mc "And?"

    scene day_04_office_sandra_mc_scene_13 with dissolve
    s "It looks like she came here to make a transfer from the company account."
    mc "How is that possible? You were supposed to deprive her of her rights to bank accounts."
    s "And I did it. Somebody had to help her with that. But I don't know who."
    mc "But I know, who it was."

    scene black with fade
    "{color=#D2691E}*You open the door and call Clara, but she's not at the secretary's office.*{/color}"

    scene day_04_office_sandra_mc_scene_14 with dissolve
    mc "Where the fuck is she?"
    s "I haven't seen her in a while."
    mc "I'll be right back."

    scene black with fade
    "{color=#D2691E}*You're going to the fourth floor. You enter room 405. Inside a young man is sitting behind a desk.*{/color}"

    scene day_04_office_steven_scene_1 with dissolve
    st "Hello, boss."
    mc "Steven?"
    st "Yes."
    mc "You are fired."

    scene day_04_office_steven_scene_2 with dissolve
    st "What have I done?"
    mc "You don't know? Get your things and get out of my sight."
    st "But, boss..."
    mc "You have fifteen minutes to leave the building or you're gonna be thrown out of here."
    mc "Next time, think about who you're helping."

    scene black with fade
    "{color=#D2691E}*You're going back to your office. Along the way, you try to find Clara, but she is nowhere to be found.*{/color}"
    "{color=#D2691E}*Sandra and Isabella are waiting on you in your office.*{/color}"

    scene day_04_office_sandra_mc_scene_15 with dissolve
    mc "Where the fuck is Clara?"
    s "I don't know."
    i "I saw her downstairs with some woman thirty minutes ago."
    mc "Goddamnit."

    scene day_04_office_sandra_mc_scene_16 with dissolve
    s "Did you find out anything?"
    mc "Yes, it was one of the employees. His name is Steven."
    mc "But it doesn't matter anyway. I already fired him and I'm not going to change my mind."
    mc "Isabella can you do me a favor and find Clara?"
    i "Yes, of course."

    scene day_04_office_sandra_mc_scene_17 with dissolve
    s "You're right. You have indulged them too much. Now the rest of them will know that you are not kidding. Such a situation is unlikely to happen again."
    s "Linda has transferred $50,000 from the company's account to an unknown account. I tried to block the transfer, but the bank says there is nothing we can do about it."
    s "The only option we have is to report the case to the police."
    mc "No. I can handle this on my own."
    s "Are you sure?"

    scene day_04_office_sandra_mc_scene_18 with dissolve
    mc "Yeah. I was wrong about all this, but I'm a fast learner. I won't make that mistake again."
    mc "I'm leaving."
    s "Where are you going?"
    mc "To the bank."
    jump clara_lisa

label clara_lisa:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    if clara_submission == 5:

        scene day_04_linda_clara_outside_scene_1 with dissolve
        li "What's wrong with your face?"
        c "Nothing."
        li "Your cheeks are red."
        c "Ah, it must be an allergy."

    else:

        scene day_04_linda_clara_outside_scene_1 with dissolve
        c "It seems that everything worked out."
        li "Yes, it was easy."
        c "Do you think this bastard might suspect something?"

        scene day_04_linda_clara_outside_scene_2 with dissolve
        li "I don't think so. He's a loser, isn't he?"
        c "Yeah. I do what I want and he hasn't figured it out yet."
        li "HEHE. Be careful anyway. We can't give him any reason to suspect you of anything."

    scene day_04_linda_clara_outside_scene_3 with dissolve
    c "So... what are you going to do now?"
    li "I don't know. For now, I need to rest. This case of paying off my debts ended up killing me badly."
    "{color=#D2691E}*RING RING*{/color}"

    scene day_04_linda_clara_outside_scene_4 with dissolve
    li "Hello?"
    st "He fired me. What am I supposed to do now?"
    li "What are you talking about, Steven?"
    st "He found out that I helped you. He came to my office and fired me."

    scene day_04_linda_clara_outside_scene_5 with dissolve
    st "That's the fucking way it ends when you help others."
    li "Stop whining. I can't help it. How was I supposed to know that bastard could do such a thing?"
    li "You owed me a favor, now we're even."
    st "You will regret it."
    li "For once, be a man and not a fucking pussy."

    scene day_04_linda_clara_outside_scene_6 with dissolve
    c "What happened?"
    li "He fired Steven."
    c "Really?"
    li "I guess."
    c "Maybe we underestimated him?"
    li "I don't think so. He doesn't know what he's doing. It was a coincidence that he found out anything."
    c "If you say so."

    scene day_04_linda_clara_outside_scene_7 with dissolve
    li "Do your job and don't worry about anything. I have everything under control."
    c "How did he find out about Steven?"
    li "Does it matter? Who cares about that idiot?"

    scene day_04_linda_clara_outside_scene_8 with dissolve
    c "It would be good to know who told [player_name] about you and Steven."
    c "Wait a second. It was that new girl, Amy."

    scene day_04_linda_clara_outside_scene_9 with dissolve
    c "She came to his office and she wanted to talk with him about something important."
    li "Take care of her. I hate informers."
    c "Okay."
    jump mary_hotel

label mary_hotel:

    scene black with dissolve
    "{color=#D2691E}*In the bank, you managed to get everything done.*{/color}"
    "{color=#D2691E}*The transfer has been canceled, but it will take a few days for Linda to find out about it.*{/color}"
    "{color=#D2691E}*Instead of going back to the office, you decide to check again if Eric is home.*{/color}"
    "{color=#D2691E}*Unfortunately, you're not lucky again.*{/color}"

    scene black with dissolve
    "{color=#D2691E}*RING RING*{/color}"

    scene day_04_mary_john_lobby_phone_1 with dissolve
    mary "Hey boss."
    mc "Hey."
    mary "I'm at the hotel."
    mc "Well, that's great. I'll be right there."
    mary "Okay. I'm waiting."

    scene black with fade
    "{color=#D2691E}*15 minutes later you're there. You enter the hotel and see Mary waiting for you.*{/color}"

    scene day_04_hotel_lobby_mary_1 with dissolve
    $ renpy.pause ()

    scene day_04_hotel_lobby_mary_2 with dissolve
    mary "I've missed you so much."

    scene day_04_hotel_lobby_mary_3 with dissolve
    mc "I've missed you too, I'm so glad you came."

    scene day_04_hotel_lobby_mary_4 with dissolve
    $ renpy.pause ()

    scene day_04_hotel_room_mary_1 with dissolve
    mary "What's up, boss? How are you doing?"
    mc "Nothing good. It's not the same without you and Khloe. I hate hotels and I hate waking up in an empty bed in the morning."
    mc "I missed you and your beautiful body warming me up on a cold morning."
    mary "HAHA, [player_name] - a romantic."
    mc "Well, I also missed your sarcasm and sense of humor. I open up to you and you sass me?"
    mary "Poor baby. HAHA"
    mary "I'll go change."

    scene day_04_hotel_mary_1 with dissolve
    "{color=#D2691E}*Mary goes into the bathroom.*{/color}"
    "{color=#D2691E}*You stare at her. At her beautiful, slender body, firm breasts, perfectly shaped bottom and long legs.*{/color}"

    scene day_04_hotel_mary_2 with dissolve
    "{color=#D2691E}*It's only been a few days but you feel like you haven't seen her for a year.*{/color}"

    scene day_04_hotel_mary_3 with dissolve
    mary "Pervert...."
    "{color=#D2691E}*Mary laughs at you.*{/color}"
    jump mary_blowjob_day_4

label mary_blowjob_day_4:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_04_hotel_mary_4 with dissolve
    mc "What? It's not my fault you're so beautiful or didn't close the door."
    mary "Stop staring at me, you pervert."
    mc "Never!"
    mary "HEHE."

    scene day_04_hotel_mary_5 with dissolve
    mary "Hmm. What's this?"
    mc "What?"
    "{color=#D2691E}*Mary looks down and points at your swollen member.*{/color}"
    "{color=#D2691E}*Without saying anything, she kneels before you and starts sucking it.*{/color}"

    scene day_04_hotel_mary_6 with dissolve
    mc "Mary! What are you doing?"
    "{color=#FF69B4}*But Mary doesn't do anything to herself about your protests.*{/color}"

    scene day_04_hotel_mary_7 with dissolve
    "{color=#FF69B4}*She starts with long, slow licks from top to bottom, and teases a little with her tongue on the head.*{/color}"
    "{color=#FF69B4}*She is practically French kissing the head and playing with the tip of your foreskin using her lips and tongue.*{/color}"

    scene day_04_hotel_mary_8 with dissolve
    mc "You're a naughty girl, Mary..."
    "{color=#FF69B4}*You're trying to say something, but the pleasure Mary gives you makes it impossible for you to pronounce a word.*{/color}"
    "{color=#FF69B4}*Mary gives you lustful looks and moans with every stroke she makes.*{/color}"

    scene day_04_hotel_mary_9 with dissolve
    "{color=#FF69B4}*She uses her hand with her mouth to jerk you off very slowly.*{/color}"
    "{color=#FF69B4}*She doesn't vary the speed or pressure or change hands at all, she just keeps going slowly and teases the tip of your cock with her tongue.*{/color}"

    scene day_04_hotel_mary_10 with dissolve
    "{color=#FF69B4}*Your whole body feels electric and every time she touches you, you have shivers.*{/color}"
    "{color=#FF69B4}*The pleasure spreads through your whole body. You lost track of where you're and who you're and just become lost in the pleasure.*{/color}"

    scene day_04_hotel_mary_11 with dissolve
    "{color=#FF69B4}*She puts your dick even deeper in her mouth. You can feel your dick's head touching her throat.*{/color}"
    "{color=#FF69B4}*She starts deepthroating you, licking the base of your cock with her tongue while you're deep inside her mouth.*{/color}"

    scene day_04_hotel_mary_12 with dissolve
    mc "Oh my fucking God, Mary. I'm cumming..."

    call screen mary_day_04_cumshots

label cumshot_mouth:

    hide screen mary_day_04_cumshots

    scene day_04_hotel_mary_13 with dissolve
    mc "Mary... don't stop. I'm going to explode in your hot mouth."
    "{color=#FF69B4}*She grips you hard and sucks you gently while you're cumming.*{/color}"
    mc "Oh my fucking God!"

    scene day_04_hotel_mary_14 with dissolve
    "{color=#FF69B4}*Your hot cum fills her mouth and covers her breasts.*{/color}"
    mc "Jesus, Mary, I've never experienced anything like that before."

    scene day_04_hotel_mary_18 with dissolve
    mary "I'm glad you liked it."
    mc "It was goddamn incredible."

    scene day_04_hotel_mary_19 with dissolve
    mary "Hehe."
    mary "Do you wish I'd listened to you?"
    mc "Eh. Of course not you, naughty girl."
    $ renpy.end_replay()

    jump after_blowjob_day_4

label cumshot_facial:

    hide screen mary_day_04_cumshots

    scene day_04_hotel_mary_16 with dissolve
    mc "Mary... don't stop. I'm going to explode on your face."
    "{color=#FF69B4}*She grips you hard and sucks you gently while you're cumming.*{/color}"
    mc "Oh my fucking God!"

    scene day_04_hotel_mary_17 with dissolve
    "{color=#FF69B4}*You pull your dick out of her mouth and the hot sperm covers her face.*{/color}"
    "{color=#FF69B4}*Mary grabs your dick and plays with the tip of it with her tongue. Then she puts your dick in her mouth.*{/color}"
    mc "Jesus, Mary, I've never experienced anything like that before."

    scene day_04_hotel_mary_18 with dissolve
    mary "I'm glad you liked it."
    mc "It was goddamn incredible."

    scene day_04_hotel_mary_19 with dissolve
    mary "Hehe."
    mary "Do you wish I'd listened to you?"
    mc "Eh. Of course not you, naughty girl."
    $ renpy.end_replay()

    jump after_blowjob_day_4

label cumshot_breasts:

    hide screen mary_day_04_cumshots

    scene day_04_hotel_mary_15a with dissolve
    mc "Mary... don't stop. I'm going to explode on your beautiful breasts."
    "{color=#FF69B4}*She grips you hard and sucks you gently while you're cumming.*{/color}"
    mc "Oh my fucking God!"

    scene day_04_hotel_mary_15 with dissolve
    "{color=#FF69B4}*You pull your dick out of her mouth and the hot sperm covers her breasts.*{/color}"
    "{color=#FF69B4}*Mary grabs your dick and plays with the tip of it with her tongue. Then she puts your dick in her mouth.*{/color}"
    mc "Jesus, Mary, I've never experienced anything like that before."

    scene day_04_hotel_mary_18 with dissolve
    mary "I'm glad you liked it."
    mc "It was goddamn incredible."

    scene day_04_hotel_mary_19 with dissolve
    mary "Hehe."
    mary "Do you wish I'd listened to you?"
    mc "Eh. Of course not you, naughty girl."
    $ renpy.end_replay()

    jump after_blowjob_day_4

label after_blowjob_day_4:

    scene day_04_hotel_mary_20 with dissolve
    mary "All right, then. Tell me what the job is."
    mc "It's hard to call it a job, but let's start from the beginning."

    menu job:

        "{color=#74B2F4}Tell her about Linda.{/color}" if linda_day_04 == False:

            scene day_04_hotel_mary_22 with dissolve
            mc "Our main goal is Linda. She pisses me off and she's getting more and more brazen."
            mc "I'm just coming back from the bank because the bitch snuck into the office and transferred $50,000 to herself."
            mary "Not bad. HAHA"
            mc "I managed to block the transfer. But in about two days Linda will realize that something went wrong and will try again."
            mc "Generally speaking, I want to know something about her, about her past, about what she does all day long. I want to repay this bitch for everything she did to me."

            scene day_04_hotel_mary_24 with dissolve
            mc "Also, any information about her is priceless. Then we will have to figure out how to humiliate her so much that she will remember about it until the end of her miserable life."
            mc "I will deprive her of everything. Including her daughters."
            mary "It can be done. There shouldn't be any problems with that."
            mary "I'll find something to make her obey to you completely."
            mc "I knew I can count on you."
            $ linda_day_04 = True
            jump job

        "{color=#74B2F4}Tell her about Nicole.{/color}" if nicole_day_04 == False:

            scene day_04_hotel_mary_23 with dissolve
            mc "I would like to know something about Nicole. She is Linda's middle daughter and she is the only one who wants nothing to do with me."
            mc "In general, I don't know anything about her. From what Lisa told me, Nicole could be a member of a gang or something."
            mc " Maybe you can establish something that will help me to convince Nicole that I have no bad intentions about her."
            mc "Or maybe we can get some information that will allow me to blackmail her a little bit. I don't care. You know that I don't like it when something is not my way."

            scene day_04_hotel_mary_25 with dissolve
            mary "Hehe. Sure, boss. Don't worry about it. Something will be found on that snot to make her obey you."
            mc "And that's what I like about you, Mary. You know exactly what your boss likes."
            $ nicole_day_04 = True
            jump job

        "{color=#74B2F4}Tell her about Sandra.{/color}" if sandra_day_04 == False:

            scene day_04_hotel_mary_21 with dissolve
            mc "The lawyer I hired told me about what happened to her once. About twelve years ago She became a victim of a stupid joke that had a very strong impact on her psyche."
            mc "The police quickly dropped the case and the perpetrators were never punished. Maybe you could find out something about it? This case continues to bother me."

            scene day_04_hotel_mary_26 with dissolve
            mc "I believe you should find some basic information about the case in the precinct's records room."

            scene day_04_hotel_mary_27 with dissolve
            mary "Don't worry about it. I know how to find the information I need."
            $ sandra_day_04 = True
            jump job

            if linda_day_04 == True and nicole_day_04 == True and sandra_day_04 = True:
                jump chit_chat_day_04

label chit_chat_day_04:

    scene day_04_hotel_mary_28 with dissolve
    mary "Don't worry, boss. I will do everything I can to establish the necessary information."
    mary "Besides, I like this approach to things myself. The most important thing is to achieve your goal, the rest doesn't matter."
    mc "And that's why you're my right hand."

    scene day_04_hotel_mary_29 with dissolve
    mary "That's the only reason? I thought that was something else?"
    mc "I don't know what are you talking about..."
    mary "Of course..."

    menu khloe_day_4:
        "{color=#74B2F4}Ask Mary about Khloe.{/color}" if khloe_day_4 == False:

            scene day_04_hotel_mary_30 with dissolve
            mc "How's Khloe doing?"
            mary "I don't know. She hasn't contacted me recently."
            mary "The last time I talked to her, she was mad at you."
            mc "I'm not surprised at all."
            mary "You left her alone with the job."

            scene day_04_hotel_mary_31 with dissolve
            mc "I know..."
            mary "But I'm sure you'll find a way to make her happy."
            mc "HAHA. I will certainly find it."
            mary "Start by calling her and buy her something nice. You know she likes gifts."

            scene day_04_hotel_mary_32 with dissolve
            mc "Yes, she does."
            mc "I'll go shopping, but somehow I don't feel like calling her."
            mary "Do as you like, but I think you should show a little interest after you left her alone."
            mc "All right. As usual, you're right."

            menu call_khloe:

                "{color=#74B2F4}Call Khloe now.{/color} [KhloePath]":

                    scene day_04_hotel_mary_33 with dissolve
                    mc "Hi, Khloe."
                    kh "What an honor it has been for me... The boss himself calls me. About fucking time."
                    mc "I know you're mad at me, but I couldn't help it. I had to come here and do some family business."
                    kh "Yes, I am angry. You left me alone with the hardest thing we've ever had. We planned this together and you have no idea how long it took me to deal with all this alone."
                    mc "I will make it up to you, I promise."
                    kh "We will see..."
                    kh "Where is Mary anyway? "
                    mc "She came to me today to help me finish some things as soon as possible."
                    kh "What the fuck?"
                    kh "Put her on the phone."
                    $ khloe_enabled = True

                    scene day_04_hotel_mary_34 with dissolve
                    "{color=#D2691E}*You give the phone back to scared Mary.*{/color}"
                    kh "..."
                    mary "I'm sorry."
                    kh "..."
                    mary "Somebody had to help him! I didn't have anyone free to come here."
                    kh "..."
                    mary "Don't be upset."
                    kh "..."
                    mary "We'll try to get back as soon as possible."
                    kh "..."
                    mary "No, I don't have a job for you right now."
                    kh "..."
                    mary "Bye, darling."

                    scene day_04_hotel_mary_33 with dissolve
                    "{color=#D2691E}*Mary gives you the phone.*{/color}"
                    mc "Khloe, if you want, come to us. Together we'll finish things here faster and be able to go back to Los Angeles."
                    kh "I will think about it."
                    mc "That's great. I'll send you an address."
                    mc "Bye, my beauty."
                    $ khloe_day_4 = True
                    jump khloe_day_4

                "{color=#74B2F4}Call Khloe later.{/color}":

                    scene day_04_hotel_mary_27 with dissolve
                    mc "I will call her later. I'm not in the mood right now."
                    mary "Do as you like, but I think you should call her now."
                    mc "Eh. Okay, I will call her right now..."
                    mc "Maybe you are right and I shouldn't postpone it any longer."
                    mc "Hi, Khloe."
                    kh "What an honor it has been for me... The boss himself calls me. About fucking time."
                    mc "I know you're mad at me, but I couldn't help it. I had to come here and do some family business."
                    kh "Yes, I am angry. You left me alone with the hardest thing we've ever had. We planned this together and you have no idea how long it took me to deal with all this alone."
                    mc "I will make it up to you, I promise."
                    kh "We will see..."
                    kh "Where is Mary anyway? "
                    mc "She came to me today to help me finish some things as soon as possible."
                    kh "What the fuck?"
                    kh "Put her on the phone."
                    $ khloe_enabled = True

                    scene day_04_hotel_mary_34 with dissolve
                    "{color=#D2691E}*You give the phone back to scared Mary.*{/color}"
                    kh "..."
                    mary "I'm sorry."
                    kh "..."
                    mary "Somebody had to help him! I didn't have anyone free to come here."
                    kh "..."
                    mary "Don't be upset."
                    kh "..."
                    mary "We'll try to get back as soon as possible."
                    kh "..."
                    mary "No, I don't have a job for you right now."
                    kh "..."
                    mary "Bye, darling."

                    scene day_04_hotel_mary_35 with dissolve
                    "{color=#D2691E}*Mary gives you the phone.*{/color}"
                    mc "Khloe, if you want, come to us. Together we'll finish things here faster and be able to go back to Los Angeles."
                    kh "I will think about it."
                    mc "That's great. I'll send you an address."
                    mc "Bye, my beauty."
                    $ khloe_day_4 = True
                    jump khloe_day_4

        "{color=#74B2F4}Ask Mary how she is doing.{/color}" if khloe_a_day_4 == False:

            scene day_04_hotel_mary_30 with dissolve
            mc "Are you okay?"
            mary "Yeah. Except I missed you and Khloe so much."
            mary "I don't like it when you both go away."
            mary "I have to wake up alone in that huge bed...."
            mary "I have no one to cuddle up to..."

            scene day_04_hotel_mary_31 with dissolve
            mary "Nobody has been yelling at me since the morning..."
            mary "It's generally sad to be all alone..."
            mc "I hate to leave you all alone, too. It makes me sad when I have to leave but sometimes I can't help it."
            mary "I know that but it doesn't help at all."

            scene day_04_hotel_mary_32 with dissolve
            mary "So it's good that I came to you because I don't know how much longer I could stand it alone, and besides, angry Khloe is worse than a venomous snake."
            mc "Our sweet Khloe... I love her, but sometimes I feel like strangling her."
            mary "I know something about it."
            $ khloe_a_day_4 = True
            jump khloe_day_4

            if khloe_a_day_4 == True and khloe_day_4 == True:
                jump shopping_day_4

label shopping_day_4:

    scene day_04_hotel_mary_20 with dissolve
    mary "All right, let's cut the flattery, there's work to be done."
    mc "Make yourself comfortable. I'm going to the office. I have a few people to lay off from work. No cocksucker is going to make an idiot out of me."
    mary "Have fun."
    mc "You too."

    scene black with dissolve
    "{color=#D2691E}*On your way to the office you pass a lingerie shop and decide to go in and buy something for the girls.*{/color}"

    scene day_04_mc_emily_scene_15 with dissolve
    sw "Hello."
    sw "I'll be right with you."

    scene day_04_mc_emily_scene_16 with dissolve
    sw "Sorry to keep you waiting."
    mc "It's okay."
    sw "Oh! Hi, [player_name]."
    mc "Emily? I didn't think you worked here!  "
    em "What a nice surprise."

    scene day_04_mc_emily_scene_17 with dissolve
    em "Can I help you with something?"
    mc "I'm looking for something sexy as a gift."
    em "Do you have something specific in mind?"
    mc "I've been thinking about some outfit, but nothing specific comes to my mind."
    em "Just give me a moment, I'll find something."
    mc "Sure."

    scene day_04_mc_emily_scene_10 with dissolve
    "{color=#D2691E}*A few minutes later Emily comes back with some boxes and puts them on the counter.*{/color}"
    mc "All the outfits look very sexy, but I can't decide on any."

    if emily_love >= 2:

        menu emily_help:

            "{color=#74B2F4}I think I will buy all of them.{/color}":

                scene day_04_mc_emily_scene_10 with dissolve
                mc "I think I will buy all of them. It's really hard to decide right now."
                em "Of course."
                mc "Would you gift-wrap all of them, please?"
                em "Sure."

            "{color=#74B2F4}Could you hold that for me?{/color} [EmilyPath]":

                scene day_04_mc_emily_scene_10 with dissolve
                em "I can see that you are not convinced. I can put on some of these clothes, maybe it will make your decision easier."
                mc "I don't want to cause you any problems."
                em "No problem. Let's go to the fitting room."

                scene day_04_mc_emily_scene_1 with dissolve
                "{color=#D2691E}*Emily disappears into the fitting room to leave in her first outfit after a while.*{/color}"
                em "So how about this one?"
                mc "Wow."
                mc "You look amazing... I'm speechless."
                em "I will try on the second outfit."

                scene day_04_mc_emily_scene_2 with dissolve
                "{color=#D2691E}*The girl smiles at you.*{/color}"
                em "Will this one be better?"
                mc "I don't know. Could you try the other one on?"
                em "Sure."

                scene day_04_mc_emily_scene_3 with dissolve
                "{color=#D2691E}*After a while Emily leaves the dressing room in her third outfit.*{/color}"
                em "So how do you like the outfits?"
                em "Did you like what you saw?"
                mc "You looked divine in all of them."
                em "Thank you, but that's not what I meant."
                mc "Yes. I love these outfits and I'll buy all of them."
                em "That's great."

                scene day_04_mc_emily_scene_4 with dissolve
                "{color=#D2691E}*Emily walks into the fitting room again, but this time she doesn't close the door.*{/color}"
                "{color=#D2691E}*You stare at her as she dresses up and you admire every inch of her divine body.*{/color}"

                scene day_04_mc_emily_scene_5 with dissolve
                "{color=#81F79F}*I have a strange feeling that she didn't close the door on purpose.*{/color}"

                scene day_04_mc_emily_scene_6 with dissolve
                "{color=#81F79F}*Maybe I could arrange a drink with her?*{/color}"

                scene day_04_mc_emily_scene_7 with dissolve
                em "So you've decided on all three?"
                mc "Yes."

                scene day_04_mc_emily_scene_8 with dissolve
                mc "Would you gift-wrap all of them, please?"
                em "Sure."
                em "Follow me."

                scene day_04_mc_emily_scene_9 with dissolve
                mc "Thank you very much."
                em "You are welcome."

                scene day_04_mc_emily_scene_12 with dissolve
                "{color=#D2691E}*You are already at the door when you turn to Emily.*{/color}"

                menu ask_emily_for_drink:

                    "{color=#74B2F4}Ask her for a drink.{/color} [EmilyLovePath]":

                        scene day_04_mc_emily_scene_12 with dissolve
                        mc "Listen, would you like to go for a drink tomorrow night?"
                        em "Actually, why not?"
                        mc "Do you know the pub 'Pink Rabbit'?"
                        em "Yes."

                        scene day_04_mc_emily_scene_13 with dissolve
                        mc "Let's say 9pm. Is it okay for you?"
                        em "Sure."
                        mc "So I'll see you later."
                        em "Bye."
                        $ emily_drink = True
                        $ emily_love += 1
                        jump office_day_04_scene_2

                    "{color=#74B2F4}Thank her again.{/color}":

                        scene day_04_mc_emily_scene_13 with dissolve
                        mc "Thank you so much for your help."
                        mc "Have a nice day."
                        em "You too."
                        jump office_day_04_scene_2

    else:

        scene day_04_mc_emily_scene_7 with dissolve
        mc "Hmm. I think I will buy all of them. It's really hard to decide now."
        em "Of course."
        mc "Would you gift-wrap all of them, please?"
        em "Sure."

        scene day_04_mc_emily_scene_13 with dissolve
        mc "Thank you so much for your help."
        mc "Have a nice day."
        em "You too."
        jump office_day_04_scene_2

label office_day_04_scene_2:
    $ renpy.end_replay()
    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_04_office_clara_mc_scene_2 with dissolve
    mc "Clara, where's Sandra?"
    c "I don't know."
    mc "Then find her."
    mc "I want to talk to you both."

    scene day_04_office_sandra_mc_scene_20 with dissolve
    "{color=#D2691E}*10 minutes later the girls enter your office.*{/color}"
    mc "Now listen to me carefully."
    mc "What happened today is unacceptable."
    mc "You both will take full responsibility for this."

    scene day_04_office_sandra_mc_scene_21 with dissolve
    mc "Clara, you assured me that I could trust you, that you would be a loyal and good employee, and you allowed my worst enemy to move freely within the office."
    mc "Sandra, I'm disappointed in you. I can't understand why you'd rather sit here and do nothing than find Linda and throw her out."
    mc "Your behavior was reckless. You have put me and the whole company at risk. I can't tolerate it."
    mc "I will consider our further cooperation."
    mc "You will both bear the consequences of today's events."

    scene day_04_office_sandra_mc_scene_22 with dissolve
    mc "Sandra, I will talk with you later, now leave us."
    mc "Clara, you are staying."
    c "But, boss..."
    mc "Silence!"
    mc "Sandra, leave us alone."

    if clara_submission >= 5:

        menu clara_humiliating_next_chapter:

            "{color=#74B2F4}Punish her.{/color} [ClaraSubmissionPath]":

                scene day_04_clara_punish_1_1 with dissolve
                mc "Get over here!"
                "{color=#D2691E}*You grab her by the throat and whisper in her ear with rage in your voice.*{/color}"
                mc "Do you really think I'm an idiot?"

                scene day_04_clara_punish_1_2 with dissolve
                "{color=#D2691E}*Clara is shaking her head negatively, unable to pronounce a word.*{/color}"
                mc "You thought you were gonna screw me over, laugh in my face and continue working with Linda with impunity?"
                mc "You made a mistake and underestimated me."
                mc "And now you will know the power of my wrath."

                scene day_04_clara_punish_1_3 with dissolve
                "{color=#D2691E}*Clara tries to catch her breath, and tears run down her cheeks.*{/color}"
                c "I don't understand what you mean."
                mc "Fucking hell, are you really that stupid?"

                scene day_04_clara_punish_1_4 with dissolve
                "{color=#D2691E}*You come up to her and grab her from behind.*{/color}"
                mc "A few people have seen you with Linda, so don't fuckin' say you don't know what I mean."
                mc "I gave you a chance, but you threw it away, so now you're gonna pay for everything you did to me."
                mc "Lean over!"

                scene day_04_clara_punish_1_5 with dissolve
                "{color=#D2691E}*You take off her skirt in one, quick move.*{/color}"
                c "What the fuck are you doing?"
                mc "Shut up, bitch!"

                scene day_04_clara_punish_1_6 with dissolve
                "{color=#D2691E}*Clara tries to free herself, but you push her to the desk.*{/color}"
                mc "Stop resisting or it will hurt more!"
                "{color=#D2691E}*Clara keeps fighting for a while, but gives up quickly.*{/color}"
                mc "That's better, bitch!"

                scene day_04_clara_punish_1_7 with dissolve
                "{color=#D2691E}*You raise your hand and you slap her ass with all your might.*{/color}"
                "{color=#D2691E}*Surprised and scared, the girl makes a loud cry out of herself.*{/color}"
                mc "Shut up, bitch!"
                "{color=#D2691E}*You slap her alternately to one buttock, until they're both scarlet and red.*{/color}"
                mc "Did you understand the lesson?"

                scene day_04_clara_punish_1_8 with dissolve
                "{color=#D2691E}*Clara nods.*{/color}"
                mc "If I find out that you've told anyone about this, or that you're still seeing Linda, or you're plotting against me I won't be so nice."
                mc "You understand me, bitch?"
                "{color=#D2691E}*Clara is nodding her head again.*{/color}"
                mc "Now get your rags and get the fuck out of here."
                $ clara_submission += 3

            "{color=#74B2F4}Warn her.{/color}":

                scene day_04_clara_punish_1_8 with dissolve
                "{color=#D2691E}*You come up to her and whisper.*{/color}"
                mc "Don't play games with me, I'm warning you."
                mc "This is the last warning. If you let me down again, I won't have any more pity for you."
                "{color=#D2691E}*Clara is nodding her head.*{/color}"
                mc "Then get the fuck out of here and remember that I'm watching you."
                $ clara_submission += 1

    else:

        scene day_04_clara_punish_1_8 with dissolve
        "{color=#D2691E}*You come up to her and whisper in her ear.*{/color}"
        mc "Don't play games with me, I'm warning you."
        mc "This is the last warning. If you let me down again, I won't have any more pity for you."
        "{color=#D2691E}*Clara is nodding her head.*{/color}"
        mc "Then get the fuck out of here and remember that I'm watching you."
        $ clara_submission += 1
    $ renpy.end_replay()
    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_04_holy_scene_1 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{/color}"
    mc "Come in, please."
    h "Good afternoon, sir."
    mc "How can I help you?"
    h "My name is Holly Davis. I am Sandra White's secretary."
    mc "Oh, yes. I remember. We met a few days ago at the reading of my Father's will."
    h "Exactly."
    mc "What can I do for you?"

    scene day_04_holy_scene_2 with dissolve
    h "I brought these documents for Mrs. White."
    mc "And what are these documents?"
    h "Mrs. White is still running a few more court cases and will need those documents. We have to vacate the office by tomorrow, so I thought I'd bring her these documents."
    mc "I will pass them on to her."
    h "Thank you."
    h "In fact, it's a pity it turned out that way, but I understand her. I worked well with her and now I have to look for a new job."

    menu holy_job_offer:

        "{color=#74B2F4}Offer her a job.{/color} [HolyLovePath]":

            scene day_04_holy_scene_2 with dissolve
            mc "Indeed, it is a sad case. But maybe I can do something about it."

            scene day_04_holy_scene_3 with dissolve
            h "Really?"
            mc "Yes. I need a trusted secretary. A trusted secretary if you know what I'm talking about."
            h "I guess so."
            mc "The work is not hard and the pay is decent."
            mc "The only condition is that I want to have full confidence in you in every aspect. Whatever happens stays between us."
            mc "Various things are happening in this company, so far I don't know who I can trust and who I can't, so I need people from outside who aren't involved in the games between me and Linda, former president of this company."
            h "I understand. What would I do as part of my job?"

            scene day_04_holy_scene_4 with dissolve
            mc "The same as any trusted secretary."
            h "All right. Is there any specific dress code in the company?"
            mc "The sexier the better. HEHE."
            mc "Of course I'm kidding."
            h "Of course."
            mc "Think about it. Here is my card. If you make a decision, please call me. You can start working tomorrow."
            h "I will be in touch with you for sure."

            scene day_04_holy_scene_5 with dissolve
            mc "Well, I'll see you then."
            h "Bye."
            $ holy_love += 1
            $ holy_hired = True
            jump nicole_bench

        "{color=#74B2F4}Tell her you are sorry about her job.{/color}":

            scene day_04_holy_scene_2 with dissolve
            mc "I'm sorry to hear that."
            mc "I hope everything will sort out sooner or later and you will find new job."
            h "Thank you."
            mc "Bye."
            jump nicole_bench

label nicole_bench:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_04_nicole_garden_bench_1 with dissolve
    "{color=#D2691E}*Nicole sits on a bench behind the house and smokes a cigarette nervously.*{/color}"

    scene day_04_nicole_garden_bench_2 with dissolve
    n "What am I supposed to do?"
    n "Nobody wants to lend me a penny. Not to mention $5,000. I have about 24 hours left to raise that money."
    n "Why was I so stupid?"
    n "Son of a bitch won't leave me alone. He'll probably ask for $10,000 in a while and then what am I going to do?"

    scene day_04_nicole_garden_bench_3 with dissolve
    n "I don't think I have any other choice. I have to ask [player_name]...."
    n "I can imagine him asking me why I need so much money. Eh. I can't tell him the truth. I have to make up a story and lie to him."
    n "I'll text him that I'd like to meet him tomorrow morning."
    jump day_04_pool

label day_04_pool:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_1[hair]" with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_2[hair]" with dissolve
    l "You're finally here."
    r "I'm sorry I'm late."
    r "I hope you don't mind, but I invited my new friend."
    l "Of course I don't mind."
    l "But where is she?"

    scene expression "day_04_lisa_pool_3[hair]" with dissolve
    r "She is waiting in front of the house. She didn't want to come in without your permission."
    l "Hehe. Then call her."

    scene expression "day_04_lisa_pool_5[hair]" with dissolve
    r "Lisa, meet Amy. Amy, this is Lisa."
    amy "How are you?"
    $ amy_enabled = True

    scene expression "day_04_lisa_pool_6[hair]" with dissolve
    l "Nice to meet you, too. Make yourselves comfortable. And change your clothes."

    scene expression "day_04_lisa_pool_7[hair]" with dissolve
    "{color=#D2691E}*The girls undressed and lay down on the deckchairs.*{/color}"
    l "Where did you meet?"
    r "A few days ago in a club. I didn't tell you anything, because you're busy with your [player_name] all the time."
    l "I haven't seen you in our town before, Amy."
    amy "I'm on vacation visiting my grandmother, she lives on the other side of town."
    amy " Unfortunately her health is not so good, so it looks like I'm going to stay here longer to take care of her."

    scene expression "day_04_lisa_pool_8[hair]" with dissolve
    "{color=#D2691E}*The girls talked about things for some time. Finally, Rachel got up from the deckchair.*{/color}"
    r "Enough of this chit-chat."
    r "It's about time to go swimming."

    scene expression "day_04_lisa_pool_9[hair]" with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_10[hair]" with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_11[hair]" with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_12[hair]" with dissolve
    $ renpy.pause ()

    scene expression "day_04_lisa_pool_13[hair]" with dissolve
    "{color=#D2691E}*The girls were swimming, jumping into the water and fooling around  for a long time.*{/color}"
    "{color=#D2691E}*Lisa notices that something is going on between Rachel and Amy. The girls have something more serious in common than just acquaintance.*{/color}"
    l "Seriously, Rachel, get a room."
    l "I'm going to get something to drink. And you're supposed to behave here."
    r "Sure."
    jump lisa_rachel_pool

label lisa_rachel_pool:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_04_lisa_pool_14 with dissolve
    "{color=#D2691E}*Lisa goes home to prepare something to drink. Meanwhile, Rachel and Amy aren't going to behave at all.*{/color}"
    "{color=#FF69B4}*The girls hug each other and start kissing passionately.*{/color}"

    scene day_04_lisa_pool_15 with dissolve
    "{color=#FF69B4}*Amy takes off Rachel's top and gently teases her erected nipples with her tongue.*{/color}"

    scene day_04_lisa_pool_16 with dissolve
    "{color=#FF69B4}*Amy caresses her breasts with one hand and reaches into her pussy with the other.*{/color}"

    scene day_04_lisa_pool_17 with dissolve
    "{color=#FF69B4}*She slowly and gently massages Rachel's clitoris with her fingers. Rachel moans quietly.*{/color}"

    scene day_04_lisa_pool_18 with dissolve
    "{color=#FF69B4}*Amy opens Rachel's vulva lips and slips two fingers into her pussy.*{/color}"
    r "Don't stop. Oh, yeah."

    scene day_04_lisa_pool_19 with dissolve
    "{color=#FF69B4}*Rachel wants to feel Amy's fresh skin on her skin, so she takes off Amy's top.*{/color}"
    "{color=#FF69B4}*Rachel moans louder and louder. Her breath is getting faster. Her body is resilient while she waits for the wave of pleasure to come.*{/color}"
    r "Don't stop. I am cummmming!"

    scene day_04_lisa_pool_20 with dissolve
    with flash
    with flash
    with flash
    $ renpy.pause ()
    "{color=#FF69B4}*Rachel's body is flooded with a hot wave of pleasure. The girl moans loudly, unable to catch her breath.*{/color}"
    "{color=#FF69B4}*But Amy doesn't stop. She pulls her fingers out of Rachel's pussy and starts massaging her clitoris.*{/color}"

    scene day_04_lisa_pool_22 with dissolve
    "{color=#FF69B4}*She kisses Rachel passionately. Rachel's body trembles with delight, and every muscle is tense to the limit.*{/color}"
    "{color=#FF69B4}*In the end, Amy releases Rachel from her love embrace. Rachel is exhausted, but happy.*{/color}"

    scene day_04_lisa_pool_21 with dissolve
    r "You little devil..."
    r "It was insanely intense."
    amy "I hope you liked it."
    r "Oh, yes!"

    scene day_04_lisa_pool_23 with dissolve
    "{color=#FF69B4}*Suddenly Rachel picks up Amy and sits her on the edge of the pool.*{/color}"
    "{color=#FF69B4}*Rachel takes off her panties and throws them in the pool.*{/color}"
    "{color=#FF69B4}*She gently opens Amy's legs and she can finally admire her beautiful pussy.*{/color}"

    menu lisa_lesbian:

        "{color=#74B2F4}Stay and watch.{/color} [LisaLesbianPath]":

            scene expression "day_04_lisa_pool_23a[hair]" with dissolve
            l "What the hell is going on here?"
            l "Why are they not ashamed of themselves?"
            "{color=#D2691E}*Lisa wants to turn around and leave, but her desire keeps her from leaving.*{/color}"

            scene expression "day_04_lisa_pool_23b[hair]" with dissolve
            "{color=#D2691E}*She feels her nipples hardening and her pussy getting wet.*{/color}"
            l "What's happening to me?"
            l "Why am I getting excited?"
            l "Am I a lesbian?"

            menu lisa_fingering:

                "{color=#74B2F4}Masturbate.{/color} [LisaLesbianPath]":

                    scene expression "day_04_lisa_pool_23c[hair]" with dissolve
                    "{color=#D2691E}*Lisa is getting more and more aroused. She puts down the glass and sits on a chair.*{/color}"
                    "{color=#D2691E}*She can't stop looking at Rachel and Amy.*{/color}"

                    scene expression "day_04_lisa_pool_23d[hair]" with dissolve
                    "{color=#FF69B4}*Lisa sighes in resignation and gives up fighting the feeling of arousal that has stewing in her lower abdomen since she saw Rachel licking Amy's pussy.*{/color}"
                    "{color=#FF69B4}*She allows her legs to part and she reaches her panties, slightly tugging on them.*{/color}"

                    scene expression "day_04_lisa_pool_23e[hair]" with dissolve
                    "{color=#FF69B4}*She feels her hand reach her bare shaved pussy. Slowly, she slides her index finger inside her wet and tight pussy.*{/color}"

                    scene expression "day_04_lisa_pool_23f[hair]" with dissolve
                    "{color=#FF69B4}*She inserts it quickly and she audibly gasps at the sensation.*{/color}"
                    "{color=#FF69B4}*Lisa starts breathing hard as her finger massage her g-spot.*{/color}"

                    scene expression "day_04_lisa_pool_23g[hair]" with dissolve
                    "{color=#FF69B4}*She is practically panting now, and making no effort to keep from moaning loudly.*{/color}"
                    "{color=#FF69B4}*She starts rubbing her clit to get more pleasure.*{/color}"

                    scene expression "day_04_lisa_pool_23h[hair]" with dissolve
                    "{color=#FF69B4}*Her eyes are closed and she is squirming with arousal. She keeps on and on until she begins to shudder.*{/color}"
                    "{color=#FF69B4}*She clenches her pussy walls around her hand hard, then releases as liquid gushed out of her cunt.*{/color}"

                    scene expression "day_04_lisa_pool_23i[hair]" with flash
                    with flash
                    with flash
                    l "Oh, my fucking God."

                    scene expression "day_04_lisa_pool_23j[hair]" with dissolve
                    "{color=#D2691E}*Lisa raises her head and sees Amy and Rachel watching her with a lewd smile on their faces.*{/color}"

                    scene expression "day_04_lisa_pool_23ja[hair]" with dissolve
                    "{color=#D2691E}*Lisa breaks off the chair and runs back in the house.*{/color}"
                    l "What have I done?"
                    $ lisa_masturbate = True

                "{color=#74B2F4}Just watch.{/color}":

                    scene expression "day_04_lisa_pool_23a[hair]" with dissolve
                    "{color=#D2691E}*Lisa stands there like she's enchanted and staring at her best friend lick Amy's pussy with passion.*{/color}"
                    "{color=#D2691E}*When Amy starts moaning in delight, Lisa turns around and goes back in the house.*{/color}"


        "{color=#74B2F4}Go back inside.{/color}":

            scene expression "day_04_lisa_pool_23a[hair]" with dissolve
            l "What the fuck they are doing?"
            l "I will have a word with Rachel when they are done."
            "{color=#D2691E}*Lisa turns around and goes back in the house.*{/color}"

    scene day_04_lisa_pool_23 with dissolve
    if lisa_masturbate == True:
        "{color=#FF69B4}*After Lisa leaves Rachel goes back down on Amy.*{/color}"

        scene day_04_lisa_pool_24 with dissolve
        "{color=#FF69B4}*Rachel puts her head between the girl's legs and very slowly starts teasing Amy's clitoris with her tongue.*{/color}"
    else:
        "{color=#FF69B4}*Rachel puts her head between the girl's legs and very slowly starts teasing Amy's clitoris with her tongue.*{/color}"

    r "You taste wonderful."

    scene day_04_lisa_pool_25 with dissolve
    "{color=#FF69B4}*Amy starts moaning. Her breasts waving gently to the rhythm of her body.*{/color}"

    scene day_04_lisa_pool_26 with dissolve
    $ renpy.pause ()

    scene day_04_lisa_pool_27 with dissolve
    $ renpy.pause ()

    scene day_04_lisa_pool_31 with dissolve
    "{color=#FF69B4}*Rachel licks her vulva and clitoris. Seeing Amy's growing arousal, she puts two fingers in her wet pussy.*{/color}"
    amy "Don't stop. Lick my tight and wet pussy. Oh, yeah, just like that."

    scene day_04_lisa_pool_32 with dissolve
    "{color=#FF69B4}*Rachel caresses Amy's clitoris more and more. Amy's body tightens while waiting for an orgasm.*{/color}"
    "{color=#FF69B4}*Rachel feels Amy tremble. Eventually, Amy freezes for a split second, and after a while, she gives herself up to full ecstasy.*{/color}"

    scene day_04_lisa_pool_30 with dissolve
    with flash
    with flash
    with flash
    $ renpy.pause ()

    scene day_04_lisa_pool_29 with dissolve
    "{color=#FF69B4}*Rachel presses her head hard against Amy's nectar-dripping pussy.*{/color}"

    scene day_04_lisa_pool_28 with dissolve
    "{color=#FF69B4}*Rachel once again starts teasing her pussy with her tongue, while lickin' the sweet juices leaking out of her.*{/color}"
    "{color=#FF69B4}*Amy trembles with pleasure for another moment, until she finally makes her last loud moan.*{/color}"

    scene day_04_lisa_pool_33 with dissolve
    amy "It was amazing."
    r "We have to do it again soon."
    amy "No doubt about it."
    $ renpy.end_replay()

    scene day_04_lisa_pool_34 with dissolve
    amy "Why don't we bring Lisa into the relationship? She seems so sweet. It could be great to have fun with the three of us."
    r "I don't think she would be interested. She's in love with [player_name] so I wouldn't think about her yet."
    amy "Okay. But I guess we can ask her?"
    r "I believe we can."
    jump sandra_home_day_04

label sandra_home_day_04:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_04_sandra_home_1 with dissolve
    "{color=#D2691E}*You try to call Sandra again, but she still doesn't answer. You get in the car and go to her.*{/color}"
    "{color=#D2691E}*KNOCK KNOCK*{/color}"

    scene day_04_sandra_home_2 with dissolve
    s "What do you want?"
    mc "Talk to you."
    s "After what you did to me? I don't want to talk to you."

    scene day_04_sandra_home_3 with dissolve
    "{color=#D2691E}*Sandra tries to close the door, but you manage to stop her at the last minute.*{/color}"
    s "What are you doing?"
    mc "Will you be so kind as to give me a moment to explain?"
    s "No. Get out of my sight."
    mc "Come on, Sandra. Don't make me beg you."
    s "Fine...You have 5 minutes and then get out."

    scene day_04_sandra_home_5  with dissolve
    "{color=#D2691E}*You sit on the couch.*{/color}"
    s "What are you waiting for? Say what you have to say."
    mc "I don't know what you're upset about. It was just a show for Clara. If I had told you earlier, it wouldn't have been so realistic."
    mc "That way your reactions were natural. I thought you'd find out what was going on instead of being offended also Clara will trust you more than if it didn't look natural."

    scene day_04_sandra_home_6 with dissolve
    "{color=#D2691E}*You approach her. You embrace her tenderly.*{/color}"
    mc "Leave it alone, please."
    s "I'm sorry. I don't know why I reacted like that. I could have guessed what you meant."
    mc "It doesn't matter. Everything is fine."
    mc "It was a very hard day. I am exhausted. I'm going to the hotel to get some sleep."

    if s_dinner_day_3 == True:

        scene day_04_sandra_living_room_scene_1 with dissolve
        "{color=#D2691E}*After a moment of hesitation, Sandra asks you.*{/color}"
        s "Why don't you stay a little longer? We'll eat something, maybe watch a movie."

        menu sandra_offer_day_04:

            "{color=#74B2F4}Actually, it's a good idea.{/color} [SandraLovePath]":

                mc "Hmm. Why not?"
                s "That's great."
                $ sandra_love += 1
                $ s_dinner = True

                jump dinner_day_04

            "{color=#74B2F4}Maybe another time.{/color}":

                mc "I'm sorry, but I'm exhausted. Maybe another time."
                s "I understand."
                mc "Good night."
                $ sandra_love -= 2

                jump end_of_day_four

    else:

        jump end_of_day_four

label dinner_day_04:

    scene day_04_sandra_living_room_scene_3 with dissolve
    s "Would you like a drink?"
    mc "Hmm. I'd like a beer if it's not a problem."
    s "Yeah, sure."
    mc "Thank you."

    scene day_04_sandra_living_room_scene_4 with dissolve
    "{color=#D2691E}*You are sitting in silence. Finally, Sandra breaks the silence.*{/color}"
    s "Is there something wrong? You are not saying anything."
    mc "A lot happened and it was a very tiring day.  I now have a lot to think about."
    s "In fact, this thing with Linda is very disturbing."

    scene day_04_sandra_living_room_scene_5 with dissolve
    mc "That's right. Although we tried to prevent such a situation, she was able to bypass our security measures easily."
    mc "We can't work in such conditions."
    s "I don't know what else we could do."
    mc "Well, I don't know either."

    scene day_04_sandra_living_room_scene_6 with dissolve
    mc "Besides, Linda is not the only problem. I also have a problem with Jennifer."
    s "Why?"
    mc "Eh. It's about her boyfriend. Something happened with him and he became aggressive."
    mc "I have to do something about it."
    s "It doesn't sound good. Poor girl."
    mc "Yeah."

    scene day_04_sandra_home_7 with dissolve
    s "So Jennifer changed her attitude towards you?"
    mc "I don't know. She apologized to me for her behavior and I feel like she doesn't know what she feels about me."
    s "But it's still progress."
    mc "It's better than if she was still angry with me."
    mc "I have to do something about her boyfriend. I hope that if I deal with him, Jennifer will change her attitude towards me completely."
    s "I'm sure she will."

    scene day_04_sandra_living_room_scene_7 with dissolve
    "{color=#D2691E}*Sandra is silent for a moment.*{/color}"
    s "Do you care about these girls?"
    mc "Of course. They are like sisters to me."
    mc "Something worries you?"
    s "I'm not sure but I shouldn't bother you with speculation."

    scene day_04_sandra_living_room_scene_8 with dissolve
    mc "What are you talking about?"
    s "You know..."
    mc "No, I don't know."
    s "Nevermind..."
    s "Let's go to the kitchen. I'm hungry. I'll cook something for us."

    scene day_04_sandra_living_room_scene_9 with dissolve
    "{color=#D2691E}*Sandra is starting to make you dinner. There are wonderful smells in the whole kitchen.*{/color}"
    s "Would you like something else to drink? How about another beer?"
    mc "I'd rather have a whiskey if you have one."
    s "Sure."
    mc "Thanks."

    scene day_04_sandra_living_room_scene_7 with dissolve
    mc "You know... I look at you and I can't believe how lucky I was to meet you."
    s "Oh, stop it. I'm not special at all."
    mc "But you are. Not only you're beautiful, but you're also so intelligent."
    s "I don't know what to say. Thank you..."

    scene black with dissolve
    "{color=#D2691E}*After dinner, Sandra comes up to you and hugs you.*{/color}"
    "{color=#D2691E}*Her body is trembling. You hold her tighter to yourself.*{/color}"

    scene day_04_sandra_living_room_scene_10 with dissolve
    s "Thank you for being with me. I thought I could never be able to be closer to a man again."
    s "Thank you for everything."
    mc "Thank you too for a wonderful evening."
    mc "It's getting late, so I think I should go now."
    s "Okay. I'll see you tomorrow at the office."
    mc "Sleep well."
    $ renpy.pause ()

label end_of_day_four:

    scene black with dissolve
    show bg end_of_day_04 with dissolve
    $ renpy.pause ()
    jump day_05
