label day_08:

    $ day = "Day 8"
    $ save_name = "Day 8"

#####################################################################################################################################################
                                                    #############PROLOGUE - CLARA'S DECISIONS##################   done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_00:

    scene black with dissolve
    show bg day_08 with Dissolve(2)
    $ renpy.pause ()

    if clara_spanking == True:

        scene day_08_scene_00_clara_1 with dissolve
        $ renpy.pause()

        scene day_08_scene_00_clara_3 with dissolve
        c "Oh, yes [player_name]. Spank me!"

        scene day_08_scene_00_clara_4 with dissolve
        c "Yes, just like that."
        c "Harder!"

        scene day_08_scene_00_clara_5 with dissolve
        $ renpy.pause ()

        scene black with fade
        pause 1.0

        scene day_08_scene_00_clara_6 with dissolve
        "{color=#D2691E}*The sound of the alarm clock is tearing Clara out of her sleep.*{/color}"

        scene day_08_scene_00_clara_6a with dissolve
        c "Fuckin' alarm clock."
        c "Such a beautiful dream..."

        scene day_08_scene_00_clara_7 with dissolve
        "{color=#D2691E}*Clara lies in bed staring at the ceiling.*{/color}"
        c "I wonder how far [player_name] could go."
        c "Just the thought of his hard hand on my bottom gives me shivers."

        scene day_08_scene_00_clara_8 with dissolve
        c "Maybe it would be worth checking it out?"
        c "I don't think it's gonna be hard to drive him nuts again. A little provocation and maybe he'll want to give me some spanking again."
        c "How about I do something worse this time?"

        scene day_08_scene_00_clara_9 with dissolve
        c "It's been a long time since I felt this way with any guy. There is something about [player_name] that makes me wet."
        c "It is nice to feel dominated by a strong man again."

        scene day_08_scene_00_clara_10 with dissolve
        "{color=#D2691E}*Clara gets out of bed and starts getting dressed.*{/color}"
        c "I wonder why Linda hasn't spoken to me by now."
        c "I could call her."

        scene day_08_scene_00_clara_11 with dissolve
        "{color=#D2691E}*She's clasping her bra.*{/color}"
        c "In fact, fuck her."
        c "I won't call her. She must first apologize to me."

        scene day_08_scene_00_clara_12 with dissolve
        c "Until she does, I don't give a shit about her. Let her worry about herself."
        c "I'm fed up with her moods and constantly insulting me for no reason."
        c "Stupid cunt."

        scene day_08_scene_00_clara_13 with dissolve
        c "Now I need to focus on myself and pissing off [player_name]."
        c "It would be really fun if something came out of it."

        scene day_08_scene_00_clara_14 with dissolve
        c "Maybe in the end this week won't be as shitty as last ones."
        c "Fingers crossed."

        jump day_08_scene_01

    else:

        scene day_08_scene_00_clara_7 with dissolve
        "{color=#D2691E}*Clara lies in bed staring at the ceiling.*{/color}"
        c "I had such a beautiful dream."
        c "I wonder if I could provoke [player_name] to finally give me some spanking."
        c "Just the thought of his hard hand on my bottom gives me shivers."

        scene day_08_scene_00_clara_8 with dissolve
        c "Maybe it would be worth checking it out?"
        c "I don't think it's gonna be hard to drive him nuts again. A little provocation and maybe he'll want to give me some spanking finally."

        scene day_08_scene_00_clara_9 with dissolve
        c "It's been a long time since I felt this way with any guy. There is something about [player_name] that makes me wet."
        c "It would be nice to feel dominated by a strong man again."

        scene day_08_scene_00_clara_10 with dissolve
        "{color=#D2691E}*Clara gets out of bed and starts getting dressed.*{/color}"
        c "I wonder why Linda hasn't spoken to me by now."
        c "I could call her."

        scene day_08_scene_00_clara_11 with dissolve
        "{color=#D2691E}*She's clasping her bra.*{/color}"
        c "In fact, fuck her."
        c "I won't call her. She must first apologize to me."

        scene day_08_scene_00_clara_12 with dissolve
        c "Until she does, I don't give a shit about her. Let her worry about herself."
        c "I'm fed up with her moods and constantly insulting me for no reason."
        c "Stupid cunt."

        scene day_08_scene_00_clara_13 with dissolve
        c "Now I need to focus on myself and pissing off [player_name]."
        c "It would be really fun if something came out of it."

        scene day_08_scene_00_clara_14 with dissolve
        c "Maybe in the end this week won't be as shitty as last ones."
        c "Fingers crossed."

        jump day_08_scene_01

#####################################################################################################################################################
                                                    ############# SCENE 01 - MC DILEMMAS#############    done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_01:

    if clara_spanking == True:

        scene black with dissolve
        show bg in_the_meantime with dissolve
        $ renpy.pause()

    else:

        scene black with fade
        pause 1.0

    scene day_08_scene_01_mc_dilemmas_1 with dissolve
    "{color=#D2691E}*You wake up early in the morning, and the girls are still asleep.*{/color}"

    scene day_08_scene_01_mc_dilemmas_2 with dissolve
    "{color=#D2691E}*You carefully get up from the bed and go out on the terrace.*{/color}"

    scene day_08_scene_01_mc_dilemmas_3 with dissolve
    "{color=#D2691E}*Even though it is still summer, the morning is exceptionally cold.*{/color}"

    menu mc_dilemmas_day_08:

        "{color=#74B2F4}Clara.{/color}" if clara_mc_dilemma_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_5 with dissolve
            "{color=#81F79F}*What should I do with this woman?*{/color}"
            "{color=#81F79F}*I'm annoyed by her presence, but I'm afraid that if I fire her it will cause me even more problems.*{/color}"

            scene day_08_scene_01_mc_dilemmas_6 with dissolve
            "{color=#81F79F}*Maybe it will be better if I have her close to me and in this way I can control her?*{/color}"
            "{color=#81F79F}*Maybe now that Linda is no longer with her, she won't pose such a threat as before?*{/color}"

            scene day_08_scene_01_mc_dilemmas_7 with dissolve
            "{color=#81F79F}*But should I take the risk?*{/color}"
            $ clara_mc_dilemma_day_08 = True
            jump mc_dilemmas_day_08

        "{color=#74B2F4}Sandra and Emily.{/color}" if sandra_emily_dilemma_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_8 with dissolve
            "{color=#81F79F}*Should I engage in a closer relationship with them?*{/color}"
            "{color=#81F79F}*I already know how Emily feels about me and honestly it scares me a little.*{/color}"

            scene day_08_scene_01_mc_dilemmas_9 with dissolve
            "{color=#81F79F}*If I refuse her now, I will hurt her, but should I worry about it?*{/color}"
            "{color=#81F79F}*Why can't I be tough and indifferent, why do I always have to think about everything so much and worry about the feelings of others and not my own?*{/color}"

            scene day_08_scene_01_mc_dilemmas_10 with dissolve
            "{color=#81F79F}*As if that wasn't enough, I'm going to talk to Sandra, but what am I supposed to tell this woman?*{/color}"

            scene day_08_scene_01_mc_dilemmas_11 with dissolve
            "{color=#81F79F}*She is a beautiful and intelligent woman and could probably contribute a lot to our professional and private life.*{/color}"
            "{color=#81F79F}*But these conversations, explaining to others that I live in an open relationship, that it's cool that I can't get involved with just one person is so fucking tiring that I don't know if I want to go through it all again.*{/color}"

            scene day_08_scene_01_mc_dilemmas_12 with dissolve
            "{color=#81F79F}*I've already explained it to Lisa and Emily and I don't have the strength to have the same conversation again. I don't know what to do...*{/color}"
            $ sandra_emily_dilemma_day_08 = True
            jump mc_dilemmas_day_08

        "{color=#74B2F4}Jennifer, Nicole and Lisa.{/color}" if jenn_nic_lisa_dilemma_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_13 with dissolve
            "{color=#81F79F}*Fortunately, our relations have improved significantly over the last few days. I am especially happy with Jennifer's attitude.*{/color}"
            "{color=#81F79F}*She opened up and finally it occurred to her that I am not a bad person.*{/color}"

            scene day_08_scene_01_mc_dilemmas_14 with dissolve
            "{color=#81F79F}*Again we could enjoy our company and for a while I felt like I used to.*{/color}"
            "{color=#81F79F}*Very nice feeling.*{/color}"

            if jennifer_kiss_day_06 == True:

                scene day_08_scene_01_mc_dilemmas_15 with dissolve
                "{color=#81F79F}*I am still wondering about that kiss.*{/color}"
                "{color=#81F79F}*Was it an accident, a moment of weakness, or is there more to it?*{/color}"

                scene day_08_scene_01_mc_dilemmas_16 with dissolve
                "{color=#81F79F}*But I will do nothing about it. I do not want to lose her again.*{/color}"
                "{color=#81F79F}*If it was a coincidence, I will simply forget about it, and if there is something behind it, I leave to Jennifer's initiative.*{/color}"

                scene day_08_scene_01_mc_dilemmas_17 with dissolve
                "{color=#81F79F}*The same applies to Nicole. I don't mind being close to each other, even closer than ever, but I don't mean to push them or encourage them to do anything, let alone convince them.*{/color}"

            else:

                scene day_08_scene_01_mc_dilemmas_17 with dissolve
                "{color=#81F79F}*The same applies to Nicole. I don't mind being close to each other, even closer than ever, but I don't mean to push them or encourage them to do anything, let alone convince them.*{/color}"

            scene day_08_scene_01_mc_dilemmas_18 with dissolve
            "{color=#81F79F}*If something is to be out of this, it must happen by itself. The situation with Lisa is different.*{/color}"
            "{color=#81F79F}*I hope that regardless of her decision we will remain friends and my sweet little Lisa will not suffer because of me.*{/color}"
            $ jenn_nic_lisa_dilemma_day_08 = True
            jump mc_dilemmas_day_08

        "{color=#74B2F4}Linda.{/color}" if linda_dilemma_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_19 with dissolve
            "{color=#81F79F}*Linda's case went faster than I could have imagined.*{/color}"
            "{color=#81F79F}*I wonder if Ming fulfilled our agreement and Linda was taught a lesson.*{/color}"

            scene day_08_scene_01_mc_dilemmas_20 with dissolve
            "{color=#81F79F}*I'll find out tonight. In a few days I will have to take Linda away from there, but I have no idea what to do with her.*{/color}"
            "{color=#81F79F}*Especially now that Jennifer begged me to find out what was happening to her and help her. I have to think about it.*{/color}"

            scene day_08_scene_01_mc_dilemmas_21 with dissolve
            "{color=#81F79F}*I will talk to Khloe and Mary, maybe they will come up with some interesting ideas.*{/color}"
            "{color=#81F79F}*So far I have to pay Ming for Linda's debts, and she will still be under Ming's control for a few days.*{/color}"
            $ linda_dilemma_day_08 = True
            jump mc_dilemmas_day_08

    if linda_dilemma_day_08 == True and jenn_nic_lisa_dilemma_day_08 == True and sandra_emily_dilemma_day_08 == True and clara_mc_dilemma_day_08 == True:
        jump day_08_scene_01_a

label day_08_scene_01_a:

    scene day_08_scene_01_mc_dilemmas_22 with dissolve
    "{color=#D2691E}*You are so immersed in your own thoughts that you do not notice that Mary is also awake.*{/color}"
    "{color=#D2691E}*Only the touch of her warm and wonderfully delicate hand makes you come back to reality.*{/color}"

    scene day_08_scene_01_mc_dilemmas_23 with dissolve
    mary "You had nightmares again?"
    mc "No, I just can't sleep."

    scene day_08_scene_01_mc_dilemmas_24 with dissolve
    "{color=#D2691E}*Mary kisses you on the shoulder.*{/color}"
    mary "Come inside, it is terribly cold here."
    mary "I'm going to put something on."

    scene day_08_scene_01_mc_dilemmas_25 with dissolve
    "{color=#D2691E}*Mary disappears behind the door, and you return to your thoughts.*{/color}"

    scene day_08_scene_01_mc_dilemmas_26 with dissolve
    "{color=#81F79F}*What is this all about?*{/color}"
    "{color=#81F79F}*What has my father been hiding all these years?*{/color}"

    scene day_08_scene_01_mc_dilemmas_27 with dissolve
    "{color=#81F79F}*Why has he suddenly remembered that he has a son?*{/color}"
    "{color=#81F79F}*What was the real reason that Linda kicked me out of the house and my father did not protest?*{/color}"

    scene day_08_scene_01_mc_dilemmas_28 with dissolve
    "{color=#81F79F}*Why didn't he look for me?*{/color}"
    "{color=#81F79F}*Why did he break off all contacts with me completely?*{/color}"

    scene day_08_scene_01_mc_dilemmas_29 with dissolve
    "{color=#81F79F}*So many questions and no answers...*{/color}"
    "{color=#81F79F}*And on top of all that, there are these mysterious packages.*{/color}"
    "{color=#81F79F}*Who sent them and why now?*{/color}"

    scene day_08_scene_01_mc_dilemmas_30 with dissolve
    "{color=#D2691E}*Mary comes back wrapped in a bathrobe, holding a cup of steaming coffee in her hands.*{/color}"

    scene day_08_scene_01_mc_dilemmas_32 with dissolve
    mary "What are you thinking about?"
    mc "I am wondering about everything that has happened in my life."

    scene day_08_scene_01_mc_dilemmas_33 with dissolve
    mc "On my father's behavior, on what he really hid all these years."
    mc "I have so many questions and so far no answers."

    scene day_08_scene_01_mc_dilemmas_34 with dissolve
    "{color=#D2691E}*Mary cuddles up to you.*{/color}"
    mary "Don't worry. We are here with you to find answers to all your questions and we will not leave here until we find out the whole truth."

    menu mary_love_day_08:

        "{color=#74B2F4}I love you.{/color} [MaryLovePath] [KhloeLovePath]":

            scene day_08_scene_01_mc_dilemmas_35 with dissolve
            "{color=#D2691E}*You kiss her on the forehead.*{/color}"
            mc "I love you guys."
            mc "I don't know what I would do if I didn't have you and Khloe with me."

            scene day_08_scene_01_mc_dilemmas_36 with dissolve
            mc "You are my whole life."

            scene day_08_scene_01_mc_dilemmas_37 with dissolve
            mc "You think we'll get to the truth?"
            mary "Yes, I am convinced of that. But we need some time and patience to solve this puzzle, but I know we will."
            $ mary_love += 1
            $ khloe_love += 1

        "{color=#74B2F4}Say nothing.{/color}":

            scene day_08_scene_01_mc_dilemmas_37 with dissolve
            mc "You think we'll get to the truth?"
            mary "Yes, I am convinced of that. But we need some time and patience to solve this puzzle, but I know we will."

    scene day_08_scene_01_mc_dilemmas_38 with dissolve
    "{color=#D2691E}*Mary is looking at you closely.*{/color}"
    mary "I have the impression that something else is worrying you."

    scene day_08_scene_01_mc_dilemmas_39 with dissolve
    mc "You're right."
    mc "Before you got up, I was still thinking about what to do with Clara, Linda and the other girls."

    scene day_08_scene_01_mc_dilemmas_40 with dissolve
    mary "You don't need to worry about it. You have a free hand when it comes to them and you can make the decisions you think are best."
    mary "We will not interfere and will accept your decisions."
    mc "Thank you."

    scene black with fade
    "{color=#D2691E}*You go back into the house.*{/color}"

    scene day_08_scene_01_mc_dilemmas_41 with dissolve
    "{color=#D2691E}*You sit on the couch and Mary sits on your lap and cuddles up to you.*{/color}"
    mary "Jesus, I'm frozen."

    scene day_08_scene_01_mc_dilemmas_42 with dissolve
    "{color=#D2691E}*You hold her tightly and stay together for a while.*{/color}"

    menu mary_questions_day_08:

        "{color=#74B2F4}The key.{/color}" if key_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_43 with dissolve
            mc "Mary, we need to move forward with things related to my father."
            mc "Today I have to pick up the flash drive, so you will have to carefully examine its content. "

            scene day_08_scene_01_mc_dilemmas_44 with dissolve
            mc "We need to find out what this key is for, who sent both packages and why my father is indicated as sender of one of them."
            mc "Without this information, we are still pretty much in the dark about everything."

            scene day_08_scene_01_mc_dilemmas_45 with dissolve
            mary "I know, I'm working on it."
            mc "That's good."
            $ key_day_08 = True

            jump mary_questions_day_08

        "{color=#74B2F4}Karen.{/color}" if karen_day_08 == False:

            scene day_08_scene_01_mc_dilemmas_46 with dissolve
            mc "Did Khloe say anything about Karen?"
            mary "Nothing interesting, actually."

            scene day_08_scene_01_mc_dilemmas_47 with dissolve
            mary "She hung around for a few hours, but did not notice anything suspicious."
            mary "I did some research here and there and it looks like Karen is an ordinary woman."

            scene day_08_scene_01_mc_dilemmas_48 with dissolve
            mary "She has no police record, no criminal record, works in a hypermarket as a cashier."
            mary "She has an adult daughter, who lives with her. Her name is Jessica and she is 19 years old."

            scene day_08_scene_01_mc_dilemmas_49 with dissolve
            mary "Her husband was killed in a car accident many years ago. Since then, she has not been involved with anyone."
            mc "Great."

            scene day_08_scene_01_mc_dilemmas_50 with dissolve
            mary "Do you have any idea how to end this case?"
            mc "No, but I have some time, so I'll come up with something. I have no intention of acting hastily."
            mary "That's good."
            $ karen_day_08 = True

            jump mary_questions_day_08

    if karen_day_08 and key_day_08 == True:

        jump day_08_scene_01_b

label day_08_scene_01_b:

    scene day_08_scene_01_mc_dilemmas_51 with dissolve
    "{color=#D2691E}*You lean down and kiss Mary.*{/color}"
    mc "I love you."
    mary "I love you too."

    jump day_08_scene_02

