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

        frame:
            padding (20, 20)

            grid 4 4:
                xcenter 0.5
                yspacing 20
                style_prefix "check"

                textbutton "Linda Path" action [ToggleVariable("LindaSubmissionPath", false_value="", true_value="{color=#0f0}[Linda Sub Path]"), ToggleVariable("LindaLovePath", false_value="", true_value="{color=#0f0}[Linda Love Path]")]
                textbutton "Jennifer Path" action [ToggleVariable("JenniferPath", false_value="", true_value="{color=#0f0}[Jennifer Path]"), ToggleVariable("JenniferLovePath", false_value="", true_value="{color=#0f0}[Jennifer Love Path]")]
                textbutton "Nicole Path" action [ToggleVariable("NicoleSubmissionPath", false_value="", true_value="{color=#0f0}[Nicole Sub Path]"), ToggleVariable("NicoleLovePath", false_value="", true_value="{color=#0f0}[Nicole Love Path]")]
                textbutton "Lisa Path" action [ToggleVariable("LisaLovePath", false_value="", true_value="{color=#0f0}[Lisa Love Path]"), ToggleVariable("LisaLesbianPath", false_value="", true_value="{color=#0f0}[Lisa Lesbian Path]"), ToggleVariable("LisaHaremPath", false_value="", true_value="{color=#0f0}[Lisa Harem Path]"), ToggleVariable("_LisaLovePath", false_value="", true_value="{color=#f00}[Lisa Love Path]")]
                textbutton "Kelly Path" action ToggleVariable("KellyPath", false_value="", true_value="{color=#0f0}[Kelly Path]")
                textbutton "Sandra Path" action [ToggleVariable("SandraLovePath", false_value="", true_value="{color=#0f0}[Sandra Love Path]")]
                textbutton "Sandra & Emily Path" action [ToggleVariable("SandraEmilyPath", false_value="", true_value="{color=#0f0}[Sandra+Emily Path]"), ToggleVariable("_SandraEmilyPath", false_value="", true_value="{color=#f00}[Sandra+Emily Path]")]
                textbutton "Clara Path" action ToggleVariable("ClaraSubmissionPath", false_value="", true_value="{color=#0f0}[Clara Sub Path]")
                textbutton "Emily Path" action [ToggleVariable("EmilyPath", false_value="", true_value="{color=#0f0}[Emily Path]"), ToggleVariable("EmilyLovePath", false_value="", true_value="{color=#0f0}[Emily Love Path]")]
                textbutton "Khloe Path" action ToggleVariable("KhloePath", false_value="", true_value="{color=#0f0}[Khloe Path]")
                textbutton "Holy Path" action ToggleVariable("HolyLovePath", false_value="", true_value="{color=#0f0}[Holy Path]")
                textbutton "Keira Path" action ToggleVariable("KeiraSubmissionPath", false_value="", true_value="{color=#0f0}[Keira Sub Path]")
                textbutton "Isabella Path" action ToggleVariable("IsabellaLovePath", false_value="", true_value="{color=#0f0}[Isabella Path]")
                textbutton "Becky Path" action ToggleVariable("BeckyPath", false_value="", true_value="{color=#0f0}[Becky Path]")
                textbutton "Rachel Path" action ToggleVariable("RachelLovePath", false_value="", true_value="{color=#0f0}[Rachel Path]")
                textbutton "Amy Path" action ToggleVariable("AmyLovePath", false_value="", true_value="{color=#0f0}[Amy Path]")

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
