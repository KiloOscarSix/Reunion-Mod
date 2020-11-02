label day_02:
    $ day = "Day 2"
    $ save_name = "Day 2"

label jennifer_apologize:

    scene black with dissolve
    show bg day_02 with dissolve
    $ renpy.pause ()

    scene day_02_lisa_room_apologize_scene_1 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{/color}"
    "{color=#D2691E}*Lisa's asleep. Knocking on the door wakes her up.*{/color}"
    l "Who's there?"

    scene day_02_lisa_room_apologize_scene_1a with dissolve
    j "It's me."

    scene day_02_lisa_room_apologize_scene_2 with dissolve
    l "Go away."
    j "Please, let me in. I wanted to apologize to you."
    l "Eh. Okay, it's open."

    scene day_02_lisa_room_apologize_scene_3 with dissolve
    "{color=#D2691E}*Jennifer enters the room. Lisa notices a shy smile on her face.*{/color}"
    j "Good morning, Lisa."
    l "Jesus, what time is it?"
    j "6 am"
    j "I'm sorry to wake you at this early hour, but I'm about to go to work and I wanted to talk to you."

    scene day_02_lisa_room_apologize_scene_4 with dissolve
    l "Okay..."
    j "I want to apologize to you with all my heart for my behavior yesterday."
    j "I don't know what came over me. I didn't want to be mean or rude."
    j "I'm sorry that I made you cry."

    scene day_02_lisa_room_apologize_scene_5 with dissolve
    "{color=#D2691E}*Jennifer sits on the bed next to her sister.*{/color}"
    j "Can you forgive me?"
    l "Why are you behaving like our mother?"
    j "I don't know. I'm trying to protect us, but it looks like I suck at it. I didn't want to be like her. You know that I hate the way she treats us as much as you do."
    j "If I'm behaving like her, believe me, it wasn't intended."
    j "I promise you that I will work on it so it doesn't happen again in the future."

    scene day_02_lisa_room_apologize_scene_6 with dissolve
    "{color=#D2691E}*Lisa holds Jennifer's hand and the tears drop down her cheeks.*{/color}"
    l "I do love you, Jennifer. I'll help you with everything, so you won't have to deal with this mess alone."
    l "But promise me one thing."
    j "Whatever you wish, Lisa."
    l "Give [player_name] a chance."
    j "..."

    scene day_02_lisa_room_apologize_scene_7 with dissolve
    j "Why are you defending him so much? Did you forget what he did to us?"
    l "Of course I didn't, but we haven't even given him a chance to explain himself. Maybe there is something we don't know about?"
    l "Maybe he had some reasons he couldn't tell us about before?"

    scene day_02_lisa_room_apologize_scene_8 with dissolve
    j "Do you really believe that?"
    l "It looks like you already forgot how close we were with him?"
    j "No, I haven't forgotten about our relationship. I haven't forgotten what he did for us all."
    j "But I also haven't forgotten that he left us all of a sudden without a word."

    scene day_02_lisa_room_apologize_scene_9 with dissolve
    l "But don't you think that no matter what he deserves the chance to explain himself?"
    l "I suffered even more than you. But I won't judge him till he gets his chance to tell me what happened ten years ago."
    j "Hmm. Maybe you're right. Maybe I should give him a chance too."
    j "I'll think about it."
    j "I love you, Lisa."
    l "I love you too."

    if k_sex == True:
        jump kelly_morning
    else:
        jump alone_morning