#####################################################################################################################################################
                                                    ############# SCENE 02 - NICOLE DILEMMAS#############   done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_02:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    if nicole_helped == True:

        scene day_08_scene_02_nicole_2 with dissolve
        "{color=#D2691E}*Nicole sits on the bed and holds one of your letters in her hands.*{/color}"

        scene day_08_scene_02_nicole_3 with dissolve
        "{color=#D2691E}*She's been reading them all night.*{/color}"
        n "What's all this about? Why did my mother throw him out of the house? Why did his father hide these letters from us?"
        n "It doesn't make any sense. Why did they want us to hate him?"

        scene day_08_scene_02_nicole_4 with dissolve
        n "How am I gonna make up for my behavior? Jesus... How could I have been so unfair...? Why did I believe so blindly in everything my mother said...?"
        n "What am I gonna do now?"

        scene day_08_scene_02_nicole_5 with dissolve
        n "He really must care about me if, despite everything I did to him, he was the same [player_name] as he used to be."
        n "I have to make it up to him. I have to convince him that I really care about him and about us."

        scene day_08_scene_02_nicole_6 with dissolve
        n "I hope we will start over and be happy again as we used to be."
        n "It would be so great."

        scene day_08_scene_02_nicole_7 with dissolve
        "{color=#D2691E}*Nicole takes another letter in her hand and starts reading.*{/color}"

        scene day_08_scene_02_nicole_8 with dissolve
        "{i}'My dear Nicole.'{/i}"
        "{i}I understand that you are angry with me, but I tried to explain to you what forced me to leave without a word.{/i}"
        "{i}I was hoping that you would try to understand me that we will still go through this difficult period together, supporting each other.{/i}"

        scene day_08_scene_02_nicole_9 with dissolve
        "{i}I am extremely sorry that despite my requests, explanations and apologies, you did not write even a word to me.{/i}"
        "{i}Many times I sent you my new home address, my phone number and email address. I cannot understand why you did not write or call me.{/i}"
        "{i}Do you hate me that much Nicole?{/i}"

        scene day_08_scene_02_nicole_10 with dissolve
        "{i}I will not bother you or your sisters. This is my last letter.{/i}"
        "{i}I have lost hope that you will ever forgive me and give me a second chance to be together. It has been eight months since I left.{/i}"
        "{i}I have sent almost 100 letters to you, and none of you have said a word to me. I don't understand it. I thought we had something more in common, but I think I was wrong.{/i}"

        scene day_08_scene_02_nicole_11 with dissolve
        "{i}(…){/i}"
        "{i}I miss your smile, your joy and your jokes so much.{/i}"

        scene day_08_scene_02_nicole_12 with dissolve
        "{i}Often lying in bed in this musty hole, I remember this wonderful time we spent together. I hope that everything is fine with you, that you are happy.{/i}"
        "{i}(…){/i}"

        scene day_08_scene_02_nicole_13 with dissolve
        "{i}This is the last letter I write to you.{/i}"
        "{i}I love you and I always will.{/i}"
        "{i}Your [player_name].{/i}"

        scene day_08_scene_02_nicole_14 with dissolve
        "{color=#D2691E}*Nicole puts away your letter wet from tears.*{/color}"
        n "Mother! Why did you do this to us!"
        n "I hate you!"

        scene day_08_scene_02_nicole_15 with dissolve
        "{color=#D2691E}*Weeping more and more, Nicole lies down on her bed.*{/color}"
        n "I can't understand why she did it."
        n "What kind of person you have to be to punish your own children like that?"

        scene day_08_scene_02_nicole_16 with dissolve
        n "I will never forgive her. NEVER!"

        scene day_08_scene_02_nicole_17 with dissolve
        n "Only now I understand what [player_name] suffered."
        n "I have never before wondered what he was going through."

        scene day_08_scene_02_nicole_18 with dissolve
        n "It was always just me and nothing else mattered."
        n "Poor [player_name] has gone through hell."

        scene day_08_scene_02_nicole_19 with dissolve
        n "I am not at all surprised that he did not come back here earlier."
        n "I wouldn't want to come back here in his place either."

        scene day_08_scene_02_nicole_20 with dissolve
        n "I just can't understand why my mother did all this, why she kept telling us for so many years that [player_name] left us, that he was a bad person, that he didn't love us, that he did it on purpose."

        scene day_08_scene_02_nicole_21 with dissolve
        n "But she will pay for everything she has done to me and [player_name]."
        n "You hear me, Mother? You will pay me for everything!"
        n "I swear!"

        jump day_08_scene_03

    else:

        scene day_08_scene_02_nicole_22 with dissolve
        "{color=#D2691E}*Nicole's lying on the bed, staring at the ceiling.*{/color}"
        n "Come up with a punishment for yourself... What a son of a bitch... He did it on purpose to get back at me."

        scene day_08_scene_02_nicole_23 with dissolve
        n "And what kind of punishment am I supposed to think of?"
        n "He's fucked up, that's all."

        scene day_08_scene_02_nicole_24 with dissolve
        "{color=#D2691E}*Minutes go by and Nicole gets more and more angry.*{/color}"
        n "I can't fucking think of anything, and I gotta figure something out."

        scene day_08_scene_02_nicole_25 with dissolve
        n "If I don't give him an answer today, he's gonna leave me completely alone and I'm gonna be in even more trouble."
        n "I'm not gonna think of anything. I don't know what he expects, so I don't think there's any point in thinking about it anymore."
        n "I'll meet him and see how the conversation goes."

        scene day_08_scene_02_nicole_26 with dissolve
        n "As a last resort, I'll show him my tits or blow him..."
        n "Jesus, how low I fell... My life is a mockery...."

        jump day_08_scene_03

#####################################################################################################################################################
                                                    ############# SCENE 03 - JENNIFER'S FANTASIES#############    done and rendered
#####################################################################################################################################################
label day_08_scene_03:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname
        $ jennifer_kiss_day_06 = persistent.jennifer_kiss_day_06

        show screen endreplay_button

    if jennifer_kiss_day_06 == True:

        scene day_08_scene_03_jennifer_1 with dissolve
        "{color=#D2691E}*Jennifer wakes up.*{/color}"

        scene day_08_scene_03_jennifer_1a with dissolve
        "{color=#D2691E}*She lies on her bed for a long time thinking about the events of yesterday..*{/color}"
        j "I'm so tired... Yesterday was so exhausting."

        scene day_08_scene_03_jennifer_1b with dissolve
        j "Fortunately, today I have a day off from work, so maybe I will manage to regain my strength somehow."

        scene day_08_scene_03_jennifer_1c with dissolve
        j "I have to take a shower."

        scene day_08_scene_03_jennifer_1d with dissolve
        "{color=#D2691E}*Jennifer walks in the bathroom and undresses.*{/color}"

        scene day_08_scene_03_jennifer_2 with dissolve
        "{color=#D2691E}*She stands in front of the mirror and looks at herself carefully.*{/color}"
        j "Am I pretty?"
        j "I guess I still have that thing."

        scene day_08_scene_03_jennifer_3 with dissolve
        j "Why can't I find myself some nice and caring guy?"
        j "I always come across some arrogant idiot who only wants to fuck me."

        scene day_08_scene_03_jennifer_4 with dissolve
        j "It's time to get back to normal life. I have to see Jill. I haven't seen her in so long..."
        j "I need to regain my confidence again."

        scene day_08_scene_03_jennifer_5 with dissolve
        "{color=#D2691E}*Jennifer turns on the water. A warm stream of water flows down her naked body.*{/color}"
        j "I haven't touched myself for so long. I wonder if I still remember how to do that..."

        scene day_08_scene_03_jennifer_6 with dissolve
        "{color=#D2691E}*Jennifer's right hand is slowly moving down towards her sweet spot.*{/color}"
        "{color=#D2691E}*The streams of water flow down her body, caressing her gently.*{/color}"

        scene day_08_scene_03_jennifer_7 with dissolve
        $ renpy.pause ()

        scene day_08_scene_03_jennifer_8 with dissolve
        "{color=#D2691E}*She sits down, spreads her legs and opens her vulva lips.*{/color}"
        "{color=#D2691E}*Jennifer starts thinking about her favorite hero of her erotic fantasies. She imagines how he holds her tightly, how he tenderly caresses her whole body.*{/color}"

        scene day_08_scene_03_jennifer_9 with dissolve
        "{color=#D2691E}*Jennifer admires his muscular, perfect body through the eyes of her imagination. She is getting more and more excited as she thinks about him.*{/color}"
        "{color=#D2691E}*Her fingers effectively massage her clitoris, causing her to shiver.*{/color}"

        scene day_08_scene_03_jennifer_10 with dissolve
        "{color=#D2691E}*Jennifer slowly slips one finger into her wet and tight pussy.*{/color}"

        scene day_08_scene_03_jennifer_11 with dissolve
        "{color=#D2691E}*Her body is strained and her breathing is getting faster and faster.*{/color}"
        "{color=#D2691E}*When she finally reaches her G-spot, a loud groan of delight comes out of her mouth.*{/color}"

        scene day_08_scene_03_jennifer_12 with dissolve
        "{color=#D2691E}*Her moves become stronger and faster. Her fingers are reaching the farthest corners of her juice-drenched pussy.*{/color}"
        "{color=#D2691E}*Jennifer feels an orgasm coming up. Her clitoris is getting more and more sensitive but she keeps caressing it to intensify her pleasure even more.*{/color}"

        scene day_08_scene_03_jennifer_13 with dissolve
        "{color=#D2691E}*Her body's tensing up. She is ready for the incoming wave of pleasure.*{/color}"
        "{color=#D2691E}*Just a few more strong moves, just a few more seconds for her body to shake with spasms of pleasure.*{/color}"

        scene day_08_scene_03_jennifer_14 with dissolve
        "{color=#D2691E}*Jennifer clenches her thighs to intensify her climax. She starts to scream.*{/color}"
        j "Yes, [player_name]! Don't stop!"

        scene day_08_scene_03_jennifer_15 with dissolve
        "{color=#D2691E}*She leans her back against the wall and tries to calm her breath.*{/color}"
        j "God, that was so intense."

        scene day_08_scene_03_jennifer_16 with dissolve
        "{color=#D2691E}*Only now does Jennifer realize that she was shouting [player_name]'s name.*{/color}"
        j "Did I really think about [player_name]? Something is really wrong with me..."

        scene day_08_scene_03_jennifer_17 with dissolve
        "{color=#D2691E}*Jennifer finishes her shower and slowly returns to her room.*{/color}"

        scene day_08_scene_03_jennifer_18 with dissolve
        "{color=#D2691E}*She looks through her lingere' drawer.*{/color}"
        "{color=#D2691E}*Finally she decides to put on a black thong and bra.*{/color}"
        j "What is happening to me?"

        scene day_08_scene_03_jennifer_19 with dissolve
        j "First I kiss [player_name] like a lover, and now I touch myself thinking about him."
        j "Is it possible that I feel something for him?"
        j "No, that's impossible. What an idiotic thought..."

        scene day_08_scene_03_jennifer_20 with dissolve
        j "Eh... I don't think I believe that myself."
        j "All in all, I must admit that no other man was as close to me as [player_name]."
        j "Maybe there is something in it... Only time will tell..."
        $ renpy.end_replay()

        jump jennifer_jill

    else:

        scene day_08_scene_03_jennifer_1 with dissolve
        "{color=#D2691E}*Jennifer wakes up.*{/color}"

        scene day_08_scene_03_jennifer_1a with dissolve
        j "Why can't I find myself some nice and caring guy?"
        j "I always come across some arrogant idiot who only wants to fuck me."

        scene day_08_scene_03_jennifer_1b with dissolve
        j "It's time to get back to normal life. I have to meet Jill. I haven't seen her in so long..."
        j "I need to regain my confidence again."

        $ renpy.end_replay()

        jump jennifer_jill

label jennifer_jill:

    scene black with fade

    scene day_08_scene_03_jennifer_21 with dissolve
    j "How long has it been since I last talked to Jill?"
    j "Almost a year..."

    scene day_08_scene_03_jennifer_22 with dissolve
    j "I wonder if she will want to talk to me at all."
    j "Our last conversation did not end nicely, and it was all because of that son of a bitch Eric."

    scene day_08_scene_03_jennifer_23 with dissolve
    j "I'm sure she has already forgiven me..."
    j "But why am I so nervous..."

    scene day_08_scene_03_jennifer_jill_1 with dissolve
    j "Hello, Jill."
    jill "Oh my fucking god! Is it really you, Jennifer?"
    j "Yes, it's me."

    scene day_08_scene_03_jennifer_jill_2 with dissolve
    jill "I'm so glad you finally called. We haven't talked for six months now."
    j "I think it's almost a year."
    jill "How are you doing?"
    j "I'm fine, thanks."

    scene day_08_scene_03_jennifer_jill_3 with dissolve
    j "I broke up with Eric and I am trying to start over."
    jill "That's great. I really hate that morron."
    j "I was blind and stupid, and I pushed you away because of him."
    jill "Don't worry about it. I'm glad you decided to move forward."

    scene day_08_scene_03_jennifer_jill_4 with dissolve
    j "Look, maybe we could meet and talk."
    jill "Oh, yeah. I would love to."
    j "How about tomorrow?"
    jill "Sure. I'll come to you after I get off of work."

    scene day_08_scene_03_jennifer_jill_5 with dissolve
    j "Great. I can't wait."
    jill "I'm so glad you finally called me. I've missed you so much."
    j "I missed you too."

    scene day_08_scene_03_jennifer_jill_6 with dissolve
    jill "I'll see you tomorrow."
    jill "Bye."
    j "Bye."

    $ jill_enabled = True

    jump day_08_scene_04

#####################################################################################################################################################
                                                    ############# SCENE 04 - CHANGES, CHANGES#############    done and rendered
