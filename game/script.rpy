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
    define tuk= Character("Tukang Batagor", callback=callback) #tukang batagor

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

    jump deskripsi_latar

    return

label end:
    return

label deskripsi_latar:
    scene bg_utopian

    nar "Kamu melangkahkan kakimu ke bagian terbaik dari kota ini, yaitu centre square"

    y "Kota ini adalah kota dimana impian terwujud"
    y "Kota banyak orang mengadu nasib"
    y "Kota dimana orang orang hidup dengan tenang dan bahagia"
    y "Kota utopia"
    pause 1
    y "Mungkin itulah yang dipikirkan orang orang yang belum pernah menginjakkan kaki disini"
    y "...."

    nar "Kamu membuka handphonemu"
    nar "Kamu membuka berkas dari organisasimu"

    y "Tingkat kriminalitas 20 persen "
    y "1 dari 5 orang disini adalah seorang kriminal"
    y "Itukah definisi utopia bagimu?"

    nar "Kamu membaca lagi berkasmu"

    y "50 persen dari kejahatan tersebut adalah"
    y "...."
    y "Penggelapan pajak"
    y "Pantas saja mereka bisa lolos dengan tindak kriminalnya"
    y "Hukum disini bisa dibeli dengan uang"

    nar "Kamu membuka folder terakhir di berkas organisasimu"
    nar "'Seorang detektif yang baik seharusnya sudah tau apa yang ingin dia investigasi'"
    y "Apa ini?"
    y "....."
    y "Bro Rendra memang suka iseng"

    nar "Sudah beberapa jam semenjak terakhir kamu menyantap hidangan"
    nar "Menanggapi kelaparanmu,"
    nar "Kamu menghampiri sebuah stand batagor yang ada di pinggir jalan"

    scene bg_foodstand

    y "Bang, Batagor 50rb ya"
    tuk "Makan disini apa dibawa pulang, Pak?"
    y "Makan sini aja ya"
    tuk "Oke, tunggu sebentar ya"
    y "Oke"

    nar "Kamu melihat ada tumpukan koran-koran di meja stand itu"

    menu:
        "Ambil koran?"

        "Ambil Koran":
            image koran = "koran.png"
            show koran

            y "Bang, emangnya koran masih kepake ya disini?"
            tuk "..."

            nar "Abang batagor melirik ke kanan kiri dan mendekat kepadamu seakan akan membisikkan sesuatu"
            tuk "Kalau pake koran nggak dicek pemerintah pak"
            tuk "Ini jadi satu satunya media yang bisa kita percaya"
            y "Oh"
            y "Izin baca ya bang"

            tuk "Sok aja atuh"

            nar "Kamu mulai membuka koran tersebut lembar per lembar"
            nar "Semuanya berita masih terasa normal"
            nar "Sorry, normal disini adalah normal standard Taksopolis"
            nar "Sampai di halaman terakhir, kamu melihat nama sebuah perusahaan yang sedang mekar"
            hide koran

        "Biarin aja":
            y "Bang, disini ada perusahaan yang belakangan ini cepet banget pertumbuhannya ngga ya?"
            tuk "Maksudnya, pak?"
            y "Ya, kayak kemaren ngga kedengeran apa apa tiba tiba langsung booming"
            tuk "Hmm...."
            nar "Abang batagor melirik ke kanan kiri dan mendekat kepadamu seakan akan membisikkan sesuatu"
            tuk "Ada pak, bahkan katanya pendapatan setahunnya bisa sampai 400 Miliar USD, Dominion Corp" 


    y "400 Miliar USD dalam setahun?!"
    y "Perusahaan apa ini?! Bahkan aku nggak pernah melihatnya!"
    tuk "Punten pak, ini batagornya"
    y "Oh iya, makasih bang"
    
    nar "Kamu melanjutkan ke-kagetanmu sambil makan batagor"

    y "Dominion corp, perusahaan consultant..."
    y "Mungkinkah ini...."

    scene bg_hitam

    nar "Hatimu terguncang"
    nar "Jiwamu penasaran"
    y "Mungkin inilah yang dimaksud Bro Rendra, haruskah aku ungkap semua ini?"
    menu :
        "Apa yang akan kamu lakukan?"

        "Tindak lanjuti" :
            jump tindaklanjut

        "Abaikan, biarkan dirimu bersantai sejenak" :
            jump Abaikan