label kelly_morning:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_02_hotel_room_scene_1_bed with dissolve
    "{color=#D2691E}*RING RING RING*{/color}"
    "{color=#81F79F}*Seriously, what time is it?*{/color}"

    scene day_02_hotel_room_scene_2_bed_phone with dissolve
    mc "Hello?"
    sec "I'm sorry for disturbing you at such an early hour. I'm Mrs. White's secretary. Mrs. White would like you to attend a meeting
    at your father's company at 10 o'clock."
    sec "Does this suit you?"
    mc "Good morning. Thanks for the information."
    mc "Of course. I'll be there."
    sec "Thank you. Have a nice day, sir."

    scene day_02_hotel_room_scene_3_bed with dissolve
    "{color=#81F79F}*Kelly is so beautiful. I love the way her breasts shake with each breath.*{/color}"
    "{color=#D2691E}*She cuddles to you. The scent of her hair and warmth of her body make you drift away for a moment.*{/color}"
    mc "Good morning, beautiful."
    k "Hey."
    mc "You look so sexy in the morning."
    k "Thank you. It was a wonderful night. You know how to please a woman."

    scene day_02_hotel_room_scene_4_bed with dissolve
    k "What are you thinking about?"
    mc "About you mostly. It's a pity that it was just a one-night thing."
    k "I wish it could be longer."
    k "But at least it was a wonderful night. I'm so glad that we met."

    scene day_02_hotel_room_scene_5_bed with dissolve
    mc "Yeah. Eh. I have to get up. I have a meeting at 10 am and it's getting late already."
    k "Oh well. I thought we could eat breakfast together, but in this case, I'll get going too."

    scene day_02_hotel_room_scene_6_bed with dissolve
    "{color=#D2691E}*You know you have to get up finally, but until the last second you postpone this moment.*{/color}"
    mc "I need to take a shower."

    scene day_02_hotel_bathroom_scene_1 with dissolve
    "{color=#D2691E}*Few minutes later Kelly opens the door and enters the bathroom.*{/color}"
    k "[player_name], I just had a phone call from the Airline. I have to be at the airport in two hours, so I guess this is our goodbye."
    mc "Eh."
    mc "Can I get at least one last kiss from my beautiful lady?"

    scene day_02_hotel_bathroom_scene_2 with dissolve
    k "Of course. You deserved even two kisses. Hehe."

    menu sex_02:

        "{color=#74B2F4}Make sure she won't forget you.{/color} [KellyPath]":

            scene day_02_hotel_bathroom_scene_2a with dissolve
            k "What are you doing?"
            "{color=#D2691E}*You kiss her passionately while taking off her bathrobe. Your right hand is wandering down her body.*{/color}"

            scene day_02_hotel_bathroom_scene_10 with dissolve
            mc "I'm making sure you won't forget about me."

            scene day_02_hotel_bathroom_scene_4 with dissolve
            k "Oh."
            "{color=#FF69B4}*She closes her eyes and moans quietly.*{/color}"

            scene day_02_hotel_bathroom_scene_5 with dissolve
            "{color=#FF69B4}*Your hand reaches her sweet spot and you gently start to rub her clitoris with your fingers.*{/color}"
            "{color=#FF69B4}*She visibly enjoys your hands groping her body and the touch of yours on her exposed breasts and cunt.*{/color}"
            mc "You're already dripping wet."
            k "Mmm. Yes. The way you kiss me and touch me makes me so aroused."

            scene day_02_hotel_bathroom_scene_6 with dissolve
            "{color=#FF69B4}*You push two fingers inside her wet and tight pussy. You feel her juices drip off her beautiful cunt.{/color}"
            "{color=#FF69B4}*With your other hand, you caress her bosom. Your tongue swirls around her erect nipples.*{/color}"
            "{color=#FF69B4}*Kelly's lewd moans become louder and louder.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_1 with dissolve
            "{color=#FF69B4}*She shifts her position to allow you even better access to her wet slit.*{/color}"
            "{color=#FF69B4}*Her breathing quickens and her moans become ever more measured.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_2 with dissolve
            "{color=#FF69B4}*Soon, Kelly is moaning with pleasure, interspersed by the sounds of suckling mouth and lapping tongue.*{/color}"
            "{color=#FF69B4}*Excerting just the right amount of pressure on her clit, she orgasms in your face.*{/color}"
            k "Oh my fucking God... This is so amazing... I'm cumming!"

            scene day_02_hotel_bathroom_sex_scene_2 with flash
            with flash
            with flash

            scene day_02_hotel_bathroom_sex_scene_3 with dissolve
            "{color=#FF69B4}*After she stops trembling she kneels before you with lewd smile.*{/color}"
            k "I want to suck that monster of yours."
            "{color=#FF69B4}*She grabs hold of your erect cock and starts stroking it.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_4 with dissolve
            "{color=#FF69B4}*She starts slowly at first, licking the shaft from your balls to the very tip of your penis.*{/color}"
            "{color=#FF69B4}*The precum that starts flowing is lapped up before she takes your entire member into her mouth.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_5 with dissolve
            "{color=#FF69B4}*Kelly attempts to take the full length of your big cock in her mouth.{/color}"
            "{color=#FF69B4}*She starts to move her head up and down your shaft.*{/color}"
            mc "You're amazing. No woman has ever sucked my dick the way you do."

            scene day_02_hotel_bathroom_sex_scene_6 with dissolve
            "{color=#FF69B4}*With each licking, you feel a growing desire to dive your swollen cock in her tight pussy.*{/color}"
            "{color=#FF69B4}*Kelly feels your cock pulsate, so she squeezes it tighter and starts sucking on its tip.*{/color}"
            "{color=#FF69B4}*You feel that if you let her continue to caress your member like this, you'll soon reach your limits, so you pull out.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_7 with dissolve
            "{color=#FF69B4}*Kelly's pussy is slick with her juices, so you have no trouble entering her.*{/color}"
            "{color=#FF69B4}*You slam your dick deep inside her ribbed tunnel and Kelly starts moaning with pleasure.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_8 with dissolve
            "{color=#FF69B4}*The sight of Kelly's beautiful body paired with the pleasure her cunt is granting your cock make you very close to cumming.*{/color}"
            "{color=#FF69B4}*You pull out of Kelly to shift your position.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_9 with dissolve
            "{color=#FF69B4}*You love the sight of her ass so you turn her over and reinsert your cock into her pussy again.*{/color}"
            k "This feels so great. Keep going like that."
            "{color=#FF69B4}*You keep your dick buried deep in her wet and tight pussy.*{/color}"

            scene day_02_hotel_bathroom_sex_scene_10 with dissolve
            "{color=#FF69B4}*As you ride her, her ass bounces on the rhythm of your love-making, interspersed with hoarse moans of pleasure from her.*{/color}"
            "{color=#FF69B4}*Kelly turns her head and bites her lip with a lustful smile. Every muscle in her body taut in anticipation.*{/color}"
            "{color=#FF69B4}*You know this isn't the time for an orgasm yet.*{/color}"

            scene day_02_hotel_bathroom_scene_7 with dissolve
            "{color=#FF69B4}*You lift her and push against the wall. You gently spread her legs.*{/color}"
            "{color=#FF69B4}*Having backed her up against the wall, you press your cock against the lips of her cunt.*{/color}"
            k "Oh yes, [player_name] DO IT!  Push your huge dick into my tight pussy."

            show wally_kelly at wally_kelly_day_02
            k "Oh yeah. Just like that. Don't stop."
            "{color=#FF69B4}*Slipping past her lips, you enter her in one thrust, she is wet enough to do so.*{/color}"
            "{color=#FF69B4}*You feel that her body is tightening with every thrust you make. Her pussy is throbbing inside.*{/color}"
            mc "You're so beautiful. Every inch of your body is perfect."
            k "I'm cumming, [player_name]!"

            scene day_02_hotel_bathroom_scene_7 with flash
            with flash
            with flash
            "{color=#FF69B4}*Her orgasm is so potent that you have to hold her tight as to not let her slip off your cock.*{/color}"
            "{color=#FF69B4}*Completing a few more thrusts by yourself in her convulsing pussy, you feel you're ready too.*{/color}"
            mc "I'm cumming too!"

            call screen kelly_day_02_cumshot

        "{color=#74B2F4}Goodbye.{/color}":

            scene day_02_hotel_bathroom_scene_1 with dissolve
            k "Goodbye, [player_name]."
            mc "Take care, Kelly."
            $ renpy.end_replay()

            jump office_day_02a

label cumshot_day_02_facial:

    hide screen kelly_day_02_cumshot

    scene day_02_hotel_bathroom_facial with dissolve
    "{color=#FF69B4}*Kelly drops on her knees and opens her mouth*.{/color}"
    "{color=#FF69B4}*The torrent of your warm cum splashes on her breasts and face.*{/color}"
    mc "Wow. You're incredible."
    $ kelly_love += 1
    $ renpy.end_replay()

    jump kelly_hugs

label cumshot_day_02_creampie:

    hide screen kelly_day_02_cumshot

    scene day_02_hotel_bathroom_scene_9 with dissolve
    "{color=#FF69B4}*Few more thrusts. She pushes your member even deeper inside her sweet pussy and the torrent of warm seed fills her fully.*{/color}"
    "{color=#FF69B4}*You pull out your cock and the seed slowly drips out of her.*{/color}"
    mc "Oh my God..."
    $ kelly_love += 1
    $ kelly_creampie += 1
    $ renpy.end_replay()

    jump kelly_hugs

