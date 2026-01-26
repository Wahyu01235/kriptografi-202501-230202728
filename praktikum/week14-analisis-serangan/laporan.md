# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: Analisis Serangan Kriptografi  
Nama: Achamad Wahyudi  
NIM: 230202728 
Kelas: 5IKRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Analisis serangan kriptografi berangkat dari prinsip paling fundamental bahwa keamanan suatu sistem kriptografi tidak diukur dari kerahasiaan algoritma, melainkan dari ketahanan mekanismenya terhadap upaya adversarial yang realistis. Premis ini, yang diformalkan melalui prinsip Kerckhoffs pada abad ke-19, menolak bias umum bahwa “algoritma yang disembunyikan” otomatis aman. Dalam konteks modern, analisis serangan berfokus pada pemodelan kemampuan penyerang—apa yang diketahui, apa yang dapat diobservasi, dan sumber daya apa yang dimiliki—karena keamanan sejati adalah persoalan asumsi matematis dan operasional, bukan sekadar kompleksitas implementasi.

Secara konseptual, serangan kriptografi diklasifikasikan berdasarkan vektor dan tingkat akses penyerang, seperti ciphertext-only attack, known-plaintext attack, chosen-plaintext attack, hingga chosen-ciphertext attack. Evolusi klasifikasi ini mencerminkan pemahaman bahwa kelemahan sering kali muncul bukan dari algoritma inti, tetapi dari interaksi sistem dengan lingkungannya. Selain serangan matematis terhadap struktur aljabar atau teori bilangan, berkembang pula serangan non-tradisional seperti side-channel attack yang mengeksploitasi kebocoran fisik—waktu eksekusi, konsumsi daya, atau radiasi elektromagnetik—yang secara historis diabaikan oleh model keamanan ideal.

Dari sudut pandang mekanisme teknis, analisis serangan kriptografi menguji sejauh mana asumsi dasar seperti kesulitan faktorisasi, discrete logarithm problem, atau collision resistance pada fungsi hash benar-benar bertahan di bawah kemajuan komputasi dan teknik analitik baru. Di sinilah bias “keamanan statis” sering muncul: sistem dianggap aman hanya karena belum pernah diretas. Padahal, sejarah kriptografi menunjukkan bahwa banyak skema runtuh bukan karena brute force, melainkan karena celah konseptual kecil yang terakumulasi menjadi kegagalan sistemik.

Sebagai strategi defensif, analisis serangan kriptografi mendorong desain berbasis worst-case adversary dan evaluasi berlapis (defense in depth), di mana kegagalan satu komponen tidak langsung meruntuhkan keseluruhan sistem. Namun, argumen tandingannya jelas: peningkatan kompleksitas untuk mengantisipasi semua skenario serangan dapat memperbesar permukaan kesalahan implementasi. Dampak jangka panjangnya bersifat domino—keputusan desain kriptografi memengaruhi kepercayaan publik, stabilitas ekonomi digital, dan ketahanan infrastruktur kritis—sehingga analisis serangan bukan sekadar latihan akademik, melainkan fondasi strategis bagi keamanan sistem modern.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Kriptografi modern dirancang untuk melindungi kerahasiaan, integritas, dan autentikasi data. Namun, dalam praktiknya banyak sistem kriptografi mengalami kegagalan bukan semata karena teori matematika yang lemah, melainkan akibat asumsi desain yang keliru, implementasi yang tidak aman, atau konfigurasi sistem yang usang. Laporan ini menganalisis satu kasus nyata serangan kriptografi dengan pendekatan evaluatif dan strategis, mulai dari identifikasi serangan, analisis kelemahan, hingga rekomendasi solusi.

---

### Langkah 1 — Identifikasi Serangan

Kasus yang dianalisis adalah **serangan brute force dan collision attack pada fungsi hash MD5**. MD5 (Message Digest Algorithm 5) secara historis digunakan secara luas untuk penyimpanan password, checksum file, dan tanda tangan digital. Namun, sejak pertengahan 2000-an, MD5 terbukti rentan terhadap collision attack, di mana dua input berbeda dapat menghasilkan nilai hash yang sama.

Vektor serangan utama berasal dari kemampuan penyerang untuk mengeksploitasi kelemahan kriptografis MD5 guna mempercepat pencarian collision atau menebak hash password melalui brute force dan dictionary attack. Penyebab utama kelemahan ini bukan berasal dari kesalahan operasional semata, melainkan dari desain algoritma MD5 itu sendiri yang tidak lagi mampu menjamin sifat collision resistance dalam konteks komputasi modern.

