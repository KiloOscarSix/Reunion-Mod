label day_06:

    $ day = "Day 6"
    $ save_name = "Day 6"
    $ changeWallpaper()

#####################################################################################################################################################
                                                    #############SCENE 01 - Jennifer and Lisa#############
#####################################################################################################################################################
label day_06_scene_1:

    show bg day_06 with Dissolve(2)
    $ renpy.pause ()

    scene expression "day_06_scene_01_jennifer_1[hair]" with dissolve
    "{color=#D2691E}*Jennifer wakes up in a good mood.*{/color}"
    "{color=#D2691E}*She finally decided to dump Eric.*{/color}"
    "{color=#81F79F}*I'm sick and tired of that idiot. It's about time I move on and forget about him.*{/color}"

    scene expression "day_06_scene_01_jennifer_2[hair]" with dissolve
    "{color=#D2691E}*She gets out of bed trying not to wake up Lisa.*{/color}"
    "{color=#D2691E}*She takes the phone and sends a message to Eric.*{/color}"
    "{color=#81F79F}*What a relief.*{/color}"


label day_06_scene_1_1:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_06_scene_01_jennifer_3 with dissolve
    "{color=#D2691E}*Jennifer goes to the bathroom to take a shower.*{/color}"

    scene day_06_scene_01_jennifer_4 with dissolve
    "{color=#81F79F}*I've had enough of my pathetic life.*{/color}"
    "{color=#81F79F}*I also deserve to be happy. I have to start using life and not wait for God knows what.*{/color}"

    scene day_06_scene_01_jennifer_5 with dissolve
    "{color=#81F79F}*Getting rid of Eric was the best decision, finally I'm free to focus on myself.*{/color}"
    "{color=#81F79F}*I have to start seeing my friends again. Over the last few months I lost contact with all of them.*{/color}"
    "{color=#81F79F}*I really miss Jill... I have to call and meet with her.*"

    scene day_06_scene_01_jennifer_6 with dissolve
    "{color=#D2691E}*Jennifer finishes her shower and goes back to her room. Lisa is still sleeping.*{/color}"
    "{color=#81F79F}*I also need to rebuild my relationship with [player_name]. It would be great if we could be as close as we used to be.*{/color}"
    "{color=#81F79F}*I'm glad Lisa convinced me to call him yesterday. I'll need to cook something delicious for him. Finally, I will be able to dress up in something nice for someone important to me.*{/color}"

    scene day_06_scene_01_jennifer_7 with dissolve
    "{color=#81F79F}*It's been so long since I felt beautiful.*{/color}"

    scene day_06_scene_01_jennifer_8 with dissolve
    "{color=#81F79F}*I'm gonna get some makeup and look for something sexy to wear.*{/color}"

    scene day_06_scene_01_jennifer_9 with dissolve
    $ renpy.pause ()

    scene day_06_scene_01_jennifer_10 with dissolve
    $ renpy.pause ()

    scene day_06_scene_01_jennifer_11 with dissolve
    "{color=#D2691E}*Jennifer finishes her make-up.*{/color}"

    scene day_06_scene_01_jennifer_12 with dissolve
    "{color=#81F79F}*What should I wear today?*{/color}"
    "{color=#81F79F}*Hmm... how about this?*{/color}"

    scene day_06_scene_01_jennifer_13 with dissolve
    "{color=#D2691E}*She tries on the best dress she could find and looks at herself in the mirror.*{/color}"
    "{color=#81F79F}*That's fine, but not sexy enough. I haven't been able to go shopping in a long time because of Eric.*{/color}"
    "{color=#81F79F}*I need to go shopping.*{/color}"
    $ renpy.end_replay()

    scene expression "day_06_scene_01_jennifer_14[hair]" with dissolve
    l "Jesus, Jennifer. What time is it?"
    j "It's 8 am. Come on, get up."
    l "It's Saturday for God's sake."

    scene expression "day_06_scene_01_jennifer_15[hair]" with dissolve
    j "So what? Sun is shining already and I'd like you to go to the mall with me."
    l "Eh... okay. What are you going to buy?"
    j "Something sexy for today's dinner with [player_name]."

    scene expression "day_06_scene_01_jennifer_16[hair]" with dissolve
    l "Okay, but I need a shower first."
    l "Give me 30 minutes."
    j "Okay, sure."

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene expression "day_06_scene_01_jennifer_17[hair]" with dissolve
    l "So where do we go first?"
    j "Let's go to the lingerie shop first."

    scene expression "day_06_scene_01_jennifer_18[hair]" with dissolve
    l "I see you're in a good mood today."
    j "Yes, I'm in very good mood. I dumped Eric this morning."
    l "Finally!"

    scene expression "day_06_scene_01_jennifer_19[hair]" with dissolve
    j "I'm glad I'm done with him, but most of all I'm happy that I am going to meet [player_name] and talk to him."
    j "You were right. I misjudged him and acted like crap toward him."

    scene expression "day_06_scene_01_jennifer_20[hair]" with dissolve
    j "It's time to forget about the past and start enjoying life again."
    l "Nice to see that smile on your face again."

    scene expression "day_06_scene_01_jennifer_21[hair]" with dissolve
    "{color=#D2691E}*The girls are browsing the store for a while, looking for something nice for themselves.*{/color}"
    j "I found two lovely sets."
    l "Me too."
    j "Let's go to the dressing room."

    scene expression "day_06_scene_01_jennifer_22[hair]" with dissolve
    "{color=#D2691E}*Jennifer enters the dressing room first.*{/color}"

    scene expression "day_06_scene_01_jennifer_23[hair]" with dissolve
    "{color=#D2691E}*After a few minutes she opens the door and shyly comes out of the fitting booth.*{/color}"
    j "What do you think?"
    l "You look amazing."

    scene expression "day_06_scene_01_jennifer_24[hair]" with dissolve
    j "Don't I look too fat in this?"
    l "Come on. You look great."
    j "I don't know. I'll try the second set."

    scene expression "day_06_scene_01_jennifer_25[hair]" with dissolve
    j "And what do you think of this?"
    l "I'm speechless. Just great."
    j "I like it too."
    l "But I think the first set was better."

    scene expression "day_06_scene_01_jennifer_26[hair]" with dissolve
    "{color=#D2691E}*Jennifer goes back in the fitting booth.*{/color}"
    j "I'll think about which one to buy."
    l "Okay, it's my turn now."

    scene expression "day_06_scene_01_jennifer_27[hair]" with dissolve
    "{color=#D2691E}*A moment later, Lisa comes out of the fitting booth.*{/color}"
    l "So?"

    scene expression "day_06_scene_01_jennifer_28[hair]" with dissolve
    "{color=#D2691E}*Jennifer looks at her sister in disbelief.*{/color}"
    j "Very nice, but this underwear covers practically nothing."
    j "What do you think?"
    wo "I think it fits you perfectly."

    scene expression "day_06_scene_01_jennifer_29[hair]" with dissolve
    "{color=#D2691E}*Lisa is smiling lewdly.*{/color}"
    l "That's exactly the point."
    l "I will try the second set."

    scene expression "day_06_scene_01_jennifer_30[hair]" with dissolve
    l "How do you like this one?"
    j "I think you look better in this one."
    l "I think I'll take both sets."

    scene expression "day_06_scene_01_jennifer_31[hair]" with dissolve
    "{color=#D2691E}*Lisa dresses quickly and leaves the fitting booth.*{/color}"
    l "Which set are you going to buy?"
    j "I'll buy both."
    l "Hehe, me too."

    scene expression "day_06_scene_01_jennifer_32[hair]" with dissolve
    "{color=#D2691E}*The girls go to the cashier, pay for their shopping and leave the store.*{/color}"
    l "So where are we going now?"

    jump day_06_scene_2

#####################################################################################################################################################
                                        #############SCENE 02 - Mc going to bank with documents#############
#####################################################################################################################################################
label day_06_scene_2:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_06_scene_02_mc_mary_khloe_1 with dissolve
    kh "How can you live in this crap hotel."
    kh "You can't even take a proper shower."
    mary "Yes, I know. I've already talked to [player_name] about it."

    scene day_06_scene_02_mc_mary_khloe_2 with dissolve
    "{color=#D2691E}*Khloe comes up to you and tries to wake you up.*{/color}"
    kh "Get up, sleepyhead."
    kh "How long can you sleep?"

    menu wake_up:

        "{color=#74B2F4}What's going on?{/color}":

            mc "What's going on?"

            scene day_06_scene_02_mc_mary_khloe_3 with dissolve
            kh "If I'm going to stay in this shithole with you, we have to get out of here."
            mc "Okay, but why are you so upset?"
            kh "Because I couldn't take a shower! There is no hot water."

        "{color=#74B2F4}Five more minutes.{/color}":

            mc "Come on. Five more minutes."
            kh "Get up, now!"

            scene day_06_scene_02_mc_mary_khloe_3 with dissolve
            kh "If I'm going to stay in this shithole with you, we have to get out of here."
            mc "Okay, but why the nerves?"
            kh "Because I couldn't take a shower! There is no hot water."

    scene day_06_scene_02_mc_mary_khloe_4 with dissolve
    mc "Okay, we'll find something that suits you better."
    kh "I hope so."

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_02_mc_mary_khloe_5 with dissolve
    kh "What are you wearing?"
    kh "You look like a bum, don't you have any other clothes?"
    kh "Go get changed immediately, I can't look at you being dressed up like that."

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_02_mc_mary_khloe_5a with dissolve
    kh "Much better."
    mc "What a relief."

    scene day_06_scene_02_mc_mary_khloe_5b with dissolve
    kh "Fuck... I totally forgot that I have something for you."
    kh "Yesterday afternoon a courier delivered a package to our address for you."

    scene day_06_scene_02_mc_mary_khloe_6 with dissolve
    "{color=#D2691E}*Mary looks at you in surprise.*{/color}"
    mc "Who's this package from?"
    kh "I don't know. I didn't open it. I'll get it for you right away."

    scene day_06_scene_02_mc_mary_khloe_7 with dissolve
    "{color=#D2691E}*Khloe comes back after a while with a small package in her hands.*{/color}"

    scene day_06_scene_02_mc_mary_khloe_7a with dissolve
    "{color=#D2691E}*You take it from her and look at the sender.*{/color}"
    mc "Fuck me."

    scene day_06_scene_02_mc_mary_khloe_8 with dissolve
    mary "Who is it from?"
    mc "You won't believe it. It's from my father."
    mary "What?"

    scene day_06_scene_02_mc_mary_khloe_9 with dissolve
    "{color=#D2691E}*You open the package and look inside."
    mc "Fuck me."
    mary "What is it?"
    mc "All the letters I wrote to the girls after Linda kicked me out."

    scene day_06_scene_02_mc_mary_khloe_10 with dissolve
    mary "Are you kidding me?"
    mc "I'm totally serious."
    mary "Why did he have them and why were they sent to you just now?"
    mc "How should I know?"

    scene day_06_scene_02_mc_mary_khloe_11 with dissolve
    mary "When was this package sent?"
    mc "Hmm. Two days ago."
    mary "How could he do that if he died 10 days ago?"
    mc "Do you think he planned that?"

    scene day_06_scene_02_mc_mary_khloe_12 with dissolve
    mary "Do you mean sending the package or his death?"
    mc "Hmm... Both?"
    mary "I don't know, but it's getting more and more mysterious and strange."
    mc "Yeah, what the fuck is going on here?"

    scene day_06_scene_02_mc_mary_khloe_13 with dissolve
    mary "Look at these envelops. It seems that nobody ever opened these letters."
    mary "This is very strange."
    kh "Can someone explain to me what the fuck is going on here?"

    scene day_06_scene_02_mc_mary_khloe_14 with dissolve
    mary "We are trying to figure out why his father kept all his letters."
    kh "What letters?"
    mc "After Linda kicked me out of the house, I sent letters to Jennifer, Lisa and Nicole."
    kh "What the fuck?"

    scene day_06_scene_02_mc_mary_khloe_15 with dissolve
    kh "But why did you send letters to them? Couldn't you call them or send them an e-mail?"
    mc "I suspect Linda stole my phone and blocked my email account."

    scene day_06_scene_02_mc_mary_khloe_16 with dissolve
    mc "I had no other choice. Who remembers phone numbers or email addresses now?"
    mc "That's what phones are for..."
    kh "I guess..."

    scene day_06_scene_02_mc_mary_khloe_17 with dissolve
    mc "Hmm. Looks like there is something more."
    mc "There are land ownership deeds from 30 years ago, but without my father's signature on them."
    mary "Seriously, what is going on here?"
    mc "I have no idea."

    scene day_06_scene_02_mc_mary_khloe_18 with dissolve
    mc "We'll have to find out what kind of property those are and who the owners are."
    mc "And try to find out why my father had these deeds."

    scene day_06_scene_02_mc_mary_khloe_19 with dissolve
    kh "So it looks like we have a family mystery to solve."
    mary "Such a small town and so many secrets."

    scene day_06_scene_02_mc_mary_khloe_20 with dissolve
    mc "Fuck this shit."
    mc "All these years I was convinced that Linda was behind everything..."
    mary "We still don't know what role Linda played in this whole thing."

    scene day_06_scene_02_mc_mary_khloe_21 with dissolve
    mary "We have to find out what it's all about."
    kh "And we will. Don't worry about it. Mary and I are here for you."

    scene day_06_scene_02_mc_mary_khloe_22 with dissolve
    mc "Thanks my beauties. I don't know what I would do without you."
    mary "Khloe is right. Sooner or later we will find out the truth."
    mc "I hope so."

    jump day_6_scene_3

