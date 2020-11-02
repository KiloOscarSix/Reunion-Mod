init python:

    g = Gallery()

    g.button("Rain")
    g.unlock_image("rain.png")

    g.transition = dissolve

default persistent.galleryUnlocked = False

screen gallery_navigation():

    tag menu

    add "images/gallery_background.png"

    modal True

    hbox:
        xcenter 0.5
        ypos 75

        if persistent.galleryUnlocked:
            textbutton "Lock Scenes":
                action SetVariable("persistent.galleryUnlocked", False)
                text_size 50
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.galleryUnlocked", True)
                text_size 50

    vbox:
        style_prefix "gallery_nav"

        textbutton _("Linda") action [Show("gallery_linda"), Hide("gallery_navigation")]
        textbutton _("Lisa") action [Show("gallery_lisa"), Hide("gallery_navigation")]
        textbutton _("Jennifer") action [Show("gallery_jennifer"), Hide("gallery_navigation")]
        textbutton _("Kelly") action [Show("gallery_kelly"), Hide("gallery_navigation")]
        textbutton _("Nicole") action [Show("gallery_nicole"), Hide("gallery_navigation")]
        # textbutton _("Sandra") action [Show("gallery_sandra"), Hide("gallery_navigation")]
        textbutton _("Mary") action [Show("gallery_mary"), Hide("gallery_navigation")]
        textbutton _("Khloe") action [Show("gallery_khloe"), Hide("gallery_navigation")]
        textbutton _("Emily") action [Show("gallery_emily"), Hide("gallery_navigation")]
        textbutton _("Rachel") action [Show("gallery_rachel"), Hide("gallery_navigation")]
        textbutton _("Amy") action [Show("gallery_amy"), Hide("gallery_navigation")]

    vbox:
        style_prefix "gallery2_nav"

        xalign 0.9
        yalign 0.5
        spacing 23
        # textbutton _("Karen") action [Show("gallery_karen"), Hide("gallery_navigation")]
        # textbutton _("megan") action [Show("gallery_megan"), Hide("gallery_navigation")]
        textbutton _("Keira") action [Show("gallery_keira"), Hide("gallery_navigation")]
        # textbutton _("Holly") action [Show("gallery_holy"), Hide("gallery_navigation")]
        textbutton _("Becky") action [Show("gallery_becky"), Hide("gallery_navigation")]
        textbutton _("Isabella") action [Show("gallery_isabella"), Hide("gallery_navigation")]
        textbutton _("Clara") action [Show("gallery_clara"), Hide("gallery_navigation")]
        # textbutton _("Ming") action [Show("gallery_ming"), Hide("gallery_navigation")]

    if main_menu:
        textbutton _("Return") action [Hide("gallery_navigation"), Hide("displayTextScreen"), Show("main_menu")] xalign 0.97 yalign 0.95
    else:
        textbutton _("Return") action [Hide("gallery_navigation"), Hide("displayTextScreen"), Show("phone_main_screen")] xalign 0.97 yalign 0.95

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle Transform("gui/gallery.png", zoom=0.8)
        action NullAction()

style gallery_nav_vbox:
    xalign 0.1
    yalign 0.5
    spacing 23

style gallery_nav_button_text:
    font "fonts/28DaysLater.ttf"

style gallery2_nav_button_text:
    font "fonts/28DaysLater.ttf"

style gallery_stuff_grid:
    xalign 0.5
    yalign 0.5
    xspacing 20
    yspacing 20

style gallery_stuff_hbox:
    xalign 0.5
    yanchor 0.9
    ypos 0.95
    xspacing 10

style gallery_stuff_button_text:
    font "fonts/28DaysLater.ttf"

screen endreplay_button():

    textbutton _("End Replay") action EndReplay(confirm=True) xalign 0.97 yalign 0.95

