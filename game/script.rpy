init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("typing.ogg", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

##Semua alur wajib dibuat menjadi label label agar mudah manajemen nya

init :    
    define nar= Character("", callback=callback) #Narrator
    define y = Character("You", callback=callback) #Detektif
    define b= Character("Bro Rendra", callback=callback) #Bos Detektif
    define di= Character("Baskoro Aryatama", callback=callback) #Direktur 
    define an= Character("Anita Kartika", callback=callback) #HRD


#label start SELALU muncul di new game
label start:
    scene bg_darkalley
    #show eileen happy

    nar "Sebuah lorong gelap, di pinggiran kota metropolitan"
    nar "Kota dimana semua orang bisa mendapatkan semua yang mereka mau"
    nar "wanita, kekuasaan, tahta,"


    nar "buzz... buzz..."
    y "Rendra?"
    b "Adi..."
    b "Brief yang kamu butuhkan sudah saya kirim lewat email ya"
    b "Hati-hati untuk redemption kali ini"
    nar "beep..."

    play sound "rokok.ogg"
    pause 4
    y "Taksopolis..."
    y "Entah apa yang akan kau berikan padaku kali ini"

    return