#####################################################################################################################################################
label day_08_scene_04:

    if holy_hired == True:

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause ()

        scene day_08_scene_04_office_1 with dissolve
        mc "Good morning, ladies."
        s "Good morning."
        h "Good morning."

        scene day_08_scene_04_office_2 with dissolve
        mc "Good to see you. I would like to talk to you. There are a few things we need to discuss."
        mc "Is Isabella already here and working?"

        scene day_08_scene_04_office_3 with dissolve
        s "Yes. I'll call her right away."
        mc "Great. I'll be waiting for you in the office."

        scene day_08_scene_04_office_4 with dissolve
        "{color=#D2691E}*A few minutes later all the ladies enter the office.*{/color}"
        mc "Sit down, please."

        scene day_08_scene_04_office_5 with dissolve
        mc "First of all, I would like to welcome Holly into our company."
        mc "I hope that our cooperation will be successful and we will be satisfied with it."

        scene day_08_scene_04_office_6 with dissolve
        h "Thank you very much. I promise that I will do my best to make it happen."
        mc "I'm glad to hear it."

        scene day_08_scene_04_office_7 with dissolve
        mc "As I said before, there are a few things I need to discuss with you. I'm not hiding the fact that we have some changes ahead of us, and they're quite a big one."
        mc "Unfortunately, the current situation both in this company and in my private life leaves me no choice."

        scene day_08_scene_04_office_8 with dissolve
        mc "In order for us to function normally and develop our company, but also to enjoy the work itself, certain matters must be dealt with."

        menu day_08_office_choices_holly:

            "{color=#74B2F4}The company.{/color}" if the_company == False:

                scene day_08_scene_04_office_10 with dissolve
                mc "Since my stay here is prolonged, I have to reorganize my private and professional life."
                mc "As a result, I am having to take steps to consolidate the two companies.  First I am opening a branch of my company from Los Angeles here."

                scene day_08_scene_04_office_11 with dissolve
                mc "The formalities need to be taken care of, Sandra would you please see to that?"
                s "Of course."

                scene day_08_scene_04_office_12 with dissolve
                mc "Great. Unfortunately, due to the nature of my business, we urgently need to verify all the employees who work in my father's company."
                mc "But I'll take care of this personally."

                scene day_08_scene_04_office_13 with dissolve
                mc "The branch of my company will be working here as well. Isabella, you and I will walk around the building and find the best area for the branch offices to be."
                mc "We need to keep these offices together and minimize the offices we relocate in this company."
                i "Of course."

                scene day_08_scene_04_office_14 with dissolve
                mc "We will later address if there needs to be anyone laid off and they will be treated to a fair severance and best possible references according to their personel record."
                mc "Holly, I'm asking you to take care of this. Sandra will help you if you need her."
                h "Of course."
                $ the_company = True

                jump day_08_office_choices_holly

            "{color=#74B2F4}Promotions.{/color}" if promotions == False:

                scene day_08_scene_04_office_15 with dissolve
                mc "More work and more responsibility await you, and I would like to offer you new positions."

                menu promotions_day_8:

                    "{color=#74B2F4}Sandra.{/color} [SandraLovePath]" if sandra_promotion == False:

                        scene day_08_scene_04_office_16 with dissolve
                        mc "Sandra, I'd like you to take over my father's company and therefore become vice president of the company."
                        s "Oh?!"
                        mc "Do you agree?"

                        scene day_08_scene_04_office_17 with dissolve
                        s "I don't know what to say..."
                        mc "I need your answer now."
                        s "I agree."
                        $ sandra_love += 1
                        $ sandra_promotion = True
                        jump promotions_day_8

                    "{color=#74B2F4}Holly.{/color} [HolyLovePath]" if holly_promotion == False:

                        scene day_08_scene_04_office_18 with dissolve
                        mc "Holly, because of your previous cooperation with Sandra, you will become Sandra's assistant."

                        scene day_08_scene_04_office_19 with dissolve
                        "{color=#D2691E}*Holly looks at you in amazement.*{/color}"
                        mc "I take it you don't mind?"
                        h "Uh...no..."
                        $ holy_love += 1
                        $ holly_promotion = True
                        jump promotions_day_8

                    "{color=#74B2F4}Isabella.{/color} [IsabellaLovePath]" if isabella_promotion == False:

                        scene day_08_scene_04_office_20 with dissolve
                        mc "From now on, Isabella will be the link between Sandra and me."
                        mc "This will involve a lot of responsibility and a lot of work."

                        scene day_08_scene_04_office_21 with dissolve
                        mc "You will have to coordinate the work of both companies, work with me, Sandra and my two associates, whom you will meet tomorrow."
                        mc "Isabella, are you ready to take on this challenge?"

                        scene day_08_scene_04_office_22 with dissolve
                        i "Yes."
                        mc "I'm very glad about that."
                        $ isabella_love += 1
                        $ isabella_promotion = True
                        jump promotions_day_8

                $ promotions = True

                if sandra_promotion == True and holly_promotion == True and isabella_promotion == True:
                    jump day_08_office_choices_holly

        if the_company == True and promotions == True:
            jump day_08_office_part_2

    else:

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause ()

        scene day_08_scene_04_office_1 with dissolve
        mc "Good morning."
        s "Good morning."

        scene day_08_scene_04_office_2 with dissolve
        mc "Good to see you. I would like to talk to you. There are a few things we need to discuss."
        mc "Is Isabella already here and working?"

        scene day_08_scene_04_office_3 with dissolve
        s "Yes. I'll call her right away."
        mc "Great. I'll be waiting for you in the office."

        scene day_08_scene_04_office_4 with dissolve
        "{color=#D2691E}*A few minutes later all the ladies enter the office.*{/color}"
        mc "Sit down, please."

        scene day_08_scene_04_office_7 with dissolve
        mc "As I said before, there are a few things I need to discuss with you. I'm not hiding the fact that we have some changes ahead of us, and they're quite a big one."
        mc "Unfortunately, the current situation both in this company and in my private life leaves me no choice."

        scene day_08_scene_04_office_8 with dissolve
        mc "In order for us to function normally and develop our company, but also to enjoy the work itself, certain matters must be dealt with."

        menu day_08_office_choices:

            "{color=#74B2F4}The company.{/color}" if the_company == False:

                scene day_08_scene_04_office_10 with dissolve
                mc "Since my stay here is prolonged, I have to reorganize my private and professional life."
                mc "As a result, I am having to take steps to consolidate the two companies. First I am opening a branch of my company from Los Angeles here."

                scene day_08_scene_04_office_11 with dissolve
                mc "The formalities need to be taken care of, Sandra would you please see to that?"
                s "Of course."

                scene day_08_scene_04_office_12 with dissolve
                mc "Great. Unfortunately, due to the nature of my business, we urgently need to verify all the employees who work in my father's company."
                mc "But I'll take care of this personally."

                scene day_08_scene_04_office_13 with dissolve
                mc "The branch of my company will be working here as well. Isabella, you and I will walk around the building and find the best area for the branch offices to be. We need to keep these offices together and minimize the offices we relocate in this company."
                i "Of course."
                mc "We will later address if there needs to be anyone laid off and they will be treated to a fair severance and best possible references according to their personel record."
                s "Of course."
                $ the_company = True

                jump day_08_office_choices

            "{color=#74B2F4}Promotions.{/color}" if promotions == False:

                scene day_08_scene_04_office_15 with dissolve
                mc "More work and more responsibility await you, and I would like to offer you new positions."

                menu promotions_day_8_no_holly:

                    "{color=#74B2F4}Sandra.{/color} [SandraLovePath]" if sandra_promotion == False:

                        scene day_08_scene_04_office_16 with dissolve
                        mc "Sandra, I'd like you to take over my father's company and therefore become vice president of the company."
                        s "Oh?!"
                        mc "Do you agree?"

                        scene day_08_scene_04_office_17 with dissolve
                        s "I don't know what to say..."
                        mc "I need your answer now."
                        s "I agree."
                        $ sandra_love += 1
                        $ sandra_promotion = True
                        jump promotions_day_8_no_holly

                    "{color=#74B2F4}Isabella.{/color} [IsabellaLovePath]" if isabella_promotion == False:

                        scene day_08_scene_04_office_20 with dissolve
                        mc "From now on, Isabella will be the link between Sandra and me."
                        mc "This will involve a lot of responsibility and a lot of work."

                        scene day_08_scene_04_office_21 with dissolve
                        mc "You will have to coordinate the work of both companies, work with me, Sandra and my two associates, whom you will meet tomorrow."
                        mc "Isabella, are you ready to take on this challenge?"

                        scene day_08_scene_04_office_22 with dissolve
                        i "Yes."
                        mc "I'm very glad about that."
                        $ isabella_love += 1
                        $ isabella_promotion = True
                        jump promotions_day_8_no_holly

                $ promotions = True

                if sandra_promotion == True and isabella_promotion == True:
                    jump day_08_office_choices

        if the_company == True and promotions == True:
            jump day_08_office_part_2


label day_08_office_part_2:

    if holy_hired == True:

        scene day_08_scene_04_office_23 with dissolve
        mc "My dear ladies, we have a lot of work ahead of us, but I believe we can do it if we work together."
        mc "Sandra, I ask you to prepare all the necessary documents for your new assignments."

        scene day_08_scene_04_office_24 with dissolve
        s "I'll take care of everything."
        h "If I may say something, I think we'll need a secretary."

        scene day_08_scene_04_office_25 with dissolve
        mc "You're right, but I'll take care of it myself."
        s "What about Clara?"
        mc "Clara is a separate topic, but don't worry about that either. I'll take care of it myself."

        scene day_08_scene_04_office_26 with dissolve
        mc "Sandra, there is an empty room next to my office. I want you to adopt it for your office. This way we can have direct contact with each other and we only need one secretary."
        i "I'll take care of it."
        mc "If you need to buy equipment or furniture, choose something yourself."

        scene day_08_scene_04_office_27 with dissolve
        mc "Okay. That's all for now. Let's get to work."

        scene day_08_scene_04_office_28 with dissolve
        "{color=#D2691E}*Holly and Isabella leave the office, but Sandra stops at the door.*{/color}"
        s "Thank you so much."
        mc "There's nothing to thank me for, I'm sure you'll do great with everything."

        scene day_08_scene_04_office_29 with dissolve
        s "I don't know."
        mc "A little more self-confidence."

        scene day_08_scene_04_office_30 with dissolve
        "{color=#D2691E}*Sandra is smiling at you.*{/color}"
        s "I'd like to talk to you about one thing. Would you find a moment to visit me tonight?"
        mc "I still have a lot of things to do today. Could we meet up for tomorrow night?"
        s "Sure, around 7 p.m.?"
        mc "Yeah, sounds great."

        if amy_help == True:

            scene day_08_scene_04_office_33 with dissolve
            "{color=#D2691E}*You're about to close the door, but you notice Amy walking down the hallway and you call out for her.*{/color}"

            scene day_08_scene_04_office_34 with dissolve
            mc "Amy!"

            scene day_08_scene_04_office_35 with dissolve
            "{color=#D2691E}*The girl stops and turns around.*{/color}"
            mc "Can I see you for a moment?"
            amy "Of course."

            scene day_08_scene_04_office_36 with dissolve
            "{color=#D2691E}*You're going into the office together.*{/color}"
            mc "Sit down, please."
            amy "Did something happen? Did I do something wrong?"

            scene day_08_scene_04_office_37 with dissolve
            "{color=#D2691E}*You smile at her.*{/color}"
            mc "I'm still waiting for that promised drink."
            amy "Oh, yes. I'm very sorry, but my grandmother was feeling very bad yesterday and I spent the whole afternoon and evening with her."
            mc "I'm sorry to hear that. Don't worry about that drink. I was joking."

            scene day_08_scene_04_office_38 with dissolve
            mc "I want to talk to you about your situation."
            mc "I recently found out about your Grandma. You take care of her yourself, right?"
            amy "Yes."

            scene day_08_scene_04_office_39 with dissolve
            mc "What about your parents?"
            amy "My parents divorced a few years ago. I haven't had any contact with my mother since then, and until then my father took care of my grandmother, but he had to go back to work."
            mc "Then why didn't you take your grandmother home?"

            scene day_08_scene_04_office_40 with dissolve
            amy "Because she doesn't want to leave. She was born in this town, spent her whole life here and wants to die here."
            amy "I recently graduated from school, so my dad asked me to come here for a while and take care of her."
            mc "Very noble of you."

            menu amy_new_job:

                "{color=#74B2F4}Offer her a new job.{/color} [AmyLovePath]":

                    scene day_08_scene_04_office_41 with dissolve
                    amy "Unfortunately, because of his health, dad had to change his job and we can barely make a living."
                    mc "I think I will be able to help you. There are some organizational changes in the company and I would like to offer you a job."
                    amy "Oh?!"

                    scene day_08_scene_04_office_42 with dissolve
                    mc "Right now, I could offer you a secretarial position. It's a lot of work, but I think it's worth a try."
                    amy "I don't know how to thank you."

                    scene day_08_scene_04_office_43 with dissolve
                    amy "I'll do my best and I'm not gonna disappoint you."
                    mc "I'm sure about that."

                    scene day_08_scene_04_office_44 with dissolve
                    amy "When would I start?"
                    mc "From tomorrow."

                    scene day_08_scene_04_office_45 with dissolve
                    "{color=#D2691E}*Amy comes up to you and hugs you.*{/color}"
                    amy "I don't know how I'm gonna repay you."
                    mc "Let's start with that overdue drink."
                    amy "Sure. Hehe."

                    scene day_08_scene_04_office_46 with dissolve
                    amy "Damnit... I completely forgot about Grandma."
                    amy "I don't know if I can handle everything."
                    $ amy_love += 1

                    menu amy_nurse:

                        "{color=#74B2F4}I hired a nurse for your grandmother.{/color} [AmyLovePath]":

                            scene day_08_scene_04_office_47 with dissolve
                            mc "I talked to a nurse this morning and set up a meeting with her. Here's her phone number."
                            mc "Call her. I paid for her services for three months."

                            scene day_08_scene_04_office_48 with dissolve
                            mc "You can take care of your work and not worry about your grandma."
                            amy "Oh, my God!"
                            amy "Thank you very much."

                            scene day_08_scene_04_office_49 with dissolve
                            amy "How will I repay you?"
                            mc "Calm down, please. I don't want you to come out of my office crying."
                            mc "Besides, I already told you. Invite me for a drink."

                            scene day_08_scene_04_office_50 with dissolve
                            amy "One drink is not enough."
                            amy "I need to think about something extra."
                            mc "For now, focus on your work."
                            $ amy_love += 2

                            scene day_08_scene_04_office_53 with dissolve
                            mc "Tomorrow at 9:00 a.m. there will be an official meeting and I want you to be there."
                            mc "Besides, clean up your office, hand your things over to other employees and get ready for your new job. You start at 8 a.m."
                            amy "Of course."

                            scene day_08_scene_04_office_54 with dissolve
                            "{color=#D2691E}*Amy kisses you on the cheek.*{/color}"
                            amy "Thank you, sir."

                            menu dont_call_me_sir:

                                "{color=#74B2F4}Please, call me [player_name]{/color} [AmyLovePath]":

                                    scene day_08_scene_04_office_54a with dissolve
                                    mc "Please, call me [player_name]."
                                    amy "Of course."

                                    $ amy_call_me_john = True
                                    $ amy_love += 1

                                    jump day_08_scene_05

                                "{color=#74B2F4}Say nothing{/color}":

                                    jump day_08_scene_05

                        "{color=#74B2F4}You're gonna have to get through this somehow.{/color}":

                            scene day_08_scene_04_office_51 with dissolve
                            mc "You're gonna have to get through this somehow."
                            mc "I think for the money you're gonna make now you can hire someone to help you with your grandma."

                            scene day_08_scene_04_office_52 with dissolve
                            amy "I can do this."
                            mc "I'm glad to hear that."

                            scene day_08_scene_04_office_53 with dissolve
                            mc "Tomorrow at 9:00 a.m. there will be a meeting."
                            mc "Besides, clean up your office, hand your things over to other employees and get ready for your new job. You start at 8 a.m."
                            amy "Of course."

                            scene day_08_scene_04_office_54 with dissolve
                            "{color=#D2691E}*Amy embraces you and kisses on the cheek.*{/color}"
                            amy "Thank you."

                            jump day_08_scene_05

                "{color=#74B2F4}Inform her about the meeting.{/color}":

                    scene day_08_scene_04_office_54 with dissolve
                    mc "Tomorrow at 9:00 a. m. there will be a meeting."
                    amy "Of course."

                    scene day_08_scene_04_office_52 with dissolve
                    mc "If you need help with your grandma, let me know."
                    mc "Maybe we can come up with something to help you."
                    amy "Thank you."

                    jump day_08_scene_05

        else:

            scene day_08_scene_04_office_33 with dissolve
            "{color=#D2691E}*You're about to close the door, but you notice Amy walking down the hallway and you call out for her.*{/color}"

            scene day_08_scene_04_office_34 with dissolve
            mc "Amy!"

            scene day_08_scene_04_office_35 with dissolve
            "{color=#D2691E}*The girl stops and turns to you.*{/color}"
            mc "Tomorrow at 9:00 a. m. there will be a meeting."
            amy "Of course."

            jump day_08_scene_05

    else:

        scene day_08_scene_04_office_23 with dissolve
        mc "My dear ladies, we have a lot of work ahead of us, but I believe we can do it if we work together."
        mc "Sandra, I ask you to prepare all the necessary documents for your new assignments."
        s "I'll take care of everything."

        scene day_08_scene_04_office_25 with dissolve
        s "What about Clara?"
        mc "Clara is a separate topic, but don't worry about that either. I'll take care of it myself."

        scene day_08_scene_04_office_26 with dissolve
        mc "Sandra, there is an empty room next to my office. I want you to adopt it for your office. This way we can have direct contact with each other and we only need one secretary."
        i "I'll take care of it."
        mc "If you need to buy equipment or furniture, choose something yourself."

        scene day_08_scene_04_office_27 with dissolve
        mc "Okay. That's all for now. Let's get to work."

        scene day_08_scene_04_office_28 with dissolve
        "{color=#D2691E}*Isabella leave the office, but Sandra stops at the door.*{/color}"
        s "Thank you so much."
        mc "There's nothing to thank me for, I'm sure you'll do great with everything."

        scene day_08_scene_04_office_29 with dissolve
        s "I don't know."
        mc "A little more self-confidence."

        scene day_08_scene_04_office_30 with dissolve
        "{color=#D2691E}*Sandra is smiling at you.*{/color}"
        s "I'd like to talk to you about one thing. Would you find a moment to visit me tonight?"
        mc "I still have a lot of things to do today. Could we meet up for tomorrow night?"
        s "Sure, around 7 p.m.?"
        mc "Yeah, sounds great."

        if amy_help == True:

            scene day_08_scene_04_office_33 with dissolve
            "{color=#D2691E}*You're about to close the door, but you notice Amy walking down the hallway and you call out for her.*{/color}"

            scene day_08_scene_04_office_34 with dissolve
            mc "Amy!"

            scene day_08_scene_04_office_35 with dissolve
            "{color=#D2691E}*The girl stops and turns around.*{/color}"
            mc "Can I see you for a moment?"
            amy "Of course."

            scene day_08_scene_04_office_36 with dissolve
            "{color=#D2691E}*You're going into the office together.*{/color}"
            mc "Sit down, please."
            amy "Did something happen? Did I do something wrong?"

            scene day_08_scene_04_office_37 with dissolve
            "{color=#D2691E}*You smile at her.*{/color}"
            mc "I'm still waiting for that promised drink."
            amy "Oh, yes. I'm very sorry, but my grandmother was feeling very bad yesterday and I spent the whole afternoon and evening with her."
            mc "I'm sorry to hear that. Don't worry about that drink. I was joking."

            scene day_08_scene_04_office_38 with dissolve
            mc "I want to talk to you about your situation."
            mc "I recently found out about your Grandma. You take care of her yourself, right?"
            amy "Yes."

            scene day_08_scene_04_office_39 with dissolve
            mc "What about your parents?"
            amy "My parents divorced a few years ago. I haven't had any contact with my mother since then, and until then my father took care of my grandmother, but he had to go back to work."
            mc "Then why didn't you take your grandmother home?"

            scene day_08_scene_04_office_40 with dissolve
            amy "Because she doesn't want to leave. She was born in this town, spent her whole life here and wants to die here."
            amy "I recently graduated from school, so my dad asked me to come here for a while and take care of her."
            mc "Very noble of you."

            menu amy_new_job_no_holly:

                "{color=#74B2F4}Offer her a new job.{/color} [AmyLovePath]":

                    scene day_08_scene_04_office_41 with dissolve
                    amy "Unfortunately, because of his health, dad had to change his job and we can barely make a living."
                    mc "I think I will be able to help you. There are some organizational changes in the company and I would like to offer you a job."
                    amy "Oh?!"

                    scene day_08_scene_04_office_42 with dissolve
                    mc "Right now, I could offer you a secretarial position. It's a lot of work, but I think it's worth a try."
                    amy "I don't know how to thank you."

                    scene day_08_scene_04_office_43 with dissolve
                    amy "I'll do my best and I'm not gonna disappoint you."
                    mc "I'm sure about that."

                    scene day_08_scene_04_office_44 with dissolve
                    amy "When would I start?"
                    mc "From tomorrow."

                    scene day_08_scene_04_office_45 with dissolve
                    "{color=#D2691E}*Amy comes up to you and hugs you.*{/color}"
                    amy "I don't know how I'm gonna repay you."
                    mc "Let's start with that overdue drink."
                    amy "Sure. Hehe."

                    scene day_08_scene_04_office_46 with dissolve
                    amy "Damnit... I completely forgot about Grandma."
                    amy "I don't know if I can handle everything."
                    $ amy_love += 1

                    menu amy_nurse_no_holly:

                        "{color=#74B2F4}I hired a nurse for your grandmother.{/color} [AmyLovePath]":

                            scene day_08_scene_04_office_47 with dissolve
                            mc "I talked to a nurse this morning and set up a meeting with her. Here's her phone number."
                            mc "Call her. I paid for her services for three months."

                            scene day_08_scene_04_office_48 with dissolve
                            mc "You can take care of your work and not worry about your grandma."
                            amy "Oh, my God!"
                            amy "Thank you very much."

                            scene day_08_scene_04_office_49 with dissolve
                            amy "How will I repay you?"
                            mc "Calm down, please. I don't want you to come out of my office crying."
                            mc "Besides, I already told you. Invite me for a drink."

                            scene day_08_scene_04_office_50 with dissolve
                            amy "One drink is not enough."
                            amy "I need to think about something extra."
                            mc "For now, focus on your work."
                            $ amy_love += 2

                            scene day_08_scene_04_office_53 with dissolve
                            mc "Tomorrow at 9:00 a.m. there will be an official meeting and I want you to be there."
                            mc "Besides, clean up your office, hand your things over to other employees and get ready for your new job. You start at 8 a.m."
                            amy "Of course."

                            scene day_08_scene_04_office_54 with dissolve
                            "{color=#D2691E}*Amy kisses you on the cheek.*{/color}"
                            amy "Thank you, sir."

                            menu dont_call_me_sir_no_holly:

                                "{color=#74B2F4}Please, call me [player_name]{/color} [AmyLovePath]":

                                    scene day_08_scene_04_office_54a with dissolve
                                    mc "Please, call me [player_name]."
                                    amy "Of course."

                                    $ amy_call_me_john = True
                                    $ amy_love += 1

                                    jump day_08_scene_05

                                "{color=#74B2F4}Say nothing{/color}":

                                    jump day_08_scene_05

                        "{color=#74B2F4}You're gonna have to get through this somehow.{/color}":

                            scene day_08_scene_04_office_51 with dissolve
                            mc "You're gonna have to get through this somehow."
                            mc "I think for the money you're gonna make now you can hire someone to help you with your grandma."

                            scene day_08_scene_04_office_52 with dissolve
                            amy "I can do this."
                            mc "I'm glad to hear that."

                            scene day_08_scene_04_office_53 with dissolve
                            mc "Tomorrow at 9:00 a.m. there will be a meeting."
                            mc "Besides, clean up your office, hand your things over to other employees and get ready for your new job. You start at 8 a.m."
                            amy "Of course."

                            scene day_08_scene_04_office_54 with dissolve
                            "{color=#D2691E}*Amy embraces you and kisses on the cheek.*{/color}"
                            amy "Thank you."

                            jump day_08_scene_05

                "{color=#74B2F4}Inform her about the meeting.{/color}":

                    scene day_08_scene_04_office_54 with dissolve
                    mc "Tomorrow at 9:00 a. m. there will be a meeting."
                    amy "Of course."

                    scene day_08_scene_04_office_52 with dissolve
                    mc "If you need help with your grandma, let me know."
                    mc "Maybe we can come up with something to help you."
                    amy "Thank you."

                    jump day_08_scene_05

        else:

            scene day_08_scene_04_office_33 with dissolve
            "{color=#D2691E}*You're about to close the door, but you notice Amy walking down the hallway and you call out for her.*{/color}"

            scene day_08_scene_04_office_34 with dissolve
            mc "Amy!"

            scene day_08_scene_04_office_35 with dissolve
            "{color=#D2691E}*The girl stops and turns to you.*{/color}"
            mc "Tomorrow at 9:00 a. m. there will be a meeting."
            amy "Of course."

            jump day_08_scene_05

