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
    define un= Character("???", callback=callback)
    define Police= Character("Polisi", callback=callback) #untuk orang orang yang dibuat tidak perlu tau namanya
    
###screen disclaimer ():

screen credits_screen():
    tag menu

    vbox:
        spacing 10
        align (0.5, 0.1)
        
        text "Game Visual Novel Ini dibuat oleh:" size 30 bold True
        
        text "- Project Manager:" size 22
        text "1. Merlin Aurelia - 12823008 - Meteorologi" size 20

        text "- Game Designer:" size 22
        text "1. Habib Annaafi Syafrin - 13723049 - Teknik Material" size 20
        text "2. Alexander Gultom - 13723019 - Teknik Material" size 20
        text "3. Jiro Adika Faruq - 12023099 - Teknik Perminyakan" size 20
        text "4. Lika Adzkia - 12220070" size 20
        text "5. Dafa Abdillah - 13021076" size 20

        text "- Script Writer/Story Developer:" size 22
        text "1. Arla Lian Sabilla - 12823037 - Meteorologi" size 20
        text "2. Sabrina Nurul Khatimah - 12823037 - Meteorologi" size 20
        text "3. Taqidito Ilham Pratama - 18023039 - Teknik Tenaga Listrik" size 20

        text "- Programmer:" size 22
        text "1. Taqidito Ilham P - 18023039 - Teknik Tenaga Listrik" size 20
        text "2. Farrell Astrada - 18321021 - Teknik Biomedis" size 20

        text "- Graphic Designer/Illustrator:" size 22
        text "1. Keysha Fatimah - 12823027" size 20
        text "2. Nadhirah Alma Tawfiqa - 12823016" size 20
        text "3. Taza Nadia Az Zahra - 12823045" size 20
        text "4. Taqidito Ilham Pratama - 18023039 - Teknik Tenaga Listrik" size 20

        text "- UI/UX Designer:" size 22
        text "1. Benedito Benito Tei De Mori - 15320085 - Teknik Lingkungan" size 20

        text "- Sound Designer/Composer:" size 22
        text "1. Kevin A. Aryasena - 12923047 - Oseanografi" size 20

        text "- Quality Assurance (QA) Tester:" size 22
        text "1. Salsabila Effendi - 12823066 - Meteorologi" size 20
        text "2. Erin Carolina - 15323012" size 20

        text "- Publication Specialist:" size 22
        text "1. Grace Situmeang - 15323088 - Teknik Lingkungan" size 20

        text "Dibimbing oleh Bapak Harry Nuriman, untuk tugas PKWN." size 22 bold True

        textbutton "Kembali ke Menu Utama" action Return() align (0.5, 0.9)


image You_Merengut="You/You_Merengut.png"
image You_Mewing="You/You_Mewing.png"
image You_Senyum="You/You_Senyum.png"

image Rendra_Datar:
    "Rendra/Rendra_Datar.png"
    zoom 1.5
image Rendra_Hepi:
    "Rendra/Rendra_Hepi.png"
    zoom 1.5

image Baskoro_Datar:
    "Director/Baskoro_Datar.png"
    zoom 1.2
image Baskoro_Nyengir:
    "Director/Baskoro_Nyengir.png"
    zoom 1.2

image HRD_Senyum:
    "HRD/HRD_Senyum.png"
    zoom 1.5

image HRD_Datar:
    "HRD/HRD_Datar.png"
    zoom 1.5

image HRD_Resah:
    "HRD/HRD_Resah.png"
    zoom 1.5

image Batagor:
    "Batagor/Batagor.png"
    zoom 1.5
    yalign 0.5

image Bisikan:
    "Bisikan.png"
    zoom 1.5
    yalign 0.5

#label start SELALU muncul di new gamez
label start:
    ####ttempat disclaimer
    scene bg_darkalley
    #show eileen happy

    play music "initial_dark_alley_intro (1).wav" loop
    nar "Sebuah lorong gelap, di pinggiran kota metropolitan"
    nar "Kota dimana semua orang bisa mendapatkan semua yang mereka mau"
    nar "wanita, kekuasaan, tahta,"
    nar "Di antara bayangan dan bau asam dari lorong itu, Seakan membisikkan sesuatu padamu"  
    nar "'Jangan percaya dengan mereka yang tidak mendengar...'"
    nar "suara itu seperti bisikan hantu, samar tapi cukup tajam untuk menusuk telingamu."  

    nar "kamu melihat seorang ibu tua sedang duduk memeluk anaknya yang sakit."  
    nar "Rumah sakit menolak mereka karena tak mampu membayar biaya pengobatan."  
    show You_Merengut at left  
    y "Kalau saja pajak itu tidak digelapkan... kalau saja mereka punya healthcare yang layak..."  
    nar "Kemarahanmu semakin membara. Kamu berjanji, kebenaran ini harus terungkap."  


    nar "buzz... buzz..."
    nar "Handphonemu berdering"
    show You_Mewing at left
    y "Rendra?"
    show Rendra_Datar at center

    b "...."
    b "Brief yang kamu butuhkan sudah saya kirim lewat email ya"
    b "Kau tahu, kadang tugas seperti ini membuatku bertanya: apa masih ada keadilan di Taksopolis?"  
    b "Hati-hati, mereka yang akan kau hadapi... tidak akan segan-segan menghapusmu."
    b "satu hal lagi"
    b "Mulai sekarang kau adalah.."
    show Rendra_Hepi at center
    b "Adi Prayoga" 
    nar "beep..."
    hide Rendra_Hepi
    hide Rendra_Datar
    play sound "rokok.ogg"
    pause 4
    y "Taksopolis..."
    hide You_Mewing
    show You_Senyum at left
    y "Entah apa yang akan kau berikan padaku kali ini"

    jump deskripsi_latar

    return

label end:
    return