#####################################################################################################################################################
                                #############SCENE 03 - Linda trying to collect money to pay off her debt#############
#####################################################################################################################################################
label day_6_scene_3:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_06_scene_03_linda_1 with dissolve
    li "What am I supposed to do now?"
    li "I went all over the city, all my friends, bookmakers and nobody wants to lend me a penny."
    li "I have only a few hours left..."

    scene day_06_scene_03_linda_2 with dissolve
    li "If I don't give them this money back, they will do something terrible to me. I don't want to be anyone's slave, or even worse."
    li "They are probably not going to kill me, but will probably make me a slave. What kind of life is that? I've seen such girls before."
    li "First they make them addicted to drugs, and then they treat them worse than animals."

    scene day_06_scene_03_linda_3 with dissolve
    li "I have to think of something! But what?"
    li "*Even Clara won't talk to me, but can I really blame her? I've been treating her like shit. Eh, whatever, fuck that bitch, I'm not going to ask her for help."
    li "She will come to me begging for forgiveness."

    scene day_06_scene_03_linda_4 with dissolve
    li "If I could get the money out of the company account somehow..."
    li "But I don't have any other fucking option. Clara doesn't have access to the account, and Steven would probably sooner strangle me before helping me again."
    li "Think, woman. Your life depends on it."

    scene day_06_scene_03_linda_5 with dissolve
    li "Only [player_name] has access to the account, but he won't help me. Anyway, I don't even know if I could ask him for anything."
    li "So I'm fucked. I'll be a slave to some fucking filthy old man for the rest of my life."

    scene day_06_scene_03_linda_6 with dissolve
    "{color=#D2691E}*Linda starts crying.*{/color}"
    li "I have to go to that mean bitch and beg her to postpone the payment of the debt, and then I'll come up with something."
    li "This is probably the only way out of this nasty situation."

    scene day_06_scene_03_linda_7 with dissolve
    "{color=#D2691E}*Linda gets in the cab and goes to the club.*{/color}"
    "{color=#D2691E}*Security guards let her in.*{/color}"

    scene day_06_scene_03_linda_8 with dissolve
    "{color=#D2691E}*Linda knocks on the door.*{/color}"
    ming "Come in!"

    scene day_06_scene_03_linda_9 with dissolve
    "{color=#D2691E}*Linda slowly opens the door and goes inside. The room is dark, and the smell of incense and marijuana is in the air.*{/color}"
    "{color=#D2691E}*Mrs. Ming is sitting behind a big desk.*{/color}"
    li "Good evening, ma'am."

    scene day_06_scene_03_linda_10 with dissolve
    ming "What do you want? I hope you brought the money. I am tired of financing your whims."
    li "So... I'm very sorry, but there were some unforeseen circumstances and I came to ask you to postpone the payment of my debt for a few days."
    li "I promise I will pay everything including interest."

    scene day_06_scene_03_linda_11 with dissolve
    ming "Do you take me for some lowly bookie you can feed your bullshit to? I don't care about your problems, a deal's a deal."
    ming "You have time up to 8 pm to pay off the entire debt, which at the moment is $100,000."

    scene day_06_scene_03_linda_12 with dissolve
    li "$100.000? I borrowed $50,000!"
    ming "You dare come here moaning like a whore asking me to give you more time, you spoil my mood and you piss me off, and you wonder why I increase your debt?"

    scene day_06_scene_03_linda_13 with dissolve
    li "Where will I get so much money from?"
    ming "What the fuck do I care? This is your problem. Get the fuck out of here before you piss me off so much that I'll increase your debt to $200,000."

    scene day_06_scene_03_linda_14 with dissolve
    "{color=#D2691E}*Tears run down Linda's cheeks.*{/color}"
    ming "I don't need to remind you what awaits you if you don't pay me. I already have a few people who'd be willing to pay me a lot of money for you to become their slave."

    scene day_06_scene_03_linda_15 with dissolve
    "{color=#D2691E}*Linda is shaking.*{/color}"
    ming "Get the fuck out of here."

    scene day_06_scene_03_linda_16 with dissolve
    "{color=#D2691E}*Linda leaves the club. She gets weak and falls to the ground.*{/color}"

    scene day_06_scene_03_linda_17 with dissolve
    "{color=#D2691E}*She slowly gets up.*{/color}"
    "{color=#D2691E}*Linda finally realizes what a hopeless situation she's in.*{/color}"

    scene day_06_scene_03_linda_18 with dissolve
    "{color=#D2691E}*With a wobbly step, she moves slowly towards the city center.*{/color}"

    jump day_6_scene_4

#####################################################################################################################################################
                                            #############SCENE 04 - Nicole meets with blackmailer#############
#####################################################################################################################################################
label day_6_scene_4:

    if nicole_helped == True:

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause ()

        scene day_06_scene_04_nicole_1 with dissolve
        "{color=#81F79F}*I still have some time. Maybe I'll find a place to hide and wait for this bastard. I could finally find out who he is.*{/color}"
        "{color=#81F79F}*Just where I could hide so he wouldn't notice me.*{/color}"

        scene day_06_scene_04_nicole_2 with dissolve
        "{color=#D2691E}*Nicole slowly goes to a place and she's looking for a place where she can hide.*{/color}"
        "{color=#81F79F}*Why don't I hide behind those garbage cans? It smells terrible but there's plenty of room and I'll have a good view of that part of the parking lot.*{/color}"

        scene day_06_scene_04_nicole_3 with dissolve
        "{color=#D2691E}*She hides the envelope with money the same way she always does and she walks towards the entrance to the shopping centre.*{/color}"
        "{color=#D2691E}*As she passes the garbage bins, she quickly hides behind them.*{/color}"

        scene day_06_scene_04_nicole_4 with dissolve
        "{color=#D2691E}*Time is passing but nobody showes up at the parking lot to pick up the money.*{/color}"
        "{color=#D2691E}*Suddenly her phone rings.*{/color}"

        scene day_06_scene_04_nicole_5 with dissolve
        blackmailer "What do you think you're doing?"
        n "Nothing. I just delivered the money."
        blackmailer "I know. What are you doing behind these garbage cans?"

        scene day_06_scene_04_nicole_6 with dissolve
        "{color=#D2691E}*Nicole freezes.*{/color}"
        blackmailer "Yes, you stupid bitch. I can see you. You broke the terms of our deal."
        n "No, no, no!"

        scene day_06_scene_04_nicole_7 with dissolve
        blackmailer "You will be punished for disobedience."
        blackmailer "You have two hours to send me new photos. But this time I want to see some dildo action."
        n "Fuck you!"

        scene day_06_scene_04_nicole_8 with dissolve
        blackmailer "Don't try to piss me off even more. Obey me or I will destroy your life."
        n "Why are you doing this to me?"

        scene day_06_scene_04_nicole_9 with dissolve
        blackmailer "Because I like watching how you masturbating for me."
        n "Fucking pervert!"

        scene day_06_scene_04_nicole_10 with dissolve
        blackmailer "Because you can't shut the fuck up and you keep sassing me, you'll pay me another $5,000 by tomorrow night."
        n "How dare you! You'll regret it, I swear! I will find a way to punish you for what you are doing to me."
        blackmailer "Shut the fuck up. Do as I tell you or you will regret it even more."

        scene day_06_scene_04_nicole_11 with dissolve
        "{color=#D2691E}*Nicole started crying.*{/color}"
        blackmailer "Now you know, you stupid bitch, that it's not worth messing with me."
        blackmailer "I want those pictures in two hours."
        blackmailer "So get the fuck out of there and start pushing big dildo into your tight pussy."

        scene day_06_scene_04_nicole_12 with dissolve
        n "Oh my fucking god! What have I done?"

        jump day_6_scene_5

    else:

        scene black with dissolve
        show bg in_the_meantime with dissolve
        $ renpy.pause ()

        scene day_06_scene_04_nicole_13 with dissolve
        "{color=#81F79F}*I don't have any money for this motherfucker. I think I have to call him and beg him to postpone the payment deadline.*{/color}"
        "{color=#81F79F}*How stupid am I? If I didn't make up that stupid story of a sick friend, I would have the money by now and I wouldn't need to keep humiliating myself in front of this cocksucker anymore.*{/color}"
        "{color=#81F79F}*But I'm always the smartest...*{/color}"

        scene day_06_scene_04_nicole_14 with dissolve
        "{color=#D2691E}*Nicole's calling the blackmailer.*{/color}"
        blackmailer "What do you want?"
        n "I don't have that money for you..... You didn't give me enough time..."

        scene day_06_scene_04_nicole_15 with dissolve
        blackmailer "I don't give a fuck!"
        blackmailer "You didn't keep our deal and you'll be punished for it."
        n "What are you gonna do to me?"

        scene day_06_scene_04_nicole_16 with dissolve
        blackmailer "Let's see."
        blackmailer "I got it. In two hours you'll send me beautiful pictures of you putting a big dildo into your ass."
        n "Are you fucking crazy? You want me to stick a dildo up my ass?"

        scene day_06_scene_04_nicole_17 with dissolve
        blackmailer "And take pictures. HAHAHAHA"
        blackmailer "You have 24 hours to deliver the money to me. If you fail again, the punishment will be more severe."
        n "Fuck off!"

        scene day_06_scene_04_nicole_18 with dissolve
        blackmailer "Remember, two hours. Just this time, I want to have some nice close-ups!"
        n "Fuck off!"

        scene day_06_scene_04_nicole_19 with dissolve
        "{color=#D2691E}*Nicole throws her phone on the bed and starts sobbing.*{/color}"
        n "I've had enough of all this..."

        jump day_6_scene_5


#####################################################################################################################################################
                                        #############SCENE 05 - Sandra and Emily##########################