#####################################################################################################################################################
                                                    ############# SCENE 05 - LINDA'S SECOND LESSON#############    done and rendered
#####################################################################################################################################################
label day_08_scene_05:

    scene black with dissolve
    show bg in_the_meantime with dissolve
    $ renpy.pause ()

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname

        show screen endreplay_button

    scene day_08_scene_05_linda_1 with dissolve
    "{color=#D2691E}*Linda wakes up in a sheer panic.*{/color}"
    "{color=#D2691E}*She slowly opens her eyes.*{/color}"

    scene day_08_scene_05_linda_2 with dissolve
    "{color=#D2691E}*As her eyes are getting used to seeing in the dark, she notices she is in a different room.*{/color}"
    li "How is it possible?"
    li "Did they move me while I was sleeping?"

    scene day_08_scene_05_linda_3 with dissolve
    "{color=#D2691E}*She reaches at her neck, there is a leather collar wrapped tightly around. She looks down, only to notice she is still completely naked.*{/color}"
    "{color=#D2691E}*Tears are welling up in her eyes as she wonders what the hell will happen to her.*{/color}"

    scene day_08_scene_05_linda_4 with dissolve
    li "Did they already sell me?"
    li "Where the fuck am I?"

    scene day_08_scene_05_linda_5 with dissolve
    li "HELP! Can anyone hear me?"
    "{color=#D2691E}*Her voice echoes in the hollow chambers.*{/color}"

    scene day_08_scene_05_linda_6 with dissolve
    li "HELP!"
    "{color=#D2691E}*Suddenly she hears heavy footsteps approaching her room.*{/color}"

    scene day_08_scene_05_linda_7 with dissolve
    "{color=#D2691E}*Linda hears someone open the door to her room and a tall man walks in.*{/color}"
    "{color=#D2691E}*He peeks at her and her naked body.*{/color}"

    scene day_08_scene_05_linda_8 with dissolve
    "{color=#D2691E}*Linda instinctively retracts into the corner trying to hide from his gaze.*{/color}"
    "{color=#D2691E}*She examines his face and recognizes him.*{/color}"
    "{color=#D2691E}*This is Mr. D - her master.*{/color}"

    scene day_08_scene_05_linda_9 with dissolve
    mrd "This is your first and last warning."
    mrd "Because I haven't had a chance to get you acquainted with the rules here, I won't punish you this time."
    mrd "But break a rule one more time and I will punish you hard."

    scene day_08_scene_05_linda_10 with dissolve
    mrd "First rule - You are forbidden from speaking without permission."
    mrd "Second rule - You will be naked and leashed at all times."
    mrd "Third rule - You will willingly accept anything that I or the other masters do to your helpless body."

    scene day_08_scene_05_linda_11 with dissolve
    mrd "Within next few days you are going to be sold at the auction and you'll find a new home."
    mrd "Until then, you must follow the rules, because Mrs. Ming is willing to leave you here until you pay off all of your debt."
    mrd "And believe me, you wouldn't want to experience that."

    scene day_08_scene_05_linda_12 with dissolve
    mrd "Do you understand?"
    li "...Uh...eh...yes."

    scene day_08_scene_05_linda_13 with dissolve
    "{color=#D2691E}*Mr. D leaves the room closing the door behind him.*{/color}"
    "{color=#D2691E}*Linda falls on her bed and starts weeping.*{/color}"
    $ renpy.end_replay()

    jump day_08_scene_06

#####################################################################################################################################################
                                                    ############# SCENE 06 - KEIRA PLANS REVEALED#############    done and rendered
#####################################################################################################################################################
label day_08_scene_06:

    if _in_replay:

        $ player_name = persistent.name
        $ player_surname = persistent.surname
        $ keira_blackmail = persistent.keira_blackmail

        show screen endreplay_button

    if keira_blackmail == True:

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause ()

        scene day_08_scene_06_keira_1 with dissolve
        ke "I' m glad you're here. I was just thinking about you."
        mc "Hello."

        scene day_08_scene_06_keira_2 with dissolve
        ke "Would you like a drink?"

        menu drink_keira:

            "{color=#74B2F4}Yes, please.{/color} [KeiraPath]":

                scene day_08_scene_06_keira_3 with dissolve
                mc "I'd like that."
                ke "Whiskey?"
                mc "Yes."

                scene day_08_scene_06_keira_4 with dissolve
                mc "Did you manage to decrypt the flash drive?"
                ke "Yeah. I had some problems with it, but I finally made it."

                scene day_08_scene_06_keira_5 with dissolve
                "{color=#D2691E}*Keira is pouring whiskey into a glass.*{/color}"
                mc "That's good. Can I have it back?"

                scene day_08_scene_06_keira_6 with dissolve
                "{color=#D2691E}*You watch her body sway with the motion of silent music coming from the speakers as she moves towards you.*{/color}"
                ke "Of course. It's on the desk."

                scene day_08_scene_06_keira_7 with dissolve
                "{color=#D2691E}*You could swear she just bitted up her bottom lip knowing you are watching her.*{/color}"
                "{color=#D2691E}*She gazes up at you locking eyes the second she did.*{/color}"

                scene day_08_scene_06_keira_8 with dissolve
                "{color=#D2691E}*You watch her reaching up and slides her delicate hand around to the back of her neck and begins to rub it.*{/color}"
                "{color=#D2691E}*She ever so slowly rolles her head letting out a soft moan as she did tilting her chin up.*{/color}"

                scene day_08_scene_06_keira_9 with dissolve
                "{color=#D2691E}*Keira tosses her head up with intensity displayes the most lustful gaze for you.*{/color}"

                scene day_08_scene_06_keira_10 with dissolve
                "{color=#D2691E}*You step in front of her and pull her chin up to meet you.*{/color}"
                mc "Let’s just cut through all the bullshit here lady. I just want to get back my flash drive."

                scene day_08_scene_06_keira_11 with dissolve
                "{color=#D2691E}*You release her chin from your fingertips and let out a sigh.*{/color}"
                ke "Of course."

                scene day_08_scene_06_keira_12 with dissolve
                "{color=#D2691E}*She takes your glass from you and rests it back on the desk, grabbing your hand in hers and slipping her lips over the tip of your ring finger.*{/color}"
                "{color=#D2691E}*She is slowly sliding it all the way down into her mouth, then just as slowly removing it, using her tongue to savour every inch while you watch on in startled delight.*{/color}"

                scene day_08_scene_06_keira_13 with dissolve
                ke "Sit down."

                scene day_08_scene_06_keira_14 with dissolve
                "{color=#FF69B4}*She removes her top, then slides her pants.*{/color}"

                scene day_08_scene_06_keira_15 with dissolve
                "{color=#FF69B4}*She kicks off her heels and then removes her red lacy bra.*{/color}"

                scene day_08_scene_06_keira_16 with dissolve
                "{color=#FF69B4}*She starts to dance. Her moves are slow and seductive.*{/color}"

                scene day_08_scene_06_keira_17 with dissolve
                "{color=#FF69B4}*Your gaze is intense and fixed on only her exposed breasts. Her hands massage her own creamy soft flesh, begging for you to join her.*{/color}"
                ke "Do you like what you are seeing?"

                scene day_08_scene_06_keira_18 with dissolve
                "{color=#FF69B4}*She smiles at you flirtatiously.*{/color}"

                scene day_08_scene_06_keira_19 with dissolve
                "{color=#FF69B4}*Seeing your growing desire she reaches for her erected nipples and she massages her breasts with care.*{/color}"

                scene day_08_scene_06_keira_20 with dissolve
                "{color=#FF69B4}*Her other hand slides down her body reaching her sweet spot.*{/color}"
                ke "I want you. I want you NOW!"

                scene day_08_scene_06_keira_21 with dissolve
                "{color=#FF69B4}*She slides her panties off and she climbes on top of you.*{/color}"

                menu sex_keira:

                    "{color=#74B2F4}Stop her.{/color}":

                        scene day_08_scene_06_keira_22 with dissolve
                        mc "What the fuck do you think you are doing?"
                        mc "Get off me now."

                        scene day_08_scene_06_keira_23 with dissolve
                        ke "Sorry, I thought you wanted to fuck me."

                        scene day_08_scene_06_keira_24 with dissolve
                        "{color=#FF69B4}*Keira is picking up her things from the floor and running out of the office."

                        scene day_08_scene_06_keira_25 with dissolve
                        "{color=#FF69B4}*You get up, take your flash drive from the desk and leave."

                        jump keira_and_megan

                    "{color=#74B2F4}Fuck her.{/color} [KeiraPath]":

                        scene day_08_scene_06_keira_26 with dissolve
                        ke "I have to have you right now."

                        scene day_08_scene_06_keira_27 with dissolve
                        "{color=#FF69B4}*She whispered into your ear, pulling open your belt buckle and unzipping your pants.*{/color}"

                        scene day_08_scene_06_keira_28 with dissolve
                        "{color=#FF69B4}*She leans in and kisses you, licking your lips and forcing her way into your mouth.*{/color}"
                        "{color=#FF69B4}*It is rough, wet and excited.*{/color}"

                        scene day_08_scene_06_keira_29 with dissolve
                        "{color=#FF69B4}*The tip of your dick is pointing up, less than an inch from the entrance to her pussy.*{/color}"

                        scene day_08_scene_06_keira_30 with dissolve
                        "{color=#FF69B4}*Then Keira simply lowers herself, and you slide inside with one, hard thrust.*{/color}"

                        scene day_08_scene_06_keira_31 with dissolve
                        "{color=#FF69B4}*You respond with equal amounts of enthusiasm, securing your hands around her waist to plunge yourself deeper and deeper inside her.*{/color}"

                        scene day_08_scene_06_keira_32 with dissolve
                        $ renpy.pause ()

                        scene day_08_scene_06_keira_33 with dissolve
                        $ renpy.pause ()

                        scene day_08_scene_06_keira_34 with dissolve
                        "{color=#FF69B4}*You lift her up and throw her down onto the desk.*{/color}"

                        scene day_08_scene_06_keira_35 with dissolve
                        "{color=#FF69B4}*The pleasure inside her reaches a near painful crescendo that begs release as you tug on her hair, grab her hips and drive into her.*{/color}"
                        ke "Fuck me harder."

                        scene day_08_scene_06_keira_36 with dissolve
                        "{color=#FF69B4}*She says and your rhythm picks up.*{/color}"

                        scene day_08_scene_06_keira_37 with dissolve
                        "{color=#FF69B4}*She lets out a loud screaming-moan of pleasure that lasts several seconds and her body trembles.*{/color}"

                        scene day_08_scene_06_keira_38 with dissolve
                        $ renpy. pause ()

                        scene day_08_scene_06_keira_39 with flash
                        with flash
                        with flash

                        scene day_08_scene_06_keira_40 with dissolve
                        "{color=#FF69B4}*You pull out your dick and force her to change position.*{/color}"

                        scene day_08_scene_06_keira_41 with dissolve
                        "{color=#FF69B4}*You look down at her gorgeous ass and slap her buttocks.*{/color}"

                        scene day_08_scene_06_keira_42 with dissolve
                        "{color=#FF69B4}*She open her legs more and you enter her in one thrust, she is wet enough to do so.*{/color}"

                        scene day_08_scene_06_keira_43 with dissolve
                        "{color=#FF69B4}*As you ride her, her ass bounces on the rhythm of your love-making, interspersed with hoarse moans of pleasure from her.*{/color}"

                        scene day_08_scene_06_keira_44 with dissolve
                        "{color=#FF69B4}*You keep your dick buried deep in her wet and tight pussy.*{/color}"

                        scene day_08_scene_06_keira_45 with dissolve
                        $ renpy.pause ()

                        scene day_08_scene_06_keira_46 with dissolve
                        "{color=#FF69B4}*Your breathing increases, you are almost there.*{/color}"
                        "{color=#FF69B4}*Just a few more strokes...*{/color}"

                        scene day_08_scene_06_keira_47 with dissolve
                        "{color=#FF69B4}*You grunt loudly. You cum with a powerful, almost painful force.*{/color}"

                        call screen keira_day_08_cumshots

            "{color=#74B2F4}No, thank you.{/color}":

                scene day_08_scene_06_keira_56 with dissolve
                mc "No, thank you. Let's get down to business."
                ke "Of course."

                scene day_08_scene_06_keira_57 with dissolve
                ke "As promised, the flash drive has been decrypted."
                mc "Great."
                ke "Unfortunately, it took more work than I expected. You owe me $2,000."

                scene day_08_scene_06_keira_58 with dissolve
                mc "There was no extra charge."
                ke "Well... that's what you owe, either you pay or the disk stays with me."

                scene day_08_scene_06_keira_59 with dissolve
                "{color=#D2691E}*You put money on the desk.*{/color}"
                mc "Now my flash drive."
                ke "Business with you is pure pleasure."

                scene day_08_scene_06_keira_60 with dissolve
                "{color=#D2691E}*You take the disk and leave without a word.*{/color}"

                jump keira_and_megan

        label keira_day_08_creampie:

        hide screen keira_day_08_cumshots

        scene day_08_scene_06_keira_50 with dissolve
        "{color=#FF69B4}*You push your member even deeper inside her sweet pussy and the torrent of warm seed fills her fully.*{/color}"
        "{color=#FF69B4}*You pull out your cock and the seed slowly drips out of her.*{/color}"
        $ keira_creampie += 1
        $ renpy.end_replay()

        jump keira_after_sex_day_08

        label keira_day_08_back:

        hide screen keira_day_08_cumshots

        scene day_08_scene_06_keira_49 with dissolve
        "{color=#FF69B4}*You slowly pull out your cock out of Keira's cunt and the warm torrent of your cum splashes on her back and ass.*{/color}"
        $ renpy.end_replay()

        jump keira_after_sex_day_08

        label keira_day_08_facial:

        hide screen keira_day_08_cumshots

        scene day_08_scene_06_keira_48 with dissolve
        "{color=#FF69B4}*Keira turns to you and opens her mouth*.{/color}"
        "{color=#FF69B4}*The torrent of your warm cum splashes on her face.*{/color}"
        $ renpy.end_replay()

        jump keira_after_sex_day_08

        label keira_after_sex_day_08:

        scene black with fade
        $ renpy.pause(1)

        scene day_08_scene_06_keira_51 with dissolve
        mc "Now let's get down to business."
        ke "Of course."

        scene day_08_scene_06_keira_52 with dissolve
        ke "As promised, the flash drive has been decrypted."
        mc "Great."

        scene day_08_scene_06_keira_53 with dissolve
        ke "Business with you is pure pleasure."
        mc "With you too."

        scene day_08_scene_06_keira_54 with dissolve
        ke "If you ever need to decipher something, you know where to find me."
        mc "Sure."
        ke "See you later."

        scene day_08_scene_06_keira_55 with dissolve
        "{color=#D2691E}*You take the disk and leave.*{/color}"
        $ keira_sex = True

        jump keira_and_megan

        label keira_and_megan:

        scene black with fade
        $ renpy.pause(1)

        scene day_08_scene_06_keira_61 with dissolve
        meg "So? Did it work?"

        if keira_sex == True:

            scene day_08_scene_06_keira_62 with dissolve
            ke "I think so."
            meg "What do you mean?"
            ke "I seduced him and he fucked me, but I don't know if anything was recorded."

            scene day_08_scene_06_keira_63 with dissolve
            meg "Can't you do anything right?"
            ke "Leave me alone, Megan."
            ke "I was supposed to seduce him? I seduced him. Was he supposed to fuck me? He fucked me."

            scene day_08_scene_06_keira_64 with dissolve
            meg "We don't get shit if we don't get anything recorded."
            ke "Yeah, but you were the one setting up the camera, so get the fuck away from me and check the recording first."
            meg "You're so nervous."

            scene day_08_scene_06_keira_65 with dissolve
            "{color=#D2691E}*Megan takes the camera and checks the recording.*{/color}"
            meg "Your naked ass looks pretty good on this video."
            ke "Fuck you."

            scene day_08_scene_06_keira_66 with dissolve
            meg "Haha."
            ke "So everything's okay?"
            meg "Yes. Time to move on to the next stage of our plan."
            $ megan_enabled = True

            jump day_08_scene_07

        else:

            scene day_08_scene_06_keira_61 with dissolve
            ke "No. He ignored me completely."
            meg "Fuckin' hell, what are we gonna do now?"

            scene day_08_scene_06_keira_62 with dissolve
            ke "Megan, calm down. We'll figure something out."
            meg "I wonder what. That was the perfect plan, and now I don't know what to do."
            ke "I'm sure we'll come up with something."
            $ megan_enabled = True

            jump day_08_scene_07

    else:

        jump day_08_scene_07