label kelly_hugs:

    scene day_02_hotel_room_scene_1_goodbye with dissolve
    "{color=#D2691E}*Kelly gets dressed and you walk her to the door.*{/color}"
    "{color=#D2691E}*You gently cuddle to her and she whispers in your ear.*{/color}"
    k "Thank you for such a wonderful time. I'll never forget you. I hope we'll meet again one day."
    k "It was such a great goodbye. I couldn't imagine a better way to do it."
    mc "You're so perfect. I couldn't resist and I didn't want to just let you go."
    k "I left you my address and phone number."

    scene day_02_hotel_room_scene_2_goodbye with dissolve
    k "Don't forget about me. And visit me when you're in Los Angeles. I'll be waiting."
    mc "I won't forget you. Don't worry. I'll do what I can to finish my businesses here."
    mc "In the meantime dream about me."
    k "You bet, I will."
    k "Goodbye."

    jump office_day_02a

label alone_morning:

    scene day_02_phone_holy_john_alone_1 with dissolve
    "{color=#D2691E}*RING RING RING*{/color}"
    mc "Hello?"
    sec "I'm sorry for disturbing you at such an early hour. I'm Mrs. White's secretary. Mrs. White would like you to attend a meeting
    at your father's company at 10 o'clock."
    sec "Does this suit you?"
    mc "Good morning. Thanks for the information."
    mc "Of course. I'll be there."
    sec "Thank you. Have a nice day, sir."

    jump office_day_02a

label office_day_02a:

    scene black with dissolve
    show bg at_the_office with dissolve
    $ renpy.pause ()

    scene day_02_secretariat_scene_1 with dissolve
    sec2 "Good morning, how may I help you?"
    law "My name is Sandra White and this is [player_name] [player_surname] - the new president of this company."

    scene day_02_secretariat_scene_2 with dissolve
    sec2 "..."

    scene day_02_secretariat_scene_3 with dissolve
    "{color=#D2691E}*You hear some noises. The door opens and you see Linda.*{/color}"
    "{color=#D2691E}*She is furious.*{/color}"
    li "What the fuck are you doing here? I told you that you won't take over MY COMPANY!"
    li "GET THE FUCK OUT OF HERE!"

    menu linda_reply_day_02:

        "{color=#74B2F4}Let Sandra reply.{/color} [SandraLovePath]": #+1 love and harem

            scene day_02_secretariat_scene_4 with dissolve
            s "According to the will of the deceased, Mr. [player_name] [player_surname] is the owner of the company."
            s "I'm truly sorry but you have nothing to say about it."
            s "So, let us pass or I'll call the police."
            $ sandra_love += 1
            jump office_day_02

        "{color=#74B2F4}Reply yourself.{/color} [LindaSubmissionPath]":

            scene day_02_secretariat_scene_4 with dissolve
            mc "Linda, unfortunately, you have nothing to say in this matter."
            mc "You got rid of me for ten years, but I've come back and this time I won't give up so easily."
            $ linda_submission += 1
            jump office_day_02

label office_day_02:

    scene day_02_secretariat_scene_5 with dissolve
    "{color=#D2691E}*With each passing second rage from her face disappears and changes into terror.*{/color}"
    li "You have no right."
    mc "Move away. My patience is starting to run thin."

    scene day_02_secretariat_scene_5 with dissolve
    "{color=#D2691E}*Her confidence is gone. Her body is trembling and you see the fear in her eyes.*{/color}"
    li "But...you can't..."
    mc "Yeah, you just said that."

    menu linda_reply_day_2:

        "{color=#74B2F4}Move closer to her.{/color} [LindaSubmissionPath]":

            scene day_02_secretariat_scene_6 with dissolve
            "{color=#D2691E}*You move closer to her.*{/color}"
            mc "{color=#7FFFD4}*whisper in her ear*{/color} This is just the beginning."
            mc "{color=#7FFFD4}*whisper*{/color} You will pay for everything you did to me, I swear."
            "{color=#D2691E}*You push her away and enter the office.*{/color}"
            $ linda_submission += 1

        "{color=#74B2F4}Push her away.{/color} [LindaLovePath]":

            scene day_02_office_scene_2 with dissolve
            "{color=#D2691E}*You push her away and enter the office.*{/color}"

    scene day_02_office_scene_2 with dissolve
    "{color=#D2691E}*You cross the room and sit down behind the desk.*{/color}"
    "{color=#D2691E}*All the tension is gone and a smile appears on your face.*{/color}"
    s "Are you all right?"
    mc "Yes, I haven't felt this good in a very long time."

    scene day_02_office_scene_2 with dissolve
    "{color=#D2691E}*The lawyer gives you a couple of folders.*{/color}"
    s "Okay. Here you have all the necessary documents. If you have any problems, please call me and I will try to help you."
    mc "Thank you."
    s "Have a nice day, sir."

    scene day_02_office_scene_3 with dissolve
    "{color=#D2691E}*Sandra turns around and she is about to leave your office.*{/color}"
    $ renpy.pause ()

    scene day_02_office_scene_4 with dissolve
    mc "Mrs. White! Please wait."

    scene day_02_office_scene_5 with dissolve
    mc "I'm grateful for your commitment and help. I would like to hire you for your services."
    mc "I'll need trusted people to deal with this mess."

    scene day_02_office_scene2_5 with dissolve
    "{color=#D2691E}*She stands in front of you with a confused expression on her face.*{/color}"
    "{color=#D2691E}*You finally notice how beautiful she is. You can't take off your eyes of her bosom. Her body is so perfectly shaped.*{/color}"
    s "Oh! Thank you very much, Mr. [player_surname]..."
    mc "Please, call me [player_name]."

    scene day_02_office_scene_5 with dissolve
    s "Thank you, [player_name]."
    mc "Alright, so... When can you start?"
    s "Straight away."
    mc "Oh! That's great."

    scene day_02_office_scene2_4 with dissolve
    "{color=#D2691E}*Sandra's smiling at you. She seems to be very grateful for your offer.*{/color}"
    mc "So, I would like you to start getting the documents I might need to run this company without problems."
    mc "Next, please prepare a list of the employees hired by Linda and prepare the necessary documents to fire them if needed."
    mc "And the most important thing. Prepare a contract for your services."
    mc "Also, as I want to have you here, we will share this office."
    s "Okay. That’s not a problem. There is plenty of room here. I’ll start working on these documents."

    scene day_02_office_scene2_3 with dissolve
    mc "Great."
    mc "What about your salary?"
    s "I have no idea."
    mc "Just name the price you consider as a fair one."
    "{color=#D2691E}*Sandra's surprised. It seems like she didn't expect you to let her determine her salary.*{/color}"
    s "…Okay…"
    jump bench_in_the_park