#####################################################################################################################################################
label day_6_scene_5:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    scene day_06_scene_05_sandra_emily_1 with dissolve
    em "Hey, Sandra."
    s "Hey. What are you doing here? I didn't expect you here today."
    em "I was around and decided to come visit you."
    s "Come in, please."

    scene day_06_scene_05_sandra_emily_2 with dissolve
    em "What's up?"
    s "Nothing interesting. I'm cleaning up the house."

    scene day_06_scene_05_sandra_emily_3 with dissolve
    s "Would you like something to drink?"
    em "I'd love to. Something cold."
    s "Wait me out on the terrace."

    scene day_06_scene_05_sandra_emily_4 with dissolve
    "{color=#D2691E}*After a few minutes, Sandra goes out to the terrace with the drinks in her hand.*{/color}"
    "{color=#D2691E}*Emily's standing there staring away.*{/color}"
    s "Here you go."

    scene day_06_scene_05_sandra_emily_5 with dissolve
    "{color=#D2691E}*Sandra's voice tears her out of her thoughts.*{/color}"
    s "Something happened?"
    em "We have to talk."

    scene day_06_scene_05_sandra_emily_6 with dissolve
    s "Okay. Sit down and tell me what's going on."
    em "It's not that simple."
    em "I don't know how to tell you this."

    scene day_06_scene_05_sandra_emily_7 with dissolve
    s "Just tell me, nothing bad will happen."
    em "I wouldn't be so sure, and that's what worries me."
    s "You're scaring me."

    scene day_06_scene_05_sandra_emily_8 with dissolve
    em "There are two things I would like to discuss with you."
    em "Both of them are connected."

    scene day_06_scene_05_sandra_emily_9 with dissolve
    em "For several months now, I have the feeling that our relationship has changed."
    em "I don't know if you've got that impression either, but it doesn't matter anyway."
    em "All this time I didn't know what caused it, but I think I finally know the answer."

    scene day_06_scene_05_sandra_emily_10 with dissolve
    em "When I realized why this was happening, I panicked."
    em "First I was afraid of what I realized, and now I'm afraid of what you're going to tell me."
    s "You're scaring me."

    scene day_06_scene_05_sandra_emily_11 with dissolve
    "{color=#D2691E}*Emily lowers her head and speaks in a barely audible voice.*{/color}"
    em "Sandra...For some time now, I've had the feeling that something has been going on between us."

    scene day_06_scene_05_sandra_emily_12 with dissolve
    "{color=#D2691E}*Sandra is silent, so Emily raises her head and looks her right in the eye and says.*{/color}"
    em "I don't know if you feel the same way about me, but I couldn't hide it from you anymore."

    menu sandra_love:

        "{color=#74B2F4}Yes, I feel that too.{/color} [SandraEmilyPath]":

            scene day_06_scene_05_sandra_emily_13 with dissolve
            "{color=#D2691E}*Sandra gets up and comes up to Emily.*{/color}"

            scene day_06_scene_05_sandra_emily_14 with dissolve
            "{color=#D2691E}*Tears are running down Emily's face.*{/color}"

            scene day_06_scene_05_sandra_emily_15 with dissolve
            "{color=#D2691E}*Sandra touches her face and rubs her tears with her thumb.*{/color}"

            scene day_06_scene_05_sandra_emily_16 with dissolve
            s "I think you are right. This thought has been bothering me for months now, but I was afraid to tell you."
            s "I'm so glad one of us finally dared to say it out loud."
            s "This uncertainty has driven me crazy."

            scene day_06_scene_05_sandra_emily_17 with dissolve
            "{color=#D2691E}*Emily is smiling at Sandra.*{/color}"
            em "I was sure it was just my imagination, but something happened and I had to be sure."
            s "What happened?"

            scene day_06_scene_05_sandra_emily_18 with dissolve
            em "[player_name]..."
            s " Right..."
            em "Do you feel anything for him?"

            scene day_06_scene_05_sandra_emily_19 with dissolve
            s "I don't know. I like him, I feel safe with him, but is that love?"
            s "I think it's too early to say that."
            em "If you have any feelings about me, why did you get involved with him?"

            scene day_06_scene_05_sandra_emily_20 with dissolve
            s "I don't know. He charmed me with his personality."
            s "You know I've never actually met anyone after my experiences."
            s "But he's different. There's something about his behavior, the way he talks to me, the way he treats me, which hasn't let me get past him."

            scene day_06_scene_05_sandra_emily_21 with dissolve
            s "Besides, all the time I've been keeping my mind off the idea that I've become a lesbian and that what I feel for you is a real feeling."
            em "I get it."
            em "You know... I've known him for a long time, too."

            scene day_06_scene_05_sandra_emily_22 with dissolve
            s "Oh?"
            em " Do you remember how I once told you about school love, that I couldn't get the courage to confess my feelings?"
            em "And then he suddenly disappeared. He left everything overnight and left town."

            scene day_06_scene_05_sandra_emily_23 with dissolve
            s "I remember. You couldn't recover for a long time."
            em "It turns out that my beloved from years ago and [player_name] are one and the same person."
            em "I found that out when I saw him the day you went on a date."

            scene day_06_scene_05_sandra_emily_24 with dissolve
            em "Even though so many years have passed, my feelings for him have not changed."
            em "I thought I'd had those feelings behind me a long time ago, but apparently I've only managed to put it down somewhere inside me, and now it's all coming back to life."
            s "And what are we going to do about it now?"

            scene day_06_scene_05_sandra_emily_25 with dissolve
            em "I don't know..."
            s "Do you think there could be physical contact between you and me, or are our feelings rather platonic?"
            em "Eh... I don't know that either."

            scene day_06_scene_05_sandra_emily_26 with dissolve
            em "But I think there's a way to find out."

            scene day_06_scene_05_sandra_emily_27 with dissolve
            "{color=#D2691E}*Emily comes up to Sandra, embraces her, and their lips meet in a shy kiss.*{/color}"
            "{color=#D2691E}*The initially shy kiss becomes more and more passionate with every second.*{/color}"
            "{color=#D2691E}*The girls are kissing slowly for while, then they start to pick up the speed.*{/color}"

            scene day_06_scene_05_sandra_emily_28 with dissolve
            "{color=#D2691E}*Emily bites Sandra's lip. Sandra lets out a small moan and bites hers back.*{/color}"
            "{color=#D2691E}*Emily smiles and proceedes to slide her tongue in Sandra'a mouth. They swirl their tongues around each other for a good time before Emily pulls back and looks at Sandra.*{/color}"

            scene day_06_scene_05_sandra_emily_29 with dissolve
            em "I think we know the answer."
            "{color=#D2691E}*Sandra is smiling at Emily.*{/color}"
            s "I guess so."
            s "The question is what do we do with [player_name]."

            scene day_06_scene_05_sandra_emily_30 with dissolve
            em "I don't know..."
            em "I see that neither of us wants to give up on him."
            s "I think there's something about it..."

            scene day_06_scene_05_sandra_emily_31 with dissolve
            em "Well, we could be with him together."
            s "Are you serious?"
            em "Why not?"

            scene day_06_scene_05_sandra_emily_32 with dissolve
            em "I can't deal with my feelings for him, so that's the only logical solution."
            em "Of course we both have to agree to that."

            scene day_06_scene_05_sandra_emily_33 with dissolve
            "{color=#D2691E}*Sandra puts her hand on Emily's thigh.*{/color}"
            s "You know damn well I can't ask you to do that and I don't think I want to."
            s "There's something very exciting, something mysterious, something I want to participate in."
            s "There is something unique about him, so I guess it's really worth the risk."

            scene day_06_scene_05_sandra_emily_34 with dissolve
            em "I think so too. We both know what we want to do. If we don't like it, he'll understand."
            s "I don't believe in what's happening. I've been alone for so many years. I was afraid to be involved with anyone, and now all of a sudden I confessed my feelings to my closest friend and I can't give up on the guy I just met."
            s " How did this happen?"

            scene day_06_scene_05_sandra_emily_35 with dissolve
            em "Hehe. Maybe it's time for a change?"
            s "I think you're right."

            scene day_06_scene_05_sandra_emily_36 with dissolve
            s "Okay, how do we know [player_name] will want to be involved in something like this?"
            em "We don't know. We need to talk to him."

            scene day_06_scene_05_sandra_emily_37 with dissolve
            s "Okay. I'll call him and set up a time to talk about this."
            em "Super."
            $ sandra_emily_harem = True

        "{color=#74B2F4}You feel something for me?{/color} [_SandraEmilyPath]":

            scene day_06_scene_05_sandra_emily_45 with dissolve
            "{color=#D2691E}*Sandra looks at Emily in disbelief.*{/color}"
            s "You surprised me... I don't know what to tell you..."

            scene day_06_scene_05_sandra_emily_46 with dissolve
            "{color=#D2691E}*Emily starts crying.*{/color}"
            "{color=#D2691E}*Sandra comes up to her and hugs her.*{/color}"
            s "I'm really sorry, but I don't feel the same way about you."

            scene day_06_scene_05_sandra_emily_47 with dissolve
            s "I love you like a friend, but..."
            em "I get it."
            em "You don't have to say anything else."

            scene day_06_scene_05_sandra_emily_48 with dissolve
            s "I'm so sorry..."
            em "I know."
            em "I'm gonna go."

            scene day_06_scene_05_sandra_emily_49 with dissolve
            s "Wait."
            em "I'm sorry, but I want to be alone now."

            $ sandra_no_love_for_emily = True

            jump day_6_scene_6

#####################################################################################################################################################
                #############SCENE 06 - Mary, Khloe and Mc. Presents and Mary tells Mc who is blackmailing Nicole#############
#####################################################################################################################################################
label day_6_scene_6:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_06_khloe_mary_linda_1 with dissolve
    show screen panty_sniffer
    $ renpy.pause ()
    hide screen panty_sniffer

    label panty_sniffing:

        scene day_06_scene_06_khloe_mary_linda_1 with dissolve
        mc "Girls, could you come over here for a minute, please?"
        kh "What's up?"

    scene day_06_scene_06_khloe_mary_linda_2 with dissolve
    mc "Khloe.... I'd like to apologize for leaving you alone with your last assignment."
    mc "I know we had a different agreement and I know you had a lot more work to do because of me."
    mc "I also wanted to thank you for having forgiven me and for coming to us. I missed you very much. Here, a small gift for you as an apology and again, I'm sorry. "

    scene day_06_scene_06_khloe_mary_linda_3 with dissolve
    kh "Oh, you didn't have to do that. I know you're going through difficult times. I was angry, but I'm over it."

    scene day_06_scene_06_khloe_mary_linda_4 with dissolve
    mc "And this one is for you, Mary. Thank you for being here with me and for supporting me."

    scene day_06_scene_06_khloe_mary_linda_5 with dissolve
    "{color=#D2691E}*Mary and Khloe unpack the presents. *{/color}"

    scene day_06_scene_06_khloe_mary_linda_6 with dissolve
    "{color=#D2691E}*They look at each other and start laughing.*{/color}"
    kh "Turn around!"

    scene day_06_scene_06_khloe_mary_linda_7 with dissolve
    kh "We are ready."
    mary "How do you like us?"
    mc "You look wonderful."

    scene day_06_scene_06_khloe_mary_linda_8 with dissolve
    "{color=#D2691E}*Your phone rings.*{/color}"
    mc "Seriously..."

    scene day_06_scene_06_khloe_mary_linda_9 with dissolve
    li "[player_name]?"
    mc "Yes. Who am I talking to?"
    li "..."

    scene day_06_scene_06_khloe_mary_linda_10 with dissolve
    mc "Hello?"
    li "It's me, Linda."
    mc "Really? What do you want?"

    scene day_06_scene_06_khloe_mary_linda_11 with dissolve
    li "I'm begging you, don't hang up on me until you hear me out."
    mc "Why would I listen to anything you have to say?"
    li "Because you're a good person and I'm fucked."

    scene day_06_scene_06_khloe_mary_linda_12 with dissolve
    mc "Thanks to you, I'm not a good person at all. And the fact that you're fucked up makes me very happy, so I don't see any reason to continue this conversation."
    li "I'm begging you. Could we meet?"
    mc "No."

    scene day_06_scene_06_khloe_mary_linda_13 with dissolve
    "{color=#D2691E}*You hang up but Linda calls you again.*{/color}"

    menu linda_calls:

        "{color=#74B2F4}Pick up the phone.{/color} [LindaSubmissionPath]":

            mc "Seriously, Linda, fuck off and don't call me again. We have nothing to talk about."

            scene day_06_scene_06_khloe_mary_linda_14 with dissolve
            li "Give me two minutes. I am begging you. It doesn't cost you anything, and maybe you'll have a chance to get back at me."
            mc "Eh, I can tell you're not going to give up and stop bothering me. Fine, you have two minutes."

            scene day_06_scene_06_khloe_mary_linda_15 with dissolve
            "{color=#D2691E}*Linda briefly tells you what happened and asks you for help.*{/color}"
            mc "You don't deserve anything better than what's supposed to happen to you."
            li "I know... but I'm still begging you for help."

            scene day_06_scene_06_khloe_mary_linda_16 with dissolve
            mc "I will think about it."
            li "Thank you. Can I call you in a while?"
            mc "No, I'll call you when I've made my decision."
            li "Okay. I'll be waiting."

            scene day_06_scene_06_khloe_mary_linda_17 with dissolve
            mary "Who was that?"
            mc "Linda..."
            mary "Oh, shit. Really? What did she want?"
            $ linda_help = True
            $ linda_submission += 1

        "{color=#74B2F4}Ignore Linda.{/color}":

            scene day_06_scene_06_khloe_mary_linda_17 with dissolve
            mary "Who was that?"
            mc "Linda..."
            mary "Oh, shit. Really? What did she want?"

    scene day_06_scene_06_khloe_mary_linda_18 with dissolve
    mc "I guess she finally found out that I blocked her transfer and I guess that's why she's in serious trouble."
    mary "Finally the stupid bitch gets what she deserves."
    mary "But what did she want?"

    scene day_06_scene_06_khloe_mary_linda_19 with dissolve
    kh "Who is Linda?"
    mary "Linda is a woman who lived with [player_name]'s father and who kicked [player_name] out ten years ago."
    mc "She wanted me to help her."

    scene day_06_scene_06_khloe_mary_linda_20 with dissolve
    kh "And what are you going to do?"
    mc "There's a chance to get revenge. This situation must be somehow exploited to our advantage."
    mary "I agree."

    menu questions_about_linda:

        "{color=#74B2F4}Ask Mary if she has any new information about Linda.{/color}" if linda_day_06_1 == False:

            scene day_06_scene_06_khloe_mary_linda_21 with dissolve
            mc "Any luck finding out anything new about her?"
            mary "Well, there's not much of it."
            mc "What do we know?"

            scene day_06_scene_06_khloe_mary_linda_22 with dissolve
            mary "Linda has a gambling addiction. I'm sure that's the reason of her debts."
            mc "I have no doubt about that."

            scene day_06_scene_06_khloe_mary_linda_23 with dissolve
            mary "Besides, it looks like Linda is involved in some suspicious business. I don't really know what's going on yet, but I'm working on it."
            mary "I also found out that Linda was planning to sell the house to pay off her debts and wanted to get rid of her daughters. Lisa was supposed to go to boarding school, just like Nicole."

            scene day_06_scene_06_khloe_mary_linda_24 with dissolve
            kh "What a mean cunt."
            $ linda_day_06_1 = True

            menu detailed_questions_about_linda:

                "{color=#74B2F4}Ask Mary if she knows who Linda's in debt to.{/color}" if linda_day_06_1a == False:

                    scene day_06_scene_06_khloe_mary_linda_25 with dissolve
                    mc "Do you know who she might have been in debt to?"
                    mary "Well... there's only one person in this town who has the money and power to run a casino."
                    mary "Her name is Ming. She is the queen of the criminal world here. She owns several clubs and casinos."

                    scene day_06_scene_06_khloe_mary_linda_26 with dissolve
                    mary "Besides, she's a drug dealer and is involved in illegal pornography."
                    mc "I like her already..."
                    $ linda_day_06_1a = True

                    jump detailed_questions_about_linda

                "{color=#74B2F4}Ask Mary who Linda wanted to sell the house to.{/color}" if linda_day_06_1b == False:

                    scene day_06_scene_06_khloe_mary_linda_27 with dissolve
                    mc "If you found out that Linda was trying to sell the house, then maybe you know who?"
                    mary "No, I'm afraid not. The person who was supposed to be the buyer does not exist, so it was probably a false name, but we can guess it was almost certainly Ming."

                    scene day_06_scene_06_khloe_mary_linda_28 with dissolve
                    mary "But I haven't found any connection between them, so it's just my guess."
                    mc "It's still more than I expected."
                    $ linda_day_06_1b = True
                    jump detailed_questions_about_linda

            if linda_day_06_1a == True and linda_day_06_1b == True:
                jump questions_about_linda

        "{color=#74B2F4}Ask Mary if there's anything else you should know.{/color}" if linda_day_06_2 == False:

            scene day_06_scene_06_khloe_mary_linda_29 with dissolve
            mc "Is there anything else you've been able to determine that I should know about?"
            mary "Linda's very close with Clara, but you probably already knew that."

            scene day_06_scene_06_khloe_mary_linda_30 with dissolve
            mary "But what you don't know is that Clara spent three years in prison for cheating and scamming money."
            mary "Anyway, Linda was in jail too. She spent less than a year there before she got involved with your father."

            scene day_06_scene_06_khloe_mary_linda_31 with dissolve
            mary "That's probably when they met and became friends."
            mc "I had no idea about that."
            $ linda_day_06_2 = True
            jump questions_about_linda

    if linda_day_06_1 == True and linda_day_06_2 == True:
        jump next