#####################################################################################################################################################
                                                    ############# SCENE 07 - MYSTERIOUS FLASH DRIVE CONTENT#############    done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_07:

    scene black with dissolve
    show some_time_later with dissolve
    $ renpy.pause()

    scene day_08_scene_07_flash_drive_1 with dissolve
    "{color=#D2691E}*You entering the house.*{/color}"
    "{color=#D2691E}*Mary is sitting at the table staring at the laptop screen.*{/color}"

    scene day_08_scene_07_flash_drive_2 with dissolve
    mc "Hello, dear. How are you doing?"
    mary "Oh, already here?"
    mc "I've arranged everything and decided to spend some time with you, because I have to leave again in the evening."

    scene day_08_scene_07_flash_drive_3 with dissolve
    mc "What are you doing?"
    mary "I'm trying to find some kind of a starting point, something where we could start our investigation."

    scene day_08_scene_07_flash_drive_4 with dissolve
    mc "Did you manage to find something?"
    mary "Not much so far."
    mary "I have looked through the police file of your mother's disappearance case and I must say honestly that this case is strange."

    scene day_08_scene_07_flash_drive_5 with dissolve
    mary "I feel something is wrong with all of this, but I don't know what and it annoys me terribly."
    mary "Do you remember anything about those events?"

    scene day_08_scene_07_flash_drive_6 with dissolve
    "{color=#D2691E}*You stare at the floor for a while, then you embrace Mary and start talking.*{/color}"
    mc "It was a very difficult time for me."
    mary "I am not surprised at all."

    scene day_08_scene_07_flash_drive_7 with dissolve
    mc "The investigation took a very long time, but did not bring any results."
    mc "My father, irritated by the helplessness of the police, hired two private detectives."
    mc "They were supposed to be the best in their field, with great experience in searching for missing persons."

    scene day_08_scene_07_flash_drive_8 with dissolve
    mc "They checked all possible leads and all possible scenarios - suicide, kidnapping, disappearance, escape, but they found absolutely nothing."
    mc "It looked as if my mother had disapeared into thin air."

    scene day_08_scene_07_flash_drive_9 with dissolve
    mc "Two or three weeks after my mother disappeared, a strange woman contacted the police claiming she saw my mother leaving with a man."
    mc "She claimed she had suitcases with her and it looked like she was leaving us."
    mc "We explained to the police that it was impossible, that all her personal belongings, clothes, etc. are where they always are, that nothing has disappeared, but the investigators found her testimony credible and some time later the investigation was closed."

    scene day_08_scene_07_flash_drive_10 with dissolve
    mc "The Private detectives looked for my mother for a long while, checking the witness' testimony out but they found absolutely nothing."
    mc "Eventually, my father decided that maybe she actually just left us and after six or seven months the investigation was over."

    scene day_08_scene_07_flash_drive_11 with dissolve
    mc "My father shut down and cut himself off from everyone."
    mc "My father had practically no contact with anyone untill suddenly he started seeing Linda."

    scene day_08_scene_07_flash_drive_12 with dissolve
    mc "They had known each other for as long as I can remember, but he never paid muce attention to her until I suddenly saw them together one day."
    mc "And so one nightmare turned into another."
    mary "I am so sorry."

    scene day_08_scene_07_flash_drive_13 with dissolve
    mary "It must have been a traumatic experience."
    mc "So many years have passed and I still can't talk about it..."
    mc "I still have a hard time thinking about that time."

    scene day_08_scene_07_flash_drive_14 with dissolve
    mary "How did you manage to recover after this?"
    mc "Well... Except for my mother and father, I had no other family. For some time, I tried to find out how to deal with it myself, but I couldn't."

    scene day_08_scene_07_flash_drive_15 with dissolve
    mc "It was then that Jennifer, Nicole and Lisa came to my aid."
    mc "They helped me to deal with all this and became a new family for me."

    scene day_08_scene_07_flash_drive_16 with dissolve
    "{color=#D2691E}*Mary is hugging you.*{/color}"
    mary "Now I understand what this intimacy between you and them is about and why you care so much about your relationship with them."

    if keira_blackmail == True:

        scene day_08_scene_07_flash_drive_17 with dissolve
        "{color=#D2691E}*You both keep quiet for a while hugging each other.*{/color}"
        mc "Okay, enough of these memories."
        mc "I have that flash drive back. Can you check what's on it?"

        scene day_08_scene_07_flash_drive_18 with dissolve
        "{color=#D2691E}*Mary takes a flash drive from you and plugs it into her laptop.*{/color}"
        "{color=#D2691E}*A moment later, the contents of the drive appear on the screen.*{/color}"
        mc "So?"

        scene day_08_scene_07_flash_drive_19 with dissolve
        mary "I don't know. There are a lot of files here."
        mc "Well, then open them one by one."

        scene day_08_scene_07_flash_drive_20 with dissolve
        "{color=#D2691E}*Mary clicks on the first file and lots of numbers and letters appear on the screen.*{/color}"
        mary "Strange..."
        mc "What the fuck is this?"

        scene day_08_scene_07_flash_drive_21 with dissolve
        mary "I don't know. It doesn't make sense."
        mc "Open another one."

        scene day_08_scene_07_flash_drive_22 with dissolve
        "{color=#D2691E}*Mary opens another file, but its content is as strange as the first.*{/color}"
        "{color=#D2691E}*Mary checks a few more, but the effect is the same.*{/color}"

        scene day_08_scene_07_flash_drive_23 with dissolve
        mc "What is this about?"
        mary "I don't know."
        mc "Maybe the one who decrypted the flash drive did it?"

        scene day_08_scene_07_flash_drive_24 with dissolve
        mary "I don't think so."
        mary "Give me a moment."
        mc "Sure."

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause()

        scene day_08_scene_07_flash_drive_25 with dissolve
        mc "Did you find out anything?"
        mary "Yes. The files are unchanged."
        mary "No one has modified them. But their contents have been additionally encrypted."


        scene day_08_scene_07_flash_drive_26 with dissolve
        mary "There's nothing here to enter a password or bypass it."
        mary "There are many different encryption systems, but it seems to me that in our case Rijndael code was used."
        mary "It is a very complicated system."

        scene day_08_scene_07_flash_drive_27 with dissolve
        mary "Anyone who wants to access information must have an encryption key to decrypt the file and restore it to a readable format."
        mc "So we can't do anything without this key?"
        mary "I am afraid this will be problamatic though."

        scene day_08_scene_07_flash_drive_28 with dissolve
        mc "Fuck!"
        mc "Why did someone send me this if I can't read it?"
        mary "I don't know, I don't understand it either."

        scene day_08_scene_07_flash_drive_29 with dissolve
        mc "Maybe the key is stored somewhere on this flash drive?"
        mary "Maybe, but it will take me some time to check for it."
        mc "Goddamnit."

        scene day_08_scene_07_flash_drive_30 with dissolve
        mc "I was hoping that we would find something here that would allow us to move on, and now there is another problem."
        mc "I've had enough of this."
        mary "Don't get upset."

        scene day_08_scene_07_flash_drive_31 with dissolve
        mary "Give me some time, I'll come up with something."
        mary "I will carefully check every file, maybe only some have been encrypted."
        mc "Okay."

        scene day_08_scene_07_flash_drive_32 with dissolve
        "{color=#D2691E}*You're circling around the room wondering what to do next.*{/color}"
        mc "We completely forgot about the key that was in the package with this flash drive."
        mc "It was sent for a reason."

        scene day_08_scene_07_flash_drive_33 with dissolve
        mary "I agree, but how do we determine what this key is for?"
        mc "Maybe it has something to do with the sender of the package?"
        mc "Have you managed to determine who sent it?"

        scene day_08_scene_07_flash_drive_34 with dissolve
        mary "I only have an address, but I have no idea if this is the real one."
        mc "Okay. That's something to start with."

        scene day_08_scene_07_flash_drive_35 with dissolve
        mc "I'll take this key and go check this address, and you try to decrypt these files in the meantime."
        mary "Okay, but I' m begging you, be careful."

        scene black with dissolve
        show bg one_hour_later with dissolve
        $ renpy.pause()

        scene day_08_scene_07_flash_drive_36 with dissolve
        "{color=#D2691E}*Less than an hour later you park across from the address.*{/color}"

        scene day_08_scene_07_flash_drive_37 with dissolve
        "{color=#D2691E}*You get out of the car and look around.*{/color}"
        "{color=#D2691E}*You have a strange feeling that you know this place, that you've been here before.*{/color}"

        scene day_08_scene_07_flash_drive_38 with dissolve
        "{color=#D2691E}*You look at the building.*{/color}"
        "{color=#D2691E}*You've definitely been here before, but you can't remember when or why.*{/color}"

        scene day_08_scene_07_flash_drive_39 with dissolve
        "{color=#D2691E}*You look around trying to remember but nothing comes to mind.*{/color}"
        "{color=#D2691E}*Frustraited by this, you get back into the car.*{/color}"

        scene day_08_scene_07_flash_drive_40 with dissolve
        mc "Fuck me, I'm getting old if I can't remember such simple things..."
        mc "I know I've been here before, why can't I remember anything?"

        scene day_08_scene_07_flash_drive_41 with dissolve
        "{color=#D2691E}*You think about what you should do now.*{/color}"
        "{color=#D2691E}*Whether to simply enter the building or will it be safer to wait and watch?*{/color}"

        menu enter_the_building:

            "{color=#74B2F4}Wait.{/color} [KeiraPath]":

                scene day_08_scene_07_flash_drive_42 with dissolve
                "{color=#D2691E}*You decide to wait.*{/color}"
                "{color=#D2691E}*Time passes by slowly, seconds becoming minutes.*{/color}"
                "{color=#D2691E}*You hate to wait.*{/color}"

                scene day_08_scene_07_flash_drive_43 with dissolve
                "{color=#D2691E}*Just as you are about to get out of the car when the door to the building opens and two women come out.*{/color}"
                "{color=#D2691E}*You look at them closely.*{/color}"

                scene day_08_scene_07_flash_drive_44 with dissolve
                mc "Fuck! It's Keira."
                mc "What the fuck is going on here?"

                scene day_08_scene_07_flash_drive_45 with dissolve
                "{color=#D2691E}*You wait for the women to disappear around the corner and get out of the car.*{/color}"
                "{color=#D2691E}*You quickly cross the street and enter the building.*{/color}"

                scene day_08_scene_07_flash_drive_46 with dissolve
                "{color=#D2691E}*You take the key out of your pocket and start climbing the stairs to the 1st floor.*{/color}"
                "{color=#D2691E}*It turns out that there are two apartments there. You look at the key and then carefully at the doors and locks.*{/color}"

                scene day_08_scene_07_flash_drive_47 with dissolve
                "{color=#D2691E}*Your key doesn't work on those doors.*{/color}"
                "{color=#D2691E}*You move up to the 2nd floor and try again but still no luck.*{/color}"

                scene day_08_scene_07_flash_drive_48 with dissolve
                "{color=#D2691E}*You only have one floor left. You're going up the stairs.*{/color}"
                "{color=#D2691E}*There's only one door on the 3rd floor. When you look at it you get that strange feeling again.*{/color}"
                mc "I've been here before."

                scene day_08_scene_07_flash_drive_49 with dissolve
                "{color=#D2691E}*You take time wondering what to do now.*{/color}"
                "{color=#D2691E}*KNOCK KNOCK.*{/color}"

                scene day_08_scene_07_flash_drive_50 with dissolve
                "{color=#D2691E}*Silence.*{/color}"
                "{color=#D2691E}*You take the key and put it in the lock. You turn it carefully.*{/color}"
                "{color=#D2691E}*You hear the sound of the pawls moving.*{/color}"

                scene day_08_scene_07_flash_drive_51 with dissolve
                "{color=#D2691E}*You turn the key and the lock opens, allowing you entry..*{/color}"
                "{color=#D2691E}*You enter carefully.*{/color}"

                scene day_08_scene_07_flash_drive_52 with dissolve
                "{color=#D2691E}*You enter the living room and start a thorough search of the apartment.*{/color}"
                "{color=#D2691E}*You are looking for anything to help uncover the truth.*{/color}"
                "{color=#D2691E}*Unfortunately, you don't find anything in the living room.*{/color}"

                scene day_08_scene_07_flash_drive_53 with dissolve
                "{color=#D2691E}*You go to the next room.*{/color}"

                scene day_08_scene_07_flash_drive_54 with dissolve
                "{color=#D2691E}*You look into the closet standing in the corner, but all you find there are women's clothes.*{/color}"

                scene day_08_scene_07_flash_drive_55 with dissolve
                "{color=#D2691E}*You go on and enter the next room.*{/color}"
                "{color=#D2691E}*There's a large desk in the middle and several monitors on it.*{/color}"

                scene day_08_scene_07_flash_drive_56 with dissolve
                "{color=#D2691E}*You move closer and look at them.*{/color}"

                scene day_08_scene_07_flash_drive_57 with dissolve
                mc "Hmmm, this looks like a camera monitoring station."
                mc "Is it monitoring?"

                scene day_08_scene_07_flash_drive_58 with dissolve
                "{color=#D2691E}*You sit behind a desk and start browsing through computer content.*{/color}"
                "{color=#D2691E}*You find a lot of video recordings in one of the directories.*{/color}"

                scene day_08_scene_07_flash_drive_59 with dissolve
                "{color=#D2691E}*You run the first file and see Keira appear on the screen at her desk and then you see yourself enter a short while later.*{/color}"
                "{color=#D2691E}*She sits behind a desk and does something on the computer.*{/color}"
                "{color=#D2691E}*After a short while the door to her office opens and you go inside.*{/color}"

                scene day_08_scene_07_flash_drive_60 with dissolve
                mc "What the fuck?"
                mc "Why was this bitch recording our meeting?"

                scene day_08_scene_07_flash_drive_61 with dissolve
                "{color=#D2691E}*You don't find anything interesting in several other files.*{/color}"
                "{color=#D2691E}*You continue your search and find a folder with a great many files named with dates and people's names.*{/color}"

                scene day_08_scene_07_flash_drive_62 with dissolve
                "{color=#D2691E}*In one of them you find more files with recordings.*{/color}"
                "{color=#D2691E}*This time, however, the files are sorted by the dates of the recordings and the names of people who were recorded.*{/color}"

                scene day_08_scene_07_flash_drive_63 with dissolve
                "{color=#D2691E}*The list is very long. You browse through it looking for your name, but you find nothing.*{/color}"
                "{color=#D2691E}*You are about to close the folder when one name catches your eye.*{/color}"
                "{color=#D2691E}*Ming.*{/color}"

                scene day_08_scene_07_flash_drive_64 with dissolve
                "{color=#D2691E}*You check all the files carefully and it turns out that there are over thirty with the name Ming.*{/color}"
                "{color=#D2691E}*You activate a trace program on the computer for Mary with your phone.*{/color}"

                scene day_08_scene_07_flash_drive_65 with dissolve
                "{color=#D2691E}*You turn everything off and hurry out of the apartment.*{/color}"
                "{color=#D2691E}*You get in the car and start the engine.*{/color}"

                scene day_08_scene_07_flash_drive_66 with dissolve
                "{color=#D2691E}*You're about to drive off when Keira comes around the corner.*{/color}"
                mc "Fuck, another minute and we'd run into each other."

                scene day_08_scene_07_flash_drive_67 with dissolve
                "{color=#D2691E}*You wait until she disappears inside the building and you leave.*{/color}"

                $ check_the_building = True

                jump day_08_scene_07_a

            "{color=#74B2F4}Go in.{/color}":

                scene day_08_scene_07_flash_drive_67a with dissolve
                "{color=#D2691E}*You get out of the car and cross the street.*{/color}"

                scene day_08_scene_07_flash_drive_67b with dissolve
                "{color=#D2691E}*You walk up to the door when it suddenly opens.*{/color}"
                "{color=#D2691E}*Two women are leaving the building*{/color}"

                scene day_08_scene_07_flash_drive_67c with dissolve
                "{color=#D2691E}*You look at them and freeze.*{/color}"
                ke "[player_name]?"
                mc "Keira?"

                scene day_08_scene_07_flash_drive_67d with dissolve
                ke "What are you doing here?"
                mc "I'm visiting a friend, but I think I got the wrong address."

                scene day_08_scene_07_flash_drive_67e with dissolve
                "{color=#D2691E}*Keira looks at you suspiciously, but does not comment on your lie.*{/color}"
                ke "Have a nice day."
                mc "You too."

                scene day_08_scene_07_flash_drive_67f with dissolve
                "{color=#D2691E}*You get in the car and start the engine.*{/color}"

                scene day_08_scene_07_flash_drive_67g with dissolve
                "{color=#D2691E}*You leave in order to not cause any more suspicion.*{/color}"

                jump day_08_scene_07_a

        label day_08_scene_07_a:

        if check_the_building == True:

            scene day_08_scene_07_flash_drive_68 with dissolve
            "{color=#D2691E}*Thirty minutes later you enter the house.*{/color}"
            mary "It's good to see you."
            mary "We were starting to worry about you."

            scene day_08_scene_07_flash_drive_69 with dissolve
            mary "Did you manage to find anything?"
            mc "Yes. The woman who decrypted the flash drive for me lives at this address."

            scene day_08_scene_07_flash_drive_70 with dissolve
            mary "Are you kidding?"
            mc "No. This is the key to her apartment."
            mc "I only found her computer and it had lots of videos. I also installed your tracking program on her computer and took these pictures."

            scene day_08_scene_07_flash_drive_71 with dissolve
            "{color=#D2691E}*You sit next to Mary and show her pictures.*{/color}"
            mc "It looks like she has access to surveillance cameras from all over this town and of certain people."
            mary "A serious matter."

            scene day_08_scene_07_flash_drive_72 with dissolve
            mary "You think she's blackmailing them?"
            mary "Or is she working for them and hence the cameras and recordings?"

            scene day_08_scene_07_flash_drive_73 with dissolve
            mc "I have no idea, but it looks more like surveillance than cooperation."
            mc "We need to find out what kind of people are on this list."
            mc "Then maybe it will be easier for us to determine her intentions."

            scene day_08_scene_07_flash_drive_74 with dissolve
            mc "Where is Khloe?"
            mary "I don't know, she was just here."
            mc "Khloe!"
            kh "I'm coming, why are you yelling?"

            scene day_08_scene_07_flash_drive_75 with dissolve
            kh "What happened?"
            mc "I have a job for you."
            kh "Finally!"

            scene day_08_scene_07_flash_drive_76 with dissolve
            mc "You will go to this address."
            mc "The apartment is located on the third floor. Here's the key."

            scene day_08_scene_07_flash_drive_77 with dissolve
            mc "I want you to thoroughly search this apartment."
            mc "Any corner, nook and cranny. Just as you always do."

            scene day_08_scene_07_flash_drive_78 with dissolve
            mc "Besides, I want you to follow the woman who lives there. Her name is Keira."
            mc "I want to know her every move. What she does, what her habits are, who she meets. Everything."
            kh "Sure, I know what to do."

            scene day_08_scene_07_flash_drive_79 with dissolve
            mary "[player_name], you don't think she sent us this package?"
            mc "Of course not."
            mc "I am convinced that the sender deliberately indicated this address to show us this apartment, and as such, it is a priority for us at the moment."

            scene day_08_scene_07_flash_drive_80 with dissolve
            mc "There must be something in this apartment that will allow us to move forward."
            mc "I have the impression that Keira and her business is just a random bonus."
            mc "Did you manage to do something with this flash drive?"

            scene day_08_scene_07_flash_drive_81 with dissolve
            mary "Not yet, but I was wrong on which cipher it is."
            mc "I guess this is good news."
            mary "I'll do my magic and get full access to the original files."

            scene day_08_scene_07_flash_drive_82 with dissolve
            mc "Great, I can't wait to find out what we have."
            mary "It'll take a while so you have to be patient."
            mc "I understand."

            scene day_08_scene_07_flash_drive_83 with dissolve
            mc "Oh, and Khloe, I'd like you to rip the contents of all the disks you find in that apartment."
            mary "Don't worry about that. Khloe knows what to do."

            scene day_08_scene_07_flash_drive_84 with dissolve
            mc "Okay. I'm going to Ming. I have to give her money."
            mc "I'll probably be back late."
            mc "Khloe... be careful."

            scene day_08_scene_07_flash_drive_85 with dissolve
            kh "As always, boss."
            mary "You take care of yourself too."
            mc "See you tonight."

            jump day_08_scene_08

        else:

            scene day_08_scene_07_flash_drive_68 with dissolve
            "{color=#D2691E}*Some time later you enter the house.*{/color}"
            mary "It's good to see you."

            scene day_08_scene_07_flash_drive_69 with dissolve
            mary "Did you manage to find something?"
            mc "Yes. The woman who decrypted the flash drive for me lives at this address."

            scene day_08_scene_07_flash_drive_70 with dissolve
            mary "Are you kidding?"
            mc "No."

            scene day_08_scene_07_flash_drive_72 with dissolve
            mc "I was just about to enter the building when the door opened and two women almost bumped into me."
            mary "One of them was Keira. I don't know the other one."

            scene day_08_scene_07_flash_drive_73 with dissolve
            mary "Do you think she lives there?"
            mc " For sure."
            mary "I don't understand it."
            mc "Believe me, so do I."

            scene day_08_scene_07_flash_drive_74 with dissolve
            mc "Where is Khloe?"
            mary "I don't know, she was just here."
            mc "Khloe!"
            kh "I'm coming, why are you yelling?"

            scene day_08_scene_07_flash_drive_75 with dissolve
            kh "What happened?"
            mc "I have a job for you."
            kh "Finally!"

            scene day_08_scene_07_flash_drive_76 with dissolve
            mc "You will go to this address."
            mc "Here's the key. Determine if this key fits into any of the apartments."
            mc "If so, I want you to search this apartment thoroughly, but so as not to leave any trail."

            scene day_08_scene_07_flash_drive_77 with dissolve
            mc "Any corner, nook and cranny. Just as you can."
            mc "I would go with you, but I can't show up there anymore."
            kh "No problem."

            scene day_08_scene_07_flash_drive_78 with dissolve
            mc "Besides, I want you to follow the woman who lives there. Her name is Keira."
            mc "I want to know her every move. What she does, what her habits are, who she meets. Everything."
            kh "Sure, I know what to do."

            scene day_08_scene_07_flash_drive_79 with dissolve
            mary "[player_name], you don't think she sent us this package?"
            mc "Of course not."
            mc "I am convinced that the sender deliberately indicated this address to show us this apartment, and as such, it is a priority for us at the moment."

            scene day_08_scene_07_flash_drive_80 with dissolve
            mc "There must be something in this apartment that will allow us to move forward."
            mc "Did you manage to do something with this flash drive?"

            scene day_08_scene_07_flash_drive_81 with dissolve
            mary "Not yet, but this is not the cipher I told you about."
            mc "I guess this is a good news."
            mary "Yes, I'll do some magic and I should get full access to the original files."

            scene day_08_scene_07_flash_drive_82 with dissolve
            mc "Great, I can't wait to find out what we have there."
            mary "You have to be patient, because it's gonna take a while."
            mc "I understand."

            scene day_08_scene_07_flash_drive_83 with dissolve
            mc "Oh, and Khloe, I'd like you to copy the contents of all the disks you find in that apartment."
            mc "Mary will explain you what to do."
            mary "Don't worry about that. Khloe knows what to do."

            scene day_08_scene_07_flash_drive_84 with dissolve
            mc "Okay. I'm going to Ming. I have to give her money."
            mc "I'll probably be back late."
            mc "Khloe... be careful."

            scene day_08_scene_07_flash_drive_85 with dissolve
            kh "As always, boss."
            mary "You take care of yourself too."
            mc "See you tonight."

            jump day_08_scene_08

    else:

        scene day_08_scene_07_flash_drive_17 with dissolve
        "{color=#D2691E}*You both keep quiet for a while hugging each other.*{/color}"
        mc "Okay, enough of these memories."
        mc "I gave you the flash drive few days ago. Did you manage to encrypt its content?"

        scene day_08_scene_07_flash_drive_19 with dissolve
        mary "Yes, but there is something wrong with the files and I haven't been able to determine what it is about yet."
        mc "Okay, could you show me?"

        scene day_08_scene_07_flash_drive_20 with dissolve
        "{color=#D2691E}*Mary clicks on the first file and lots of numbers and letters appear on the screen.*{/color}"
        mc "What the fuck is this?"
        mary "As I told you just now, I haven't figured it out yet."

        scene day_08_scene_07_flash_drive_21 with dissolve
        mc "Open another one."

        scene day_08_scene_07_flash_drive_22 with dissolve
        "{color=#D2691E}*Mary opens another file, but its content is as strange as the first one.*{/color}"
        "{color=#D2691E}*Mary checks a few more, but the effect is the same.*{/color}"

        scene day_08_scene_07_flash_drive_26 with dissolve
        mary "It seems to me that someone additionally used some kind of data encryption system."
        mary "There are many of them, but it seems to me that in our case Rijndael code was used."

        scene day_08_scene_07_flash_drive_27 with dissolve
        mc "I never heard about it."
        mary "Well, anyone who wants to access information must have an encryption key to decrypt the file and restore it to a readable format."
        mc "So we can't do anything without this key?"
        mary "I am afraid there may be a problem with this."

        scene day_08_scene_07_flash_drive_28 with dissolve
        mc "Fuck!"
        mc "Why did someone send me this if I can't read it?"
        mary "I don't know. I don't understand it either."

        scene day_08_scene_07_flash_drive_29 with dissolve
        mc "Maybe this key is stored somewhere on this flash drive?"
        mary "Maybe, but I haven't found anything so far."
        mc "Goddamnit."

        scene day_08_scene_07_flash_drive_30 with dissolve
        mc "I was hoping that we would find something here that would allow us to move on, and then there is another problem."
        mc "I've had enough of this."
        mary "Don't get upset."

        scene day_08_scene_07_flash_drive_31 with dissolve
        mary "Give me some time, I'll try to come up with something."
        mary "I will carefully check every file, maybe only some have been encrypted."
        mc "Okay."

        scene day_08_scene_07_flash_drive_32 with dissolve
        "{color=#D2691E}*You're circling around the room wondering what to do next.*{/color}"
        mc "We completely forgot about the key that was in the package with this flash drive."
        mc "It was sent for a reason."

        scene day_08_scene_07_flash_drive_33 with dissolve
        mary "I agree, but how do we determine what this key is for?"
        mc "Maybe it has something to do with the sender of the package?"
        mc "Have you managed to determine who sent it?"

        scene day_08_scene_07_flash_drive_34 with dissolve
        mary "I only have an address, but I have no idea if this is the real one."
        mc "Okay. That's something to start with."

        scene day_08_scene_07_flash_drive_35 with dissolve
        mc "I'll take this key and go check this address, and you try to decrypt these files in the meantime."
        mary "Okay, but I' m begging you, be careful."

        scene black with dissolve
        show bg one_hour_later with dissolve
        $ renpy.pause()

        scene day_08_scene_07_flash_drive_36 with dissolve
        "{color=#D2691E}*Less than an hour later you park your car by the sidewalk.*{/color}"

        scene day_08_scene_07_flash_drive_37 with dissolve
        "{color=#D2691E}*You get out of the car and look around.*{/color}"
        "{color=#D2691E}*You have a strange feeling that you know this place, that you've been here before.*{/color}"

        scene day_08_scene_07_flash_drive_38 with dissolve
        "{color=#D2691E}*You look at the building.*{/color}"
        "{color=#D2691E}*You've definitely been here before, but you can't remember when or why.*{/color}"

        scene day_08_scene_07_flash_drive_39 with dissolve
        "{color=#D2691E}*You look around trying to remember anything, but nothing comes to your mind.*{/color}"
        "{color=#D2691E}*Annoyed by this, you get in the car.*{/color}"

        scene day_08_scene_07_flash_drive_40 with dissolve
        mc "Fuck me, I'm getting old if I can't remember such simple things..."
        mc "I know I've been here before, why can't I remember anything?"

        scene day_08_scene_07_flash_drive_41 with dissolve
        "{color=#D2691E}*You're wondering what to do now.*{/color}"
        "{color=#D2691E}*Whether to simply enter the building or will it be safer to wait and watch?*{/color}"

        menu enter_the_building_a:

            "{color=#74B2F4}Wait.{/color} [KeiraPath]":

                scene day_08_scene_07_flash_drive_42 with dissolve
                "{color=#D2691E}*You decide to wait.*{/color}"
                "{color=#D2691E}*Time passes by slowly, seconds becoming minutes.*{/color}"
                "{color=#D2691E}*You hate to wait.*{/color}"

                scene day_08_scene_07_flash_drive_43 with dissolve
                "{color=#D2691E}*Just as you are about to get out of the car when the door to the building opens and two women come out.*{/color}"
                "{color=#D2691E}*You look at them closely.*{/color}"

                scene day_08_scene_07_flash_drive_44 with dissolve
                mc "Fuck! It's Keira."
                mc "What the fuck is going on here?"

                scene day_08_scene_07_flash_drive_45 with dissolve
                "{color=#D2691E}*You wait for the women to disappear around the corner and get out of the car.*{/color}"
                "{color=#D2691E}*You quickly cross the street and enter the building.*{/color}"

                scene day_08_scene_07_flash_drive_46 with dissolve
                "{color=#D2691E}*You take the key out of your pocket and start climbing the stairs to the 1st floor.*{/color}"
                "{color=#D2691E}*It turns out that there are two apartments there. You look at the key and then carefully at the doors and locks.*{/color}"

                scene day_08_scene_07_flash_drive_47 with dissolve
                "{color=#D2691E}*Your key doesn't work on those doors.*{/color}"
                "{color=#D2691E}*You move up to the 2nd floor and try again but still no luck.*{/color}"

                scene day_08_scene_07_flash_drive_48 with dissolve
                "{color=#D2691E}*You only have one floor left. You're going up the stairs.*{/color}"
                "{color=#D2691E}*There's only one door on the 3rd floor. When you look at it you get that strange feeling again.*{/color}"
                mc "I've been here before."

                scene day_08_scene_07_flash_drive_49 with dissolve
                "{color=#D2691E}*You take time wondering what to do now.*{/color}"
                "{color=#D2691E}*KNOCK KNOCK.*{/color}"

                scene day_08_scene_07_flash_drive_50 with dissolve
                "{color=#D2691E}*Silence.*{/color}"
                "{color=#D2691E}*You take the key and put it in the lock. You turn it carefully.*{/color}"
                "{color=#D2691E}*You hear the sound of the pawls moving.*{/color}"

                scene day_08_scene_07_flash_drive_51 with dissolve
                "{color=#D2691E}*You turn the key and the lock opens, allowing you entry.*{/color}"
                "{color=#D2691E}*You enter carefully.*{/color}"

                scene day_08_scene_07_flash_drive_52 with dissolve
                "{color=#D2691E}*You enter the living room and start a thorough search of the apartment.*{/color}"
                "{color=#D2691E}*You are looking for anything to help uncover the truth.*{/color}"
                "{color=#D2691E}*Unfortunately, you don't find anything in the living room.*{/color}"

                scene day_08_scene_07_flash_drive_53 with dissolve
                "{color=#D2691E}*You go to the next room.*{/color}"

                scene day_08_scene_07_flash_drive_54 with dissolve
                "{color=#D2691E}*You look into the closet standing in the corner, but all you find there are women's clothes.*{/color}"

                scene day_08_scene_07_flash_drive_55 with dissolve
                "{color=#D2691E}*You go on and enter the next room.*{/color}"
                "{color=#D2691E}*There's a large desk in the middle and several monitors on it.*{/color}"

                scene day_08_scene_07_flash_drive_56 with dissolve
                "{color=#D2691E}*You move closer and look at them.*{/color}"

                scene day_08_scene_07_flash_drive_57 with dissolve
                mc "Hmmm, this looks like a camera monitoring station."
                mc "Is it monitoring?"

                scene day_08_scene_07_flash_drive_58 with dissolve
                "{color=#D2691E}*You sit behind a desk and start browsing through computer content.*{/color}"
                "{color=#D2691E}*You find a lot of video recordings in one of the directories.*{/color}"

                scene day_08_scene_07_flash_drive_59 with dissolve
                "{color=#D2691E}*You run the first file and see Keira appear on the screen at her desk and then you see a man enter a short while later.*{/color}"

                scene day_08_scene_07_flash_drive_60 with dissolve
                mc "What the fuck?"
                mc "Why is this bitch recording her meetings?"

                scene day_08_scene_07_flash_drive_61 with dissolve
                "{color=#D2691E}*You don't find anything interesting in several other files.*{/color}"
                "{color=#D2691E}*You continue your search and find a folder with a great many files named with dates and people's names.*{/color}"

                scene day_08_scene_07_flash_drive_62 with dissolve
                "{color=#D2691E}*In one of them you find more files with recordings.*{/color}"
                "{color=#D2691E}*This time, however, the files are sorted by the dates of the recordings and the names of people who were recorded.*{/color}"

                scene day_08_scene_07_flash_drive_63 with dissolve
                "{color=#D2691E}*The list is very long, but only one name catches your eye.*{/color}"
                "{color=#D2691E}*Ming.*{/color}"

                scene day_08_scene_07_flash_drive_64 with dissolve
                "{color=#D2691E}*You check all the files carefully and it turns out that there are over thirty with the name Ming.*{/color}"
                "{color=#D2691E}*You activate a trace program on the computer for Mary with your phone.*{/color}"

                scene day_08_scene_07_flash_drive_65 with dissolve
                "{color=#D2691E}*You turn everything off and hurry out of the apartment.*{/color}"
                "{color=#D2691E}*You get in the car and start the engine.*{/color}"

                scene day_08_scene_07_flash_drive_66 with dissolve
                "{color=#D2691E}*You're about to drive off when Keira comes around the corner.*{/color}"
                mc "Fuck, another minute and we'd run into each other."

                scene day_08_scene_07_flash_drive_67 with dissolve
                "{color=#D2691E}*You wait until she disappears inside the building and you leave.*{/color}"

                $ check_the_building = True

                jump day_08_scene_07_aa

            "{color=#74B2F4}Go in.{/color}":

                scene day_08_scene_07_flash_drive_67a with dissolve
                "{color=#D2691E}*You get out of the car and cross the street.*{/color}"

                scene day_08_scene_07_flash_drive_67b with dissolve
                "{color=#D2691E}*You walk up to the door when it suddenly opens.*{/color}"
                "{color=#D2691E}*Two women are leaving the building.*{/color}"

                scene day_08_scene_07_flash_drive_67c with dissolve
                "{color=#D2691E}*You look at them and freeze.*{/color}"
                ke "[player_name]?"
                mc "Keira?"

                scene day_08_scene_07_flash_drive_67d with dissolve
                ke "What are you doing here?"
                mc "I'm visiting a friend, but I think I got the wrong address."
                ke "Have a nice day."
                mc "Thanks, you too."

                scene day_08_scene_07_flash_drive_67f with dissolve
                "{color=#D2691E}*You get in the car and start the engine.*{/color}"

                scene day_08_scene_07_flash_drive_67g with dissolve
                "{color=#D2691E}*You leave in order to not cause any more suspicion.*{/color}"

                jump day_08_scene_07_aa

    label day_08_scene_07_aa:

        if check_the_building == True:

            scene day_08_scene_07_flash_drive_68 with dissolve
            "{color=#D2691E}*Thirty minutes later you enter the house.*{/color}"
            mary "It's good to see you."
            mary "We were starting to worry about you."

            scene day_08_scene_07_flash_drive_69 with dissolve
            mary "Did you manage to find anything?"
            mc "Yes. The woman I asked to decrypt the flash drive lives at this address."

            scene day_08_scene_07_flash_drive_70 with dissolve
            mary "Are you kidding?"
            mc "No. This is the key to her apartment."
            mc "I only found her computer and it had lots of videos.  I also installed your tracking program on her computer and took these pictures."

            scene day_08_scene_07_flash_drive_71 with dissolve
            "{color=#D2691E}*You sit next to Mary and show her pictures.*{/color}"
            mc "It looks like she has access to surveillance cameras from all over this town and of certain people."
            mary "A serious matter."

            scene day_08_scene_07_flash_drive_72 with dissolve
            mary "You think she's blackmailing them?"
            mary "Or is she working for them and hence the cameras and recordings?"

            scene day_08_scene_07_flash_drive_73 with dissolve
            mc "I have no idea, but it looks more like surveillance than cooperation."
            mc "We need to find out what kind of people are on this list."
            mc "Then maybe it will be easier for us to determine her intentions."

            scene day_08_scene_07_flash_drive_74 with dissolve
            mc "Where is Khloe?"
            mary "I don't know, she was just here."
            mc "Khloe!"
            kh "I'm coming, why are you yelling?"

            scene day_08_scene_07_flash_drive_75 with dissolve
            kh "What happened?"
            mc "I have a job for you."
            kh "Finally!"

            scene day_08_scene_07_flash_drive_76 with dissolve
            mc "You will go to this address."
            mc "The apartment is located on the third floor. Here's the key."

            scene day_08_scene_07_flash_drive_77 with dissolve
            mc "I want you to thoroughly search this apartment."
            mc "Any corner, nook and cranny. Just as you always do."

            scene day_08_scene_07_flash_drive_78 with dissolve
            mc "Besides, I want you to follow the woman who lives there. Her name is Keira."
            mc "I want to know her every move. What she does, what her habits are, who she meets. Everything."
            kh "Sure, I know what to do."

            scene day_08_scene_07_flash_drive_80 with dissolve
            mc "There must be something in this apartment that will allow us to move forward."
            mc "I have the impression that Keira and her business is just a random bonus."
            mc "Did you manage to do something with this flash drive?"

            scene day_08_scene_07_flash_drive_81 with dissolve
            mary "Not yet, but I was wrong on which cipher it is."
            mc "I guess this is good news."
            mary "I'll do my magic and get full access to the original files."

            scene day_08_scene_07_flash_drive_82 with dissolve
            mc "Great, I can't wait to find out what we have."
            mary "It'll take a while so you have to be patient."
            mc "I understand."

            scene day_08_scene_07_flash_drive_83 with dissolve
            mc "Oh, and Khloe, I'd like you to rip the contents of all the disks you find in that apartment."
            mary "Don't worry about that. Khloe knows what to do."

            scene day_08_scene_07_flash_drive_84 with dissolve
            mc "Okay. I'm going to Ming. I have to give her money."
            mc "I'll probably be back late."
            mc "Khloe... be careful."

            scene day_08_scene_07_flash_drive_85 with dissolve
            kh "As always, boss."
            mary "You take care of yourself too."
            mc "See you tonight."

            jump day_08_scene_08

        else:

            scene day_08_scene_07_flash_drive_68 with dissolve
            "{color=#D2691E}*Some time later you enter the house.*{/color}"
            mary "It's good to see you."

            scene day_08_scene_07_flash_drive_69 with dissolve
            mary "Did you manage to find something?"
            mc "Yes. The woman I asked to decrypt the flash drive lives at this address."

            scene day_08_scene_07_flash_drive_70 with dissolve
            mary "Are you kidding?"
            mc "No."

            scene day_08_scene_07_flash_drive_73 with dissolve
            mc "I was just about to enter the building when the door opened and two women almost bumped into me."
            mary "One of them was Keira. I don't know the other one."

            scene day_08_scene_07_flash_drive_74 with dissolve
            mc "Where is Khloe?"
            mary "I don't know, she was just here."
            mc "Khloe!"
            kh "I'm coming, why are you yelling?"

            scene day_08_scene_07_flash_drive_75 with dissolve
            kh "What happened?"
            mc "I have a job for you."
            kh "Finally!"

            scene day_08_scene_07_flash_drive_76 with dissolve
            mc "You will go to this address."
            mc "Here's the key. Find out if this key fits into any of the apartments."
            mc "If so, I want you to search this apartment thoroughly, but so as not to leave any trail."

            scene day_08_scene_07_flash_drive_77 with dissolve
            mc "Any corner, nook and cranny. Just as you always do."
            mc "I would go with you, but I can't show up there anymore."
            kh "No problem."

            scene day_08_scene_07_flash_drive_80 with dissolve
            mc "There must be something in this apartment that will allow us to move forward."
            mc "Did you manage to do something with this flash drive?"

            scene day_08_scene_07_flash_drive_81 with dissolve
            mary "Not yet, but I was wrong on which cipher it is."
            mc "I guess this is good news."
            mary "I'll do my magic and get full access to the original files."

            scene day_08_scene_07_flash_drive_82 with dissolve
            mc "Great, I can't wait to find out what's hidden there."
            mary "It'll take a while so you have to be patient."
            mc "I understand."

            scene day_08_scene_07_flash_drive_83 with dissolve
            mc "Oh, and Khloe, I'd like you to copy the contents of all the disks you find in that apartment."
            mc "Mary will explain you what to do."
            mary "Don't worry about that. Khloe knows what to do."

            scene day_08_scene_07_flash_drive_84 with dissolve
            mc "Okay. I'm going to Ming. I have to give her money."
            mc "I'll probably be back late."
            mc "Khloe... be careful."

            scene day_08_scene_07_flash_drive_85 with dissolve
            kh "As always, boss."
            mary "You take care of yourself too."
            mc "See you tonight."

            jump day_08_scene_08


