from LIB.AppBase import AppBase
from Providers.HrefFinder import HrefFinder
from Providers.Github import Github
from Providers.Modyolo import Modyolo
from Providers.Liteapks import Liteapks
from Scrapping.Providers.ApkDone import ApkDone
from Providers.DirectLink import DirectLink


#####################################################################################
# HDO
def hdo():
    # HDO
    def HDO():
        return DirectLink()("https://hdo.app/download")

    app = AppBase("HDO", {"HDO": HDO})
    app.update()


#####################################################################################
# YOUTUBE
def youtube():
    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/youtube-arm64-v8a-revanced.apk"
        )

    # ReVanced Extended
    def revanced_extended():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/youtube-arm64-v8a-revanced-extended.apk"
        )

    # ReVanced 2
    def revanced2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "youtube"], ["extended", "arm-v7a"]
        )

    # ReVanced Extended 2
    def revanced_extended2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "youtube-revanced-extended"], ["arm-v7a"]
        )

    app = AppBase(
        "YouTube",
        {
            "ReVanced": revanced,
            "ReVanced Extended": revanced_extended,
            "ReVanced (2)": revanced2,
            "ReVanced Extended (2)": revanced_extended2,
        },
    )
    app.update()


#####################################################################################
# YOUTUBE MUSIC
def youtube_music():
    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/youtube-music-arm64-v8a-revanced.apk"
        )

    # ReVanced Extended
    def revanced_extended():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/youtube-music-arm64-v8a-revanced-extended.apk"
        )

    # ReVanced 2
    def revanced2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "music"], ["extended", "arm-v7a"]
        )

    # ReVanced Extended 2
    def revanced_extended2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "music-revanced-extended"], ["arm-v7a"]
        )

    app = AppBase(
        "YouTube Music",
        {
            "ReVanced": revanced,
            "ReVanced Extended": revanced_extended,
            "ReVanced (2)": revanced2,
            "ReVanced Extended (2)": revanced_extended2,
        },
    )
    app.update()


#####################################################################################
# TWITCH
def twitch():
    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/twitch-revanced.apk"
        )

    # ReVanced (2)
    def revanced2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "twitch", "all"], ["arm-v7a"]
        )

    app = AppBase("Twitch", {"ReVanced": revanced, "ReVanced (2)": revanced2})
    app.update()


#####################################################################################
# REDDIT
def reddit():
    # ReVanced Extended
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/reddit-revanced.apk"
        )

    # ReVanced Extended
    def revanced_extended():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/reddit-revanced-extended.apk"
        )

    app = AppBase(
        "Reddit",
        {"ReVanced": revanced, "ReVanced Extended": revanced_extended},
    )
    app.update()


#####################################################################################
# TIKTOK
def tiktok():
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/tiktok-revanced.apk"
        )

    def revanced2():
        return Github("j-hc", "revanced-magisk-module")(
            [".apk", "tiktok", "all"], ["arm-v7a"]
        )

    app = AppBase("TikTok", {"ReVanced": revanced, "ReVanced (2)": revanced2})
    app.update()


#####################################################################################
# MICROG
def microg():
    def teamvanced():
        return Github("ReVanced", "GmsCore")(["signed", ".apk"], ["hw"])

    app = AppBase("MicroG", {"TeamVanced": teamvanced})
    app.update()