label next:

    scene day_06_scene_06_khloe_mary_linda_32 with dissolve
    kh "What are you gonna do now?"
    mc "I think it would be a good idea to pay Ms. Ming a visit."
    mary "I don't know if that's a good idea."

    scene day_06_scene_06_khloe_mary_linda_33 with dissolve
    mc "Do you have a better one?"
    mary "I don't... "
    kh "It seems to me that if you really want to get back at this bitch then we have to take advantage of this situation."

    scene day_06_scene_06_khloe_mary_linda_34 with dissolve
    mc "I agree with that."
    mary "Okay, but how do you want to play this?"
    mc "I'm just wondering."

    scene day_06_scene_06_khloe_mary_linda_35 with dissolve
    kh "Buy her debts. This way you will take control of her and make her your slave."
    mary "Sometimes you scare me..."
    mc "HEHE. It's not a bad idea at all."

    scene day_06_scene_06_khloe_mary_linda_36 with dissolve
    kh "I know what I'm talking about!"
    mary "How are you gonna make her a slave?"
    kh "Well, uh... Do you remember what they did to you when you were in captivity?"

    scene day_06_scene_06_khloe_mary_linda_37 with dissolve
    mary "You've got to be kidding me!"
    kh "I am not saying that we are to beat her or torture her, but she could be locked up somewhere and given time to submit to our will."
    mc "That's a good idea."

    scene day_06_scene_06_khloe_mary_linda_38 with dissolve
    kh "We'll have her sit in a dark basement for a few days, give her some water and bread. Before long her attitude will start to change."
    kh "And by then, she'll have learned her lesson."
    mary "I don't like it, but maybe you're right. Sometimes you have to use drastic methods to achieve a goal."

    scene day_06_scene_06_khloe_mary_linda_39 with dissolve
    mc "Well, that's decided."
    mc "All right, then. So I'm going to meet Mrs. Ming."

    jump day_6_scene_7

label panty_sniffer:

    hide screen panty_sniffer
    scene panty_sniffing_1 with dissolve
    "{color=#81F79F}*You see the little blue panties lying on the couch.*{/color}"

    scene panty_sniffing_2 with dissolve
    "{color=#81F79F}*The crotch is cold and damp still.*{/color}"

    scene panty_sniffing_3 with dissolve
    "{color=#81F79F}*You are wondering if they belong to Mary or Khloe.*{/color}"

    scene panty_sniffing_4 with dissolve
    "{color=#81F79F}*You put your warm breath through the material to bring out her smells and after the initial cool damp material is warmed by your breath the smell of her sex hit you.*{/color}"

    scene panty_sniffing_5 with dissolve
    "{color=#81F79F}*It must belong to Khloe. She has the kind of pussy that smells spicy, earthy, and just reeks of sex.*{/color}"
    "{color=#81F79F}*The smell is ambrosia and just knowing that it has to be that wet because she was masturbating earlier today, is so fucking hot.*{/color}"

    jump panty_sniffing

#####################################################################################################################################################
                                            #############SCENE 07 - Mc and Ming#############
#####################################################################################################################################################
label day_6_scene_7:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_07_ming_scene_1 with dissolve
    "{color=#D2691E}*You park your car right by the club's back entrance.*{/color}"
    "{color=#D2691E}*You walk up to the door and go inside.*{/color}"
    $ ming_enabled = True

    scene day_06_scene_07_ming_scene_2 with dissolve
    "{color=#D2691E}*There's a dusk light inside.*{/color}"
    "{color=#D2691E}*You walk up to a door at the end of the hallway.*{/color}"

    scene day_06_scene_07_ming_scene_3 with dissolve
    "{color=#D2691E}*You knock on the door.*{/color}"
    "{color=#D2691E}*No answer.*{/color}"

    scene day_06_scene_07_ming_scene_4 with dissolve
    "{color=#D2691E}*You press the handle and go inside.*{/color}"
    "{color=#D2691E}*You are now in a spacious but dim room, illuminated only by the small lamp on the big wooden desk.*{/color}"

    scene day_06_scene_07_ming_scene_5 with dissolve
    "{color=#D2691E}*In the dim light, you see a figure sitting behind the desk and watching the security camera feed of the club.*{/color}"
    mc "Good evening."

    scene day_06_scene_07_ming_scene_6 with dissolve
    "{color=#D2691E}*The person behind the desk is only now aware of your presence.*{/color}"
    ming "Who are you and what do you want?"

    scene day_06_scene_07_ming_scene_7 with dissolve
    mc "My name is [player_name] [player_surname]."
    mc "Sorry to trouble you, but I have a proposition and I think you'll be interested."

    scene day_06_scene_07_ming_scene_8 with dissolve
    "{color=#D2691E}*Ming is watching you closely.*{/color}"
    ming "I've never seen you here before."
    mc "That's right."

    scene day_06_scene_07_ming_scene_9 with dissolve
    ming "I'm not in the habit of accepting unannounced guests, but since you're here, what can I do for you?"
    mc "Well... I come to you because of one of your debtors."
    mc "Linda Brown."

    scene day_06_scene_07_ming_scene_10 with dissolve
    mc "I know she owes you money, quite a lot of money."
    ming "Maybe yes, maybe no."
    mc "I'd like to pay off her debts."

    scene day_06_scene_07_ming_scene_11 with dissolve
    ming "And that's an interesting coincidence."
    mc "Why's that?"

    scene day_06_scene_07_ming_scene_12 with dissolve
    ming "Quite recently, Linda was here begging for a debt deferral."
    mc "You agreed to this?"
    ming "Of course not."

    scene day_06_scene_07_ming_scene_13 with dissolve
    ming "So you say you want to pay her debts."
    mc "Exactly, but that's not all."

    scene day_06_scene_07_ming_scene_14 with dissolve
    mc "I would also like to ask you a favor."
    ming "What kind of favor?"

    scene day_06_scene_07_ming_scene_15 with dissolve
    "{color=#D2691E}*You briefly and concisely explain your plan to Ming.*{/color}"
    "{color=#D2691E}*Ming ponders what you just told her for a few moments.*{/color}"
    ming "I think I can do this for you."

    scene day_06_scene_07_ming_scene_16 with dissolve
    mc "Great."
    ming "But all the fun will cost you $150,000."
    mc "That's a reasonable proposal."

    scene day_06_scene_07_ming_scene_17 with dissolve
    mc "I'll deliver the money Monday night."
    ming "If you're not here by 8pm  my offer is no longer valid, and you'll be in my debt."
    mc "Don't worry. I'll bring the money, and you make sure Linda gets what we agreed."

    scene day_06_scene_07_ming_scene_18 with dissolve
    "{color=#D2691E}*Ming is smiling at you.*{/color}"
    ming "I'll see you in 48 hours."
    mc "Thank you and see you later."

    jump day_6_scene_8

#####################################################################################################################################################
                                        #############SCENE 08 - Mary and Khloe##########################
#####################################################################################################################################################
label day_6_scene_8:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_08_mary_nicole_1 with dissolve
    mary "About fucking time."
    mary "I finally found you, you filthy fucker."

    scene day_06_scene_08_mary_nicole_2 with dissolve
    kh "What's up? Who did you find?"
    mary "I found the bastard blackmailing Nicole."

    scene day_06_scene_08_mary_nicole_3 with dissolve
    kh "I have no idea who she is, but that's great news."
    mary "She's one of the girls our boss cares about so much. Linda's daughter."

    scene day_06_scene_08_mary_nicole_4 with dissolve
    kh "Really? That Linda?"
    mary "Yes, the very same one."
    mary "They used to be very close in the past and now [player_name] wants to rebuild relationships with them."

    scene day_06_scene_08_mary_nicole_5 with dissolve
    mary "But Nicole hates him for some reason. So we are trying to make her change her attitude towards him."
    kh "Stupid cunt. How can anyone even hate our boss?"
    mary "What can I say, but as you can see for yourself, it's possible. But we'll handle that, too."

    scene day_06_scene_08_mary_nicole_6 with dissolve
    kh "I don't doubt it."
    mary "Let's call him."

    scene day_06_scene_08_mary_nicole_7 with dissolve
    mary "Hey boss, I have good news for you."
    mc "About time."
    mary "I know who is blackmailing Nicole."

    scene day_06_scene_08_mary_nicole_8 with dissolve
    mc "That's great."
    mc "Who is he?"
    mary "It's just that she's a woman."

    scene day_06_scene_08_mary_nicole_9 with dissolve
    mc "A woman?"
    mary "Yes. Her name is Karen Smith."
    mc "Are you kidding me?"

    scene day_06_scene_08_mary_nicole_10 with dissolve
    mary "Do you know her?"
    mc "Yes. She used to live in my neighbourhood. On the same street. A couple of houses away."
    mary "Oh, my God."

    scene day_06_scene_08_mary_nicole_11 with dissolve
    mc "She was friends with my mother. If I'm not mistaken, she had a son, I think his name was David."
    mary "That's right."

    menu access_karen_phone:

        "{color=#74B2F4}Ask Mary to access Karen's phone and email.{/color} [gr]\[Nicole Pictures\]":

            scene day_06_scene_08_mary_nicole_12 with dissolve
            mc "Could you access her e-mail and phone?"
            mary "No problem."
            mc "Great."

            scene day_06_scene_08_mary_nicole_13 with dissolve
            mc "Let me know if you find anything interesting in there."
            mary "Sure."
            mc "Thanks. Bye."
            mary "Bye."
            $ nicole_pictures = True

            jump day_06_scene_9

        "{color=#74B2F4}Don't ask Mary to access Karen's phone and email.{/color}":

            scene day_06_scene_08_mary_nicole_13 with dissolve
            mc "Thanks. Bye."
            mary "Bye."

            jump day_06_scene_9

