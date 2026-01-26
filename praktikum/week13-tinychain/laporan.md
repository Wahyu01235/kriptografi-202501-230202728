# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: TinyChain – Proof of Work (PoW)
Nama: Achmad Wahyudi 
NIM: 230202728 
Kelas: 5IKRA 

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
TinyChain dengan mekanisme Proof of Work (PoW) berangkat dari prinsip paling fundamental dalam sistem terdistribusi: bagaimana mencapai konsensus tanpa otoritas pusat di lingkungan yang bersifat trustless. Secara teoretis, PoW memanfaatkan kerja komputasi sebagai “biaya objektif” untuk mengusulkan blok baru, sehingga kejujuran menjadi strategi rasional karena setiap upaya manipulasi menuntut sumber daya nyata. TinyChain mengadopsi konsep ini dalam skala minimalis, meniru arsitektur blockchain klasik tetapi disederhanakan untuk tujuan edukasi, eksperimen, atau sistem berdaya terbatas, tanpa menghilangkan esensi kriptografi dan konsensus terdistribusi.

Secara mekanistik, PoW pada TinyChain bekerja dengan memaksa miner mencari nilai nonce yang menghasilkan hash blok di bawah tingkat kesulitan tertentu. Proses ini secara inheren bersifat probabilistik dan computationally expensive, namun mudah diverifikasi oleh node lain. Di sinilah kekuatan desain PoW muncul: asimetri antara biaya pembuatan dan biaya verifikasi. TinyChain memanfaatkan sifat ini untuk memastikan integritas rantai blok, di mana setiap blok terikat secara kriptografis dengan blok sebelumnya, sehingga perubahan satu blok akan merusak seluruh struktur hash berikutnya.

Dari perspektif keamanan, PoW pada TinyChain memberikan resistansi terhadap serangan seperti double spending dan manipulasi riwayat transaksi, selama mayoritas kekuatan komputasi berada pada node jujur. Namun, pendekatan ini membawa konsekuensi yang tidak dapat diabaikan: konsumsi energi dan latensi konfirmasi yang meningkat seiring kesulitan. TinyChain, dengan ruang lingkupnya yang kecil, secara implisit menantang asumsi bahwa PoW hanya relevan pada jaringan besar, dengan menunjukkan bahwa konsep yang sama dapat diadaptasi secara ringan untuk simulasi atau private chain.

Sebagai kerangka teoritis, TinyChain–PoW bukanlah solusi optimal untuk semua skenario, melainkan artefak konseptual untuk memahami trade-off inti blockchain: keamanan versus efisiensi. Pendekatan ini menegaskan bahwa PoW bukan sekadar algoritma, tetapi mekanisme insentif dan pertahanan sistemik yang mengandalkan hukum fisika—bukan kepercayaan—sebagai fondasi konsensus. Di titik ini, TinyChain berfungsi sebagai laboratorium intelektual yang mereduksi kompleksitas dunia nyata tanpa mengorbankan logika dasar yang membentuk teknologi blockchain modern.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
### Langkah 1 — Membuat Struktur Blok
```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
```

---

### Langkah 2 — Membuat Blockchain
```python
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```

---