label tindaklanjut:
    scene bg_hitam

    nar "Mengingat berkas yang diberikan Bro Rendra, kamu pun bergegas kembali ke penginapanmu"
    "..."
    play sound "step.ogg"
    y "Inikah..."

    scene bg_computer
    y "Kalo dugaanku benar..."
    play sound "startup.ogg"
    nar "Kamu menyalakan laptopmu dan mulai membuka berkas yang diberikan Bro Rendra"
    nar "'Seorang detektif yang baik seharusnya sudah tau apa yang ingin dia investigasi'"
    nar "'PASSWORD : (Masukkan nama pihak...)'"
    y "Dominion.."
    y "Corp.."
    y "Enter"
    pause 1
    nar "'PASSWORD Accepted'"
    y "Bisa!"
    nar "'Dominion Corp, EST Nov 2035 (1 Yr Ago)'"
    nar "'Adress : Taksopolis, Garuda Street, 49F'"
    nar "'Direktur : Prof. Baskoro Aryatama'"
    nar "'Last-year Revenue : 400B USD'"
    nar "'Employee count : 1500 Employees'"
    nar "'...'"

    y "Wah, kali ini lengkap juga datanya"
    y "Bagus sih, tapi.."
    y "Gimana caranya aku mengumpulkan bukti bukti?"
    nar "Tanpa sadar, tubuhmu mulai lemas, dirimu sudah terlalu lama bertahan tanpa tidur"
    menu :
        "Tidur?"

        "Tidur" :
            scene bg_hitam
            nar "..."
            nar "..."
            pause 1
            scene bg_computer
            
            y "!!!"
            y "Jam berapa ini?!"
            y "Bahkan aku belum selesai membaca dokumennya"
            play sound "startup.ogg"
            nar "click click... jarimu bergerak cepat di keyboard dan mousemu"
            y "...."
            nar "click!"
            nar "'NOW HIRING : Available position : Accountant; Office Boy'"
            y "Oh...."
            pause 1
            y "Ide bagus"
        "Nanti dulu" :
            nar "click click... jarimu bergerak cepat di keyboard dan mousemu"
            y "...."
            nar "click!"
            nar "'NOW HIRING : Available position : Accountant; Office Boy'"
            y "Oh...."
            pause 1
            y "Ide bagus"
            scene bg_hitam
            nar "bruk.."
            pause 1
            nar "Tubuhmu sepertinya sudah tidak kuat untuk melanjutkan investigasimu malam ini"
            nar "Kamu pun tertidur di meja kerjamu"
            nar "...."
            scene bg_computer
            y "!!!"
            y "Jam berapa ini?!"
    y "Oke, tenang"
    y "Mari kita buat formulir pendaftaran Dominion Corp terlebih dahulu"
    y "Nama... Adi Prayoga"
    y "Tanggal lahir... 23 November 2002"
    y "..."
    y "Posisi yang dilamar..."
    
    menu :
        "Sebaiknya aku melamar sebagai posisi apa?"
        "Accountant" :
            $ Accountant = 1
        "Office Boy" :
            $ Accountant = 0
    scene bg_darkalley
    play sound "step.ogg"
    pause 1
    nar "dengan waktu yang semakin menipis, kamu bergegas menuju Jalan Garuda Nomor 49F"
    nar "..."
    scene bg_kantor
    y "....."
    y "Inilah tempatnya.."
    nar "Kamu memasuki kantor tersebut dengan langkah perlahan"
    if Accountant :
        jump alur_akuntan
    else :
        jump alur_OB

label alur_akuntan:
    an "aowkako"
label alur_OB:
    an "xixixi"

label Abaikan:
    scene bg_darkalley
    nar "beep... beep..."
    nar "handphonemu berdering"

    y "Ada perlu apa Bro Rendra menelfonku?"
    nar "Kamu mengangkat telfon"

    b " Hari yang cerah, tapi suasana hariku buruk."
    b "Seburuk kerjamu"
    b "Apa kau sadar apa kesalahanmu kali ini?"
    menu :
        "Apa kamu sadar apa kesalahan yang diperbuat?"

        "Ya, Sadar" :
            y "Ya, saya sadar kesalahan yang kau maksud."
            y "Tapi menurutku itu bukan sebuah kesalahan"
            b "Aku suka kepercayaan dirimu."
            b "Tapi kau harus ingat bahwa disini kau bawahanku,"
            b "harus mengikuti perintahku."
            b "Besok kau harus mulai menyelidiki perusahaan tersebut."
            
            nar "beep... beep..."
            nar "Sebelum kamu bisa menjawab peringatan Bro Rendra, dia sudah menutup telfonnya"
            jump tindaklanjut
        "Tidak, saya mau bersantai":
            nar "Anda telah gagal menjalankan misi untuk mengungkap kasus di kota Taksopolis"

    