#####################################################################################################################################################
                                                #############SCENE 09 - Jennifer and Mc having a dinner#############
#####################################################################################################################################################

label day_06_scene_9:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_09_jennifer_1 with dissolve
    mc "Hey, Jennifer."
    j "Hey, [player_name]. I'm so glad you came."
    mc "These are for you."

    scene day_06_scene_09_jennifer_2 with dissolve
    j "Oh, such beautiful flowers, thank you so much!"
    j "Please come in. Dinner is almost ready."

    menu jennifer_compliment_day_06:

        "{color=#74B2F4}Compliment her.{/color} [JenniferLovePath]":

            scene day_06_scene_09_jennifer_2a with dissolve
            mc "You look beautiful."
            "{color=#D2691E}*Jennifer is blushing.*{/color}"
            j "You're so kind."

            scene day_06_scene_09_jennifer_3 with dissolve
            j "Would you like a drink?"
            mc "Wine is fine."
            $ jennifer_love += 1

        "{color=#74B2F4}Say nothing.{/color}":

            scene day_06_scene_09_jennifer_3 with dissolve
            j "Would you like a drink?"
            mc "Wine is fine."

    scene day_06_scene_09_jennifer_4 with dissolve
    j "Sure."
    j "Please, have a seat."
    j "So, how are you?"

    scene day_06_scene_09_jennifer_5 with dissolve
    mc "So much going lately. I'm slowly trying to solve all these problems that just keeps piling up. But when one problem is solved, a new one always pops up."
    j "That's not good."

    scene day_06_scene_09_jennifer_6 with dissolve
    mc "Well, that's how it is when you try do many things at once, but I believe I'll be able to get it all sorted out before too long."
    j "I am sure of that."

    scene day_06_scene_09_jennifer_7 with dissolve
    mc "How about you? Is Eric still bothering you?"
    j "Yes, but it's probably because I broke up with him this morning. I didn't have the strength to keep going, nothing good came of it and I wasn't happy with him at all."

    scene day_06_scene_09_jennifer_8 with dissolve
    mc "I still haven't managed to meet and have a talk with him. I've been to his house several times already, but so far no luck."
    j "Don't worry about him. Surely everything will be all right."

    scene day_06_scene_09_jennifer_9 with dissolve
    mc "I will keep trying. I can't leave that like this. He has to pay for what he did to you."
    j "You are so sweet. Thank you so much for taking care of me."

    scene day_06_scene_09_jennifer_10 with dissolve
    "{color=#D2691E}*Jennifer's serving dinner.*{/color}"
    mc "It looks and smells wonderful."
    j "Enjoy your meal."

    scene day_06_scene_09_jennifer_11 with dissolve
    "{color=#D2691E}*You are eating in silence. You enjoy every bite.*{/color}"

    menu compliment_the_dinner:

        "{color=#74B2F4}Tell her you liked the meal.{/color} [JenniferLovePath]":

            scene day_06_scene_09_jennifer_11 with dissolve
            mc "I have never eaten anything better in my life."

            scene day_06_scene_09_jennifer_12 with dissolve
            j "I am glad that you liked it."
            mc "Very much."

            scene day_06_scene_09_jennifer_13 with dissolve
            j "Would you like to take a walk?"

            $ jennifer_love += 1

            menu after_dinner:

                "{color=#74B2F4}Sure.{/color} [JenniferLovePath]":

                    scene day_06_scene_09_jennifer_13a with dissolve
                    mc "Sure."
                    j "Great. Maybe we could visit our old place?"
                    mc "That's a great idea."
                    $ jennifer_love += 1
                    jump the_walk_jennifer

                "{color=#74B2F4}I'd love to, but maybe another time.{/color}":

                    scene day_06_scene_09_jennifer_13b with dissolve
                    mc "I'm really sorry, but I have to go."
                    mc "Maybe next time."
                    j "Oh... what a shame..."

                    scene day_06_scene_09_jennifer_13c with dissolve
                    mc "Thank you for dinner."
                    mc "Bye."
                    j "Bye."
                    $ jennifer_love -= 5
                    jump day_06_scene_10

        "{color=#74B2F4}Thank you.{/color}":

            scene day_06_scene_09_jennifer_13 with dissolve
            j "Would you like to take a walk?"

            menu after_dinner1:

                "{color=#74B2F4}Sure.{/color} [JenniferLovePath]":

                    scene day_06_scene_09_jennifer_13a with dissolve
                    mc "Sure."
                    j "Great. Maybe we could visit our old place?"
                    mc "That's a great idea."
                    $ jennifer_love += 1
                    jump the_walk_jennifer

                "{color=#74B2F4}I'd love to, but maybe another time.{/color}":

                    scene day_06_scene_09_jennifer_13b with dissolve
                    mc "I'm really sorry, but I have to go."
                    mc "Maybe next time."
                    j "Oh... what a shame..."

                    scene day_06_scene_09_jennifer_13c with dissolve
                    mc "Thank you for dinner."
                    mc "Bye."
                    j "Bye."
                    $ jennifer_love -= 5
                    jump day_06_scene_10

label the_walk_jennifer:

    scene day_06_scene_09_jennifer_14 with dissolve
    "{color=#D2691E}*You walk slowly through the park talking about different things.*{/color}"

    scene day_06_scene_09_jennifer_14a with dissolve
    "{color=#D2691E}*You finally get to an almost invisible path between the trees.*{/color}"
    mc "I think this is it."
    j "Do you remember this place?"
    mc "Of course I do. We spent a lot of time here when we were kids. Are you sure you want to go there? We're a little overdressed."
    j " It doesn't matter. I want to see our place again."

    scene day_06_scene_09_jennifer_15a with dissolve
    "{color=#D2691E}*For a few minutes you walk among the trees. From a distance, you can hear the sound of water.*{/color}"
    j "It's beautiful here. I haven't been here since you left."
    j "Let's sit down for a while."

    scene day_06_scene_09_jennifer_16 with dissolve
    "{color=#D2691E}*You are sitting on a large flat stone. Jennifer leans her head against your shoulder.*{/color}"
    j "You know that you have always been more than just a friend to me?"
    mc "So have you."

    scene day_06_scene_09_jennifer_17 with dissolve
    j "I regret it so much that we couldn't grow up together. We lost so much time. And I was so terrible to you when you came back. I'm happy that you forgave me and that we could start anew."
    mc "I'm glad you're close to me again, too."

    scene day_06_scene_09_jennifer_18 with dissolve
    j "Could you tell me what happened that night, ten years ago?"
    mc "Yes, of course. You deserve to know the truth."

    scene day_06_scene_09_jennifer_19 with dissolve
    mc "It started right after you moved in. At first everything seemed normal. Linda and my father seemed happy."
    mc "But something felt off and wrong, so I tried to figure out what was really going."
    mc "I tried to find out what Linda was up to, and when I told my father everything I knew, he went and told her everything."

    scene day_06_scene_09_jennifer_20 with dissolve
    mc "He told her all my suspicions, and as you can probably guess, she didn't take that too well. She took matters into her own hands and started harassing me."
    mc "She argued with me about everything and it got worse every day."
    mc "One day I found out that one of my friends was dead. The case was strange and mysterious."

    scene day_06_scene_09_jennifer_21 with dissolve
    mc "The police determined that he had fallen off a cliff. However, they couldn't say whether it was murder or suicide."
    mc "They interrogated me several times, as well as my other friends. A few days after the incident, Linda came to me at night."
    mc "She told me that she saw me push me friend off the cliff and that the next morning she was going to tell that to the police."

    scene day_06_scene_09_jennifer_22 with dissolve
    mc "She also said that if I didn't want to spend the rest of my life behind bars, I should leave town and never come back."
    mc "That was obviously a bullshit lie. I had nothing to do with my friend's death, but it was clear to me that Linda had found a way to get rid of me for good."
    mc "I remember the mocking smile on her face when she left my room. I was in shock."

    scene day_06_scene_09_jennifer_23 with dissolve
    mc "I wasn't sure how far she would go or what nonsense she would tell the police."
    mc "I only had a few hours to make a decision. I didn't know what to do."
    mc "I was afraid that she would actually report me, that I would go to prison even though I hadn't done anything wrong."

    scene day_06_scene_09_jennifer_24 with dissolve
    mc "So I decided that I had no other choice. I packed a few things and wrote you a letter explaining everything because I couldn't find my phone anywhere."
    mc "She must've had taken it when she was in my room. I tried to get in touch with you, but with no success, she even deleted my e-mails."
    mc "The passwords were saved on my pc and probably that's why she had access to them."

    scene day_06_scene_09_jennifer_25 with dissolve
    mc "She cut me off from everything. I only remembered your phone number."
    mc "So, I called you about a million times, but you never answered. I was desperate, so I sent you letters, like, a hundred in all."
    mc "I already had a new phone at that time. So, I wrote to you where I live and gave you my new phone number. But you never called or wrote back."

    scene day_06_scene_09_jennifer_26 with dissolve
    mc "After a few months I gave up. And that's it. The whole story."

    scene day_06_scene_09_jennifer_27 with dissolve
    j "God, I can't believe what you're saying. All this time I couldn't allow myself to think that my mom could have something to do with all this."
    j "So Lisa was right all along. She always did believe you must've had a good reason to just up and leave and now it became clear that I wrongfully accused you of every bad thing. I'm so damn sorry."

    scene day_06_scene_09_jennifer_28 with dissolve
    j "You're saying you called me and I didn't answer. That's strange. I don't remember any phone calls."
    mc "How is that possible?"

    scene day_06_scene_09_jennifer_29 with dissolve
    j " Wait a second...I know... The same day when you disappeared, my mother came to me and said that you stole a lot of things when you ran away from home, including my phone."
    j "She gave me a new one, but the phone number changed...."

    scene day_06_scene_09_jennifer_30 with dissolve
    j "What a mean bitch.... How could she do that?"
    mc "Now everything makes sense."

    scene day_06_scene_09_jennifer_31 with dissolve
    mc "Now you understand why I want to take revenge on her? She took me away from you, my father, my home, my friends and my life."
    mc "It's getting late, I think we should head back."
    j "You are right."

    scene day_06_scene_09_jennifer_32 with dissolve
    "{color=#D2691E}*You're walking Jennifer home.*{/color}"
    mc "Thank you very much for a wonderful afternoon."

    scene day_06_scene_09_jennifer_33 with dissolve
    j "Thank you very much. It means a lot to me. Thank you for being honest with me and once again I apologize for everything."
    mc "Let's not talk about it anymore. The most important thing is that we are together again. The rest doesn't matter."
    j "You are right."

    menu kiss_jennifer:

        "{color=#74B2F4}Let her kiss you.{/color} [JenniferLovePath]":

            scene day_06_scene_09_jennifer_34 with dissolve
            "{color=#D2691E}*Jennifer kisses you goodbye.*{/color}"
            j "I'm so sorry, [player_name]. I shouldn't have kissed you..."
            mc "Don't worry, it's okay. I wanted you to, I liked it."
            "{color=#D2691E}*But Jennifer doesn't listen. Covering her face with her hands, she runs home.*{/color}"
            mc "Eh..."
            $ jennifer_love += 1
            $ jennifer_kiss_day_06 = True
            $ persistent.jennifer_kiss_day_06 = jennifer_kiss_day_06
            jump day_06_scene_10

        "{color=#74B2F4}Hug her.{/color}":

            scene day_06_scene_09_jennifer_34a with dissolve
            "{color=#D2691E}*You hug her.*{/color}"
            mc "See you tomorrow."
            j "Bye."

            jump day_06_scene_10

#####################################################################################################################################################
                                                #############SCENE 10 - Nicole taking photos#############
#####################################################################################################################################################