label deskripsi_latar:
    scene bg_utopian
    play music "utopia_bg.wav" loop
    nar "Kamu menghela napas panjang. Bermodalkan berkas, kamu melangkah menuju pusat kota, tempat cerita ini akan benar-benar dimulai."

    show You_Mewing at left
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
    hide You_Mewing
    show You_Merengut at left
    y "Itukah definisi utopia bagimu?"

    nar "Kamu membaca lagi berkasmu"

    y "50 persen dari kejahatan tersebut adalah"
    y "...."
    hide You_Merengut
    show You_Mewing at left
    y "Penggelapan pajak"
    y "Pantas saja mereka bisa lolos dengan tindak kriminalnya"
    y "Hukum disini bisa dibeli dengan uang"

    nar "Kamu membuka folder terakhir di berkas organisasimu"
    nar "'Seorang detektif yang baik seharusnya sudah tau apa yang ingin dia investigasi'"
    y "Apa ini?"
    y "....."
    y "Bro Rendra memang suka iseng"

    scene bg_darkalley
    nar "Kota Taksopolis tampak megah dari kejauhan. Namun semakin dalam kamu melangkah, semakin banyak kejujuran yang terlihat terkubur."  
    nar "Bangunan kumuh berdiri di antara gedung-gedung pencakar langit milik para taipan."  
    nar "Jalanan penuh lubang, anak-anak berlari tanpa alas kaki, dan bau sampah menyengat hidungmu."  

    show You_Merengut at left
    y "...Beginikah hasil dari sebuah kota yang diatur oleh orang-orang serakah?"
    pause 1
    nar "Sudah beberapa jam semenjak terakhir kamu menyantap hidangan"
    nar "Menanggapi kelaparanmu,"
    nar "Kamu menghampiri sebuah stand batagor yang ada di pinggir jalan"

    scene bg_foodstand
    play music "foodstand.wav" loop
    show You_Senyum at left
    y "Bang, Batagor 50rb ya"
    show Batagor at center
    tuk "Makan disini apa dibawa pulang, Pak?"
    y "Makan sini aja ya"
    tuk "Oke, tunggu sebentar ya"
    y "Oke"
    hide Batagor
    nar "Kamu melihat ada tumpukan koran-koran di meja stand itu"
    hide You_Senyum
    menu:
        "Ambil koran?"

        "Ambil Koran":
            image koran :
                "koran.png"
                yalign 0.5
            show koran
            show You_Mewing at left

            y "Bang, emangnya koran masih kepake ya disini?"
            show Batagor at center
            tuk "..."

            nar "Abang batagor melirik ke kanan kiri dan mendekat kepadamu seakan akan membisikkan sesuatu"
            tuk "Kalau pake koran nggak dicek pemerintah pak"
            tuk "Ini jadi satu satunya media yang bisa kita percaya"
            y "Oh gitu ya pak"
            nar "Tatapan tukang batagor tiba-tiba tajam."  
            tuk "Bapak penasaran, ya? Saya tahu perusahaan itu... Dominion Corp."  
            tuk "Hati-hati, Pak. Mata-mata mereka ada di mana-mana." 
            y "Izin baca ya bang"

            tuk "Sok aja atuh"

            nar "Kamu mulai membuka koran tersebut lembar per lembar"
            nar "Semuanya berita masih terasa normal"
            nar "Sorry, normal disini adalah normal standard Taksopolis"
            nar "Sampai di halaman terakhir, kamu melihat nama sebuah perusahaan yang sedang mekar"
            hide koran

        "Biarin aja":
            show You_Mewing at left
            y "Bang, disini ada perusahaan yang belakangan ini cepet banget pertumbuhannya ngga ya?"
            tuk "Maksudnya, pak?"
            y "Ya, kayak kemaren ngga kedengeran apa apa tiba tiba langsung booming"
            tuk "Hmm...."
            nar "Abang batagor melirik ke kanan kiri dan mendekat kepadamu seakan akan membisikkan sesuatu"
            tuk "Ada pak, bahkan katanya pendapatan setahunnya bisa sampai 400 Miliar USD, Dominion Corp" 

    hide You_Mewing
    with vpunch    
    y "400 Miliar USD dalam setahun?!"
    y "Perusahaan apa ini?! Bahkan aku nggak pernah melihatnya!"
    tuk "Punten pak, ini batagornya"
    y "Oh iya, makasih bang"
    
    nar "Kamu melanjutkan ke-kagetanmu sambil makan batagor"

    ##space untuk pengembangan##

    hide Batagor
    y "Dominion corp, perusahaan consultant..."
    hide You_Mewing 
    show You_Senyum at left
    y "Mungkinkah ini...."

    scene bg_hitam
    play music "bg_hitam.wav" loop
    nar "Jantungmu berdegup cepat."
    nar "Rasanya seperti dihimpit oleh rasa takut sekaligus penasaran."
    y "Mungkin inilah yang dimaksud Bro Rendra, haruskah aku ungkap semua ini?"
    menu :
        "Apa yang akan kamu lakukan?"

        "Tindak lanjuti" :
            nar "Kamu tahu, setiap langkah membawa risiko. Tapi mundur sekarang bukanlah pilihan." 
            jump tindaklanjut
        "Abaikan, biarkan dirimu bersantai sejenak" :
            nar "Pikiranmu berkata untuk berhenti sejenak, tapi nuranimu menggelitik: 'Apa ini tindakan yang benar?'"
            jump Abaikan