label bench_in_the_park:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_02_park_lisa_rachel_scene_1 with dissolve
    "{color=#D2691E}*The park looks wonderful this time of year. The sun's rays shine through the crowns of the trees.
    The birds are tweeting.*{/color}"
    "{color=#D2691E}*Lisa and Rachel love to meet here. The girls have their favorite place in the park.
    Not far from the old fountain is a bench hidden behind trees, where practically no one looks.*{/color}"

    scene day_02_park_lisa_rachel_scene_2 with dissolve
    l "Hey, Rachel."
    r "Hey, bestie. What’s up?"

    scene day_02_park_lisa_rachel_scene_3 with dissolve
    l "[player_name] is back!"

    scene day_02_park_lisa_rachel_scene_7 with dissolve
    "{color=#D2691E}*Lisa's very excited.*{/color=#D2691E}"
    l "Do you remember when I told you about him?"
    r "How could I forget? If I let you, you would talk about him all the time."
    r "How long since you last saw him?"
    l "Almost ten years."
    r "Have you met him yet?"

    scene day_02_park_lisa_rachel_scene_4 with dissolve
    "{color=#D2691E}*Lisa is excited. She walks around the bench and wobbles her hands nervously.*{/color}"
    l "Yes. We met yesterday. I was so excited, but my stupid sisters pissed him off. So I didn't have a chance to talk to him."
    r "Eh. Yeah, those two can be annoying sometimes."
    r "Seriously, calm down!"
    r "What the hell is wrong with you?"
    l "Sorry."

    scene day_02_park_lisa_rachel_scene_5 with dissolve
    r "Now, tell me what is going on?"
    l "I've never told you this before. Don't get me wrong, but ..."
    l "All these years, I've imagined that he's my boyfriend. I know it sounds stupid, but you know how it was. After my father's death, he was the only one who was there for me."
    l "I could always count on him and he was so wonderful to me. I was already enchanted by him then. It wasn't love, but you understand."
    l "When he left without saying a word, I was devastated. All this time I didn't allow myself to think that he did it for no good reason."
    l "I always believed he would come back. That I would see him again and maybe something good would come out of it. That's why I couldn't find a boyfriend."
    l "None of them were even close to a match for him."

    scene day_02_park_lisa_rachel_scene_6 with dissolve
    r "You know, everything is fine, but how can you be sure that he is interested in you in the same way? What if he has a wife or fiancée? Have you thought about it?"
    l "No. I'm sure he's not seeing anyone, or at least I strongly believe in it. "
    r "What if you're wrong and for some reason, you're not gonna be together? Remember that he is much older than you."
    l "I try not to think about it. Do you think that what I feel for him is normal? Maybe there is something wrong with me?"
    r "You worry too much about it. Stop analyzing it like this and be more spontaneous."
    r "Have you thought about changing your hairstyle or hair color? Also, start dressing differently."

    scene day_02_park_lisa_rachel_scene_7 with dissolve
    r "Remember, every guy will be judging your appearance first. Highlight your strengths. You have beautiful breasts and an incredible ass. Expose them more. Let them stand out."
    l "Hmm. I wasn't thinking about changing my hairstyle. But maybe you're right. Are you serious about these clothes? Should I dress like you?"
    r "Something like that."
    l "Hmm. Okay. I believe I can do it."
    l "It bothers me so much, tell me one thing please."
    l "Are you sure there's nothing wrong with me wanting to go out with him?"
    r "Pull yourself together. He's not your brother, is he?"
    l "Well, he's not, but he's always been like family to me."

    scene day_02_park_lisa_rachel_scene_8 with dissolve
    r "I don't have the patience for you anymore. Decide what you want. For me, there is nothing wrong with it and you have nothing to worry about."
    r "Start acting for a change, because he'll go somewhere again, and then you won't let me live it down."
    l "I love you, Rachel. Thanks for everything."
    r "Good luck with that. Let me know how you're doing. I'll see you soon."

label sandra_hired_day_02_01:

    scene black with dissolve
    show bg at_the_office with dissolve
    $ renpy.pause ()

    scene day_02_office_scene2_1 with dissolve
    "{color=#D2691E}*Together with Sandra you spent the whole day in the office working on papers.*{/color}"
    "{color=#D2691E}*For the most of the day, you couldn't focus on anything but her.*{/color}"

    scene day_02_office_scene2_2 with dissolve
    "{color=#D2691E}*You sat like a hypnotized person, unable to take your eyes off her.*{/color}"
    "{color=#D2691E}*She had to notice that you were staring at her because she smiled happily from time to time.*{/color}"
    mc "I think that's enough for one day. It's getting late and we need some rest."

    scene day_02_office_scene2_3 with dissolve
    mc "A lot of work ahead of us before we can deal with this mess."
    s "Right. I didn't even notice that it was so late."

    scene day_02_office_scene2_4 with dissolve
    "{color=#D2691E}*Sandra's packing her things. You're staring at her like a horny teenager again. She notices it, and smiles to you.*{/color}"
    mc "I'm... so glad... that you decided... to work for me."

    scene day_02_office_scene2_5 with dissolve
    s "Thank you for the trust. I won't let you down."
    mc "I'm sure you won't."

    scene day_02_office_scene2_6 with dissolve
    "{color=#D2691E}*She wrote something on a piece of paper and gave it to you.*{/color}"
    s "Here is my private number. Call me, if you need any help... or just someone to talk to."
    mc "Oh. Thank you."
    s "Catch you later. Bye."

    scene day_02_office_scene_3 with dissolve
    "{color=#81F79F}*I should probably visit Lisa. She was very sad yesterday.*{/color}"
    "{color=#81F79F}*Damnit, I wasn't planning to confront Linda now.*{/color}"
    "{color=#81F79F}*But Lisa is much more important for me so I don't think I have any other choice and I have to risk meeting Linda.*{/color}"
    jump your_house