label day_06_scene_10:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname
        $ nicole_helped = persistent.nicole_helped

        show screen endreplay_button

    if nicole_helped == True:

        scene black with dissolve
        show bg in_the_meantime with dissolve
        $ renpy.pause ()

        scene day_06_scene_10_nicole_1 with dissolve
        "{color=#81F79F}*I'm sick and tired of this shit. This constant humiliation makes me sick.*{/color}"
        "{color=#81F79F}*I would like to finally get back my normal life.*{/color}"

        scene day_06_scene_10_nicole_2 with dissolve
        "{color=#81F79F}*I miss the smile, the joy of life. If only I could go back in time...*{/color}"
        "{color=#81F79F}*I was so naive.... I got involved in this shit and I don't know how to get out of that now.*{/color}"

        scene day_06_scene_10_nicole_3 with dissolve
        "{color=#81F79F}*Everyone moved away from me. Even my mother left me....*{/color}"
        "{color=#81F79F}*I don't know why I followed her example. Nothing good came of it.*{/color}"

        scene day_06_scene_10_nicole_4 with dissolve
        "{color=#81F79F}*But who will want to help me after everything I've done to my loved ones? Even my friends turned their backs on me and they don't want anything to do with me.*{/color}"
        "{color=#81F79F}*But can I blame them for that? After what I've done to them?*{/color}"
        "{color=#81F79F}*Only [player_name] is still showing any willingness to help me.*{/color}"

        scene day_06_scene_10_nicole_5 with dissolve
        "{color=#81F79F}*His speech made me think. Maybe he is right?*{/color}"
        "{color=#81F79F}*But will we be able to forgive each other and start over? It would be so great, I miss him so much.*{/color}"
        "{color=#81F79F}*I have to meet with him as soon as possible and try to talk to him honestly. Maybe we could at least improve our relationship a little bit.*{/color}"

        scene day_06_scene_10_nicole_6 with dissolve
        "{color=#81F79F}*And maybe then I could tell him everything that happened to me and ask for help.*{/color}"
        "{color=#81F79F}*I had his number somewhere.*{/color}"

        scene day_06_scene_10_nicole_7 with dissolve
        n "Hi, [player_name]. This is Nicole."
        mc "Hi. What's up?"

        scene day_06_scene_10_nicole_8 with dissolve
        n "I was thinking about what you told me today and I was wondering if you would find some time today to meet with me?"
        mc "Hmm. It could be tricky to find some free time today, but I will try."
        mc "But if I can't make it today, I'll be at your place tomorrow, so we can talk then if you still want to."

        scene day_06_scene_10_nicole_9 with dissolve
        n "Let me know if you find some time today. I will be at home whole evening anyway."
        mc "Okay, sure."
        n "What time will you be with us tomorrow?"

        scene day_06_scene_10_nicole_10 with dissolve
        mc "Around noon. I want to tell you all about something, so it would be good if you were home then."
        n "I will be there."
        mc "Great."

        scene day_06_scene_10_nicole_11 with dissolve
        n "It was nice to talk to you."
        mc "Thanks for the call."
        mc "Bye-bye."

        scene day_06_scene_10_nicole_12 with dissolve
        "{color=#81F79F}*Hmm. It wasn't that bad. He really seems to be honest with me. I can't fuck it up like always.*{/color}"
        "{color=#81F79F}*I sincerely hope that he will come to me today.*{/color}"

        scene day_06_scene_10_nicole_13 with dissolve
        "{color=#D2691E}*Nicole's lying on the bed for a while. A gentle smile appears on her face.*{/color}"

        scene day_06_scene_10_nicole_14 with dissolve
        "{color=#D2691E}*Unfortunately, she soon remembers the pictures she has to take and the smile disappears from her face.*{/color}"
        "{color=#81F79F}*Now I have to take the fucking pictures.*{/color}"
        "{color=#81F79F}*I hate that fucking cocksucker.*{/color}"

        scene day_06_scene_10_nicole_15 with dissolve
        "{color=#81F79F}*I have to humiliate myself for him again.*{/color}"
        "{color=#81F79F}*How can he be so ruthless to me?*{/color}"

        scene day_06_scene_10_nicole_16 with dissolve
        "{color=#D2691E}*Nicole undresses and lies down on the bed. She sets up a camera and takes the dildo.*{/color}"
        "{color=#81F79F}*Let's get this over with.*{/color}"

        scene day_06_scene_10_nicole_17 with dissolve
        "{color=#FF69B4}*She opens her legs wide. She starts slowly massaging her clitoris. Her pussy gets wet. She moves the dildo up and down.*{/color}"

        scene day_06_scene_10_nicole_18 with dissolve
        "{color=#FF69B4}*She tilts the vulva weights and slowly puts the dildo into her wet pussy.*{/color}"

        scene day_06_scene_10_nicole_19 with dissolve
        "{color=#FF69B4}*Initial anger subsides and Nicole starts moaning quietly with pleasure.*{/color}"

        scene day_06_scene_10_nicole_20 with dissolve
        "{color=#FF69B4}*She pushes the dildo deeper and deeper into her tight pussy.*{/color}"

        scene day_06_scene_10_nicole_21 with dissolve
        "{color=#FF69B4}*She caresses her breast with her free hand and plays with her swollen nipple.*{/color}"

        scene day_06_scene_10_nicole_22 with dissolve
        "{color=#FF69B4}*Nicole tightens her muscles to make her tight pussy even tighter.*{/color}"

        scene day_06_scene_10_nicole_23 with dissolve
        "{color=#FF69B4}*Her moves are getting faster and faster.*{/color}"

        scene day_06_scene_10_nicole_24 with dissolve
        "{color=#FF69B4}*Her body is resilient in delight. The girl leans her head back and moans louder and louder.*{/color}"
        "{color=#FF69B4}*Finally, a wave of warmth and pleasure spreads over her body.*{/color}"

        scene day_06_scene_10_nicole_25 with flash
        with flash
        with flash

        scene day_06_scene_10_nicole_26 with dissolve
        "{color=#FF69B4}*She pulls the dildo out of her pussy and turns off the camera.*{/color}"
        n "Fuck... I got carried away again."

        scene day_06_scene_10_nicole_27 with dissolve
        "{color=#D2691E}*Nicole starts sobbing.*{/color}"
        n "What should I do to get rid of this bastard?"

        scene day_06_scene_10_nicole_28 with dissolve
        n "[player_name] is my only hope. If he won't help me, then no one will."

        $ renpy.end_replay()

        jump day_06_scene_11

    else:

        scene day_06_scene_10_nicole_29 with dissolve
        "{color=#81F79F}*Every man's a fucking pig.*{/color}"
        "{color=#81F79F}*How can he treat a woman like this, what am I, a doll or something?*{/color}"

        scene day_06_scene_10_nicole_30 with dissolve
        "{color=#81F79F}*What's that dickhead thinking?*{/color}"
        "{color=#81F79F}*Someday I'll finally get him and rip off his fucking dick and his balls.*{/color}"

        scene day_06_scene_10_nicole_31 with dissolve
        "{color=#D2691E}*Nicole takes off her clothes and puts them on the floor.*{/color}"
        "{color=#81F79F}*What am I gonna do with [player_name]? I need his help because where else would I get the money by tomorrow?*{/color}"
        "{color=#81F79F}*I'm so fucked.*{/color}"

        scene day_06_scene_10_nicole_32 with dissolve
        "{color=#81F79F}*How am I supposed to come up with a way to punish myself...*{/color}"
        "{color=#81F79F}*And what am I supposed to do?*{/color}"

        scene day_06_scene_10_nicole_33 with dissolve
        "{color=#81F79F}*It would be easier if he told me to do something, but no... why make my life easier.*{/color}"
        "{color=#81F79F}*Dickhead...*{/color}"

        scene day_06_scene_10_nicole_34 with dissolve
        "{color=#81F79F}*Focus. Whining won't help me. I have to convince [player_name] that I'm serious about what he told me.*{/color}"
        "{color=#81F79F}*Maybe it won't be that bad, though, because what could be worse than putting a dildo up your ass and taking pictures for some fat, disgusting pervert....*{/color}"

        scene day_06_scene_10_nicole_35 with dissolve
        "{color=#81F79F}*[player_name] probably wants to teach me a lesson but once I've proven to him that I care, then maybe he'll help me and we'll get rid of this blackmailer.*{/color}"
        "{color=#81F79F}*Oh, fuck. I can't think of anything.... Maybe I'll just show him my tits....*{/color}"
        "{color=#81F79F}*Eh. I'll think about it, and now you have to take those fucking pictures.*{/color}"

        scene day_06_scene_10_nicole_36 with dissolve
        "{color=#FF69B4}*Nicole pulls out a dildo and a lube. She sets up a camera.*{/color}"

        scene day_06_scene_10_nicole_37 with dissolve
        "{color=#FF69B4}*She lubricates her anus with a lube and slowly starts putting the dildo up her ass.*{/color}"

        scene day_06_scene_10_nicole_38 with dissolve
        "{color=#FF69B4}*Oh, Jesus... It's too big... Why didn't I buy a smaller dildo...?*{/color}"
        "{color=#FF69B4}*Nicole clenches her teeth in pain, as she inch by inch inserts the dildo deeper in her ass.*{/color}"

        scene day_06_scene_10_nicole_39 with dissolve
        "{color=#FF69B4}*Her tight hole is slowly getting used to the size of a dildo.*{/color}"

        scene day_06_scene_10_nicole_40 with dissolve
        "{color=#FF69B4}*Nicole starts moving it backwards and forwards in slow motion.*{/color}"

        scene day_06_scene_10_nicole_41 with dissolve
        "{color=#FF69B4}*The pain slowly disappears and Nicole starts to feel the pleasure.*{/color}"

        scene day_06_scene_10_nicole_42 with dissolve
        "{color=#FF69B4}*But after a while, she starts to get carried away with the pleasure she's starting to feel and moans quietly.*{/color}"

        scene day_06_scene_10_nicole_43 with dissolve
        "{color=#FF69B4}*She reaches down to her now wet pussy and starts rubbing her clitoris.*{/color}"

        scene day_06_scene_10_nicole_44 with dissolve
        "{color=#FF69B4}*Her moans become louder and louder, and the dildo slips deeper and faster into her ass.*{/color}"

        scene day_06_scene_10_nicole_45 with dissolve
        "{color=#FF69B4}*Nicole feels the orgasm coming. She puts two fingers in her juice-dripping pussy and starts to fingering herself.*{/color}"
        "{color=#FF69B4}*After all, her body is shaken by spasms of pleasure. A heat wave spreads all over her body.*{/color}"

        scene day_06_scene_10_nicole_46 with flash
        with flash
        with flash

        scene day_06_scene_10_nicole_47 with dissolve
        "{color=#FF69B4}*Nicole makes a loud and long moan and falls on the bed.*{/color}"
        n "Fuck... I got carried away again."

        scene day_06_scene_10_nicole_48 with dissolve
        "{color=#D2691E}*Nicole starts sobbing.*{/color}"
        n "What should I do to get rid of this bastard?"
        n "[player_name] is my only hope. If he won't help me, then no one will."

        $ renpy.end_replay()

        jump day_06_scene_11

#####################################################################################################################################################
                                            #############SCENE 11 - MC and Lisa#############
#####################################################################################################################################################