label tindaklanjut:
    scene bg_hitam
    nar "Mengingat berkas yang diberikan Bro Rendra, kamu pun bergegas kembali ke penginapanmu"
    "..."
    play sound "step.ogg"
    y "Inikah..."

    scene bg_computer
    play music "initial_dark_alley_intro (1).wav" loop
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
    with vpunch
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
            
            with vpunch
            y "!!!"
            y "Jam berapa ini?!"
            y "Bahkan aku belum selesai membaca dokumennya"
            play sound "startup.ogg"
            nar "click click... jarimu bergerak cepat di keyboard dan mousemu"
            y "...."
            nar "click!"
            with vpunch
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
            with vpunch
            y "!!!"
            y "Jam berapa ini?!"
    y "Oke, tenang"
    y "Mari kita isi form pendaftaran Dominion Corp terlebih dahulu"
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
    play music "bg_hitam.wav" loop

    nar "Di perjalanan menuju kantor Dominion Corp, kamu melewati sebuah panti asuhan tua."  
    nar "Atap bangunan itu bocor, dindingnya retak, dan anak-anak berlarian tanpa sepatu."

    show You_Merengut at left
    y "Panti ini... tidak layak dihuni. Bahkan untuk anak kecil sekalipun."
    nar "Seorang wanita paruh baya muncul, wajahnya letih namun penuh senyum kecil."  
    un "Selamat sore, Pak. Mencari sesuatu?"

    menu:
        "Tanya tentang panti asuhan ini":
            un "Dulu pemerintah sering membantu kami. Tapi sekarang, bantuan itu hilang... katanya tidak ada dana."  
            show You_Mewing at left
            y "Tidak ada dana? Tapi anggaran seharusnya mencukupi..."

            un "Kalau pajak dibayarkan tepat waktu, mungkin sekolah ini sudah direnovasi. Anak-anak pantas dapat masa depan, bukan?"  
            y "...Pajak itu bukan sekadar angka. Ini soal kehidupan."

        "Lewati dan lanjutkan perjalanan":
            nar "Kamu menundukkan kepala dan pergi. Namun gambaran wajah anak-anak itu tetap membekas di benakmu."  
            y "...Aku harus menyelesaikan ini."

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


##PERCABANGAN BESAR


label alur_akuntan:
    scene bg_kantor
    play music "bg_kantor.wav" loop
    nar "Kamu berdiri di depan gedung Dominion Corp, bangunan tinggi dengan kaca-kaca berkilauan yang memantulkan cahaya matahari."
    nar "Pintu otomatis terbuka, menyambutmu masuk ke lobi yang megah namun dingin."
    y "...Bangunan ini terlihat sempurna, tapi aku tahu ada rahasia kotor di dalamnya..."
    nar "Seorang resepsionis wanita berdiri di balik meja besar, tersenyum sopan saat melihatmu mendekat."

    un "Selamat datang di Dominion Corp. Anda Adi Prayoga, bukan? Pelamar posisi akuntan?"
    y "Ya, betul. Saya punya jadwal wawancara hari ini."
    un "Bagus. Silakan Ikuti saya ke ruang HRD, ya"

    scene bg_hitam
    nar "Kamu melangkah dengan perlahan di belakang wanita tersebut"
    nar "Jantungmu berdegup kencang, serasa seperti akan sidang skripsi"
    nar "Sepanjang perjalanan, kamu memperhatikan setiap sudut ruangan dengan seksama."
    y "...Segalanya terlihat terlalu sempurna di sini..." 
    y "...Apa ini cara mereka menutupi kebusukan mereka?..."

    scene bg_ruanghrd
    play music "hrd_mulai_diwawancara.wav" loop
    nar "Langkah wanita tersebut kemudian berhenti di depan ruangan bertuliskan 'HRD' "
    show HRD_Senyum at center
    un "Silakan masuk. Ini adalah ruang wawancara kami."
    an "Selamat datang di Dominion Corp, Pak Adi. Saya Anita Kartika, kepala HRD."
    y "Terima kasih, Ibu Anita. Sebuah kehormatan bisa hadir di sini."
    nar "Dirimu sadar betul untuk tidak membuat blunder di hari wawancaramu"
    nar "Ruang itu minimalis "
    nar "hanya ada meja panjang dengan beberapa kursi dan sebuah layar besar di dinding."
    an "Saya akan langsung ke inti wawancara ini." 
    an "Pertama-tama, apa yang membuat Anda tertarik melamar ke Dominion Corp?"

    $ counter = 0

    menu:
        "Kebetulan skill dan kemampuan saya sesuai dengan yang dicari perusahaan Ibu":
            $ counter += 1
            an "Jawaban yang bagus. Kami memang mencari kandidat dengan kemampuan seperti itu."
        "Saya anaknya direktur, Bu":
            an "Itu bukan alasan yang cukup kuat untuk melamar di sini."
        "Saya ingin menyelidiki tentang penggelapan pajak kantor ini, Bu":
            an "Itu alasan yang aneh. Apakah Anda serius?"

    an "Apa yang Anda ketahui tentang posisi yang Anda lamar ini?"

    menu:
        "Saya tahu posisi ini membutuhkan ketelitian dalam menganalisis laporan keuangan":
            $ counter += 1
            an "Benar sekali. Itu adalah salah satu keahlian utama yang kami butuhkan."
        "Saya tidak terlalu paham, tapi saya yakin bisa belajar sambil bekerja":
            an "Kami mencari kandidat yang sudah paham mengenai tanggung jawabnya."
        "Posisi ini akan memudahkan saya untuk menyelidiki perusahaan ini":
            an "Itu bukan jawaban profesional. Saya khawatir Anda tidak serius."

    an "Bagaimana Anda menghadapi tekanan kerja yang tinggi?"

    menu:
        "Saya terbiasa bekerja di bawah tekanan dan tetap menjaga hasil yang optimal":
            $ counter += 1
            an "Itu kualitas yang sangat penting. Saya suka mendengar itu."
        "Saya biasanya akan meminta banyak bantuan dari rekan kerja":
            an "Itu bukan pendekatan yang baik untuk menangani tekanan."
        "Saya cenderung menghindari situasi yang terlalu menekan":
            an "Sayangnya, di sini kami membutuhkan seseorang yang tahan terhadap tekanan."

    if counter >= 2:
        jump diterima_accountant
    else:
        jump ditolak_accountant

label diterima_accountant:
    play music "bg_pas_dapet_job.wav"
    an "Selamat, Anda diterima untuk posisi akuntan di Dominion Corp."
    an "Silakan datang besok untuk memulai hari pertama Anda."
    y "...Baik, terima kasih atas kesempatannya."
    jump bekerja_accountant