#####################################################################################################################################################
                                                    ############# SCENE 08 - PAYMENT DAY#############    done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_08:

    scene black with dissolve
    show bg some_time_later with dissolve
    $ renpy.pause()

    scene day_08_scene_08_payment_1 with dissolve
    "{color=#D2691E}*You check your watch and it's 7:30pm."
    "{color=#D2691E}*You only have half an hour left to deliver the money you promised Ming.*{/color}"

    scene day_08_scene_08_payment_2 with dissolve
    "{color=#D2691E}*You park your car in front of the club.*{/color}"
    "{color=#D2691E}*You take a briefcase with the money and get out of the car.*{/color}"

    scene day_08_scene_08_payment_3 with dissolve
    "{color=#D2691E}*There are two bodyguards standing in front of the entrance to the club.*{/color}"
    "{color=#D2691E}*You approach them and after a brief chat they let you in.*{/color}"

    scene day_08_scene_08_payment_4 with dissolve
    "{color=#D2691E}*KNOCK KNOCK*{/color}"
    ming "Come in!"

    scene day_08_scene_08_payment_5 with dissolve
    mc "Good evening."
    ming "I was starting to think you were not coming."

    scene day_08_scene_08_payment_6 with dissolve
    mc "Sorry, but I had a lot of work to do today."
    ming "You brought the money?"
    mc "Of course."

    scene day_08_scene_08_payment_7 with dissolve
    "{color=#D2691E}*You put your briefcase on her desk.*{/color}"
    mc "$150,000 as we agreed."

    scene day_08_scene_08_payment_8 with dissolve
    ming "Great."
    ming "Have a seat, would you like a drink?"

    scene day_08_scene_08_payment_9 with dissolve
    mc "No, thank you."
    mc "Did Linda cause any problems?"

    scene day_08_scene_08_payment_10 with dissolve
    ming "No, everything went according to plan."
    mc "That's good."

    scene day_08_scene_08_payment_11 with dissolve
    ming "How long should I keep her here?"
    mc "A few more days."

    scene day_08_scene_08_payment_12 with dissolve
    mc "I have to prepare everything thoroughly before I can take her from you."
    mc "Is that a problem?"

    scene day_08_scene_08_payment_13 with dissolve
    ming "Absolutely not."
    mc "That's good."

    scene day_08_scene_08_payment_14 with dissolve
    mc "I was wondering how to take her away from here and I was hoping you'd be willing to do something else for me as part of this."
    ming "What do you mean?"

    scene day_08_scene_08_payment_15 with dissolve
    mc "She once told me that if she does not pay your debts, you will sell her as a slave."
    ming "Oh? She told you that?"

    scene day_08_scene_08_payment_16 with dissolve
    mc "More or less."
    ming "So what? I have to do a little show so that she feels like I want to sell her?"

    scene day_08_scene_08_payment_17 with dissolve
    ming "And you will be the one to buy her?"
    mc "Exactly."
    mc "I just don't want her to know that I'm buying her."

    scene day_08_scene_08_payment_18 with dissolve
    "{color=#D2691E}*Ming looks at you closely.*{/color}"
    ming "You look like such a nice man but you really are a demon inside!"
    ming "Okay."

    scene day_08_scene_08_payment_19 with dissolve
    ming "You have fulfilled your part of our agreement, so now it's my turn."
    ming "In two days I will organize a show for her."

    scene day_08_scene_08_payment_20 with dissolve
    ming "Two days from now be here at 11pm."
    mc "In two days I can not do it. I'm leaving on business and I'm not coming back until Friday."

    scene day_08_scene_08_payment_21 with dissolve
    mc "We can do it either tomorrow or after my return."
    ming "Eh... Okay, let's do it tomorrow. Be here at 11pm."

    scene day_08_scene_08_payment_22 with dissolve
    mc "I will."
    ming "I'll see you tomorrow."

    scene day_08_scene_08_payment_23 with dissolve
    ming "Have a nice evening, Mr. [player_surname]."
    mc "Thank you."
    mc "Have a nice evening, Miss Ming."

    jump day_08_scene_09