screen gallery_kelly():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_kelly"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:

        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("hotel_room_01") or persistent.galleryUnlocked:
                    idle Transform("day_01_hotel_bar_scene_11_idle.png", zoom=0.3)
                    hover Transform("day_01_hotel_bar_scene_11_hover.png", zoom=0.3)
                    action Replay("hotel_room_01", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("kelly_morning") or persistent.galleryUnlocked:
                    idle Transform("day_02_hotel_room_scene_1_bed_idle.png", zoom=0.3)
                    hover Transform("day_02_hotel_room_scene_1_bed_hover.png", zoom=0.3)
                    action Replay("kelly_morning", scope={"kelly_love":99, "kelly_relationship":99}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("day_07_scene_05") or persistent.galleryUnlocked:
                    idle Transform("day_07_scene_6_kelly_1_idle.png", zoom=0.3)
                    hover Transform("day_07_scene_6_kelly_1_hover.png", zoom=0.3)
                    action Replay("day_07_scene_05", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_linda():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_linda"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_07_scene_3") or persistent.galleryUnlocked:
                    idle Transform("day_07_scene_03_linda_scene_1_idle.png", zoom=0.3)
                    hover Transform("day_07_scene_03_linda_scene_1_hover.png", zoom=0.3)
                    action Replay("day_07_scene_3", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("day_08_scene_05") or persistent.galleryUnlocked:
                    idle Transform("day_08_scene_05_linda_1_idle.png", zoom=0.3)
                    hover Transform("day_08_scene_05_linda_1_hover.png", zoom=0.3)
                    action Replay("day_08_scene_05", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_lisa():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_lisa"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("lisa_rachel_pool") or persistent.galleryUnlocked:
                    idle Transform("day_04_lisa_pool_14_idle.png", zoom=0.3)
                    hover Transform("day_04_lisa_pool_14_hover.png", zoom=0.3)
                    action Replay("lisa_rachel_pool", scope={"hair":"_lh", "lisa_relationship":99}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("galleryScene1") or persistent.galleryUnlocked:
                    idle Transform("day_06_scene_01_jennifer_23_lh.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_06_scene_01_jennifer_23_lh.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("galleryScene1", scope={"hair":"_lh"}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
            imagebutton:
                if renpy.seen_label("day_06_scene_13") or persistent.galleryUnlocked:
                    idle Transform("day_06_scene_13_jennifer_lisa_scene_10.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_06_scene_13_jennifer_lisa_scene_10.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("day_06_scene_13", scope={"lisa_masturbate":True}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_jennifer():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_jennifer"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_06_scene_1_1") or persistent.galleryUnlocked:
                    idle Transform("day_06_scene_01_jennifer_4_idle.png", zoom=0.3)
                    hover Transform("day_06_scene_01_jennifer_4_hover.png", zoom=0.3)
                    action Replay("day_06_scene_1_1", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("galleryScene1") or persistent.galleryUnlocked:
                    idle Transform("day_06_scene_01_jennifer_23_lh.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_06_scene_01_jennifer_23_lh.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("galleryScene1", scope={"hair":"_lh"}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("day_08_scene_03") or persistent.galleryUnlocked:
                    idle Transform("day_08_scene_03_jennifer_1_idle.png", zoom=0.3)
                    hover Transform("day_08_scene_03_jennifer_1_hover.png", zoom=0.3)
                    action Replay("day_08_scene_03", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_nicole():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_nicole"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_06_scene_10") or persistent.galleryUnlocked:
                    idle Transform("day_06_scene_10_nicole_1_idle.png", zoom=0.3)
                    hover Transform("day_06_scene_10_nicole_1_hover.png", zoom=0.3)
                    action Replay("day_06_scene_10", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_sandra():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_sandra"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_mary():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_mary"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("mary_blowjob_day_4") or persistent.galleryUnlocked:
                    idle Transform("day_04_hotel_mary_4_idle.png", zoom=0.3)
                    hover Transform("day_04_hotel_mary_4_hover.png", zoom=0.3)
                    action Replay("mary_blowjob_day_4", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("day_05_scene_2") or persistent.galleryUnlocked:
                    idle Transform("day_05_scene_02_mary_bedroom_scene_1_idle.png", zoom=0.3)
                    hover Transform("day_05_scene_02_mary_bedroom_scene_1_hover.png", zoom=0.3)
                    action Replay("day_05_scene_2", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("day_05_scene_6") or persistent.galleryUnlocked:
                    idle Transform("day_05_scene_06_mary_mc_hotel_scene_5.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_05_scene_06_mary_mc_hotel_scene_5.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("day_05_scene_6", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_khloe():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_khloe"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_07_scene_06") or persistent.galleryUnlocked:
                    idle Transform("day_07_scene_07_khloe_scene_9_idle.png", zoom=0.3)
                    hover Transform("day_07_scene_07_khloe_scene_9_hover.png", zoom=0.3)
                    action Replay("day_07_scene_06", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_emily():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_emily"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("emily_help") or persistent.galleryUnlocked:
                    idle Transform("day_04_mc_emily_scene_2.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_04_mc_emily_scene_2.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("emily_help", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_rachel():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_rachel"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("lisa_rachel_pool") or persistent.galleryUnlocked:
                    idle Transform("day_04_lisa_pool_14_idle.png", zoom=0.3)
                    hover Transform("day_04_lisa_pool_14_hover.png", zoom=0.3)
                    action Replay("lisa_rachel_pool", scope={"hair":"_lh", "lisa_relationship":99}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_amy():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_amy"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("lisa_rachel_pool") or persistent.galleryUnlocked:
                    idle Transform("day_04_lisa_pool_14_idle.png", zoom=0.3)
                    hover Transform("day_04_lisa_pool_14_hover.png", zoom=0.3)
                    action Replay("lisa_rachel_pool", scope={"hair":"_lh", "lisa_relationship":99}, locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_karen():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_karen"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_megan():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_megan"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_keira():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_keira"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_08_scene_06") or persistent.galleryUnlocked:
                    idle Transform("day_08_scene_06_keira_14_idle.png", zoom=0.3)
                    hover Transform("day_08_scene_06_keira_14_hover.png", zoom=0.3)
                    action Replay("day_08_scene_06", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_becky():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_becky"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("becky_replay") or persistent.galleryUnlocked:
                    idle Transform("day_05_scene_07_becky_scene_10_idle.png", zoom=0.3)
                    hover Transform("day_05_scene_07_becky_scene_10_hover.png", zoom=0.3)
                    action Replay("becky_replay", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_isabella():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_isabella"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("day_07_scene_07") or persistent.galleryUnlocked:
                    idle Transform("day_07_scene_08_isabella_1_idle.png", zoom=0.3)
                    hover Transform("day_07_scene_08_isabella_1_hover.png", zoom=0.3)
                    action Replay("day_07_scene_07", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_clara():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        # textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_clara"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("clara_humiliating_next_chapter") or persistent.galleryUnlocked:
                    idle Transform("day_04_clara_punish_1_7.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_04_clara_punish_1_7.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("clara_humiliating_next_chapter", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("clara_humiliation") or persistent.galleryUnlocked:
                    idle Transform("day_05_scene_04a_clara_mc_scene_8.png", zoom=0.3)
                    hover Transform(im.MatrixColor("day_05_scene_04a_clara_mc_scene_8.png", im.matrix.brightness(0.2)), zoom=0.3)
                    action Replay("clara_humiliation", locked=False)
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

            null
            null
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
            # imagebutton:
            #     if renpy.seen_label("label"):
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action Replay("label")
            #     else:
            #         idle Transform("locked.png", zoom=0.3)
            #         hover Transform("locked_hover.png", zoom=0.3)
            #         action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_holy():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_holy"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()

screen gallery_ming():

    add "images/gallery_background.png"

    modal True

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)

    textbutton _("Return") action [Hide("gallery_ming"), Hide("displayTextScreen"), Show("gallery_navigation")] xalign 0.97 yalign 0.95

    showif cg_page_a == 1:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
    elif cg_page_a == 2:
        grid 2 2:
            style_prefix "gallery_stuff"

            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
            imagebutton:
                if renpy.seen_label("label"):
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action Replay("label")
                else:
                    idle Transform("locked.png", zoom=0.3)
                    hover Transform("locked_hover.png", zoom=0.3)
                    action NullAction()
