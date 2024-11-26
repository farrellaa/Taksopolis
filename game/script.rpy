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
    define un= Character("???", callback=callback) #untuk orang orang yang dibuat tidak perlu tau namanya

#label start SELALU muncul di new gamez
label start:
    scene bg_darkalley
    #show eileen happy

    nar "Sebuah lorong gelap, di pinggiran kota metropolitan"
    nar "Kota dimana semua orang bisa mendapatkan semua yang mereka mau"
    nar "wanita, kekuasaan, tahta,"
    nar "Di antara bayangan dan bau asam dari lorong itu, Seakan membisikkan sesuatu padamu"  
    nar "'Jangan percaya dengan mereka yang tidak mendengar...'"
    nar "suara itu seperti bisikan hantu, samar tapi cukup tajam untuk menusuk telingamu."  


    nar "buzz... buzz..."
    nar "Handphonemu berdering"
    y "Rendra?"
    b "...."
    b "Brief yang kamu butuhkan sudah saya kirim lewat email ya"
    b "Kau tahu, kadang tugas seperti ini membuatku bertanya: apa masih ada keadilan di Taksopolis?"  
    b "Hati-hati, mereka yang akan kau hadapi... tidak akan segan-segan menghapusmu."
    b "satu hal lagi"
    b "Mulai sekarang kau adalah.."
    b "Adi Prayoga" 
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

    nar "Kamu menghela napas panjang. Bermodalkan berkas, kamu melangkah menuju pusat kota, tempat cerita ini akan benar-benar dimulai."

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

    ##space untuk pengembangan##


    y "Dominion corp, perusahaan consultant..."
    y "Mungkinkah ini...."

    scene bg_hitam

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
    nar "Langkah wanita tersebut kemudian berhenti di depan ruangan bertuliskan 'HRD' "
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
        "Kebetulan skill dan kemampuan saya sesuai dengan yang dicari perusahaan Bapak":
            $ counter += 1
            an "Jawaban yang bagus. Kami memang mencari kandidat dengan kemampuan seperti itu."
        "Saya anaknya direktur, Pak":
            an "Itu bukan alasan yang cukup kuat untuk melamar di sini."
        "Saya ingin menyelidiki tentang penggelapan pajak kantor ini, Pak":
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
    an "Selamat, Anda diterima untuk posisi akuntan di Dominion Corp."
    an "Silakan datang besok untuk memulai hari pertama Anda."
    y "...Baik, terima kasih atas kesempatannya."


label ditolak_accountant:
    an "Maaf, kami belum bisa menerima Anda untuk posisi ini. Terima kasih sudah melamar."
    y "...Terima kasih atas kesempatannya."
    nar "Hatimu bergejolak, mengapa ini bisa terjadi?"
    nar "Mungkin di misi selanjutnya dirimu bisa berbenah"
    nar "...dan berhenti mengacaukan semuanya."
    return


label alur_OB:
    scene bg_kantor
    an "Halo, selamat datang"
    an "Ini Pak Adi ya?"
    y "Oh iya bu"
    an "Selamat datang di Dominion Corp, Pak Adi."
    an "Saya Anita Kartika, kepala HRD di sini." 
    an "Saya akan menjadi pembimbing Anda selama proses orientasi."
    y "Terima kasih, Bu Anita."
    y "Sebuah kehormatan bisa bergabung di perusahaan sebesar ini."
    nar "Bu Anita menjulurkan tangannya untuk menjabat tanganku"
    nar "Rasanya dingin"
    nar "Seakan ada sesuatu yang belum aku ketahui"
    an "Oh, Anda pasti akan belajar banyak di sini." 
    an "Kita di Dominion Corp selalu menghargai kinerja keras dan... loyalitas."
    nar "Kata 'loyalitas' diucapkannya dengan penekanan yang terasa menusuk, "
    nar "seolah ada makna tersembunyi di baliknya."
    an "Ayo, saya akan memperkenalkan Anda ke area kerja."
    
    scene bg_insidekantor
    an "Ini adalah area kerja utama. Tim administrasi, operasional, dan keuangan bekerja di sini."
    nar "Ruangan itu luas, dengan meja-meja berjejer walau tidak rapi dan layar monitor yang memancarkan cahaya biru."
    nar "Namun, suasananya terlalu tenang. Tidak ada suara obrolan atau gelak tawa. Semua karyawan tampak fokus."
    nar "...atau mungkin terlalu takut untuk melakukan kesalahan."
    y "Sepertinya semua orang di sini sangat disiplin ya, Bu"
    an "Kami menghargai profesionalisme, Pak Adi."
    an " Setiap detik di Dominion Corp adalah investasi menuju kesuksesan."
    nar "Kalimat itu terdengar seperti skrip yang dihafal."

    scene bg_pintuterbuka
    nar "Ibu Anita memimpinmu menyusuri koridor panjang yang sepi." 
    nar "Suara langkahmu bergema samar di dinding putih."
    scene bg_documentroom
    an "Ini adalah area penyimpanan dokumen penting."
    an "..."
    an "Kita tidak sering membawa karyawan baru ke sini, "
    an "Tapi karena kamu nanti akan membersihkan ruangan ini, rasanya perlu untuk saya beritahu"
    nar "Nada bicaranya terdengar formal"
    y "Tentu, Ibu. Menarik sekali melihat bagaimana perusahaan sebesar ini mengelola arsipnya."
    scene bg_pintuterbuka
    nar "Namun, langkah Anita tiba-tiba melambat saat melewati pintu toilet bercat abu-abu."
    nar "Dari dalam ruangan, terdengar suara samar percakapan yang tergesa-gesa."

    un "Ini masalah serius! Mereka akan menyerang kita jika tahu soal pengurangan biaya ini."
    un "Tenang. Selama kita punya 'manajemen kreatif' di laporan pajak, semuanya akan baik-baik saja."
    un "Kau bercanda? Kita sudah memotong anggaran asuransi kesehatan, dan itu mengorbankan nyawa, Fauzan!"
    un "Aku tahu, tapi kalau kita bayar semua itu, perusahaan ini akan rugi besar. Lagipula, kematian itu bukan salah kita, kan?"

    nar "Jantungmu berdegup kencang."
    nar "Suara itu berhenti sesaat, seolah mereka tahu seseorang mendengarkan."
    nar "Wajah Ibu Anita sedikit memucat"

    an "Pak Adi, ayo kita lanjutkan tur. Tidak ada yang menarik di sini."
    nar "Kata-kata Anita keluar terlalu cepat," 
    nar "seperti berusaha menutupi sesuatu. Matanya menghindari kontak pandang denganmu."

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
    an "Baik, Pak Adi. Saya harap tur tadi memberi Anda gambaran tentang bagian mana saja yang harus diperhatikan disini"
    an "Sekarang, saya akan serahkan jadwal tugas Anda untuk hari ini."
    y "Terima kasih, Bu Anita. Saya siap bekerja."
    nar "Anita memberikanmu clipboard dengan daftar tugas. Mata kamu langsung tertuju pada salah satu tugas: 'Membersihkan Ruang Direktur.'"
    y "...Kesempatan bagus. Aku bisa mulai mencari sesuatu di sana...."
    an "Jika Anda butuh bantuan atau merasa kesulitan, jangan ragu untuk menghubungi saya, ya."
    y "Tentu, Bu. Terima kasih."
    nar "Anita tersenyum ramah sebelum meninggalkanmu untuk memulai pekerjaanmu."

    scene bg_directoroffice
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
            nar "Anda telah gagal menjalankan misi untuk mengungkap kasus di kota Taksopolis"

    