---

### Langkah 2 — Evaluasi Kelemahan

Kelemahan utama pada kasus ini terletak pada **algoritma kriptografi** yang digunakan. MD5 dirancang pada era dengan asumsi daya komputasi terbatas, sehingga panjang output hash 128-bit dan struktur internalnya kini tidak lagi memadai untuk menghadapi serangan modern. Secara matematis, MD5 telah terbukti rentan terhadap collision attack terstruktur, bukan sekadar brute force.

Namun demikian, bias umum yang perlu dikoreksi adalah anggapan bahwa “algoritma lemah adalah satu-satunya masalah”. Dalam banyak sistem, MD5 diperparah oleh **implementasi dan konfigurasi yang buruk**, seperti penyimpanan password tanpa salt atau penggunaan hash tunggal tanpa mekanisme key stretching. Dengan demikian, kegagalan sistem bersifat sistemik: kombinasi algoritma usang dan praktik keamanan yang tidak adaptif.

---

### Langkah 3 — Rekomendasi Solusi

Solusi utama yang direkomendasikan adalah **mengganti MD5 dengan algoritma yang lebih aman dan relevan**, tergantung pada konteks penggunaannya. Untuk fungsi hash umum dan integritas data, MD5 sebaiknya digantikan dengan **SHA-256 atau SHA-3**, yang memiliki ketahanan collision dan preimage yang jauh lebih kuat. Untuk penyimpanan password, penggunaan hash kriptografis biasa tetap tidak memadai; mekanisme khusus seperti **bcrypt, scrypt, atau Argon2** jauh lebih tepat karena dirancang tahan terhadap brute force berbasis GPU dan ASIC.

Alasan pemilihan algoritma tersebut adalah kemampuannya memperlambat proses hashing secara terkontrol (adaptive cost), sehingga meningkatkan biaya serangan tanpa mengorbankan kegunaan sistem secara signifikan. Dampak jangka panjangnya adalah peningkatan ketahanan sistem terhadap serangan massal, perlindungan data pengguna, serta penurunan risiko kompromi skala besar. Argumen tandingan yang perlu dipertimbangkan adalah meningkatnya beban komputasi dan kompleksitas konfigurasi, namun dalam konteks keamanan modern, biaya ini jauh lebih kecil dibandingkan risiko kegagalan keamanan sistemik.

---

## 5. Hasil dan Pembahasan
Hasil dan pembahasan dari seluruh tahapan analisis menunjukkan bahwa serangan kriptografi pada kasus MD5 bukan sekadar konsekuensi dari praktik keamanan yang lalai, melainkan kegagalan asumsi desain algoritma dalam menghadapi realitas komputasi modern. Identifikasi serangan mengungkap bahwa MD5 rentan terhadap brute force dan collision attack yang memungkinkan penyerang merekonstruksi atau memalsukan data tanpa perlu menembus sistem secara langsung. Vektor serangan ini memanfaatkan sifat deterministik hash dan lemahnya collision resistance, sehingga integritas dan autentikasi data menjadi ilusi keamanan semu. Temuan ini menantang bias umum bahwa “hash tetap aman selama tidak dibuka isinya”, padahal nilai hash itu sendiri dapat menjadi titik eksploitasi.

Evaluasi kelemahan memperjelas bahwa sumber utama kegagalan berada pada algoritma kriptografi yang sudah usang, namun diperparah oleh implementasi dan konfigurasi sistem yang tidak defensif. MD5 secara matematis tidak lagi memenuhi standar keamanan kriptografi, sementara penggunaan tanpa salt dan tanpa mekanisme penghambat komputasi mempercepat keberhasilan serangan. Di sini terlihat efek domino: kelemahan teoritis kecil yang dibiarkan akan bereskalasi menjadi risiko sistemik ketika dioperasikan dalam lingkungan nyata. Argumen tandingan yang patut dipertimbangkan adalah bahwa algoritma kuat pun dapat gagal jika implementasinya buruk, sehingga fokus eksklusif pada penggantian algoritma tanpa perbaikan praktik operasional tetap menyisakan celah keamanan.