### Langkah 3 — Analisis Proof of Work
- Perhatikan bahwa proses mining membutuhkan waktu (bergantung pada `difficulty`).  
- Analisis: semakin tinggi difficulty, semakin lama proses mining.  
- Diskusikan bagaimana hal ini menjamin keamanan blockchain.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp if timestamp else time.time()
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "nonce": self.nonce
        }

        block_string = json.dumps(block_content, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()

        print(f"Block #{self.index} successfully mined")
        print(f"Hash       : {self.hash}")
        print(f"Nonce      : {self.nonce}")
        print(f"Time Taken : {end_time - start_time:.4f} seconds\n")

class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()

        new_block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            data=data
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Hash integrity check
            if current.hash != current.calculate_hash():
                print(f"Invalid hash at block {current.index}")
                return False

            # Chain linkage check
            if current.previous_hash != previous.hash:
                print(f"Invalid chain link at block {current.index}")
                return False

        return True

    def tamper_block(self, index, new_data):
        if index <= 0 or index >= len(self.chain):
            return

        print(f"\nTampering block #{index}...\n")
        self.chain[index].data = new_data
        self.chain[index].hash = self.chain[index].calculate_hash()

# ===============================
# TEST TINYCHAIN
# ===============================

my_chain = Blockchain(difficulty=4)

print("Mining block 1...")
my_chain.add_block("A → B : 10 Coin")

print("Mining block 2...")
my_chain.add_block("B → C : 5 Coin")

print("Mining block 3...")
my_chain.add_block("C → D : 2 Coin")

print("Blockchain valid?")
print(my_chain.is_chain_valid())

# ===============================
# ATTACK SCENARIO
# ===============================

my_chain.tamper_block(1, "A → B : 1000 Coin")

print("Blockchain valid after attack?")
print(my_chain.is_chain_valid())
# ===============================
```

---

## 6. Hasil dan Pembahasan
Hasil implementasi TinyChain dengan mekanisme Proof of Work (PoW) menunjukkan bahwa setiap penambahan blok ke dalam blockchain membutuhkan proses komputasi yang tidak sepele, yang direpresentasikan melalui pencarian nilai nonce hingga hash blok memenuhi tingkat kesulitan yang ditentukan. Pada tahap pengujian, waktu penambangan meningkat seiring bertambahnya nilai difficulty, menegaskan bahwa PoW secara efektif memperkenalkan biaya nyata dalam proses pembuatan blok. Rantai blok yang dihasilkan bersifat deterministik dan dapat diverifikasi ulang, ditunjukkan oleh keberhasilan fungsi validasi dalam memastikan keterkaitan hash antarblok tanpa adanya manipulasi data.

Pembahasan lebih lanjut memperlihatkan bahwa kekuatan utama PoW dalam TinyChain bukan terletak pada kompleksitas algoritma hashing, melainkan pada asimetri antara biaya pembuatan dan biaya verifikasi blok. Node yang jujur hanya memerlukan waktu singkat untuk memverifikasi keabsahan rantai, sementara pihak yang mencoba memodifikasi satu blok harus menambang ulang seluruh blok setelahnya. Simulasi serangan dengan mengubah data pada salah satu blok secara langsung menyebabkan kegagalan validasi rantai, yang membuktikan bahwa integritas historis blockchain dijaga oleh ketergantungan kriptografis dan kerja komputasi kumulatif.

Namun demikian, hasil ini juga mengungkap keterbatasan inheren PoW. Meskipun efektif dalam menjamin keamanan dan imutabilitas, mekanisme ini menunjukkan inefisiensi dari sisi waktu dan energi, terutama ketika diterapkan pada skala yang lebih besar. Dalam konteks TinyChain, keterbatasan ini justru memperjelas tujuan sistem sebagai model konseptual dan alat pembelajaran. Dengan demikian, implementasi ini berhasil menegaskan prinsip dasar PoW sebagai mekanisme konsensus berbasis biaya fisik, sekaligus membuka ruang diskusi kritis mengenai trade-off antara keamanan, efisiensi, dan skalabilitas dalam desain sistem blockchain.

---

## 7. Jawaban Pertanyaan
1. Mengapa fungsi hash sangat penting dalam blockchain?

Fungsi hash merupakan komponen fundamental dalam blockchain karena berperan sebagai mekanisme pengikat data yang menjamin integritas dan imutabilitas sistem. Setiap blok menghasilkan nilai hash unik yang merepresentasikan seluruh isi blok tersebut, termasuk data transaksi, timestamp, nonce, dan hash blok sebelumnya. Sifat deterministik dan sensitif terhadap perubahan kecil (avalanche effect) membuat fungsi hash mampu mendeteksi manipulasi data secara instan: perubahan satu bit saja pada data akan menghasilkan hash yang sepenuhnya berbeda. Dengan demikian, hash berfungsi sebagai “sidik jari digital” yang memungkinkan node memverifikasi keaslian dan konsistensi blockchain tanpa perlu mempercayai pihak lain.

Lebih jauh, keterkaitan hash antarblok menciptakan struktur rantai yang saling bergantung secara kriptografis. Hal ini menyebabkan upaya pemalsuan satu blok tidak hanya memerlukan perubahan pada blok tersebut, tetapi juga penyesuaian seluruh blok setelahnya. Dari sudut pandang sistem terdistribusi, fungsi hash menggeser kepercayaan dari institusi atau otoritas pusat ke mekanisme matematis yang objektif dan dapat diverifikasi oleh siapa pun.

2. Bagaimana Proof of Work mencegah double spending?

Proof of Work (PoW) mencegah double spending dengan memaksa seluruh transaksi untuk tunduk pada satu riwayat bersama yang mahal untuk dimanipulasi. Dalam PoW, transaksi dianggap sah ketika telah dimasukkan ke dalam blok yang berhasil ditambang dan diterima oleh mayoritas node. Untuk melakukan double spending, penyerang harus membuat versi alternatif dari blockchain yang menghapus atau mengganti transaksi sebelumnya, lalu menambang ulang blok-blok tersebut hingga rantai palsu tersebut menjadi lebih panjang atau lebih “berat” daripada rantai asli.

Hambatan utama bagi penyerang terletak pada biaya komputasi. Selama mayoritas kekuatan hash berada pada node jujur, peluang penyerang untuk mengejar dan melampaui rantai valid sangat kecil. Dengan kata lain, PoW tidak membuat kecurangan menjadi mustahil, tetapi membuatnya secara ekonomi tidak rasional. Mekanisme ini menempatkan hukum probabilitas dan biaya fisik sebagai penjaga utama konsistensi transaksi, sehingga double spending dapat dicegah tanpa pengawas terpusat.

3. Apa kelemahan dari PoW dalam hal efisiensi energi?

Kelemahan utama Proof of Work dalam hal efisiensi energi terletak pada sifat kompetitif dan redundan dari proses mining. Banyak node melakukan perhitungan hash yang sama secara paralel, namun hanya satu yang akhirnya menghasilkan blok yang valid. Sebagian besar energi yang dikonsumsi dalam proses ini tidak berkontribusi langsung pada peningkatan utilitas sistem, melainkan terbuang sebagai konsekuensi dari mekanisme kompetisi tersebut. Pada skala jaringan besar, hal ini berujung pada konsumsi energi yang sangat tinggi.

Selain itu, PoW cenderung mendorong sentralisasi sumber daya karena penambangan menjadi lebih efisien jika dilakukan dengan perangkat keras khusus dan akses energi murah. Kondisi ini bertentangan dengan ideal desentralisasi yang menjadi fondasi blockchain. Oleh karena itu, meskipun PoW unggul dalam hal keamanan dan kesederhanaan konsep, kelemahan efisiensi energi menjadi alasan utama munculnya alternatif konsensus lain seperti Proof of Stake, yang berupaya mempertahankan keamanan tanpa biaya komputasi yang berlebihan.

---

## 8. Kesimpulan
Kesimpulan dari praktikum TinyChain dengan mekanisme Proof of Work menunjukkan bahwa prinsip dasar blockchain dapat direpresentasikan secara jelas melalui implementasi sederhana. Pembentukan blok, perhitungan hash, dan proses mining membuktikan bahwa integritas data dijaga oleh keterkaitan kriptografis antarblok serta biaya komputasi yang harus dikeluarkan untuk menambahkan data baru, sehingga kepercayaan tidak bergantung pada otoritas pusat, melainkan pada aturan matematis yang dapat diverifikasi.

Praktikum ini juga menegaskan peran Proof of Work dalam mencegah manipulasi dan double spending. Perubahan data pada satu blok menyebabkan kegagalan validasi seluruh rantai, menunjukkan bahwa pemalsuan riwayat transaksi bersifat mahal dan mudah terdeteksi. Dengan demikian, keamanan PoW bersumber dari tingginya biaya serangan, bukan dari ketidakmungkinan teknis.

Di sisi lain, hasil praktikum mengungkap keterbatasan PoW dalam efisiensi waktu dan energi, karena peningkatan tingkat kesulitan berbanding lurus dengan konsumsi sumber daya tanpa peningkatan manfaat fungsional. Oleh karena itu, Proof of Work efektif sebagai mekanisme konsensus yang aman dan kuat secara konseptual, namun kurang efisien untuk skala besar, sementara TinyChain berfungsi optimal sebagai media pembelajaran untuk memahami trade-off fundamental dalam sistem blockchain.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