#####################################################################################
# SPOTIFY
def spotify():

    # MODYOLO
    def modyolo():
        return Modyolo("spotify-music-24463")()

    # LITEAPKS
    def liteapks():
        return Liteapks("spotify-music-98")()

    # APKDONE
    def apkdone():
        return ApkDone("spotify-mod")()

    app = AppBase(
        "Spotify",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# PHOTO EDITOR PRO
def photo_editor_pro():

    # MODYOLO
    def modyolo():
        return Modyolo("polish-photo-editor-pro-2578")()

    # LITEAPKS
    def liteapks():
        return Liteapks("polish-photo-editor-pro-491")()

    # APKDONE
    def apkdone():
        return ApkDone("photo-editor-pro-apk")()

    app = AppBase(
        "Photo Editor Pro",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# PHOTOSHOP EXPRESS
def photoshop_express():

    # MODYOLO
    def modyolo():
        return Modyolo("photoshop-express-12281")()

    # LITEAPKS
    def liteapks():
        return Liteapks("photoshop-express-570")()

    # APKDONE
    def apkdone():
        return ApkDone("adobe-photoshop-express")()

    app = AppBase(
        "Photoshop Express",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# CAPCUT
def capcut():

    # MODYOLO
    def modyolo():
        return Modyolo("capcut-video-editor-29058")()

    # LITEAPKS
    def liteapks():
        return Liteapks("capcut-311")()

    # APKDONE
    def apkdone():
        return ApkDone("capcut-mod-apk")()

    app = AppBase(
        "CapCut",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# INSHOT
def inshot():

    def modyolo():
        return Modyolo("inshot-2257")()

    # LITEAPKS
    def liteapks():
        return Liteapks("inshot-pro-107")()

    # APKDONE
    def apkdone():
        return ApkDone("inshot")()

    app = AppBase(
        "InShot",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# INSTAGRAM
def instagram():

    # Instander
    def instander_clone():
        return HrefFinder()(
            "https://thedise.me/instander/repo/",
            ["clone"],
            [],
        )

    def instander_unclone():
        return HrefFinder()(
            "https://thedise.me/instander/repo/",
            [],
            ["clone"],
        )

    # HONINSTA
    def honinsta():
        return HrefFinder()(
            "https://honista.com/en/download.html",
            ["64"],
            ["32"],
        )

    def myinsta_clone():
        return HrefFinder()(
            "https://myinsta.app/",
            ["_c_", "64"],
            ["_uc_"],
        )

    def myinsta_unclone():
        return HrefFinder()("https://myinsta.app/", ["_uc_", "64"], ["_c_"])

    app = AppBase(
        "Instagram",
        {
            "MyInsta - Clone": myinsta_clone,
            "MyInsta - Unclone": myinsta_unclone,
            "Honinsta": honinsta,
            "Instander - Clone": instander_clone,
            "Instander - Unclone": instander_unclone,
        },
    )
    app.update()


#####################################################################################
# NEWPIPE
def newpipe():

    def teamnewpipe():
        return Github("TeamNewPipe", "NewPipe")([".apk"])

    app = AppBase("NewPipe", {"TeamNewPipe": teamnewpipe})
    app.update()


#####################################################################################
# SEAL
def seal():

    def junkfood02():
        return Github("JunkFood02", "Seal")(["universal", ".apk"])

    app = AppBase("Seal", {"JunkFood02": junkfood02})
    app.update()


#####################################################################################
# SMARTLAUNCHER
def smartlauncher():

    def modyolo():
        return Modyolo("smart-launcher-6-27413")()

    # LITEAPKS
    def liteapks():
        return Liteapks("smart-launcher-6-184")()

    # APKDONE
    def apkdone():
        return ApkDone("smart-launcher-5")()

    app = AppBase(
        "Smart Launcher 6",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


def niagaralauncher():

    def modyolo():
        return Modyolo("niagara-launcher-63941")()

    # LITEAPKS
    def liteapks():
        return Liteapks("niagara-launcher-75423")()

    # APKDONE
    def apkdone():
        return ApkDone("niagara-launcher")()

    app = AppBase(
        "Niagara Launcher",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# REVANCED MANAGER
def revancedManager():

    def ReVanced():
        return Github("ReVanced", "revanced-manager")([".apk"])

    app = AppBase("ReVanced Manager", {"ReVanced": ReVanced})
    app.update()


#####################################################################################
# YTDLNIS
def ytdlnis():
    def ytdlnis():
        return Github("deniscerri", "ytdlnis")([".apk", "universal"])

    app = AppBase("YTDLnis", {"deniscerr": ytdlnis})
    app.update()


#####################################################################################
# NEVER HAVE I EVER
def neverhaveiever():
    # LiteApks
    def liteapks():
        return Liteapks("never-have-i-ever-194362")()

    app = AppBase("Never Have I Ever", {"LITEAPKS": liteapks})
    app.update()


#####################################################################################
# BOREALIS
def borealis():

    # MODYOLO
    def modyolo():
        return Modyolo("borealis-icon-pack-67728")()

    # LiteApks
    def liteapks():
        return Liteapks("borealis-icon-pack-23491")()

    app = AppBase("Borealis", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# LAYERS
def layers():

    # MODYOLO
    def modyolo():
        return Modyolo("layers-icon-pack-54734")()

    # LITEAPKS
    def liteapks():
        return Liteapks("layers-glass-icon-pack-401063")()

    app = AppBase("Layers", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# AUSTRALIS
def australis():

    # MODYOLO
    def modyolo():
        return Modyolo("australis-icon-pack-208797")()

    # LiteApks
    def liteapks():
        return Liteapks("australis-icon-pack-142596")()

    app = AppBase("Australis", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# VERA
def vera():

    # MODYOLO
    def modyolo():
        return Modyolo("vera-icon-pack-54724")()

    # LITEAPKS
    def liteapks():
        return Liteapks("vera-icon-pack-22930")()

    app = AppBase("Vera", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# LINEBIT
def linebit():

    # MODYOLO
    def modyolo():
        return Modyolo("linebit-icon-pack-13472")()

    # LITEAPKS
    def liteapks():
        return Liteapks("linebit-22796")()

    app = AppBase("Linebit", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# SOUNDCLOUD
def soundcloud():

    def apkdone():
        return ApkDone("soundcloud")()

    app = AppBase(
        "SoundCloud",
        {"APKDONE": apkdone},
    )
    app.update()


#####################################################################################
# IPTV PRO
def iptvpro():

    # MODYOLO
    def modyolo():
        return Modyolo("iptv-pro-34294")()

    # LITEAPKS
    def liteapks():
        return Liteapks("iptv-pro-76245")()

    app = AppBase("IPTV Pro", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# PERFECT IPTV PLAYER
def perfectiptvplayer():

    # APKLITE
    def liteapks():
        return Liteapks("perfect-iptv-player-363415")()

    app = AppBase("Perfect IPTV Player", {"LITEAPKS": liteapks})
    app.update()


#####################################################################################
# AUTOMATE
def automate():

    # LITEAPKS
    def liteapks():
        return Liteapks("automate-360715")()

    app = AppBase("Automate", {"LITEAPKS": liteapks})
    app.update()


#####################################################################################
# AUTO CLICKER MACRO: CLICKMATE
def clickmate():

    # MODYOLO
    def modyolo():
        return Modyolo("auto-clicker-macro-clickmate-102404")()

    # LITEAPKS
    def liteapks():
        return Liteapks("auto-clicker-macro-clickmate-34853")()

    # APKDONE
    def apkdone():
        return ApkDone("clickmate")()

    app = AppBase(
        "Clickmate", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# TASKER
def tasker():

    # LITEAPKS
    def liteapks():
        return Liteapks("tasker-369228")()

    # APKDONE
    def apkdone():
        return ApkDone("tasker")()

    app = AppBase("Tasker", {"LITEAPKS": liteapks, "APKDONE": apkdone})
    app.update()


#####################################################################################
# XODO
def xodo():

    # MODYOLO
    def modyolo():
        return Modyolo("xodo-pdf-reader-editor-5752")()

    # LITEAPKS
    def liteapks():
        return Liteapks("xodo-pdf-reader-editor-78598")()

    # APKDONE
    def apkdone():
        return ApkDone("xodo-pdf-reader-editor")()

    app = AppBase(
        "Xodo", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# BRILLIANT
def brilliant():

    # APKDONE
    def apkdone():
        return ApkDone("brilliant")()

    app = AppBase("Brilliant", {"APKDONE": apkdone})
    app.update()


#####################################################################################
# MUSIXMATCH
def musixmatch():

    # MODYOLO
    def modyolo():
        return Modyolo("musixmatch-17890")()

    # LITEAPKS
    def liteapks():
        return Liteapks("musixmatch-3761")()

    # APKDONE
    def apkdone():
        return ApkDone("musixmatch")()

    app = AppBase(
        "Musixmatch", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# ONSTREAM
def onstream():

    # OnStream
    def onstream():
        return DirectLink()("https://dl.getmenow.click/onstream-latest.apk")

    app = AppBase("OnStream", {"OnStream": onstream})
    app.update()


#####################################################################################
# TELEGRAM
def telegram():

    # NekoX
    def nekox():
        return Github("NekoX-Dev", "NekoX")(["arm64", ".apk"], ["NoGcm"])

    # Forkgram
    def forkgram():
        return Github("forkgram", "TelegramAndroid")([".apk"])

    app = AppBase("Telegram", {"NekoX": nekox, "Forkgram": forkgram})
    app.update()


#####################################################################################
# SHOWLY
def showly():

    # MODYOLO
    def modyolo():
        return Modyolo("showly-58960")()

    # LITEAPKS
    def liteapks():
        return Liteapks("showly-13824")()

    app = AppBase("Showly", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# CAMSCANNER
def camscanner():

    # MODYOLO
    def modyolo():
        return Modyolo("camscanner-5320")()

    # LITEAPKS
    def liteapks():
        return Liteapks("camscanner-320")()

    # APKDONE
    def apkdone():
        return ApkDone("camscanner")()

    app = AppBase(
        "CamScanner", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# APP CLONER
def appcloner():

    # LITEAPKS
    def liteapks():
        return Liteapks("app-cloner-154")()

    # APKDONE
    def apkdone():
        return ApkDone("app-cloner-mod-apk")()

    app = AppBase("App Cloner", {"LITEAPKS": liteapks, "APKDONE": apkdone})
    app.update()


#####################################################################################
# ADGUARD
def adguard():

    # MODYOLO
    def modyolo():
        return Modyolo("adguard-28793")()

    # LITEAPKS
    def liteapks():
        return Liteapks("adguard-819")()

    # APKDONE
    def apkdone():
        return ApkDone("adguard-premium")()

    app = AppBase(
        "AdGuard", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# PICSART
def picsart():

    # MODYOLO
    def modyolo():
        return Modyolo("picsart-photo-editor-8131")()

    # LITEAPKS
    def liteapks():
        return Liteapks("picsart-136")()

    # APKDONE
    def apkdone():
        return ApkDone("picsart-app")()

    app = AppBase(
        "Picsart", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# FITIFY
def fitify():

    # MODYOLO
    def modyolo():
        return Modyolo("fitify-26376")()

    # LITEAPKS
    def liteapks():
        return Liteapks("fitify-8086")()

    # APKDONE
    def apkdone():
        return ApkDone("fitify")()

    app = AppBase(
        "Fitify", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# ENIX
def enix():

    # MODYOLO
    def modyolo():
        return Modyolo("enix-icon-pack-17851")()

    app = AppBase("ENIX", {"MODYOLO": modyolo})
    app.update()


#####################################################################################
# WPS OFFICE
def wpsoffice():

    # MODYOLO
    def modyolo():
        return Modyolo("wps-office-244438")()

    # LITEAPKS
    def liteapks():
        return Liteapks("wps-office-464")()

    app = AppBase("WPS Office", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# X-PLORE FILE MANAGER
def xplorefilemanager():

    # MODYOLO
    def modyolo():
        return Modyolo("x-plore-file-manager-48771")()

    # LITEAPKS
    def liteapks():
        return Liteapks("x-plore-file-manager-26189")()

    # APKDONE
    def apkdone():
        return ApkDone("x-plore-file-manager")()

    app = AppBase(
        "X-plore File Manager",
        {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone},
    )
    app.update()


#####################################################################################
# TRUECALLER
def truecaller():

    # MODYOLO
    def modyolo():
        return Modyolo("truecaller-261629")()

    # LITEAPKS
    def liteapks():
        return Liteapks("truecaller-89")()

    app = AppBase("Truecaller", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# ADOBE LIGHTROOM
def adobelightroom():

    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/lightroom-revanced.apk"
        )

    # MODYOLO
    def modyolo():
        return Modyolo("adobe-lightroom-6604")()

    # LITEAPKS
    def liteapks():
        return Liteapks("adobe-lightroom-205")()

    # APKDONE
    def apkdone():
        return ApkDone("adobe-lightroom")()

    app = AppBase(
        "Lightroom",
        {
            "ReVanced": revanced,
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# SHAZAM
def shazam():

    # MODYOLO
    def modyolo():
        return Modyolo("shazam-2281")()

    # LITEAPKS
    def liteapks():
        return Liteapks("shazam-8507")()

    # APKDONE
    def apkdone():
        return ApkDone("shazam")()

    app = AppBase(
        "Shazam", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# DUOLINGO
def duolingo():

    # MODYOLO
    def modyolo():
        return Modyolo("duolingo-2137")()

    # LITEAPKS
    def liteapks():
        return Liteapks("duolingo-329")()

    # APKDONE
    def apkdone():
        return ApkDone("duolingo")()

    app = AppBase(
        "Duolingo", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# MX PLAYER
def mxplayer():

    # MODYOLO
    def modyolo():
        return Modyolo("mx-player-244401")()

    # LITEAPKS
    def liteapks():
        return Liteapks("mx-player-651")()

    # APKDONE
    def apkdone():
        return ApkDone("mx-player")()

    app = AppBase(
        "MX Player", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# SNOW
def snow():

    # MODYOLO
    def modyolo():
        return Modyolo("snow-159306")()

    # LITEAPKS
    def liteapks():
        return Liteapks("snow-32696")()

    # APKDONE
    def apkdone():
        return ApkDone("snow")()

    app = AppBase(
        "SNOW", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# SD MAID PRO
def sdmaidpro():

    # MODYOLO
    def modyolo():
        return Modyolo("sd-maid-pro-3800")()

    # LITEAPKS
    def liteapks():
        return Liteapks("sd-maid-pro-527")()

    app = AppBase("SD Maid Pro", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# SD MAID SE
def sdmaidse():

    # LITEAPKS
    def liteapks():
        return Liteapks("sd-maid-2-se-199767")()

    app = AppBase("SD Maid SE", {"LITEAPKS": liteapks})
    app.update()


#####################################################################################
# 1DM+
def onedm():

    # MODYOLO
    def modyolo():
        return Modyolo("1dm-1309")()

    # LITEAPKS
    def liteapks():
        return Liteapks("1dm-3586")()

    # APKDONE
    def apkdone():
        return ApkDone("idm-music-video-torrent-downloader")()

    app = AppBase(
        "1DM+", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# MY DIARY
def mydiary():

    # MODYOLO
    def modyolo():
        return Modyolo("my-diary-16453")()

    # APKDONE
    def apkdone():
        return ApkDone("my-diary")()

    app = AppBase("My Diary", {"MODYOLO": modyolo, "APKDONE": apkdone})
    app.update()


#####################################################################################
# NZB360
def nzb360():

    # MODYOLO
    def modyolo():
        return Modyolo("nzb360-55105")()

    # LITEAPKS
    def liteapks():
        return Liteapks("nzb360-73320")()

    # APKDONE
    def apkdone():
        return ApkDone("nzb360")()

    app = AppBase(
        "nzb360", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# NOVA LAUNCHER
def novalauncher():

    # MODYOLO
    def modyolo():
        return Modyolo("nova-launcher-prime-371")()

    # LITEAPKS
    def liteapks():
        return Liteapks("nova-launcher-prime-79644")()

    # APKDONE
    def apkdone():
        return ApkDone("nova-launcher-prime-apk")()

    app = AppBase(
        "Nova Launcher", {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone}
    )
    app.update()


#####################################################################################
# WAZE
def waze():

    # MODYOLO
    def modyolo():
        return Modyolo("waze-41662")()

    # LITEAPKS
    def liteapks():
        return Liteapks("waze-navigation-live-traffic-12025")()

    app = AppBase("Waze", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# ES File Explorer
def esfilemanager():

    # MODYOLO
    def modyolo():
        return Modyolo("es-file-explorer-19868")()

    def liteapks():
        return Liteapks("es-file-explorer-3661")()

    def apkdone():
        return ApkDone("es-file-explorer")()

    app = AppBase(
        "ES File Explorer",
        {"MODYOLO": modyolo, "LITEAPKS": liteapks, "APKDONE": apkdone},
    )
    app.update()


#####################################################################################
# FRIENDLY FOR TWITTER/X
def friendlyfortwitterx():

    # MODYOLO
    def modyolo():
        return Modyolo("friendly-for-twitter-67653")()

    # LITEAPKS
    def liteapks():
        return Liteapks("friendly-for-twitter-76209")()

    app = AppBase("Friendly For Twitter/X", {"MODYOLO": modyolo, "LITEAPKS": liteapks})
    app.update()


#####################################################################################
# SNAPCHAT
def snapchat():

    # FouadMODS
    def foud():
        return HrefFinder()(
            "https://fmmods.com/fouad-snapchat/",
            ["FouadMODS", "FMSC"],
            [],
        )

    app = AppBase("Snapchat", {"FouadMODS": foud})
    app.update()


#####################################################################################
# FACEBOOK
def facebook():

    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/facebook-arm64-v8a-revanced.apk"
        )

    app = AppBase("Facebook", {"ReVanced": revanced})
    app.update()


#####################################################################################
# MESSENGER
def messenger():

    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/messenger-arm64-v8a-revanced.apk"
        )

    app = AppBase("Messenger", {"ReVanced": revanced})
    app.update()


#####################################################################################
# X
def x():

    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/twitter-stable-piko.apk"
        )

    app = AppBase("X", {"ReVanced": revanced})
    app.update()


#####################################################################################
# RAR
def rar():

    # ReVanced
    def revanced():
        return DirectLink()(
            "https://github.com/FiorenMas/Revanced-And-Revanced-Extended-Non-Root/releases/download/all/rar-revanced.apk"
        )

    app = AppBase("RAR", {"ReVanced": revanced})
    app.update()


#####################################################################################
# SECURE VPN
def secure_vpn():

    # MODYOLO
    def modyolo():
        return Modyolo("secure-vpn-36039")()

    # LITEAPKS
    def liteapks():
        return Liteapks("secure-vpn-25243")()

    # APKDONE
    def apkdone():
        return ApkDone("secure-vpn-apk")()

    app = AppBase(
        "Secure VPN",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()


#####################################################################################
# KINEMASTER
def kinemaster():

    # MODYOLO
    def modyolo():
        return Modyolo("kinemaster-5707")()

    # LITEAPKS
    def liteapks():
        return Liteapks("kinemaster-145")()

    app = AppBase(
        "KineMaster",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
        },
    )
    app.update()


#####################################################################################
# XY VPN
def xy_vpn():

    # MODYOLO
    def modyolo():
        return Modyolo("xy-vpn-174735")()

    # LITEAPKS
    def liteapks():
        return Liteapks("xy-vpn-79398")()

    # APKDONE
    def apkdone():
        return ApkDone("xy-vpn")()

    app = AppBase(
        "XY VPN",
        {
            "MODYOLO": modyolo,
            "LITEAPKS": liteapks,
            "APKDONE": apkdone,
        },
    )
    app.update()