Rekomendasi solusi menunjukkan bahwa migrasi ke algoritma yang lebih aman seperti SHA-256 untuk integritas data dan bcrypt, scrypt, atau Argon2 untuk penyimpanan password secara signifikan meningkatkan ketahanan sistem terhadap serangan modern. Pemilihan algoritma ini didasarkan pada prinsip peningkatan biaya serangan melalui kompleksitas komputasi dan adaptivitas terhadap kemajuan perangkat keras. Dampak jangka panjangnya adalah meningkatnya kepercayaan pengguna, berkurangnya risiko kebocoran massal, serta terciptanya sistem yang lebih resilien terhadap evolusi teknik serangan. Namun, sebagai devil’s advocate, peningkatan keamanan ini datang dengan konsekuensi berupa overhead komputasi dan kompleksitas pengelolaan, yang jika tidak dirancang dengan cermat justru dapat memicu kesalahan implementasi baru. Dalam konteks ini, keamanan kriptografi terbukti bukan masalah pilihan algoritma semata, melainkan keseimbangan strategis antara teori, praktik, dan realitas operasional sistem.

---

## 6. Jawaban Pertanyaan
1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Banyak sistem lama rentan karena dirancang dengan asumsi bahwa daya komputasi penyerang terbatas dan biaya serangan sangat tinggi. Seiring waktu, asumsi ini runtuh akibat kemajuan GPU, komputasi paralel, dan ketersediaan wordlist publik. Selain itu, sistem lama sering menggunakan algoritma hash cepat tanpa salt atau mekanisme perlambatan, sehingga penyerang dapat menguji jutaan hingga miliaran kemungkinan password per detik. Kerentanan ini bertahan karena bias operasional: sistem dianggap aman selama masih berjalan, meskipun konteks ancamannya telah berubah secara fundamental.

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan algoritma bersifat inheren dan teoretis, artinya algoritma tersebut tidak lagi aman meskipun diimplementasikan dengan benar, seperti MD5 yang gagal menjamin collision resistance. Sebaliknya, kelemahan implementasi muncul ketika algoritma yang secara teori kuat diterapkan secara keliru, misalnya konfigurasi mode enkripsi yang salah, manajemen kunci yang buruk, atau penggunaan parameter keamanan yang lemah. Perbedaannya penting karena mengganti algoritma tidak akan menyelesaikan masalah jika akar kegagalan berada pada implementasi sistem.

3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Organisasi dapat menjaga keamanan jangka panjang dengan memperlakukan kriptografi sebagai proses yang adaptif, bukan keputusan satu kali. Langkah kuncinya meliputi penggunaan standar kriptografi yang terbuka dan teruji, audit keamanan berkala, kemampuan migrasi algoritma (crypto-agility), serta pemantauan aktif terhadap perkembangan kriptanalisis dan teknologi komputasi. Pendekatan ini meningkatkan ketahanan sistem terhadap ancaman baru, meskipun konsekuensinya adalah bertambahnya kompleksitas dan kebutuhan tata kelola keamanan yang lebih disiplin.

---

## 7. Kesimpulan
Kesimpulan dari analisis ini menegaskan bahwa keamanan kriptografi tidak dapat dipahami sebagai properti statis yang melekat pada algoritma tertentu, melainkan sebagai hasil dari kesesuaian antara asumsi desain, kemampuan penyerang, dan konteks operasional sistem. Kasus kerentanan pada sistem lama menunjukkan bahwa algoritma yang pernah dianggap aman dapat dengan cepat menjadi titik kegagalan ketika kemajuan komputasi dan teknik serangan menggeser batas biaya serangan. Oleh karena itu, ketergantungan pada algoritma usang dan praktik konfigurasi minimalis menciptakan ilusi keamanan yang rapuh dan berisiko sistemik.

Lebih jauh, perbedaan antara kelemahan algoritma dan kelemahan implementasi menyoroti bahwa keamanan kriptografi menuntut pendekatan holistik. Algoritma yang kuat tidak menjamin keamanan apabila diterapkan secara keliru, sementara implementasi yang rapi tidak dapat menyelamatkan algoritma yang secara teoretis telah runtuh. Kesimpulan strategisnya adalah perlunya evaluasi berkelanjutan, audit berkala, dan kemampuan adaptasi kriptografi agar sistem mampu bertahan terhadap evolusi ancaman di masa depan, meskipun dengan konsekuensi meningkatnya kompleksitas dan tuntutan tata kelola keamanan yang lebih matang.

---
