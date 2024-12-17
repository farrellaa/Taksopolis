## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Tax \n Detective")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""Dalam game visual novel Tax Detective, Anda akan memerankan seorang detektif handal yang ditugaskan untuk menyelidiki kasus korupsi pajak di Dominion Corp, sebuah perusahaan besar yang dikenal penuh rahasia dan
intrik. Laporan dari atasan Anda mengungkapkan bahwa ada kejanggalan besar di dalam perusahaan ini, tetapi bukti-bukti konkret masih sulit ditemukan. 
Untuk menyusup dan mengungkap kebenaran, Anda harus memutuskan cara terbaik untuk masuk ke dalam Dominion Corp:

• Sebagai Office Boy: Menyelami kehidupan sehari-hari karyawan tingkat bawah dan mengakses ruangan direktur dan dokumen rahasia
tanpa menimbulkan kecurigaan.

• Sebagai Investor: Menyamar sebagai sosok penting yang dihormati agar dapat mendekati petinggi perusahaan dan menggali informasi dari
percakapan elit.

Setiap pilihan penyamaran membawa Anda ke jalur cerita yang berbeda dengan tantangan unik, koneksi karakter, dan kesempatan untuk menemukan petunjuk. Anda akan menghadapi dilema moral, pilihan sulit, dan kejutan yang tak terduga.

Melalui keputusan yang Anda buat, alur cerita akan berkembang ke arah yang sepenuhnya ditentukan oleh Anda. Apakah Anda akan berhasil mengungkap jaringan korupsi Dominion Corp dan membawa pelakunya ke pengadilan? Ataukah penyamaran Anda justru berakhir dengan pengkhianatan, bahaya, atau bahkan tragedi?

Game Visual Novel Ini dibuat oleh: 

- Project Manager : 

1. Merlin Aurelia -12823008 - meteorologi

- Game Designer:

1. Habib Annaafi Syafrin 13723049 - Teknik Material

2. Alexander Gultom 13723019 - Teknik Material

3. Jiro Adika Faruq - 12223099 - Teknik Perminyakan

4. Lika Adzkia 12522070

5. Dafa Abdillah 13021076

- Script Writer/Story Developer : 

1. Arla Lian Sabilla- 12823037-Meteorologi

2. Sabrina Nurul Khatimah- 12823037-Meteorologi

- Programmer:

1. Taqidito ilham p 18023039 - Teknik tenaga listrik

2. Farrell Astrada 18321021 - Teknik biomedis

- Graphic Designer/Illustrator:

1. Keysha Fatimah  -12823027

2. Nadhirah Alma Tawfiqa -12823016

3. Taza Nadia Az Zahra- 12823045

- UI/UX Designer:

1. Benedito Benito Tei De Mori - 15320085 - Teknik Lingkungan

- Sound Designer/Composer: 

1. Kevin A. Aryasena - 12923047 - Oseanografi

- Quality Assurance (QA) Tester:

1. Salsabila Effendi - 12823066 - Meteorologi 

2. Erin Carolina-15323012

- Publication Specialist:
 
 1. Grace Situmeang-15323088-Teknik Lingkungan
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Tax_Detective"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "main_menu.wav"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 35


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Taksopolis-1732172954"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