label ditolak_accountant:
    an "Maaf, kami belum bisa menerima Anda untuk posisi ini. Terima kasih sudah melamar."
    y "...Terima kasih atas kesempatannya."
    nar "Hatimu bergejolak, mengapa ini bisa terjadi?"
    nar "Mungkin di misi selanjutnya dirimu bisa berbenah"
    nar "...dan berhenti mengacaukan semuanya."
    return

label bekerja_accountant:
    $ detective_point = 0  # Variabel untuk mencatat poin deteksi yang benar

    # Scene 1: Ruang Kerja Akuntan
    scene bg_insidekantor
    play music "bg_kantor.wav" loop
    nar "Hari pertama sebagai akuntan di Dominion Corp. Ruang kerja ini tampak sunyi, tapi ada sesuatu yang terasa janggal."  
    show You_Mewing at left  
    y "Banyak angka di sini. Tapi, angka tidak pernah bohong... kecuali jika seseorang memutarbalikkannya."  
    nar "Tugas pertamamu adalah memeriksa laporan keuangan. Sebuah meja dengan tumpukan berkas menantimu."  

    # Deteksi 1: Pemotongan Asuransi
    nar "Matamu tertuju pada laporan gaji karyawan. Kamu menyisir setiap angka dengan hati-hati."  
    show You_Merengut at left  
    y "Ada yang tidak beres di sini... potongan asuransi?"

    menu:
        "Periksa lebih dalam: Potongan asuransi ini tidak tercatat dengan jelas.":
            $ detective_point += 1
            y "Potongan ini tidak ada rincian pastinya. Harusnya ada penjelasan lengkap tentang klaim asuransi."  
            nar "Bayangkan jika salah satu karyawan sakit dan asuransi itu tidak cair... Nyawa bisa terancam hanya karena ini."  
            y "Ini bukan sekadar angka, ini soal hidup dan mati."  
        "Nomor referensi tampak wajar, lanjutkan saja.":
            y "Mungkin ini bukan masalah besar. Tapi... perasaan ini masih menggangguku."  
        "Abaikan, fokus ke laporan lain.":
            y "Aku harus hati-hati. Terlalu banyak asumsi bisa membuatku melewatkan hal penting."

    # Scene 2: Ruang Arsip
    scene bg_documentroom
    play music "bg_hitam.wav" loop
    nar "Kamu pindah ke ruang arsip untuk memeriksa dokumen lebih lama. Ruangan itu dingin dan berdebu, seolah menyembunyikan banyak rahasia."  
    show You_Mewing at left  
    y "Jika ada yang ingin disembunyikan... pasti ada di sini."

    # Deteksi 2: Pengeluaran Tidak Wajar
    nar "Kamu menemukan berkas pengeluaran perusahaan. Salah satu laporan mencurigakan menarik perhatianmu."  
    menu:
        "Lihat detail pembayaran ke luar negeri: Kenapa ada biaya ini?":
            $ detective_point += 1
            y "Pembayaran luar negeri sebesar 2 miliar rupiah? Tidak ada keterangan barang atau jasa apapun."  
            y "Untuk apa uang ini? Ini jelas transaksi yang mencurigakan."  
            nar "Pikiranmu mulai mengaitkan semua ini... Ke mana larinya uang rakyat jika pajak terus dimanipulasi?"  
        "Pengeluaran ini terlihat sudah disetujui, lanjutkan saja.":
            y "Mungkin ini sah... Tapi mengapa rasanya ada yang salah?"
        "Biarkan saja. Fokus ke dokumen berikutnya.":
            y "Aku mungkin hanya berlebihan. Ada hal lain yang harus kuperiksa."

    # Refleksi di Ruang Pantry
    scene bg_kitchen
    play music "bg_hitam.wav"
    nar "Kamu menuju pantry untuk menenangkan pikiran. Beberapa karyawan berbincang di pojok, namun hening ketika melihatmu masuk."  
    show You_Merengut at left  
    y "Suasana di sini terlalu aneh. Mereka seperti takut berbicara... Apa yang mereka sembunyikan?"  
    nar "Satu suara samar terdengar dari dua karyawan di ujung ruangan."  

    show Bisikan at center with vpunch
    un "Potongan gaji kita makin besar, tapi fasilitas kesehatan malah dicabut."  
    un "Kalau begini terus, siapa yang akan bertanggung jawab kalau kita sakit?"  

    hide Bisikan
    show You_Mewing at left  
    y "...Mereka bahkan tidak tahu hak mereka. Pajak yang seharusnya untuk mereka malah lenyap begitu saja."  

    # Scene 3: Laporan Karyawan - Jumlah Karyawan Tak Wajar
    scene bg_insidekantor
    nar "Kamu kembali ke meja kerjamu dan membuka laporan terakhir: jumlah karyawan."  
    show You_Mewing at left  
    y "Jumlah karyawan resmi... 900 orang? Tunggu..."  
    nar "Kamu membuka data publik dari Dominion Corp yang diberikan oleh Bro Rendra."  

    menu:
        "Cocokkan dengan data publik: Ini tidak benar!":
            $ detective_point += 1
            with vpunch
            y "Mereka mengklaim 1500 karyawan! Tapi di sini cuma 900!"  
            y "Selisih 600 orang... Apakah ini cara mereka menghindari pajak tenaga kerja?"  
            nar "Dampaknya jelas: uang yang seharusnya untuk kesejahteraan karyawan lenyap begitu saja."  
        "Lewati saja, mungkin ini bukan masalah besar.":
            y "Angka ini aneh... Tapi aku harus berhati-hati sebelum menuduh sesuatu."  

    # Refleksi Akhir Investigasi
    scene bg_hitam
    nar "Kamu menyandarkan tubuhmu di kursi, memejamkan mata sejenak."  
    nar "Potongan asuransi yang tidak jelas. Pengeluaran misterius ke luar negeri. Jumlah karyawan yang dipalsukan."  
    show You_Merengut at left  
    y "Semua ini... tidak hanya soal uang. Ini tentang kehidupan orang-orang yang dirampas haknya."  
    y "Jika pajak itu dibayarkan dengan benar, berapa banyak sekolah yang bisa dibangun? Berapa banyak nyawa yang bisa diselamatkan?"  

    # Keputusan Akhir
    if detective_point >= 2:
        jump konvergensi_1
    else:
        jump gagal_misi