#####################################################################################################################################################
                                                    ############# SCENE 09 - PUNISHMENT FOR NICOLE#############   done and rendered - fixed
#####################################################################################################################################################
label day_08_scene_09:

    if nicole_helped == True:

        jump day_08_scene_10

    else:

        scene black with dissolve
        show bg some_time_later with dissolve
        $ renpy.pause()

        scene day_08_scene_09_punishment_1 with dissolve
        "{color=#D2691E}*Your visit to see Ming has taken a little longer than expected and as you drive up to Nicole's house, the sun is already slowly setting behind the horizon.*{/color}"
        "{color=#D2691E}*Nicole is at the door and waiting for you.*{/color}"

        scene day_08_scene_09_punishment_2 with dissolve
        "{color=#D2691E}*You get out of the car.*{/color}"
        "{color=#D2691E}*Nicole's taking a step in your direction.*{/color}"
        n "You're late!"

        menu nicole_punishment_day_8:

            "{color=#74B2F4}Ignore her.{/color}":

                scene day_08_scene_09_punishment_5 with dissolve
                mc "Have you finally made a decision?"

                scene day_08_scene_09_punishment_6 with dissolve
                "{color=#D2691E}*Nicole's looking at you insecure.*{/color}"
                n "Could we talk about this somewhere else?"
                mc "What difference does it make?"

            "{color=#74B2F4}Retort.{/color} [NicoleSubmissionPath]":

                scene day_08_scene_09_punishment_3 with dissolve
                "{color=#D2691E}*You look at her with amusement.*{/color}"
                mc "I had more important things to do."
                mc "You are not my only problem."

                scene day_08_scene_09_punishment_4 with dissolve
                "{color=#D2691E}*Your reaction has knocked Nicole off the trail, she's lowering her head and staring at the ground.*{/color}"
                mc "You're not the navel of the world. Try to remember about that."
                n "Yes... I know... sorry..."

                scene day_08_scene_09_punishment_5 with dissolve
                mc "Have you finally made a decision?"

                scene day_08_scene_09_punishment_6 with dissolve
                "{color=#D2691E}*Nicole's looking at you insecure.*{/color}"
                n "Could we talk about this somewhere else?"
                mc "What difference does it make?"
                $ nicole_submission += 1

                scene day_08_scene_09_punishment_7 with dissolve
                mc "Are you ashamed of me and don't want me to be seen with you?"
                n "No, of course not."
                n "..."
                mc "Where do you want to talk?"

                scene day_08_scene_09_punishment_8 with dissolve
                n "Maybe in the garden?"
                mc "Ok, but I don't  see you moving to there!"

                scene day_08_scene_09_punishment_9 with dissolve
                "{color=#D2691E}*Nicole avoids your eyesight and remains silent.*{/color}"
                mc "Nicole, for fuck sake! I'm losing patience, so you better start talking now."
                n "Well, I was thinking about what you told me..."

                scene day_08_scene_09_punishment_10 with dissolve
                mc "Fuck, Nicole, can you finally get it out of your head?"
                mc "Are you so dumb that you can't form a simple sentence?"

                scene day_08_scene_09_punishment_11 with dissolve
                mc "If you had to lie to me, you had no problem with it, and now what?"
                mc "Suddenly you have nothing to say to me?"

                scene day_08_scene_09_punishment_12 with dissolve
                "{color=#D2691E}*You are waiting for Nicole to say something, but she's silent staring at the ground.*{/color}"
                mc "I've had enough of this."
                mc "Put a dildo up your ass and beg for money every time he tells you to."
                mc "Your choice."

                scene day_08_scene_09_punishment_13 with dissolve
                "{color=#D2691E}*Nicole looks at you with terror in her eyes.*{/color}"
                mc "I've given you a chance, but you're pissing me off again."
                mc "All I wanted from you was sincerity and a little respect, and what did I get in return?"
                mc "All lies."

                scene day_08_scene_09_punishment_14 with dissolve
                mc "Who do you think I am?"
                mc "A horny little shit who only thinks about seeing your tits?"
                mc "Have you fallen so low?"

                scene day_08_scene_09_punishment_15 with dissolve
                mc "You have taken over all the worst qualities of your mother."
                mc "All that matters to you is money."

                scene day_08_scene_09_punishment_16 with dissolve
                mc "What happened to the lovely Nicole I knew and loved?"
                mc "You are a completely different person, a person without feelings, a person who does not know what friendship, love, sincerity and trust are."
                mc "I despise you."

                scene day_08_scene_09_punishment_17 with dissolve
                "{color=#D2691E}*You turn around and want to leave, but Nicole grabs your hand.*{/color}"
                $ nicole_submission += 2

                menu what_do_you_want:

                    "{color=#74B2F4}Ignore her and leave.{/color}":

                        scene day_08_scene_09_punishment_17 with dissolve
                        "{color=#D2691E}*You ignore her and despite her begging, you are leaving.*{/color}"

                        jump day_08_scene_10

                    "{color=#74B2F4}Humiliate her more.{/color} [NicoleSubmissionPath]":

                        scene day_08_scene_09_punishment_17 with dissolve
                        mc "What do you want from me, Nicole?"
                        mc "What do you really care about?"

                        scene day_08_scene_09_punishment_18 with dissolve
                        mc "For fuck sake, say something, or get the fuck away from me once and for all."
                        mc "I have neither the time nor the desire to deal with you."

                        scene day_08_scene_09_punishment_19 with dissolve
                        n "I..."
                        mc "Yes?"
                        n "Help me..."

                        scene day_08_scene_09_punishment_20 with dissolve
                        mc "Fuck me, Nicole."
                        mc "I didn't think you were that stupid."
                        mc "I just told you what I want from you, and you still can't do it."

                        scene day_08_scene_09_punishment_21 with dissolve
                        mc "You're empty as a blowfish."
                        mc "You have no feelings."
                        mc "I can't help you, I'm sorry."

                        scene day_08_scene_09_punishment_22 with dissolve
                        mc "You don't even deserve a little compassion."
                        mc "The Nicole I knew doesn't exist anymore, and you are a stranger to me."
                        mc "Rejoice for yourself."

                        scene day_08_scene_09_punishment_23 with dissolve
                        "{color=#D2691E}*You look at Nicole and you see that her conceit, confidence and contemptuous smile are gone.*{/color}"
                        "{color=#D2691E}*She finally realized that she had lost this battle and the powerlessness paralyzed her.*{/color}"
                        n "You are right. I am nobody."

                        scene day_08_scene_09_punishment_24 with dissolve
                        n "I always have been."
                        n "I'm sorry that I lied to you."
                        n "I only cared about your money."

                        scene day_08_scene_09_punishment_25 with dissolve
                        n "I wanted to finally free myself from this bastard who blackmails me."
                        mc "I don't believe a single word you say."
                        mc "Your conceit and self-confidence has eaten you up so much from the inside that it didn't occur to you to just come to me and say {i}Listen, I know I wasn't very nice to you, but I found myself in a difficult financial situation and I would like to ask you for a loan.{/i}"
                        mc "{i}I'll give you everything back as soon as I can.{/i}"

                        scene day_08_scene_09_punishment_26 with dissolve
                        mc "That would be enough for me to give you the money and believe me, it wouldn't even cross my mind to ask you to pay it back."
                        mc "But you don't care about the feelings of others, just like your mother."
                        mc "It's a shame to see what she made of you."

                        scene day_08_scene_09_punishment_27 with dissolve
                        n "[player_name]... I'm sorry..."
                        mc "Your apologies mean nothing to me."

                        scene day_08_scene_09_punishment_28 with dissolve
                        n "Don't say that."
                        mc "I wanted us to rebuild our relationship, but now I don't want to know you."

                        scene day_08_scene_09_punishment_29 with dissolve
                        "{color=#D2691E}*You want to leave, but Nicole is grabbing your hand again.*{/color}"
                        mc "Leave me alone."
                        n "I beg you."

                        scene day_08_scene_09_punishment_30 with dissolve
                        mc "I already told you you're nothing to me."
                        mc "I can't help you."

                        scene day_08_scene_09_punishment_31 with dissolve
                        n "I'll do whatever you want me to do. Look..."

                        scene day_08_scene_09_punishment_32 with dissolve
                        "{color=#D2691E}*Nicole removes her dress letting it fall freely to the ground.*{/color}"
                        "{color=#D2691E}*Nicole lowers her head and speaks in a quiet voice.*{/color}"
                        n "Do what you want with me. I deserved it."

                        scene day_08_scene_09_punishment_33 with dissolve
                        "{color=#D2691E}*You look at her with contempt, turn around and leave without a word.*{/color}"

                        $ nicole_submission += 1

                        jump day_08_scene_10