label your_house:

        scene black with dissolve
        show bg few_hours_later with dissolve
        $ renpy.pause ()

        scene day_02_home_entrance_scene_1 with dissolve
        "{color=#00FF00}*Almost ten years have passed since I've been here for the last time and almost nothing has changed.*{/color}"

        scene day_02_home_entrance_scene_1a with dissolve
        "{color=#D2691E}*You knock the door. You hear noises inside the house.*{/color}"
        l "Who's there?"
        "{color=#D2691E}*Lisa is staring at you with disbelief.*{/color}"

        scene day_02_home_entrance_scene_2 with dissolve
        l "[player_name]?"

        scene day_02_home_entrance_scene_3 with dissolve
        l "I'm so glad to see you again. I thought you're mad at us and I wouldn't see you again."
        mc "How could I be mad at you, sweetie?"
        l "Come in. Linda is not at home."

        scene day_02_home_kitchen_scene_1 with dissolve
        j "Who is it, Lisa?"
        l "Come here and see yourself."

        scene day_02_home_kitchen_scene_2 with dissolve
        "{color=#D2691E}*A moment later, you see Jennifer coming down the stairs.*{/color}"
        j "Oh, it's you [player_name]."

        scene day_02_home_kitchen_scene_3 with dissolve
        mc "Hey, Jennifer."

        scene day_02_kitchen_jennifer_scene_1 with dissolve
        "{color=#D2691E}*Jennifer's looking at you strangely. You have the impression that she is fighting with her feelings.*{/color}"
        j "Hey there."
        j "Listen. I'm very sorry for my behavior yesterday. I didn't want to be so mean to you."
        j "I just can't cope with all this. Nicole is driving me crazy. Our mother doesn't care about anything."

        scene day_02_kitchen_jennifer_scene_2 with dissolve
        j "Besides, I have personal problems and now, you show up out of nowhere after all these years."
        j "To everyone's surprise, you're the only heir of your father and you'll be the one to decide about our fate."

        scene day_02_kitchen_jennifer_scene_3 with dissolve
        j "That was far too much for me and hence my behavior yesterday."

        menu jennifer_cuddle:

            "{color=#74B2F4}Cuddle her tenderly.{/color}[JenniferLovePath]": # +1 harem and love

                scene day_02_kitchen_jennifer_scene_4 with dissolve
                "{color=#D2691E}*Jennifer lowers her head and begins to cry. You cuddle her tenderly and whisper in her ear.*{/color}"
                mc "{color=#7FFFD4}*whisper in her ear*{/color} Don't cry, please. You don't have to worry about anything. You can live here as long as you want."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} If you lack money or have any problems, just let me know and I'll always help you."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} Just because I have some unfinished business with your mother, it doesn't mean that I intend to hurt you in any way."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} I honestly didn't expect that my father would give me all his property. I don't know why he did it."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} But as I said, I'm not here to hurt you."

                scene day_02_kitchen_jennifer_scene_5 with dissolve
                j "Thank you..."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} I know you hate me. I know I should explain what happened to me ten years ago. But not now. I want you to know that I love you and I'll do everything for you."
                mc "{color=#7FFFD4}*whisper in her ear*{/color} Just give me a chance to prove it."

                scene day_02_kitchen_jennifer_scene_6 with dissolve
                j "{color=#7FFFD4}*whispers back*{/color} Deep in my heart I still love you too."
                mc "Don't cry. Everything will be fine. I'm here with you now and you can again count on me."
                l "What are you whispering about?"
                j "Nothing important."
                $ jennifer_love += 1
                jump dinner_with_jennifer

            "{color=#74B2F4}Tell her everything is okay.{/color}": # +1 relationship

                scene day_02_kitchen_jennifer_scene_1 with dissolve
                mc "As I said before, I'm not here to hurt you."
                mc "You can live here as long as you want."
                j "Thank you..."
                l "What are you whispering about?"
                j "Nothing important."
                jump dinner_with_jennifer

            "{color=#74B2F4}Fine.{/color}":

                scene day_02_kitchen_jennifer_scene_1 with dissolve
                mc "Fine..."
                j "I'm serious!"
                mc "Okay. I don't want to talk about that."
                mc "Let's just pretend that our conversation yesterday never happened."
                jump dinner_with_jennifer

label dinner_with_jennifer:

        scene day_02_home_kitchen_scene_1 with dissolve
        l "[player_name], are you hungry? Jennifer could cook something for you."
        l "She knows how to cook. She'll certainly cook something delicious for you."
        j "Stop it, Lisa. You'll make me blush."

        menu dinner_with_girls:

            "{color=#74B2F4}I could eat something.{/color} [JenniferLovePath]":

                mc "I could eat something. But I don't want to trouble Jennifer."
                $ jennifer_love += 1
                $ j_dinner_day_02 = True
                jump phone_sandra_emily

            "{color=#74B2F4}I'm not hungry.{/color}":

                mc "Thank you, but I'm not hungry."
                jump phone_sandra_emily

label phone_sandra_emily:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_02_phone_emily_sandra_1a with dissolve
    em "Hey, Sandra."
    s "Hey, Emily."
    em "Do you remember about yoga class tonight?"
    s "Damn. I totally forgot about it."
    em "I don’t want to hear another excuse. Be there or …"
    s "Okay. Don’t be mad. I’ll be there."
    em "You better be!"
    s "See you later."
    $ emily_enabled = True
    $ changeWallpaper()

    if j_dinner_day_02 == True:
        jump kitchen
    else:
        jump no_dinner

label kitchen:

    scene black with fade

    scene day_02_home_kitchen_scene_13 with dissolve
    "{color=#D2691E}*Jennifer's starting to cook a meal for you. The smell of the food cooking in the kitchen makes you even more hungry.*{/color}"
    l "[player_name], we have so many things to talk about. Tell me how you’re doing. What have you been up to all these years?"
    l "Where did you live?"

    scene day_02_home_kitchen_scene_9 with dissolve
    j "Lisa! Give him a break."
    l "What? I want to know what he was doing all these years?"

    scene day_02_home_kitchen_scene_7 with dissolve
    j "It’s not the right time for that. You'll have enough time to chit chat later."
    j "Now, it's more important to discuss what [player_name] is going to do with this mess."
    mc "To be honest, I have no clue what to do."

    scene day_02_home_kitchen_scene_8 with dissolve
    mc "For now I took over the company according to my father's will."

    scene day_02_home_kitchen_scene_12 with dissolve
    j "What about us? Do you want to take over the house too and move in?"
    mc "I told you already that you don't have to worry about it. I'm not here to hurt you or turn your life upside down."
    mc "You can stay here as long as you want. Even if I decide to move in there is enough room for all of us."

    scene day_02_home_kitchen_scene_13 with dissolve
    l "You should stay with us. Everything will sort itself out."
    mc "Unfortunately, it's not so easy. At this point moving in is not a good idea."

    scene day_02_home_kitchen_scene_13 with dissolve
    l "Hmm, maybe you’re right, but please stay with us for the night."
    mc "I'm not ready to face Linda yet. I don't want to risk you being hurt just because you're talking with me."
    mc "Remember... Linda is capable of anything."
    l "Okay, [player_name]. You're right."

    scene day_02_home_kitchen_scene_12 with dissolve
    j "I'm going to change and leave. Behave yourself."

    menu compliment_food:

        "{color=#74B2F4}It was really delicious.{/color} [JenniferLovePath]": # +1 harem and love

            mc "Thanks for the dinner. It was really delicious. Lisa was right. You're a great cook."
            j "Hehe. No problem. I'm glad you liked it."
            j "See you later, [player_name]."
            $ jennifer_love += 1
            jump upstairs

        "{color=#74B2F4}See you later.{/color}":

            mc "See you later, Jennifer."
            j "Take care."
            jump upstairs