label konvergensi_1:
    nar "Sepertinya feelingmu cukup kuat"
    y "Data yang saya kumpulkan sudah cukup bagus"
    y "Ini bukan kebetulan."
    y "Ada sesuatu yang sangat besar di balik semua ini."
    y "Aku harus segera melapor."
    y "Keputusan ini... tak bisa aku tunda lagi."
    jump konvergensi
    return


label alur_OB:

    scene bg_kantor
    play music "bg_kantor.wav" loop 
    show HRD_Senyum at center
    an "Halo, selamat datang"
    an "Ini Pak Adi ya?"
    show You_Senyum at left
    y "Oh iya bu"
    an "Selamat datang di Dominion Corp, Pak Adi."
    an "Saya Anita Kartika, kepala HRD di sini." 
    an "Saya akan menjadi pembimbing Anda selama proses orientasi."
    y "Terima kasih, Bu Anita."
    y "Sebuah kehormatan bisa bergabung di perusahaan sebesar ini."
    nar "Bu Anita menjulurkan tangannya untuk menjabat tanganku"
    hide You_Senyum
    show You_Merengut at left
    hide HRD_Senyum
    nar "Rasanya dingin"
    nar "Seakan ada sesuatu yang belum aku ketahui"
    show HRD_Datar at center
    an "Oh, Anda pasti akan belajar banyak di sini." 
    an "Kita di Dominion Corp selalu menghargai kinerja keras dan... loyalitas."
    nar "Kata 'loyalitas' diucapkannya dengan penekanan yang terasa menusuk, "
    nar "seolah ada makna tersembunyi di baliknya."
    an "Ayo, saya akan memperkenalkan Anda ke area kerja."
    
    scene bg_insidekantor
    play music "bg_hitam.wav" loop
    show HRD_Senyum
    an "Ini adalah area kerja utama. Tim administrasi, operasional, dan keuangan bekerja di sini."
    nar "Ruangan itu luas, dengan meja-meja berjejer walau tidak rapi dan layar monitor yang memancarkan cahaya biru."
    nar "Namun, suasananya terlalu tenang. Tidak ada suara obrolan atau gelak tawa. Semua karyawan tampak fokus."
    nar "...atau mungkin terlalu takut untuk melakukan kesalahan."
    show You_Mewing at left 
    y "Sepertinya semua orang di sini sangat disiplin ya, Bu"
    an "Kami menghargai profesionalisme, Pak Adi."
    an " Setiap detik di Dominion Corp adalah investasi menuju kesuksesan."
    nar "Kalimat itu terdengar seperti skrip yang dihafal."

    scene bg_pintuterbuka
    play music "inside_dan_tour_kantor.wav" loop
    nar "Ibu Anita memimpinmu menyusuri koridor panjang yang sepi." 
    nar "Suara langkahmu bergema samar di dinding putih."
    scene bg_documentroom
    show HRD_Senyum at center
    an "Ini adalah area penyimpanan dokumen penting."
    an "..."
    an "Kita tidak sering membawa karyawan baru ke sini, "
    an "Tapi karena kamu nanti akan membersihkan ruangan ini, rasanya perlu untuk saya beritahu"
    nar "Nada bicaranya terdengar formal"
    show You_Senyum at left
    y "Tentu, Ibu. Menarik sekali melihat bagaimana perusahaan sebesar ini mengelola arsipnya."
    scene bg_pintuterbuka
    nar "Namun, langkah Anita tiba-tiba melambat saat melewati pintu toilet bercat abu-abu."
    nar "Dari dalam ruangan, terdengar suara samar percakapan yang tergesa-gesa."

    play music "bg_hitam.wav" loop
    show Bisikan at center
    with vpunch
    un "Ini masalah serius! Mereka akan menyerang kita jika tahu soal pengurangan biaya ini."
    un "Tenang. Selama kita punya 'manajemen kreatif' di laporan pajak, semuanya akan baik-baik saja."
    un "Kau bercanda? Kita sudah memotong anggaran asuransi kesehatan, dan itu mengorbankan nyawa, Fauzan!"
    un "Aku tahu, tapi kalau kita bayar semua itu, perusahaan ini akan rugi besar. Lagipula, kematian itu bukan salah kita, kan?"

    nar "Jantungmu berdegup kencang."
    nar "Suara itu berhenti sesaat, seolah mereka tahu seseorang mendengarkan."
    nar "Wajah Ibu Anita sedikit memucat"

    hide Bisikan
    show HRD_Resah

    an "Pak Adi, ayo kita lanjutkan tur. Tidak ada yang menarik di sini."
    nar "Kata-kata Anita keluar terlalu cepat," 
    nar "seperti berusaha menutupi sesuatu. Matanya menghindari kontak pandang denganmu."

    show You_Merengut at left
    y "Tentu, Bu Anita."
    nar "Dengan demikian, tur kantor masih dilakukan oleh Ibu"
    nar "Kamu mencoba fokus pada tur, tetapi percakapan itu terus bergema di telingamu."
    y "...Mereka memotong anggaran asuransi..."
    y "...dan ada seseorang yang meninggal?..."
    y "...Aku harus menemukan lebih banyak bukti."
    y "Dunia harus tahu siapa mereka sebenarnya..."

    nar "Di sela melamunmu, Ibu Anita kembali berucap"
    an "Kadang ada kebijakan perusahaan yang sulit dimengerti oleh orang luar, Pak Adi. Kami hanya ingin menjaga keberlanjutan bisnis."
    y "Tentu saja, Bu. Saya paham sekali."
    nar "Namun, di balik senyum sopanmu, niatmu semakin kuat untuk menyelidiki lebih dalam."

    scene bg_officeboy
    play music "ruang_hrd_dan_ruang_OB.wav" loop
    show HRD_Senyum
    an "Baik, Pak Adi. Saya harap tur tadi memberi Anda gambaran tentang bagian mana saja yang harus diperhatikan disini"
    an "Sekarang, saya akan serahkan jadwal tugas Anda untuk hari ini."
    show You_Senyum at left 
    y "Terima kasih, Bu Anita. Saya siap bekerja."
    nar "Anita memberikanmu clipboard dengan daftar tugas. Mata kamu langsung tertuju pada salah satu tugas: 'Membersihkan Ruang Direktur.'"
    y "...Kesempatan bagus. Aku bisa mulai mencari sesuatu di sana...."
    an "Jika Anda butuh bantuan atau merasa kesulitan, jangan ragu untuk menghubungi saya, ya."
    y "Tentu, Bu. Terima kasih."
    nar "Anita tersenyum ramah sebelum meninggalkanmu untuk memulai pekerjaanmu."

    scene bg_directoroffice
    play music "director_office.wav" loop
    nar "Kamu membuka pintu ruangan Direktur dengan hati-hati."
    nar "Ruangan itu terlihat mewah dengan furnitur mahal dan aroma wangi kayu cendana."
    nar "Berbeda sekali seperti aroma lorong dekat penginapanmu."
    y "Baiklah, waktunya 'bekerja'"
    nar "Sambil membersihkan meja, matamu menangkap tumpukan dokumen yang terlihat mencurigakan."
    ##mulai collecting detective point
    $ detective_point =0
    $ laporan_keuangan=False

    menu:
        "Periksa dokumen di meja":
            y "Hmm, laporan keuangan bulanan. Tidak ada yang aneh di sini..."
            y "tunggu."
            y "Ada perbedaan besar antara pendapatan yang tercatat di laporan ini dan data yang aku lihat sebelumnya."
            nar "Kecurigaanmu semakin kuat."
            nar  "Kamu mengambil foto dokumen itu dengan ponselmu sebelum meletakkannya kembali."
            $ detective_point +=1
            $ laporan_keuangan=True
        "Lanjutkan bersih-bersih tanpa menyentuh apa pun":
            nar "Kamu memilih untuk tidak mengambil risiko sekarang. Ada banyak waktu untuk mencari bukti lebih besar nanti."

    scene bg_documentroom
    nar "Ruangan arsip itu sunyi."
    nar "Hanya suara langkahmu yang menggema di antara rak-rak tinggi berisi dokumen tebal."
    y "...Aku harus menemukan sesuatu."
    y "Sesuatu yang nyata."
    nar "Matamu tertuju pada sebuah file di sudut meja."
    nar "File itu terlihat baru saja digunakan."
    y "...Apa ini?"
    nar "Kamu membuka file tersebut dengan tangan gemetar."
    y "Jumlah karyawan..."
    y "Ini... tidak masuk akal."
    nar "File itu menunjukkan jumlah karyawan Dominion Corp sebenarnya hanya 900 orang."
    nar "Bukan 1500 seperti yang mereka klaim."
    y "...Mereka memalsukan data karyawan mereka."
    y "Untuk apa?"
    y "Apakah ini bagian dari manipulasi pajak mereka?"

    menu:
        "Ambil file tersebut":
            $ detective_point += 1
            $ jumlah_karyawan = True
            nar "Kamu menyelipkan file itu ke dalam tas kecilmu."
            nar "Tidak ada yang boleh tahu aku melihat ini."
        "Biarkan file tetap di sana":
            nar "Kamu memutuskan untuk meninggalkan file itu."
            nar "Tapi fakta ini terus menghantui pikiranmu."
    scene bg_kitchen
    nar "Ruangan pantry sunyi."
    nar "Hanya suara mesin kopi yang mengisi udara."
    y "...Kenapa ruangan ini terasa berbeda?"
    nar "Pandanganmu tertuju pada meja kecil di pojok ruangan."
    nar "Ada tumpukan kertas yang terlihat berantakan."
    y "...Apa ini?"
    nar "Kamu mendekati meja itu."
    nar "Tanganku gemetar."
    y "...Sebuah nota?"
    nar "Kertas itu mencatat transaksi besar."
    y "500 juta rupiah."
    y "...Tidak ada detail barang."
    y "Ini... tidak wajar."
    nar "Kamu merasa sesuatu yang aneh merayap di tubuhmu."
    nar "Ini bukti... atau jebakan?"
    
    menu:
        "Ambil nota tersebut":
            $ detective_point += 1
            $ nota = True
            nar "Kamu memasukkan nota itu ke dalam saku."
            nar "Tidak ada yang boleh tahu aku mengambil ini."
        "Biarkan nota tetap di sana":
            nar "Kamu memutuskan untuk tidak mengambil risiko."
            y "...Tapi nota itu terus memanggilku."
    scene bg_storage
    nar "Ruang penyimpanan terasa gelap dan lembap."
    nar "Lampu di langit-langit berkedip pelan, menciptakan bayangan yang bergerak-gerak."
    y "...Aku tidak seharusnya di sini."
    nar "Tapi sesuatu menarik perhatianmu."
    nar "Sebuah laci terbuka sedikit."
    nar "Di dalamnya, ada sebuah USB drive."
    y "...USB ini terlihat mencurigakan."
    nar "Tidak ada label. Tidak ada keterangan."
    y "Ini... pasti menyimpan sesuatu yang penting."
    nar "Tanganmu gemetar saat menyentuh USB itu."
    y "...Apakah aku harus mengambilnya?"
    
    nar "Kamu memegang USB itu erat-erat."
    nar "Pikiranmu bercampur aduk."
    y "...Aku harus tahu apa isinya."
    nar "Di seberang ruangan, kamu melihat sebuah komputer yang masih menyala."
    y "...Apakah aku harus memeriksanya di sini?"

    menu:
        "Periksa isi USB di komputer terdekat":
            nar "Kamu mendekati komputer itu perlahan."
            nar "Tanganku gemetar saat memasukkan USB."
            nar "Layar menyala dengan cepat."
            nar "File-file mulai terbuka. Dokumen pajak. Data rahasia."
            with vpunch
            y "Ini dia! Bukti yang aku cari..."
            nar "Tapi kemudian...."
            nar "beep... beep..."
            nar "Alarm berbunyi. Layar tiba-tiba berubah merah."
            nar "Sebuah pesan muncul di layar: 'AKSES ILEGAL TERDETEKSI.'"
            scene bg_insidekantor
            nar "Langkah kaki terdengar mendekat."
            an "Pak Adi, apa yang sedang Anda lakukan di sini?"
            nar "Suara Anita terdengar dingin, menusuk telinga."
            an "Maaf, kami tidak bisa mentoleransi tindakan seperti ini."
            nar "Tubuhmu terasa kaku."
            nar "Dalam beberapa menit, kamu sudah berada di luar gedung."
            y "...Aku dipecat."
            return

        "Tunggu sampai nanti untuk memeriksa":
            nar "Kamu menggenggam USB itu erat-erat."
            y "...Terlalu berisiko memeriksa di sini."
            nar "Kamu memutuskan untuk membawa USB itu ke tempat yang lebih aman."
            nar "Langkah kakimu terasa berat saat meninggalkan ruang penyimpanan."
            $ detective_point +=1
    if detective_point >= 2:
        jump konvergensi_1
    else:
        nar "Aku masih harus menggali lebih dalam."
        nar "Aku tak bisa membiarkan ini begitu saja."
        jump gagal_misi
        return

