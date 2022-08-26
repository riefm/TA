from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  ## GEt user message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    if 'hello' in user_msg:
        msg.body("Halo! Selamat datang di Bot Portal Informasi Prodmas Plus Kota Kediri. Info tentang apa yang ingin kamu ketahui?\n1. Informasi Kota Kediri \n2. Informasi Prodamas Plus \n \nBalas dengan ANGKA saja yaa.. Contoh: 1 \natau ketik !END untuk mengakhiri")
    elif 'menu' in user_msg:
        msg.body("--MENU UTAMA-- \n \nInformasi apa nih yang ingin kamu ketahui? \nSilahkan ketik angka\n1. Untuk Informasi Kota Kediri \n2. Untuk Informasi Prodamas Plus \n \nPilih salah satu ANGKA saja yaa.. Contoh: 1 \natau ketik !END untuk mengakhiri")
    elif 'end' in user_msg:
        msg.body("Terima kasih telah mengakses chatbot Prodamas Plus Kota Kediri! \nUntuk tahu lebih lanjut tentang Prodmas Plus, silakan akses https://prodamasdev.kedirikota.go.id \nUntuk ikuti perkembangannya, follow Instagram https://www.instagram.com/prodamasplus/")
    elif '1' in user_msg:
        msg.body("--Menu: Kota Kediri-- \n \n Informasi tentang Kota Kediri manakah yang ingin kamu ketahui? \n1. *`Profil kota`* Untuk Informasi Profil Kota Kediri \n2. *`Wilayah kota`* Untuk Informasi Wilayah Administratif Kota Kediri \n3. *`Brand kota`* Untuk Informasi Brand Kota Kediri \n4. *`Program unggulan`* Untuk Informasi Program Unggulan Pemkot Kediri \n \natau kirim kata *MENU* untuk kembali ke menu utama.")
    elif '2' in user_msg:
        msg.body('--Menu: Prodamas-- \n \nInformasi tentang Prodmas Plus manakah yang ingin kamu ketahui? Silahkan ketik\n1. *`Pengertian`* untuk Pengertian Prodamas \n2. *`Regulasi`* untuk informasi Regulasi Prodamas \n3. *`Bidang`* untuk informasi Cakupan Bidang Prodmas \n4. *`Kampung keren`* untuk informasi Daftar Kampung Keren \n5. *`KUBE`* Informasi KUBE \n6. *`Bank sampah`* untuk informasi Bank Sampah Kota Kediri \n \natau kirim kata *MENU* untuk kembali ke menu utama.')
    elif 'profil kota' in user_msg:
        msg.body("1. Profil Kota Kediri\nKota Kediri yang lahir pada tanggal 27 Juli 879 menjadi kota terbesar ketiga di Jawa Timur setelah Kota Surabaya dan Kota Malang. Seluruh wilayah Kota Kediri dikelilingi oleh Kabupaten Kediri baik di perbatasan sebelah barat, utara, timur maupun selatan.\nKota Kediri atau dikenal dengan Kota Tahu memiliki semoyan “Djojo ing Bojo” yang bermakna “Mengalahkan Marabahaya”.\n \nKetik *MENU* untuk kembali ke menu utama \natau angka *1* untuk kembali ke submenu Kota Kediri")
    elif 'wilayah kota' in user_msg:
        msg.body("2. Wilayah Administratif Kota Kediri\nKota Kediri memiliki luas sebesar 63.404 km2 terdiri dari 3 kecamatan dan 46 kelurahan.\n i. Kecamatan Mojoroto: 14 kelurahan, 100 RW, dan 486 RT\n ii. Kecamatan Kota: 17 kelurahan, 101 RW, dan 489 RT\n iii. Kecamatan Pesantren: 15 kelurahan, 129 RW, 496 RT\n \nKetik *MENU* untuk kembali ke menu utama\natau angka *1* untuk kembali ke submenu Kota Kediri")
    elif 'brand kota' in user_msg:
        msg.body("3. Brand Kota Kediri\nPada 2016, Walikota Kediri Abdullah Abu bakar mengenalkan brand kota kediri sebagai \n*“Harmoni Kediri The Service City”*\nBrand ini menegaskan bahwa Kota Kediri merupakan Kota Pelayanan dan juga sebagai Kota Jasa dan Perdagangan.\n \nKetik *MENU* untuk kembali ke menu utama \natau angka *1* untuk kembali ke submenu Kota Kediri")
    elif 'program unggulan' in user_msg:
        msg.body("4. Program Unggulan Pemerintah Kota Kediri \nUntuk mendukung percepatan pertumbuhan di bidang ekonomi, sosial, Pendidikan, kesehatan, dan bidang lainnya, Pemerintah Kota Kediri meluncurkan 10 program yang menjadi Program Unggulan Wali Kota Kediri:\n i. Prodmas Plus\n ii.Service City Card (Kartu Melayani)\n iii. Open and Clean Government\n iv. Asuransi Kesehatan Universal (UHC)\n v. Home Care Kondisi Darurat, Lansia, dan Balita\n vi. Pendidikan Gratis Dan Berkualitas\n vii. Pengembangan Usaha Milik Rw (Koperasi Rw)\n viii. Pencipataan 15.000 Wirausaha Baru\n ix. 1 Kelurahan 1 RTH\n x. Kampung Keren (Kreatif dan Independen)\n \nKetik *MENU* untuk kembali ke menu utama \natau angka *1* untuk kembali ke submenu Kota Kediri")
    elif 'pengertian' in user_msg:
        msg.body("1. Apa itu Prodamas?\n Program Pemberdayaan Masyarakat (PRODAMAS) adalah suatu program pembangunan masyarakat ditingkat kelurahan yang berbasis wilayah RT. Program ini dinisiasi oleh Walikota Kediri, Abdullah Abu Bakar yang dimulai sejak tahun 2015 sebagai upaya mewujudkan kemampuan dan kemandirian masyarakat dalam pembangunan. Program meliputi pembangunan bidang infrasturktur, sosial, dan ekonomi dengan besar anggaran Rp 50 Juta/RT. \n \nDalam perkembanganngnya, Prodamas berubah menjadi Prodmas Plus di tahun 2019. Perubahan ini ditandai dengan beberapa perbedaan, salah satunya adalah cakupan bidang yang meliputi infrastruktur, sosial budaya, ekonomi, kesehatan, pendidikan, dan kepemudaan dengan alokasi anggaran sebesar Rp 100 Juta/RT. \n \nKetik *MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas") 
    elif 'regulasi' in user_msg:
        msg.body("2. Regulasi Prodamas\nHal - hal yang mengatur Prodamas telah tercantum dalam Perwali dan telah mengalami beberapa kali perubahan. Untuk Prodamas Plus 2021, pelaksanaan program diatur dalam Peraturan Walikota Kediri Nomor 32 Tahun 2021 tentang Pedoman Teknis Program Pemberdayaan Masyarakat Plus Tahun Anggaran 2022. \nApabila ingin melihat pedoman teknis pelaksanaan Prodamas tahun-tahun sebelumnya dapat mengunjungi laman https://prodamasdev.kedirikota.go.id/tentang.\n \nKetik *!MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas")
    elif 'bidang' in user_msg:
        msg.body("3. Cakupan Bidang Prodamas\nProdamas Plus mencakup 6 bidang, yaitu: \n i. Ekonomi. \n ii. Sosial Budaya\n iii. Kesehatan \n iv. Pendidikan \n v. Kepemudaan \n vi. Infrastruktur \n \nKetik *MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas")
    elif 'kampung keren' in user_msg:
        msg.body("4. Daftar Kampung Keren\nKampung Keren Prodamas merupakan salah satu program unggulan Wali Kota Kediri. Program ini memicu tumbuhnya kreativitas dan kemandirian masyarakat di Kota Kediri untuk memunculkan karakteristik kawasan, keunikan, budaya, keterampilan dan peningkatan potensi ekonomi di kelurahannya. Saat ini ada 10 Kampung Keren di Kota Kediri, yaitu:\n i. Kampung Harmoni Betta (Ikan Cupang) \n ii. Kampung Herbal \n iii. Kampung Heritage \n iv. Kampung Pecut \n v. Kampung Seni \n vi. Kampung Tahu \n vii. Kampung Wisata Kuliner (Winer) \n viii. Kampung Tenun Ikat \n ix. Kampung Wisata Air Sumber Banteng \n x. Kampung Tani\n \nKetik *MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas")
    elif 'kube' in user_msg:
        msg.body("5. Informasi KUBE\nKUBE atau Kelompok Usaha Bersama merupakan program Pemkot Kediri untuk memberdayakan kelompok masyrakat di tingkat RT dalam upaya realisasi Prodamas.\n \nUntuk melihat persebaran KUBE di Kota kediri, kamu bisa mengunjungi laman https://prodamasdev.kedirikota.go.id/peta\n \nKetik *MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas")
    elif 'bank sampah' in user_msg:
        msg.body("6. Informasi Bank Sampah Kota Kediri\nHingga saat ini, sudah tersebar 23 bank sampah di Kecamatan Mojoroto, 18 bank sampah di Kecamatan Pesantren, 30 bank sampah di Kecamatan Kota, 15 bank sampah di sekolah, dan 5 bank sampah di pasar Kota Kediri. \n \nPada tahun 2022 dua bank sampah Kota Kediri, Dewi Sekartaji dan Hijau Daun, sudah berbasis digital. Kamu dapat memantau data sampah secara real time dan menggunakan layanan digital bank sampah melalui website dan aplikasi. \nKamu dapat memantau laporan setoran sampah dan harga jual sampah melalui website https://prodamasdev.kedirikota.go.id/banksampah. Aplikasi E-Bank Sampah Kota Kediri dapat diunduh di Google Playstore atau tekan link berikut https://play.google.com/store/apps/details?id=com.ebanksampah.kedirikota.\n \nKetik *!MENU* untuk kembali ke menu utama \natau angka *2* untuk kembali ke submenu Prodamas")
    else:
        msg.body("Ketik *hello* untuk memulai percakapan!")
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)