label upstairs:

    l "[player_name], let's go upstairs."

    menu go_to_lisa_room_kitchen:

        "{color=#74B2F4}Sure.{/color} [LisaLovePath]": #(+1 LOVE and HAREM)

            mc "Sure."
            mc "Hmm on the second thought I think it would wiser that I leave now before Linda comes back."
            l "Oh, come on. Everything will be fine."
            l "Trust me!"
            mc "Okay. Let's go."
            $ lisa_love += 1
            jump yoga_class_1

        "{color=#74B2F4}I think it would wiser that I leave now.{/color}":

            mc "Hmm on the second thought I think it would wiser that I leave now before Linda comes back."
            l "Oh, come on... You promised me."
            mc "I'm sorry, but I can't stay any longer."
            mc "Here's my phone number. Call me when you feel like it."
            mc "Goodnight."
            jump yoga_class

label no_dinner:

    j "Okay. I'm leaving you here. I'm going to change and leave. I have a few things to do today."
    j "See you later, [player_name]."
    mc "Bye, Jennifer."
    l "Let's go upstairs, [player_name]."

    menu go_to_lisa_room_no_dinner:

        "{color=#74B2F4}Sure.{/color} [LisaLovePath]": #(+1 LOVE and HAREM)

            mc "Sure."
            mc "Hmm on the second thought I think it would wiser that I leave now before Linda comes back."
            l "Oh, come on. Everything will be fine."
            l "Trust me!"
            mc "Okay. Let's go."
            $ lisa_love += 1
            jump yoga_class_1

        "{color=#74B2F4}I think it would wiser that I leave now.{/color}":

            mc "Hmm on the second thought I think it would wiser that I leave now before Linda comes back."
            l "Oh, come on... You promised me."
            mc "I'm sorry, but I can't stay any longer."
            mc "Here's my phone number. Call me when you feel like it."
            mc "Goodnight."
            jump yoga_class

label yoga_class:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_02_gym_scene_1 with dissolve
    "{color=#D2691E}*Sandra is going into the locker room.*{/color}"
    em "There you are. Right on time."
    s "I told you."
    em "Hurry up. The class is about to start."
    "{color=#D2691E}*The girls dress in a hurry.*{/color}"
    $ emily_enabled = True

    scene day_02_gym_scene_2 with dissolve
    em "So, any news?"
    s "To be honest, yes."

    scene day_02_gym_scene_3 with dissolve
    s "I finally got hired today."
    em "Wow. Finally. You deserved it, girl."

    scene day_02_gym_scene_4 with dissolve
    em "I’m so happy. I told you that you shouldn’t give up."

    scene day_02_gym_scene_5 with dissolve
    em "Tell me more about it."

    scene day_02_gym_scene_6 with dissolve
    "{color=#D2691E}The girls are entering the studio. They take up free places at the wall and start training.{/color}"
    s "Well, not much to tell. The president was one of my clients. He had to be satisfied with my services so he offered me a job."
    em "Is he handsome?"
    s "Here we go again…"
    em "Oh come on. Tell me."
    s "He is handsome… But nothing will happen, he's my boss now."

    scene day_02_gym_scene_7 with dissolve
    em "Don’t make me laugh. With this attitude, you will never find a man, not to mention a husband. Do you like him?"
    s "Do we have to go through it every freaking time?"
    em "Yes!"
    s "He is different."
    em "What do you mean?"
    s "I can’t explain it to you."
    em "Try."

    scene day_02_gym_scene_8 with dissolve
    s "He's got something in him that won't let you forget him. I don't know if you understand what I mean?"
    s "I don't know, maybe it's his confidence? It's a guy who walks into a room and knows what he wants."
    s "I think I caught his eye because he's been staring at me all day. That's what I'm talking about."
    s "Normally I would be mad if someone else did it. But he did it differently. He wasn't insistent, but determined and decisive."
    s "Fuck, I don't know how else to explain it to you."
    em "I think I know what you mean, although I've never met such a guy."

    scene day_02_gym_scene_9 with dissolve
    em "So, when will you go out with him?"
    s "I'm not going to date him!"
    em "Oh, yeah? I think you will."
    s "In fact, I think I gave him a private phone number and said something stupid."
    em "How does that seem to you? My dear, I think you're in love with him."
    s "That's a stupid idea, he's my boss silly!"
    em "Fine. Whatever."

    scene day_02_gym_scene_10 with dissolve
    s "This conversation is over."
    jump sandra_room_night

label yoga_class_1:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_02_gym_scene_1 with dissolve
    "{color=#D2691E}*Sandra is going into the locker room.*{/color}"
    em "There you are. Right on time."
    s "I told you."
    em "Hurry up. The class is about to start."

    scene day_02_gym_scene_2 with dissolve
    "{color=#D2691E}The girls dress in a hurry.{/color}"
    em "So, any news?"
    s "To be honest, yes."

    scene day_02_gym_scene_3 with dissolve
    s "I finally got hired today."
    em "Wow. Finally. You deserved it, girl."

    scene day_02_gym_scene_4 with dissolve
    em "I’m so happy. I told you that you shouldn’t give up."

    scene day_02_gym_scene_5 with dissolve
    em "Tell me more about it."

    scene day_02_gym_scene_6 with dissolve
    "{color=#D2691E}*The girls are entering the studio. They take up free places at the wall and start training.*{/color}"
    s "Well, not much to tell. The president was one of my clients. He had to be satisfied with my services so he offered me a job."
    em "Is he handsome?"
    s "Here we go again…"
    em "Oh come on. Tell me."
    s "He is handsome… But nothing will happen, he's my boss now."

    scene day_02_gym_scene_7 with dissolve
    em "Don’t make me laugh. With this attitude, you will never find a man, not to mention a husband. Do you like him?"
    s "Do we have to go through it every freaking time?"
    em "Yes!"
    s "He is different."
    em "What do you mean?"
    s "I can’t explain it to you."
    em "Try."

    scene day_02_gym_scene_8 with dissolve
    s "He's got something in him that won't let you forget him. I don't know if you understand what I mean?"
    s "I don't know, maybe it's his confidence? It's a guy who walks into a room and knows what he wants."
    s "I think I caught his eye because he's been staring at me all day. That's what I'm talking about."
    s "Normally I would be mad if someone else did it. But he did it differently. He wasn't insistent, but determined and decisive."
    s "Fuck, I don't know how else to explain it to you."
    em "I think I know what you mean, although I've never met such a guy."

    scene day_02_gym_scene_9 with dissolve
    em "So, when will you go out with him?"
    s "I'm not going to date him!"
    em "Oh, yeah? I think you will."
    s "In fact, I think I gave him a private phone number and said something stupid."
    em "How does that seem to you? My dear, I think you're in love with him."
    s "That's a stupid idea, he's my boss silly!"
    em "Fine. Whatever."

    scene day_02_gym_scene_10 with dissolve
    s "This conversation is over."
    jump lisa_room_day_02