label gagal_misi:
    scene bg_hitam
    play music "bg_hitam.wav" loop
    nar "Kamu duduk diam di sudut ruangan, tanganmu gemetar."
    nar "Semua bukti yang seharusnya kamu kumpulkan... hilang begitu saja."
    show You_Merengut at left
    y "Bagaimana ini bisa terjadi...?"
    y "Aku seharusnya lebih teliti."
    
    nar "Suara dalam pikiranmu terus menghantui. Semua perjuanganmu terasa sia-sia."
    nar "Kamu tahu, misi ini penting. Tapi kali ini, kamu gagal."
    
    scene bg_darkalley
    play sound "rain.ogg" loop
    nar "Hujan turun deras di Taksopolis, seolah ikut menertawakan kegagalanmu."
    nar "Bayangan Dominion Corp terus menghantuimu. Mereka masih bebas... dan kamu tidak bisa melakukan apa-apa."
    
    show Rendra_Datar at center
    b "Apa kau pikir ini hanya permainan, Adi?"
    with vpunch
    b "Kau biarkan mereka lolos begitu saja. Kau gagal!"
    hide Rendra_Datar

    show You_Mewing at left
    y "...Aku harus mencoba lagi. Ini belum berakhir."
    
    menu:
        "Apa yang akan kamu lakukan sekarang?"
        "Coba lagi dari awal":
            jump start
        "Keluar dari permainan":
            scene bg_hitam
            play music "ending_and_credit_scene.wav"
            nar "Kamu meninggalkan semua itu. Namun di suatu tempat, kejahatan Dominion Corp terus berlanjut..."
            "Bad Ending"
            return