#####################################################################################################################################################
                                                    ############# SCENE 10 - BAD NEWS#############   done and rendered
#####################################################################################################################################################
label day_08_scene_10:

    scene black with dissolve
    show bg later_this_night with dissolve
    $ renpy.pause()

    scene day_08_scene_10_isabella_1 with dissolve
    "{color=#D2691E}*Isabella returns home.*{/color}"
    "{color=#D2691E}*It's already dark.*{/color}"

    scene day_08_scene_10_isabella_2 with dissolve
    "{color=#D2691E}*She had to stay longer at work to prepare everything with Sandra and Holly for tomorrow's meeting.*{/color}"

    scene day_08_scene_10_isabella_3 with dissolve
    "{color=#D2691E}*She missed the last bus and she couldn't find any cab anywhere.*{/color}"
    "{color=#D2691E}*She has no choice but to walk home.*{/color}"

    scene day_08_scene_10_isabella_4 with dissolve
    "{color=#D2691E}*She's already about halfway home, when she sees some movement behind her.*{/color}"

    scene day_08_scene_10_isabella_5 with dissolve
    "{color=#D2691E}*She speeds up her steps and slowly turns her head.*{/color}"
    "{color=#D2691E}*There is no one there.*{/color}"

    scene day_08_scene_10_isabella_6 with dissolve
    "{color=#D2691E}*She's going faster and faster.*{/color}"
    "{color=#D2691E}*She wants to run, but in heels it's impossible.*{/color}"

    scene day_08_scene_10_isabella_7 with dissolve
    "{color=#D2691E}*She turns around again.*{/color}"
    "{color=#D2691E}*This time she notices a man hiding in the dark.*{/color}"

    scene day_08_scene_10_isabella_8 with dissolve
    "{color=#D2691E}*Her heart is beating like crazy.*{/color}"
    "{color=#D2691E}*She takes off her shoes and starts running.*{/color}"

    scene day_08_scene_10_isabella_9 with dissolve
    "{color=#D2691E}*She turns around again.*{/color}"
    "{color=#D2691E}*He is still there.*{/color}"

    scene day_08_scene_10_isabella_10 with dissolve
    "{color=#D2691E}*She suddenly hears the squeal of tires and a loud horn.*{/color}"

    scene day_08_scene_10_isabella_11 with dissolve
    "{color=#D2691E}*Only now she notices that she ran into the street without looking.*{/color}"
    "{color=#D2691E}*She was almost run over by a car.*{/color}"

    scene day_08_scene_10_isabella_12 with dissolve
    "{color=#D2691E}*Isabella raises her hand and smiles appologeticly.*{/color}"

    scene day_08_scene_10_isabella_13 with dissolve
    "{color=#D2691E}*The man driving the car opens the door and gets out.*{/color}"

    scene day_08_scene_10_isabella_14 with dissolve
    man "Are you okay?"
    i "Yes... I'm fine."
    i "I'm very sorry, sir, but someone was chasing me."

    scene day_08_scene_10_isabella_15 with dissolve
    "{color=#D2691E}*The driver is looking around carefully."
    man "Are you sure? No one's here."
    i "Yes, there was a man on the other side of street, hiding in the dark."

    scene day_08_scene_10_isabella_16 with dissolve
    man "Call the police?"
    i "Thank you but there is no need, I will handle it."

    scene day_08_scene_10_isabella_17 with dissolve
    "{color=#D2691E}*He nods.*{/color}"
    man "Then would you like a ride home?"

    scene day_08_scene_10_isabella_18 with dissolve
    "{color=#D2691E}*A cab comes around the corner.*{/color}"

    scene day_08_scene_10_isabella_19 with dissolve
    i "Thank you for you kind offer but I wil take that cab there. Again, I am very sorry for being so careless."

    scene day_08_scene_10_isabella_20 with dissolve
    "{color=#D2691E}*She gets in the cab.*{/color}"

    scene day_08_scene_10_isabella_21 with dissolve
    "{color=#D2691E}*The car is slowly moving and Isabella looks back again to see if it was all a trick of her mind.*{/color}"
    "{color=#D2691E}*To her horror, a mysterious figure emerges from the shadows near by.*{/color}"

    scene day_08_scene_10_isabella_22 with dissolve
    "{color=#D2691E}*Isabella trembles in fear and starts to cry.*{/color}"

    scene day_08_scene_10_isabella_23 with dissolve
    "{color=#D2691E}*A few minutes later she gets out in front of her house.*{/color}"
    "{color=#D2691E}*She quickly opens the door and goes inside.*{/color}"

    scene day_08_scene_10_isabella_24 with dissolve
    "{color=#D2691E}*Isabella locks and turns on all the lights.*{/color}"
    "{color=#D2691E}*She runs upstairs to the bedroom and collapses on the bed, trembling with fear.*{/color}"

    scene day_08_scene_10_isabella_25 with dissolve
    "{color=#D2691E}*Grabbing her phone she calls Sandra in panic.*{/color}"
    i "Sandra!"
    i "He's back!"

    scene day_08_scene_10_isabella_26 with dissolve
    s "What are you talking about? It's impossible."
    i "I'm telling you, I saw him!"
    i "He followed me on my way back from work, and yesterday I got a message from him."

    scene day_08_scene_10_isabella_27 with dissolve
    s "Are you sure it was him?"
    i "Yes!"

    scene day_08_scene_10_isabella_28 with dissolve
    s "But how is that possible?"
    s "He got 10 years in prison."

    scene day_08_scene_10_isabella_29 with dissolve
    s "He couldn't have gotten out so soon, even with good behavior."
    i "I don't know how this is possible, but I'm telling you I saw him."

    scene day_08_scene_10_isabella_30 with dissolve
    s "Okay, calm down. I'll check into it in the morning."
    s "Do you want me to come over?"

    scene day_08_scene_10_isabella_31 with dissolve
    i "No, I guess not."
    i "I've locked all the doors and windows, I should be fine."

    scene day_08_scene_10_isabella_32 with dissolve
    s "Well, if something happens, call me immediately."
    i "Okay, I will."
    s "I'll call you in the morning."

    jump day_08_scene_11

#####################################################################################################################################################
                                                    ############# SCENE 11 - ACCIDENT#############  done and rendered
#####################################################################################################################################################
label day_08_scene_11:

    scene black with dissolve
    show bg later_this_night with dissolve
    $ renpy.pause()

    scene day_08_accident_scene_1 with dissolve
    "{color=#D2691E}*Lost in thoughts about recent events, you didn't notice that you are about to blow right past your exit.*{/color}"
    "{color=#D2691E}*You stomp on the brakes, only then seeing the headlights in your rearview mirror.*{/color}"
    "{color=#D2691E}*You hear the squeal of rubber and a metallic crunch as your car rocked forward slightly.*{/color}"

    scene day_08_accident_scene_2 with dissolve
    "{color=#D2691E}*As you get out of your own car, you realize the vehicle that had hit you is a muscle car. The driver's side door opens and a pair of legs, step out of the car.*{/color}"
    "{color=#D2691E}*The girl is talking to someone on her phone, completely focused on inspecting her own vehicle.*{/color}"
    girl "No, there's no real damage."

    scene day_08_accident_scene_3 with dissolve
    girl "Maybe a scratch, but might've been there before."
    girl "No, they won't even notice it."
    girl "I don't know, some creep. He's staring at my ass right now."
    girl "Yeah, he's probably my dad's age."

    scene day_08_accident_scene_4 with dissolve
    "{color=#D2691E}*You can hear her friend's laughter through the phone as the girl gets back into her car, shooting you a look of disgust.*{/color}"

    scene day_08_accident_scene_4a with dissolve
    "{color=#D2691E}*She turns the key, the engine turning over and roaring to life, but as she tries to shut the door, you grab it, pulling it back open.*{/color}"
    girl "What the fuck is your problem, dude?"

    scene day_08_accident_scene_5 with dissolve
    mc "No damage?"
    "{color=#D2691E}*With any other young driver, you might've eaten the cost of the repair and tell them to be more careful, but something about her attitude is really getting under your skin.*{/color}"

    scene day_08_accident_scene_6 with dissolve
    "{color=#D2691E}*You grab her arm, wrenching her out of the car.*{/color}"
    girl "Ow, that hurts you asshole."

    scene day_08_accident_scene_7 with dissolve
    "{color=#D2691E}*You don't let go, instead pulling her forward, in between the two cars.*{/color}"
    mc "NO DAMAGE, HUH?"

    scene day_08_accident_scene_8 with dissolve
    "{color=#D2691E}*She cringes as you yell at her, and you can see tears already welling in her eyes.*{/color}"
    mc "Stop crying."

    scene day_08_accident_scene_9 with dissolve
    "{color=#D2691E}*She bends to inspect the large dent she had placed in your bumper.*{/color}"
    "{color=#D2691E}*Something about this girl is driving you crazy.*{/color}"

    scene day_08_accident_scene_9a with dissolve
    "{color=#D2691E}*You turn your head to face her and you notice that this time, rather than disgust, she is staring at you in fear.*{/color}"
    girl "I'm really sorry about your car, mister. But that doesn't mean..."

    scene day_08_accident_scene_10 with dissolve
    girl "You can't just put your hands on me!"
    mc "I know, I'm sorry. I'm just...it's been a long day. I shouldn't have taken it out on you. Let's just exchange insurance and we can both go on our way, okay?"

    scene day_08_accident_scene_11 with dissolve
    girl "Well, about that."
    mc "Please don't tell me you're not insured."
    girl "No, I am. It's just that, well, if I get in another accident, my mom is going to take my car away from me."

    scene day_08_accident_scene_12 with dissolve
    "{color=#D2691E}*She cooes sweetly.*{/color}"
    girl "Maybe, there's something else I could do for you?"

    scene day_08_accident_scene_13 with dissolve
    "{color=#D2691E}*She bites her lip.*{/color}"
    girl "You think I'm pretty, don't you?"
    girl "Maybe we could find somewhere private and I could give you a little show?"

    scene day_08_accident_scene_14 with dissolve
    mc "That's at least $2000 worth of damage right there, and you thought I'd let it slide for a little strip-tease, is that it?"
    girl "I saw you looking. Don't lie to me, I know what you want. I see the way you look at me, like all those other dirty old men."
    mc "I think it's best for both of us if you just give me your insurance info and leave, alright?"

    scene day_08_accident_scene_15 with dissolve
    "{color=#D2691E}*With the arrogance that can only come from a teenager, she shoves past you, sparing you one last hateful look before heading back to her car.*{/color}"
    girl "I'm leaving alright, but I'm not giving you shit. If you say anything about this accident, I'll let everyone of you neighbors know what a dirty pervert you are. I'll tell the whole town about you."
    mc "You leave and I'm calling the cops. You can tell anyone whatever you want, but checking out some 18-year old slut isn't a crime but leaving the scene of an accident is."

    scene day_08_accident_scene_16 with dissolve
    "{color=#D2691E}*She turns back to you with tears in her eyes.*{/color}"
    girl "Okay, look, I'm sorry for what I said. I..., maybe there is something I could do for you. Please? Just don't call the cops. Please?"

    scene day_08_accident_scene_17 with dissolve
    "{color=#D2691E}*You move closer to her that is when you smell it.*{/color}"
    mc "You've been drinking, haven't you?"
    girl "Yes..."

    scene day_08_accident_scene_18 with dissolve
    "{color=#D2691E}*She starts to sob and her body starts to tremble.*{/color}"
    girl "Please! Don't call the cops. We can work something out."
    mc "What your name?"

    scene day_08_accident_scene_19 with dissolve
    girl "Jessica."
    mc "Jessica what?"
    girl "Jessica Smith."
    $ jessica_enabled = True

    scene day_08_accident_scene_20 with dissolve
    jes "You're creeping me out, will you just tell me what you're going to do?"
    mc "I'm not going to do anything to you. I want to know what you are willing to offer me."

    scene day_08_accident_scene_21 with dissolve
    jes "What about a blowjob?"
    mc "This is a waste of time."

    scene day_08_accident_scene_22 with dissolve
    "{color=#D2691E}*You snap some pictures of both cars and the girl.*{/color}"
    mc "Surely you didn't think one blowjob was going to be enough to cover all the damage you did to my car, did you?"
    jes "No, I guess not."

    scene day_08_accident_scene_23 with dissolve
    mc "Here's how things are going to work."
    mc "I'm going to record you confessing to your role in the accident."
    mc "That means the texting and driving, the drinking. All of it."

    scene day_08_accident_scene_24 with dissolve
    mc "Then you're going to tell the camera that you offered to use your body to pay for the damage you caused so that you could stay out of trouble with your mom and the cops."
    jes "And then what?"
    mc "And then you will wait patiently for me to call you, wondering how you are going to pay your debt."

    scene day_08_accident_scene_25 with dissolve
    jes "I guess I don't really have much of a choice, do I?"
    mc "Of course, you have a choice. You can give me your insurance info, we can call the cops etc. Plenty of possibilities."
    jes "Allright. I will confess everything. Just don't call the cops or my mom."

    scene day_08_accident_scene_26 with dissolve
    "{color=#D2691E}*You take out your phone and turn the camera on.*{/color}"
    jes "My Name is Jessica Smith. I'm 19 years old. I was texting and driving tonight."
    jes "I also had been drinking tonight the I hit the car infront of me."

    scene day_08_accident_scene_27 with dissolve
    jes "He wanted my insurance information, but...in order to stay out of trouble with my mom and the cops..."
    jes "I decided to offer him to use me as payment for the damage I caused."
    jes "I offered him with sexual favors as a way of paying him back."

    scene day_08_accident_scene_28 with dissolve
    mc "Good girl."
    mc "Now give me your phone."

    scene day_08_accident_scene_29 with dissolve
    "{color=#D2691E}*You scroll through her pictures, select some of the racier shots she had stored and text them to yourself.*{/color}"
    "{color=#D2691E}*Then you scroll through her contact list, selecting entry for her mother and forward her contact information to yourself.*{/color}"
    jes "Why did you send my pictures to yourself?"

    scene day_08_accident_scene_30 with dissolve
    mc "Well, you can think of them as an insurance policy."
    jes "So, once we are even, you destroy them?"
    mc "Yes, I will get rid of them."

    scene day_08_accident_scene_31 with dissolve
    mc "We're done for now. You can go home."
    mc "I will be in touch so don't make anything stupid."
    jes "Okay. Thank you for not calling the cops."

    scene day_08_accident_scene_32 with dissolve
    "{color=#D2691E}*You get back to your car, turn the engine on and drive away leaving Jessica standing in the darkness.*{/color}"

    jump end_of_day_8

#####################################################################################################################################################
label end_of_day_8:

    hide screen map_button
    hide screen popup_wp

    scene silver1 with dissolve
    centered "{size=45}{font=fonts/GOTHIC.ttf}You've just reached the end of the current version of the game. \n \n I suggest you save the game here.{/font}{/size}"
    centered "{size=45}{font=fonts/GOTHIC.ttf}I hope you had a nice time playing \n \n {size=55}{b}{color=#D2691E}*REUNION.*{/color}{/size}"
    centered "{size=45}{font=fonts/GOTHIC.ttf}I hope to see you in the next installment of our story.{/font}{/size}"

    scene end_of_current_content_1 with dissolve
    $ renpy.pause ()

    scene title_screen with dissolve
    $ renpy.pause ()
    $ renpy.full_restart(target='_main_menu')