label lisa_room_day_02:

    scene black with dissolve
    show bg lisa_room with dissolve
    $ renpy.pause ()

    scene day_02_lisa_room_scene_2 with dissolve
    l "How do you like my room? I decorated it myself."
    mc "It's really nice. I like it."
    mc "It’s good to be finally back. I’ve managed to make something out of my life but it can’t be compared with being here at home with you."

    scene day_02_lisa_room_scene_1 with dissolve
    mc "You don't even know how sorry I am that I wasn't with you all when you were growing up."
    l "It was a hard time for us too, but let’s not touch those wounds. You’re back and no matter what, I won’t let you disappear again."

    scene day_02_lisa_room_scene_3 with dissolve
    l "But [player_name] …This was bothering me for so long now… Tell me… Why you left us all of sudden?"
    l "I thought we had strong bonds. Almost like brother and sisters. And then one day you just disappeared. We were blaming ourselves and we thought it was because of us.
    Please tell me what was the reason."
    mc "Well. Forgive me, sweetheart, but I’m not ready to talk about it, but I promise I’ll explain everything to you, Jennifer and Nicole.
    I know I’m asking for a lot, but please give me some time to sort out everything in my head first. Besides, I would need some proof for them."

    scene day_02_lisa_room_scene_5 with dissolve
    mc "They won’t believe me just like that. And it will take some time. I’ll explain everything when there is a right time for it. I promise."
    l "Okay, [player_name]. I trust you, don’t let us down again please."
    mc "I won’t."
    jump chit_chat_choices_01

label chit_chat_choices_01:

    scene day_02_lisa_room_scene_4

    menu chit_chat_01:

        "{color=#74B2F4}Ask her about the house.{/color}" if house == False:

            mc "How are things at home? Is everything all right?"
            l "Not much is happening. Your father built a swimming pool in the garden and added a guest house."
            l "Nothing else. Linda doesn't take care of the house at all. The garden is in terrible condition. Poor Jennifer tries to figure it out for herself. "
            mc "She needs help. I'll see what I can do about it."
            $ house = True
            jump chit_chat_choices_01

        "{color=#74B2F4}Ask her about her school.{/color}" if school == False:

            mc "How's school?"
            l "Okay, good. I'm about to start college. I can't wait."
            mc "Which one did you choose?"
            l "Unfortunately, the city college was the only place I could get to. Mother didn't give a shit about me and didn't want to help me. So I didn't have any other choice."
            mc "It doesn't matter where you study. The most important thing is that you choose what you like and want to do in life."
            $ school = True
            jump chit_chat_choices_01

        "{color=#74B2F4}Ask her about her friends.{/color}" if friends == False:

            mc "Do you have a lot of friends?"
            l "Not really. Some of my friends have already traveled to various colleges. Only my best friend Rachel stayed in town. We will go to this college together."
            mc "At least you won't be alone. You will surely meet new, cool people there."
            l "I don't care that much. I have Rachel, and now I have you. That's enough for me."
            mc "It sounded a little strange. Haven't you thought about getting a boyfriend? You're old enough to date a handsome guy."
            l "Oh, come on. You're enough for me...."
            mc "What do you mean?"
            l "Nevermind. Forget about it."
            $ friends = True
            jump chit_chat_choices_01

    if friends == True and house == True and school == True:
        jump chit_chat_choices_02

label chit_chat_choices_02:

    scene day_02_lisa_room_scene_5 with dissolve

    menu chit_chat_02:

        "{color=#74B2F4}Ask her about sisters.{/color}" if sisters == False:

            mc "How are your sisters? Do you get along somehow?"
            l "Not really. I don't have any contact with Nicole. She spends all her days with her friends. A bunch of morons."
            l "I don't know where she found them, but it's the worst band in the whole city."
            mc "Linda doesn't do anything about it?"
            l "My mother doesn't give a shit. She also has her world."
            l "I don't know what she does all day long, but she certainly doesn't work or take care of us or the house."
            mc "What about Jennifer? Today it looked as if you were close to each other."
            l "I don't know. There's something wrong with her, too. She hasn't had time for me for a long time, and then suddenly she tries to act like a mother."
            l "Yesterday she yelled at me, and this morning with tears in her eyes she apologized to me."
            l "What a messed up family..."
            $ sisters = True
            jump chit_chat_choices_02

        "{color=#74B2F4}Ask her about Linda.{/color}" if linda == False:

            mc "Are you getting along with your mother somehow?"
            l "No, I don't."
            mc "Why?"
            l "You can't even talk to her normally. It's been going on for a few good years now. I don't know what happened to her, but she acts like she's the only one who lives in this world."
            l "I think she has completely forgotten about us."
            mc "That's terrible. I thought she was mean only to me."
            l "What did she do to you?"
            mc "What do you mean, what? She threw me out of the house."
            l "Did she throw you out? I thought you left by yourself."
            mc "Why would I do that?"
            l "I have no idea. You're not telling me anything."

            scene day_02_lisa_room_scene_10 with dissolve
            mc "Okay, fine. I'll tell you everything."
            mc "It all started right after you moved in."
            mc "At first, everything looked normal. Linda and my father seemed happy."
            mc "But as it turned out later Linda wasn't at all who I thought she was."
            mc "Before she even took control of my father's company, she somehow forced him to give her access to bank accounts in some inexplicable way."
            mc "It was then that I started to be interested in what was happening in this house."
            mc "I tried to find out what Linda's intentions were. I told my father about everything, but he went straight to her."
            mc "He told her about my suspicions. As you can guess Linda took things into her own hands and started to bother me."

            scene day_02_lisa_room_scene_10a with dissolve
            mc "She was brawling with me about anything. It was getting worse every day."
            mc "One day I found out that one of my friends was dead. The case was strange and mysterious."
            mc "The police determined that he had fallen off a cliff. However, they couldn't say whether it was murder or suicide."
            mc "They interviewed me many times, as well as my friends. A few days after the incident, Linda came to me at night."
            mc "She told me that she saw me pushing my friend into the abyss and that she was going to the police in the morning to testify against me."
            mc "She also said that if I didn't want to spend the rest of my life behind bars, I should leave town and never come back."
            mc "That was obviously bullshit. I had nothing to do with my friend's death, but it was clear to me that Linda had found a way to get rid of me once and for all."
            mc "I remember the mocking smile on her face when she was leaving my room. I was in shock."

            scene day_02_lisa_room_scene_10b with dissolve
            mc "I wasn't sure how far she would go or what nonsense she would tell the police."
            mc "I only had a few hours to make a decision. I didn't know what to do."
            mc "I was afraid that she would report me, that I would go to prison even though I hadn't done anything wrong."
            mc "So I decided that I had no other choice. I packed a few things and wrote you a letter explaining everything because I couldn't find a phone anywhere."
            mc "Linda had to take it with her when she was in my room. I left the letter on my desk. I tried to get in touch with you, but I had no way. Linda even deleted my email."
            mc "The passwords were saved on my pc and probably that's why she had access to them."
            mc "She cut me off from everything. I only remembered Jennifer's phone number."
            mc "So, I called her about a million times, but she never answered. I was desperate, so I sent you letters, like, a hundred in all."

            scene day_02_lisa_room_scene_10c with dissolve
            mc "I already had a new phone at that time. So, I wrote to you where I live and gave you my new phone number. But you never called or wrote back."
            mc "After a few months I gave up. And that's it. The whole story."
            l "God, I can't believe what you're saying. All this time I knew that something had to have happened, that you had some reason for leaving us,"
            l "but I never suspected that it was my mother who made you do it. But [player_name], when we walked into your room, there was no letter on your desk."
            l "Jennifer never said you called her and we never got a letter from you either. I bet it was my mother again."

            scene day_02_lisa_room_scene_11 with dissolve
            mc "I suppose so. That would explain many things. Now you understand why I want to take revenge on her? She took me away from you, my father, my home, my friends and my life."
            l "We have to tell Jennifer and Nicole about all of this."
            mc "No. They won't believe me. I need to find some proof that it was all Linda's fault. Only then can I explain everything to them."
            mc "For now, what I have just told you must be our secret."
            l "You're right. Especially Nicole won't believe you."

            scene day_02_lisa_room_scene_12 with dissolve
            l "I will do everything I can to help you."
            mc "I don't want you to get involved. Linda is unpredictable and I don't want anything to happen to you."
            l "Maybe you are right about her."
            mc "You must be careful."
            l "Okay. Don't worry about that."
            $ linda = True
            jump chit_chat_choices_02

    if sisters == True and linda == True:
        jump lisa_help