label day_06_scene_11:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene expression "day_06_scene_11_lisa_1[hair]" with dissolve
    l "Hi, [player_name]."
    mc "Hi, sweetheart."
    l "I have a great desire to meet you today."
    mc "Yeah, sure. I would love to."
    l "'Pink Rabbit' in an hour?"
    mc "Sounds great."
    mc "Do you want me to pick you up?"
    l "No. I'll take a taxi."
    mc "Okay, I'll be waiting."

    scene expression "day_06_scene_11_lisa_2[hair]" with dissolve
    l "I think I should wear something sexy. But what? I don't have anything like that. I'm not going to go in underwear."
    l "Hmm...Maybe that dress I bought this morning?"

    scene expression "day_06_scene_11_lisa_3[hair]" with dissolve
    "{color=#D2691E}*Lisa is changing her clothes.*{/color}"
    l "I can't find anything better."

    scene black with dissolve
    show bg one_hour_later with dissolve
    $ renpy.pause ()

    scene expression "day_06_scene_11_lisa_4[hair]" with dissolve
    "{color=#D2691E}*You arrived early so you went inside the club to wait for Lisa. A few moments later she arrives.*{/color}"

    menu compliment_lisa:

        "{color=#74B2F4}Compliment her.{/color} [LisaLovePath]":

            scene expression "day_06_scene_11_lisa_4a[hair]" with dissolve
            mc "Oh, my God, Lisa... You look so beautiful..."

            scene expression "day_06_scene_11_lisa_5[hair]" with dissolve
            "{color=#D2691E}*Lisa is smiling at you flirtatiously.*{/color}"
            l "I was hoping you would say that."
            mc "How are you doing, sweetheart?"

            $ lisa_love += 1

        "{color=#74B2F4}Ask her how she is doing.{/color}":

            scene expression "day_06_scene_11_lisa_5[hair]" with dissolve
            mc "How are you doing, sweetheart?"

    scene expression "day_06_scene_11_lisa_6[hair]" with dissolve
    l "I'm fine, but I missed you so much."
    mc "I missed you too. I haven't really found time to do much anything lately, there has been too many things I've needed to deal with."

    scene expression "day_06_scene_11_lisa_7[hair]" with dissolve
    l "I know and I understand. You don't have to worry about that."
    mc "You're wonderful. You know that?"
    l "Stop it..."

    scene expression "day_06_scene_11_lisa_8[hair]" with dissolve
    mc "Do you have any plans for tomorrow?"
    l "Yeah, I'll be busy until noon. I have to meet up with Rachel and Amy, but after that I'm available."
    mc "I'd like to meet with you tomorrow, I mean with you, Jennifer and Nicole."

    scene expression "day_06_scene_11_lisa_9[hair]" with dissolve
    l "Is something wrong?"
    mc "No, I just need to talk to you."
    l "Should I talk to my sisters?"

    scene expression "day_06_scene_11_lisa_10[hair]" with dissolve
    mc "Jennifer already knows, because I saw her today. But maybe you could pass on the information to Nicole?"
    l "Sure, I can try, but I can't promise anything."
    mc "I'll send her a message just in case."

    scene expression "day_06_scene_11_lisa_11[hair]" with dissolve
    l "How did things go with Jennifer last night? She's not so mad at you anymore?"
    mc "We had a lovely dinner, and then we went for a walk in the park. We even went to our old place by the pond."

    scene expression "day_06_scene_11_lisa_12[hair]" with dissolve
    mc "We stayed there for quite a while, talking. Jennifer was finally ready to hear me out and listen to what I had to say. I told her what really happened all those years ago."
    mc "We cuddled for a while. It was all very lovely, had a wonderful time."

    scene expression "day_06_scene_11_lisa_13[hair]" with dissolve
    l "Well, that's great..."
    mc "What's wrong? Did something upset you?"

    scene expression "day_06_scene_11_lisa_14[hair]" with dissolve
    "{color=#D2691E}*She looks at you intently and takes a deep breath.*{/color}"
    l "There is something I want to tell you, but I don't know how."

    scene expression "day_06_scene_11_lisa_15[hair]" with dissolve
    mc "You know you can tell me anything, don't be afraid. Just tell me what's on your mind."
    l "Okay."

    scene expression "day_06_scene_11_lisa_16[hair]" with dissolve
    "{color=#D2691E}*Lisa takes deep breath and starts talking.*{/color}"
    l "When we were children, you were like a brother to me. I loved you with all my heart and was ready to do everything for you."
    l "I know that it may sounds idiotic, because what could a kid know about life, but believe me, I did."

    scene expression "day_06_scene_11_lisa_17[hair]" with dissolve
    l "The fact that you left us broke my heart, but all this time I strongly believed that one day you would come back and we would be together again."
    l "You could say that you became my obsession. I imagined that you were coming back, that you were with me again. With time, I began to think about you in a more intimate way."

    scene expression "day_06_scene_11_lisa_18[hair]" with dissolve
    l "I dreamt of you being my boyfriend. At school a few boys tried to date me, but I always refused because they weren't even close to be as good as you were."
    l "Now that you've finally come back... I was hoping my dreams would come true."

    scene expression "day_06_scene_11_lisa_19[hair]" with dissolve
    mc "Listen to me carefully. You are and always have been very important to me. So have your sisters. Even Nicole, who is acting just like your mother and is being real cold toward me."
    mc "I have made many mistakes in my life. One of them was leaving you ten years ago, but I can't change that now."

    scene expression "day_06_scene_11_lisa_20[hair]" with dissolve
    mc "I am trying to prove to you all that I still care about you."
    l "I know you do."
    mc "Listen, you were honest with me and you told me about your feelings. I have something to tell you, too."

    scene expression "day_06_scene_11_lisa_21[hair]" with dissolve
    "{color=#D2691E}*Lisa looks scared.*{/color}"
    l "...Okay..."
    mc "During those years when I wasn't here, a lot of things happened. Nevertheless, you have been, are and always will be very important to me."
    mc "I have loved you with all my heart since I can remember."

    scene expression "day_06_scene_11_lisa_22[hair]" with dissolve
    "{color=#D2691E}*You can feel Lisa shaking your hand tighter and her fingernails sticking into your body.*{/color}"
    mc "A few years ago, I met a girl. Her name was Khloe. Fate wanted me to save her life. This fact connected us to each other and with time we fell in love with each other."
    mc "Some time later I met another girl, Mary, in even more dramatic circumstances."

    scene expression "day_06_scene_11_lisa_23[hair]" with dissolve
    "{color=#D2691E}*You look at Lisa and see how she struggles to stop tears coming to her eyes.*{/color}"
    "{color=#D2691E}*But you can't back out now. You have to tell her the whole truth.*{/color}"

    scene expression "day_06_scene_11_lisa_24[hair]" with dissolve
    mc "She fell in love with me... but I couldn't be with her because I was still dating Khloe."
    mc "Mary suffered for a long time because she couldn't be with me, and I couldn't stand it."
    mc "One day Khloe, seeing what was happening and how it affected all of us, proposed to me and Mary that the three of us create a relationship so that none of us suffer any longer."

    scene expression "day_06_scene_11_lisa_25[hair]" with dissolve
    mc "At first it seemed ridiculous, but we decided to try. And for four years we have been together, happy."
    mc "You're probably wondering why I'm telling you all this stuff."

    menu confession_lisa_proposal:

        "{color=#74B2F4}Consider becoming part of our relationship.{/color} [LisaHaremPath]":

            scene expression "day_06_scene_11_lisa_26[hair]" with dissolve
            mc "First of all, I don't want to have any secrets with you. I don't want to lie to you. Secondly, I love you as much as you love me and I can't imagine living without you."
            mc "But I'm not alone and I can't leave Khloe and Mary even for you. It wouldn't be fair to any of you."
            mc "I am also telling you about all this because I know that what we have created with Khloe and Mary works and it's wonderful."

            scene expression "day_06_scene_11_lisa_27[hair]" with dissolve
            mc "I know it's hard for you to believe me right now, but it's the truth."
            mc "I'm also telling you this because I would love to be with you, share my joys and sorrows with you."
            mc "And I would like to ask you to consider becoming part of our relationship, instead of hating me now."

            scene expression "day_06_scene_11_lisa_28[hair]" with dissolve
            "{color=#D2691E}*For a very long time, none of you say a word. You are staring at each other. You see how Lisa fights with her thoughts, how her emotions bargain with her.*{/color}"
            l "I'm glad you told me all about that. It's good that you're not lying to me. I am grateful to you for that."
            l "You're special to me. I can't explain or justify it. That's just the way it is."

            scene expression "day_06_scene_11_lisa_29[hair]" with dissolve
            l "I don't know what to think about all this. I didn't expect anything like that."
            l "I need to think about it all, put it all in my head."
            mc "I understand you. I know it's not easy and it's not what you expected."

            scene expression "day_06_scene_11_lisa_30[hair]" with dissolve
            "{color=#D2691E}*Lisa gets up.*{/color}"
            l "I'm gonna go now. It's getting late."

            scene expression "day_06_scene_11_lisa_31[hair]" with dissolve
            "{color=#D2691E}*You get up and walk up to her. You put your arms around her and hold her tightly.*{/color}"
            "{color=#D2691E}*For a split second you feel that Lisa wants to free herself from your embrace, but eventually she relaxes.*{/color}"

            scene expression "day_06_scene_11_lisa_32[hair]" with dissolve
            mc "{color=#AFEEEE}*you whisper in her ear*{/color=#AFEEEE} I love you...and I'm really sorry if what I told you hurt you or broke your heart."
            l "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} I love you, too... I wish I could finally be with you."
            mc "{color=#AFEEEE}*you whisper*{/color=#AFEEEE} Think about what I told you. Maybe there is hope for us."

            scene expression "day_06_scene_11_lisa_33[hair]" with dissolve
            l "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} I won't give up this easily. I've waited for you for too long to give up now without a fight."
            l "{color=#AFEEEE}*she whispers*{/color=#AFEEEE} I don't know what decision I'm gonna make..."
            mc "{color=#AFEEEE}*you whisper*{/color=#AFEEEE} I'm sure it will be the right one."
            l "I'll see you around."

            scene expression "day_06_scene_11_lisa_34[hair]" with dissolve
            "{color=#D2691E}*Lisa kisses you and runs out of the bar.*{/color}"
            $ lisa_love += 2
            $ lisa_proposal = True

            jump day_06_scene_12

        "{color=#74B2F4}I can't leave Khloe and Mary.{/color} [EndRelationship]":

            scene expression "day_06_scene_11_lisa_26[hair]" with dissolve
            mc "I don't want to have any secrets with you and I couldn't lie to you."
            mc "Lisa...I'm still dating both of them and I can't leave Khloe and Mary even for you. It wouldn't be fair to any of you."

            scene expression "day_06_scene_11_lisa_28[hair]" with dissolve
            "{color=#D2691E}*For a very long time, none of you say a word. You are staring at each other. You see how Lisa fights with her thoughts, how her emotions bargain with her.*{/color}"
            l "I'm glad you told me all about that. It's good that you're not lying to me. I am grateful to you for that."
            l "You're special to me. I can't explain or justify it. That's just the way it is."

            scene expression "day_06_scene_11_lisa_29[hair]" with dissolve
            l "I don't know what to think about all this. I didn't expect anything like that."
            l "I need to think about it all, put it all in my head."
            mc "I understand you. I know it's not easy and it's not what you expected."

            scene expression "day_06_scene_11_lisa_30[hair]" with dissolve
            "{color=#D2691E}*Lisa gets up.*{/color}"
            l "I'm gonna go now. It's getting late."
            $ lisa_love -= 20

            jump day_06_scene_12

#####################################################################################################################################################
                                                #############SCENE 12 - Mc and Amy#############
#####################################################################################################################################################