label konvergensi:

    scene bg_darkalley 
    
    nar "Hari itu terasa begitu berat. Setiap langkah menuju rumah terasa lebih lama."
    nar "Kamu berjalan pulang, tubuhmu lelah, namun pikiranmu penuh dengan bayangan."
    nar "Semua petunjuk sudah terkumpul. Semua yang tersembunyi akhirnya terlihat jelas."
    show You_Mewing at left
    y "...900 karyawan, padahal yang seharusnya 1500."
    y "...Asuransi yang dipotong, namun tak tercatat dengan jelas."
    y "...Nota transaksi yang mencurigakan. Semua mengarah ke satu orang."

    show You_Merengut at left
    nar "Tak bisa lagi Kamu biarkan hal ini begitu saja. Semua bukti yang ditemukan tak bisa dibiarkan menghilang begitu saja."
    y "Direktur itu harus bertanggung jawab."

    # Scene: Bersiap
    show You_Senyum at left
    nar "Kamu berdiri, merapikan jasmu, dan memastikan semua bukti sudah di tangan."
    y "Kali ini, dia tak akan mundur. Langkah-langkah yang diambil hari ini akan menentukan segalanya."
    y "Hari ini... semuanya berakhir."

    # Scene: Tidur dan Bangun
    scene bg_computer with dissolve

    nar "Malam terasa panjang. Tidur datang dengan cepat, namun hati Kamu tak tenang."
    nar "Di dalam tidurmu, bayangan bukti dan wajah sang Direktur terus menghantui."
    nar "Dan akhirmu, pagi datang juga."

    nar "Kamu terbangun, matamu masih terasa berat, namun kini lebih pasti."
    nar "Sebuah keputusan besar menunggu. Segalanya akan berakhir hari ini."

    # Scene: Konfrontasi dengan Direktur
    scene bg_insidekantor with dissolve
    show Baskoro_Datar at center
    nar "Kamu tiba di kantor. Di ruang tengah, Direktur Baskoro duduk dengan tenang, tampak tak terganggu."
    nar "Namun Kamu tahu, semuanya sudah terungkap."

    show You_Merengut at left
    y "Kau pikir aku tak akan tahu apa yang kau sembunyikan..."
    with vpunch
    y "BASKORO!!"
    nar "Kamu melangkah mendekat. Setiap langkahmu terasa semakin penuh dengan ketegasan."
    nar "Kini, tak ada lagi tempat untuk lari."

    show Baskoro_Nyengir at center
    di "Apa maksudmu, Kamu? Semua sudah berjalan dengan baik. Semua sudah sesuai dengan prosedur."

    show You_Mewing at left
    y "Prosedur? Aku menemukan jumlah karyawan yang hanya 900, padahal seharusnya 1500!"
    y "Kau berani memalsukan data begitu besar. Kenapa?"
    nar "Kamu menatap Direktur dengan tajam, seolah menusuk langsung ke jantung kebohongannya."

    show Baskoro_Nyengir at center
    di "Itu hanya masalah kecil. Tak perlu terlalu dibesar-besarkan."

    show You_Merengut at left
    y "Tidak ada yang kecil, [di]. Asuransi yang dipotong, tak tercatat dengan benar!"
    y "Apa yang kau lakukan dengan uang itu? Kenapa kau sembunyikan dari perusahaan?"
    nar "Kamu berbicara dengan nada yang lebih keras. Rasa marah dan keteguhan mengalir dalam suaranya."

    with vpunch
    show Baskoro_Datar at center
    di "Beraninya kau, anak ingusan! Kau tidak tahu siapa yang kau lawan!"
    
    nar "Suara Baskoro menggema di ruangan. Tangannya menghantam meja dengan keras, membuat gelas di atasnya bergetar."

    scene bg_hitam with fade
    play sound "heartbeat.ogg"
    nar "Jantungmu berdebar cepat. Tapi kamu tahu, ini bukan saatnya untuk mundur."
    nar "Di luar ruangan ini, dunia sudah tahu siapa dia sebenarnya."

    scene bg_darkalley with fade
    nar "Ingatan akan hari-hari gelap di Taksopolis menghantammu. Semua rasa takut dan keputusasaan yang dirasakan karyawan..."
    nar "...kini menjadi bahan bakar keberanianmu."

    scene bg_insidekantor with fade
    show You_Mewing at left
    
    y "Kau pikir uang yang kau simpan bisa menyelamatkanmu? Pajak itu milik rakyat!"  
    y "Tanpa pajak, anak-anak kehilangan sekolah, pasien kehilangan rumah sakit, dan karyawan kehilangan nyawanya!"  
    show Baskoro_Nyengir at center  
    di "Rakyat? Negara? Mereka tidak peduli darimana uang itu berasal!"  
    show You_Merengut at left  
    y "Salah! Tanpa kepercayaan, negara ini runtuh! Kau adalah bukti buruknya penguasa yang rakus."  
    show Baskoro_Datar at center
    di "Semua itu... demi perusahaan. Demi masa depan kita."

    show You_Mewing at left
    y "Masa depan? Masa depan seperti apa yang kau maksudkan jika karyawan dibiarkan kelaparan dan asuransi tidak cair?"
    y "Aku menemukan transaksi yang mencurigakan. Dan kau mencoba menutupi semuanya."

    nar "Kamu menarik napas dalam-dalam. Semua yang tersembunyi kini sudah terungkap, tak ada lagi yang bisa disembunyikan."

    # Scene: Direktur Berusaha Keluar
    show Baskoro_Nyengir at center
    di "Aku tak bisa terus berdiri di sini. Ini semua... kebodohan. Aku akan keluar."

    show You_Merengut at left
    y "Kau kira bisa lari begitu saja, [di]?"
    nar "Kamu segera mendekatkan dirinya ke pintu. Tak ada yang bisa melarikan diri dari kebenaran."

    y "Kau pikir semua ini akan berakhir begitu saja?"
    y "Polisi sudah tahu semuanya, Baskoro. Tak ada lagi tempat untukmu bersembunyi."
    

    with vpunch
    show Baskoro_Nyengir at center
    di "POLISI? Kau pikir mereka akan percaya omonganmu? Uangku lebih berbicara daripada omong kosongmu!"

    nar "Baskoro tertawa sinis, tetapi wajahnya kini pucat. Dia tahu ini sudah berakhir."

    show You_Senyum at left
    y "Lihatlah sendiri."

    nar "Suara langkah kaki terdengar di luar pintu. Semakin mendekat."
    play sound "step.ogg"
    pause 1
    nar "Kemudian, pintu terbuka dengan kasar."

    with vpunch
    Police "Tuan Baskoro Aryatama, Anda ditangkap atas tuduhan penggelapan pajak, penipuan, dan penyalahgunaan dana perusahaan."

    show Baskoro_Datar at center with vpunch
    di "Tidak... ini tidak mungkin. Aku... AKU TAK AKAN KALAH!"

    show You_Senyum at left
    y "Sudah selesai, Baskoro. Permainanmu berakhir di sini."

    scene bg_hitam with fade
    play music "bg_pas_dapet_job.wav"
    nar "Kamu melihat Baskoro dibawa pergi oleh polisi. Suaranya memudar di balik langkah-langkah berat mereka."
    nar "Ruangan itu terasa lebih ringan sekarang. Beban yang selama ini menghimpit Taksopolis... akhirnya sirna."

    show You_Mewing at left
    y "...Akhirnya, keadilan ditegakkan."
    y "Ini bukan hanya tentang aku. Ini tentang mereka yang tak pernah didengar."

    scene bg_kantor with dissolve
    nar "Direktur ditangkap. Polisi membawanya pergi, dan ia tak bisa melarikan diri lagi."
    nar "Para karyawan yang selama ini tertipu akhirnya menerima gaji yang seharusnya mereka dapatkan."
    nar "Pajak yang selama ini belum dibayar, akhirnya lunas setelah rumah Direktur dijual."
    nar "Dan orang yang meninggal akibat tidak cairnya asuransi, keluarganya kini menerima kompensasi yang layak."

    show You_Mewing at left
    y "Akhirnya... keadilan ditegakkan."

    nar "Kamu duduk, tubuhnya terasa lelah, namun hatinya tenang."
    nar "Segala perjuangan yang dilakukan, tak sia-sia. Semua petunjuk yang terkumpul kini membawa pada akhirnya."

    scene bg_hitam
    nar "Bayarlah pajak dengan benar."  
    nar "Pajak Anda membangun sekolah, rumah sakit, dan jalan raya untuk masa depan kita bersama."  

    nar "Good Ending"
    scene black
    with fade
    "Terima kasih telah bermain!"
    call screen credits_screen
    return

    return

            



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
            play music "ending_and_credit_scene.wav" loop
            nar "Anda telah gagal menjalankan misi untuk mengungkap kasus di kota Taksopolis"

    