label lisa_help:

    scene day_02_lisa_room_scene_13 with dissolve
    l "So, what are your plans for the next days? "
    mc "I don't know yet. I didn't plan to stay here, but when I saw you again I thought I couldn't leave you again."
    mc "I want to rebuild a relationship with you. It would be great if we could be together as we used to be."
    l "I don't dream about anything else."
    mc "I would also like to take revenge on Linda. I can't stop thinking about it."
    l "I don't care what you want to do with my mom. She deserves all the worst."
    l "But promise me one thing."

    scene day_02_lisa_room_scene_13b with dissolve
    mc "Anything for you."
    l "If you decide to leave town, take me with you. I don't want to experience the same thing again."
    mc "I promise."
    l "Listen, [player_name]. I have an idea! I’ll help you with my sisters. Least I can do, [player_name]."
    l "What do you think?"

    menu:

        "{color=#74B2F4}It's a great idea.{/color} [LisaLovePath]": #(+1 LOVE and HAREM)

            scene day_02_lisa_room_scene_14 with dissolve
            mc "What do you mean?"
            l "I’ll try to talk to my sisters about you. I’ll try to convince them to trust you again or at least to give you a chance to explain everything."

            scene day_02_lisa_room_scene_14a with dissolve
            mc "Cool. This is a great idea, Lisa."
            mc "It’s good to know that I’m not alone here. That I have you by my side."
            mc "But please remember that it might be dangerous. Linda is capable of anything. So don't risk getting caught by her."
            mc "Write down my phone number. If you want to talk, just call. I’ll always find time for you."
            $ lisa_love += 1
            jump good_night

        "{color=#74B2F4}You shouldn't do it.{/color}":

            scene day_02_lisa_room_scene_13 with dissolve
            mc "Thank you, but it's too dangerous. Think about what Linda would do if she caught us."
            l "Okay. Maybe you’re right."
            jump good_night

label good_night:

    scene day_02_lisa_room_scene_15 with dissolve
    l "I love you, [player_name]"
    mc "I love you, too."
    mc "It's getting late. I should go."
    l "HAHA. Good joke. You aren’t going anywhere! You're sleeping here."
    mc "I would love to, but what if Linda caught us."
    mc "I don't want to even imagine what she'd do to you."
    l "Hmm. You’re right. It's so sweet of you that you care about me so much. Promise me that we'll see each other tomorrow."
    mc "Of course. If you want, you can come to the office. We'll have lunch and talk."
    l "Great idea."
    mc "Good night, sweetheart."
    l "Good night."
    jump lisa_room_night

label lisa_room_night:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_02_lisa_room_scene_night_1 with dissolve
    l "Damnit. It’s 2 am already and I can’t sleep."

    scene day_02_lisa_room_scene_night_2 with dissolve
    l "I can’t stop thinking about [player_name]. I’m so happy he’s back. I hope we’ll rebuild our relationship."
    l "I have to do what I can to help him with my sisters. They can ruin everything and I can’t let them do it."

    scene day_02_lisa_room_scene_night_3 with dissolve
    l "I love him so much. And… My God… He is so handsome."
    jump sandra_room_night

label sandra_room_night:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_02_sandra_room_night_scene_1 with dissolve
    s "I can’t focus. Maybe Emily is right for once. Something is intriguing about [player_name]."
    s "Am I falling in love? That's impossible. I barely know him."
    s "but that would be something new after all these years alone."

    scene day_02_sandra_room_night_scene_2 with dissolve
    s "I have to admit, he's handsome and kind."
    s "Besides, he was staring at me all day like a horny teenager."
    s "But the weird thing is, I didn't mind."

    scene day_02_sandra_room_night_scene_3 with dissolve
    s "Damnit. Even if it’s true, and I'm falling in love with him what bad could happen? In the worst scenario, he will just reject me."
    s "Not the first time, not the last time."
    s "Maybe he is the one I was waiting on for my entire life?"
    s "I highly doubt it, but who knows."

    scene black with dissolve
    show bg end_of_day_02 with dissolve
    $ renpy.pause ()
    jump day_03
