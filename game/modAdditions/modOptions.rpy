init python:
    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"
    LindaSubmissionPath = "{color=#0f0}[Linda Sub Path]"
    LindaLovePath = "{color=#0f0}[Linda Love Path]"
    JenniferPath = "{color=#0f0}[Jennifer Path]"
    JenniferLovePath = "{color=#0f0}[Jennifer Love Path]"
    NicoleSubmissionPath = "{color=#0f0}[Nicole Sub Path]"
    NicoleLovePath = "{color=#0f0}[Nicole Love Path]"
    LisaLovePath = "{color=#0f0}[Lisa Love Path]"
    LisaLesbianPath = "{color=#0f0}[Lisa Lesbian Path]"
    LisaHaremPath = "{color=#0f0}[Lisa Harem Path]"
    _LisaLovePath = "{color=#f00}[Lisa Love Path]"
    KellyPath = "{color=#0f0}[Kelly Path]"
    SandraLovePath = "{color=#0f0}[Sandra Love Path]"
    SandraEmilyPath = "{color=#0f0}[Sandra+Emily Path]"
    _SandraEmilyPath = "{color=#f00}[Sandra+Emily Path]"
    ClaraSubmissionPath = "{color=#0f0}[Clara Sub Path]"
    EmilyPath = "{color=#0f0}[Emily Path]"
    EmilyLovePath = "{color=#0f0}[Emily Love Path]"
    KhloePath = "{color=#0f0}[Khloe Path]"
    HolyLovePath = "{color=#0f0}[Holy Path]"
    KeiraSubmissionPath = "{color=#0f0}[Keira Sub Path]"
    IsabellaLovePath = "{color=#0f0}[Isabella Path]"
    BeckyPath = "{color=#0f0}[Becky Path]"
    RachelLovePath = "{color=#0f0}[Rachel Path]"
    AmyLovePath = "{color=#0f0}[Amy Path]"

    EndRelationship = "{color=#f00}[End Relationship]"


define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    python:
        persistent.y = renpy.input("Answer with your name.", default="Kyle")
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        y = renpy.input("Answer with your name.", default="Kyle")
    mod "Names successful changed"
    return