label day_06_scene_12:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_12_amy_1 with dissolve
    "{color=#D2691E}*It's been an hour since Lisa left.*{/color}"
    "{color=#D2691E}*You're still sitting in the bar and sipping a drink wondering what happened.*{/color}"

    scene day_06_scene_12_amy_2 with dissolve
    "{color=#D2691E}*A moment later you hear some loud chattering so you look to the direction where the voices come from.*{/color}"
    "{color=#D2691E}*You see two girls sitting by their table and two guys talking to them. *{/color}"

    scene day_06_scene_12_amy_3 with dissolve
    "{color=#D2691E}*The music coming from the speakers drowns out their conversation, but you can clearly see that something is wrong.*{/color}"
    "{color=#D2691E}*The other guy grabs the girl whose back is facing you and starts pulling her.*{/color}"

    menu react:

        "{color=#74B2F4}React.{/color} [AmyLovePath] [RachelLovePath]":

            scene day_06_scene_12_amy_4 with dissolve
            "{color=#D2691E}*You get up and walk up to them.*{/color}"
            guy "Come on. Just one dance."
            girl1 "Let me go!"

            scene day_06_scene_12_amy_5 with dissolve
            guy1 "We'll have some fun."
            girl2 "Fuck off."
            guy "How cocky."

            scene day_06_scene_12_amy_6 with dissolve
            mc "Leave these ladies alone. Clearly they don't want your company."
            guy1 "Get the fuck out of here."

            scene day_06_scene_12_amy_7 with dissolve
            mc "Please leave them alone."
            guy1 "And I tell you, fuck off, or..."

            scene day_06_scene_12_amy_8 with dissolve
            "{color=#D2691E}*The girls get out of the booth to get away from the jerks.*{/color}"
            mc "Or what?"
            guy "Or we'll have fun with you first, and then with these ladies."
            guy1 "Apparently somebody has problems with hearing here."

            scene day_06_scene_12_amy_9 with dissolve
            "{color=#D2691E}*One of them is trying to hit you, but you're dodging his attack.*{/color}"

            scene day_06_scene_12_amy_10 with dissolve
            "{color=#D2691E}*You bring out a quick counter and hit him in the stomach.*{/color}"

            scene day_06_scene_12_amy_10a with dissolve
            "{color=#D2691E}*He falls on the floor.*{/color}"

            scene day_06_scene_12_amy_10b with dissolve
            "{color=#D2691E}*The other guy tries to kick you, but you easily block the kick.*{/color}"

            scene day_06_scene_12_amy_10c with dissolve
            "{color=#D2691E}*You kick him in the balls with a strong blow.*{/color}"

            scene day_06_scene_12_amy_11 with dissolve
            "{color=#D2691E}*The guy bends in half and slides to the floor.*{/color}"

            scene day_06_scene_12_amy_12 with dissolve
            mc "Get your friend and get the fuck out of here."

            scene day_06_scene_12_amy_13 with dissolve
            mc "Are you okay?"
            girl1 "Yes. Thank you."
            mc "That's good. Have a good evening."

            scene day_06_scene_12_amy_14 with dissolve
            "{color=#D2691E}*You turn around, go back to your table and finish your drink.*{/color}"

            scene day_06_scene_12_amy_15 with dissolve
            "{color=#D2691E}*A few minutes later you leave the club.*{/color}"

            scene day_06_scene_12_amy_16 with dissolve
            "{color=#D2691E}*You're slowly walking up toward your car parked near the club entrance, but suddenly you're confronted by a well-built guy.*{/color}"
            "{color=#D2691E}*A few steps behind him you see the two guys you beat up inside the club only a moment ago.*{/color}"

            scene day_06_scene_12_amy_17 with dissolve
            "{color=#D2691E}*Without a single word the stranger assumes a fighting stance. His face is knotted and teeth clenched. Slowly he starts circling around you.*{/color}"
            "{color=#D2691E}*You also assume your fighting stance and wait for him to make the first move.*{/color}"

            scene day_06_scene_12_amy_18 with dissolve
            "{color=#D2691E}*The stranger's face sheds its mask of calm with a scream.*{/color}"
            man "What are you waiting for?"

            scene day_06_scene_12_amy_19 with dissolve
            "{color=#D2691E}*You take off your jacket and remain calm and wait.*{/color}"

            scene day_06_scene_12_amy_20 with dissolve
            "{color=#D2691E}*This is more than enough for the attacker. He charges with a powerful strike.*{/color}"

            scene day_06_scene_12_amy_21 with dissolve
            "{color=#D2691E}*You take a step back and easily avoid the punch. Surprised by this and missing the punch, the guy loses his balance for a brief moment.*{/color}"

            scene day_06_scene_12_amy_22 with dissolve
            "{color=#D2691E}*You seize the moment and connect his jaw with your powerful right hand, following it up with an uppercut to the liver that causes him to cringe.*{/color}"

            scene day_06_scene_12_amy_23 with dissolve
            "{color=#D2691E}*The thug loses his breath and falls to the ground. Blood is leaking from his smashed lip.*{/color}"
            "{color=#D2691E}*You stand a few steps away from him and wait.*{/color}"

            scene day_06_scene_12_amy_24 with dissolve
            "{color=#D2691E}*A moment later the guy gets back up on his feet.*{/color}"
            "{color=#D2691E}*He spits blood on the ground.*{/color}"

            scene day_06_scene_12_amy_25 with dissolve
            "{color=#D2691E}*Suddenly he explodes with an upswing hook to your jaw but you dodge it easily.*{/color}"

            scene day_06_scene_12_amy_26 with dissolve
            "{color=#D2691E}*You throw a devastating blow to the side of his head.*{/color}"
            "{color=#D2691E}*Blood sprays over your shirt.*{/color}"

            scene day_06_scene_12_amy_27 with dissolve
            man "Come on, sucker. That's all you've got?"
            "{color=#D2691E}*You smirk.*{/color}"

            scene day_06_scene_12_amy_28 with dissolve
            "{color=#D2691E}*The man charges again but this time with less energy and power.*{/color}"
            "{color=#D2691E}*You block his attack with ease.*{/color}"

            scene day_06_scene_12_amy_29 with dissolve
            "{color=#D2691E}*You drop low and connect a couple of powerful body shots, one punch hitting his diaphragm, knocking all the air out.*{/color}"

            scene day_06_scene_12_amy_30 with dissolve
            "{color=#D2691E}*He loses his breath and bends in half.*{/color}"
            "{color=#D2691E}*You kick him in the face with your knee and the man falls to the ground unconscious.*{/color}"

            scene day_06_scene_12_amy_31 with dissolve
            "{color=#D2691E}*The fight is over.*{/color}"

            scene day_06_scene_12_amy_32 with dissolve
            "{color=#D2691E}*You look around, but the other two guys are nowhere to be seen.*{/color}"

            scene day_06_scene_12_amy_33 with dissolve
            "{color=#D2691E}*You only see two girls standing near the entrance to the club and looking at the whole scene in horror.*{/color}"
            "{color=#D2691E}*They're the same girls you helped before.*{/color}"
            girl1 "Are you okay?"
            mc "Everything's fine."

            scene day_06_scene_12_amy_34 with dissolve
            "{color=#D2691E}*The girls are coming to you.*{/color}"
            girl1 "[player_name] [player_surname]?"
            mc "Yes, and you are?"

            scene day_06_scene_12_amy_35 with dissolve
            girl1 "It's me, Amy."
            girl1 "We met at your office few days ago."
            mc "Ah, yes. I'm sorry. I didn't recognize you."
            amy "It's okay. This is my friend Rachel."

            scene day_06_scene_12_amy_36 with dissolve
            r "Finally I've got the chance to meet you, just a shame it's under these circumstances."
            r "Lisa has told me a lot about you."
            mc "Ah, Rachel, Lisa's best friend."

            scene day_06_scene_12_amy_37 with dissolve
            mc "Nice to meet you too."
            mc "Come on, I'll take you home."

            scene day_06_scene_12_amy_38 with dissolve
            "{color=#D2691E}*You get in the car.*{/color}"
            r "We're very grateful for your help. I don't even want to imagine how things could've turned out if you didn't come help us."
            amy "Yes, we're also very sorry that you had to fight them because of us."

            scene day_06_scene_12_amy_39 with dissolve
            mc "Don't mention it, it was no problem at all."
            mc "The important thing is that nothing happened to you."
            r "We have to make it up to you somehow."

            scene day_06_scene_12_amy_40 with dissolve
            mc "It's really not necessary."
            amy "We insist."
            mc "All right, but maybe some other time."

            scene day_06_scene_12_amy_41 with dissolve
            r "We won't let you off the hook that easy."
            r "Tomorrow night we'll take you out for a drink."

            menu amy_rachel_date:

                "{color=#74B2F4}Don't agree.{/color}":

                    scene day_06_scene_12_amy_42 with dissolve
                    mc "I really can't."
                    r "All right, but if you change your mind, let me know."
                    mc "Okay."
                    mc "So, where are we going?"

                    scene day_06_scene_12_amy_43 with dissolve
                    "{color=#D2691E}*Amy gives you her address. The whole way to Amy's house, the girls are excitedly talking about how you handled those thugs.*{/color}"
                    "{color=#D2691E}*15 minutes later you park the car outside a small house.*{/color}"

                    scene day_06_scene_12_amy_44 with dissolve
                    amy "Thank you very much again for your help."
                    mc "Be careful and have a good night."
                    r "Good night."

                    jump day_06_scene_13

                "{color=#74B2F4}Agree.{/color} [AmyLovePath] [RachelLovePath]":

                    scene day_06_scene_12_amy_42 with dissolve
                    mc "All right."
                    r "I'll call you tomorrow to let you know when and where we'll meet."
                    mc "Fine."
                    mc "So, where are we going?"

                    scene day_06_scene_12_amy_43 with dissolve
                    "{color=#D2691E}*Amy gives you the address. All the way, the girls are excited about how you handled those thugs.*{/color}"
                    "{color=#D2691E}*15 minutes later you park the car outside a small house.*{/color}"

                    scene day_06_scene_12_amy_45 with dissolve
                    r "Your phone number, please."

                    scene day_06_scene_12_amy_46 with dissolve
                    "{color=#D2691E}*You give your number to the girls.*{/color}"
                    r "Well, then we have a date tomorrow."
                    amy "Thank you very much again for your help."
                    mc "Be careful and have a good night."
                    $ amy_love += 2
                    $ rachel_love += 2
                    $ amy_rachel_date = True

                    jump day_06_scene_13

        "{color=#74B2F4}Don't react.{/color}":

            scene day_06_scene_12_amy_14 with dissolve
            "{color=#D2691E}*In your first instinct you want to intervene, but you're too tired.*{/color}"
            "{color=#D2691E}*Besides, you've had enough of your problems, and you realize that you don't need another problem at all.*{/color}"
            "{color=#D2691E}*You finish a drink and leave the club.*{/color}"

            jump day_06_scene_13

#####################################################################################################################################################
                                            #############SCENE 13 - Jennifer and Lisa#############
#####################################################################################################################################################
label day_06_scene_13:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause ()

    scene day_06_scene_13_jennifer_lisa_scene_1 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{color=#D2691E}"
    j "Lisa? Can I come in?"

    scene expression "day_06_scene_13_jennifer_lisa_scene_2[hair]" with dissolve
    "{color=#D2691E}*But Lisa doesn't answer so Jennifer opens the door slowly and walks into the room.{/color}"

    scene expression "day_06_scene_13_jennifer_lisa_scene_3[hair]" with dissolve
    j "Lisa?"

    scene expression "day_06_scene_13_jennifer_lisa_scene_4[hair]" with dissolve
    "{color=#D2691E}*Jennifer walks closer to Lisa's bed.*{/color}"
    j "Lisa?"

    scene expression "day_06_scene_13_jennifer_lisa_scene_5[hair]" with dissolve
    "{color=#D2691E}*Jennifer lies on the bed next to her sister.*{/color}"
    j "Lisa?"

    scene expression "day_06_scene_13_jennifer_lisa_scene_6[hair]" with dissolve
    "{color=#D2691E}*In her sleep, Lisa mumbles something, then changes her position and hugs her sister.*{/color}"
    l "...[player_name]...hold me tight...."

    scene expression "day_06_scene_13_jennifer_lisa_scene_7[hair]" with dissolve
    "{color=#D2691E}*Lisa cuddles up to her sister.*{/color}"

    if lisa_masturbate == True:

        scene day_06_scene_13_jennifer_lisa_scene_8 with dissolve
        "{color=#D2691E}*Suddenly Jennifer feels her sister's leg pressing against her crotch. A heat wave spreads over her body.*{/color}"
        j "It feels good..."

        scene expression "day_06_scene_13_jennifer_lisa_scene_9[hair]" with dissolve
        "{color=#D2691E}*Jennifer closes her eyes and slowly starts rubbing her pussy against her sister's thigh.*{/color}"
        "{color=#FF69B4}*A quiet moan comes out of her mouth.*{/color=#FF69B4}"

        scene expression "day_06_scene_13_jennifer_lisa_scene_10[hair]" with dissolve
        "{color=#FF69B4}*Lisa's breasts touch her breasts. Jennifer is getting more and more horny.*{/color=#FF69B4}"

        scene day_06_scene_13_jennifer_lisa_scene_11 with dissolve
        "{color=#FF69B4}*As she rubs against her sister's thigh, she starts playing with her clitoris.*{/color=#FF69B4}"
        "{color=#FF69B4}*More and more loud moans of pleasure come out of her mouth. Every muscle in her body is stretched to its limits in anticipation of the coming wave of pleasure.*{/color=#FF69B4}"

        scene expression "day_06_scene_13_jennifer_lisa_scene_12[hair]" with dissolve
        "{color=#FF69B4}*Jennifer's body starts to tremble. Her body is shaken by spasms of pleasure. An unimaginable pleasure.*{/color=#FF69B4}"
        "{color=#FF69B4}*Jennifer lies still breathing loudly and tries to recover from the best orgasm she's ever had.*{/color=#FF69B4}"

        scene expression "day_06_scene_13_jennifer_lisa_scene_13[hair]" with dissolve
        "{color=#FF69B4}*A thought runs through her mind.*{/color=#FF69B4}"
        j "Jesus, what am I doing? How could I?"

        scene expression "day_06_scene_13_jennifer_lisa_scene_14[hair]" with dissolve
        "{color=#D2691E}*Jennifer slowly turns her head toward her sister and freezes of horror.*{/color}"
        l "I see you're having fun with yourself."

        scene expression "day_06_scene_13_jennifer_lisa_scene_15[hair]" with dissolve
        j "I'm sorry, sister. I don't know what's gotten into me."
        l "Oh, stop it. It was an interesting experience."

        scene expression "day_06_scene_13_jennifer_lisa_scene_16[hair]" with dissolve
        j "I am so ashamed..."
        l "Why? You have nothing to be ashamed of."

        scene expression "day_06_scene_13_jennifer_lisa_scene_17[hair]" with dissolve
        l "It was nice to see you enjoying yourself. Next time try not to crush my leg."
        j "Jesus, I'm sorry."
        l "Stop it at last."
        l "Come on. Give me a hug."

        scene expression "day_06_scene_13_jennifer_lisa_scene_18[hair]" with dissolve
        "{color=#D2691E}*Lisa slowly move closer to Jennifer and lean over her. She gently kisses her sister. Jennifer does not protest, but kisses back after a while. The smile appears on their faces.*{/color}"
        l "Good night, dear."
        j "Good night, Lisa."
        $ FileSave(6, confirm=False)()

        jump end_of_day_6

    else:

        scene expression "day_06_scene_13_jennifer_lisa_scene_19[hair]" with dissolve
        "{color=#D2691E}*Jennifer kisses Lisa on the forehead and falls asleep.*{/color}"
        $ FileSave(6, confirm=False)()

        jump end_of_day_6

#####################################################################################################################################################

label end_of_day_6:

    scene black with dissolve
    show end_of_day_06 with dissolve
    $ renpy.pause ()

    jump day_07
