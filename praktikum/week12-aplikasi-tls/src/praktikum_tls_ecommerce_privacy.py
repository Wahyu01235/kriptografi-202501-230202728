# =========================================================
# PRAKTIKUM KEAMANAN JARINGAN
# LANGKAH 1–3: TLS, E-COMMERCE, ETIKA & PRIVASI
# DENGAN ANALISIS OTOMATIS (100% STANDARD LIBRARY)
# =========================================================

import ssl
import socket
import os
import urllib.request
import urllib.parse
import base64
import hashlib
from datetime import datetime

# =========================================================
# LANGKAH 1: ANALISIS SSL/TLS WEBSITE E-COMMERCE
# =========================================================

def analyze_tls_certificate(hostname, port=443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            tls_version = ssock.version()

    issuer = dict(x[0] for x in cert["issuer"])

    valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z")
    valid_until = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")

    return {
        "Website": hostname,
        "Issuer CA": issuer.get("organizationName", "Unknown"),
        "Valid From": valid_from.strftime("%Y-%m-%d"),
        "Valid Until": valid_until.strftime("%Y-%m-%d"),
        "TLS Version": tls_version,
        "Cipher Suite": cipher[0],
        "Encryption": cipher[1],
        "Key Length": cipher[2]
    }

# =========================================================
# LANGKAH 2: STUDI KASUS E-COMMERCE (HTTP vs HTTPS)
# =========================================================

def send_post(url, data):
    encoded = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=encoded)
    with urllib.request.urlopen(req) as response:
        return response.read().decode()

def ecommerce_transaction_simulation():
    data = {
        "username": "user_demo",
        "password": "password123",
        "card_number": "4111111111111111",
        "amount": "150000"
    }

    https_url = "https://httpbin.org/post"
    http_url = "http://httpbin.org/post"

    https_result = send_post(https_url, data)
    http_result = send_post(http_url, data)

    analysis = [
        "Data transaksi yang dikirim melalui HTTPS dienkripsi selama proses transmisi menggunakan TLS.",
        "Pada HTTP, data dikirim dalam bentuk plaintext sehingga dapat disadap oleh pihak ketiga.",
        "TLS melindungi kerahasiaan (confidentiality) dan integritas data transaksi.",
        "Tanpa TLS, sistem rentan terhadap serangan Man-in-the-Middle (MITM), credential theft, dan session hijacking.",
        "Penggunaan TLS meningkatkan kepercayaan pengguna terhadap platform e-commerce."
    ]

    return https_result, http_result, analysis

# =========================================================
# LANGKAH 3: ANALISIS ETIKA & PRIVASI (EMAIL TERENKRIPSI)
# =========================================================

def encrypted_email_simulation():
    message = "Email internal perusahaan bersifat rahasia"

    encoded = base64.b64encode(message.encode()).decode()
    decoded = base64.b64decode(encoded.encode()).decode()
    integrity_hash = hashlib.sha256(message.encode()).hexdigest()

    analysis_points = [
        "Email terenkripsi bertujuan melindungi kerahasiaan isi pesan dari pihak yang tidak berwenang.",
        "Hanya pihak yang memiliki mekanisme dekripsi yang sesuai yang dapat membaca isi email.",
        "Dalam konteks organisasi, enkripsi email dapat menghambat proses audit dan investigasi internal.",
        "Dekripsi email karyawan oleh perusahaan menimbulkan dilema antara keamanan organisasi dan privasi individu.",
        "Kebijakan pemerintah terkait pengawasan komunikasi terenkripsi harus menyeimbangkan keamanan nasional dan hak privasi warga.",
        "Pelemahan sistem enkripsi berisiko menciptakan kerentanan sistemik yang dapat disalahgunakan."
    ]

    return message, encoded, decoded, integrity_hash, analysis_points

# =========================================================
# EXPORT HASIL + ANALISIS KE FILE HTML
# =========================================================

def export_to_html(tls_results, ecommerce_data, email_data):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "laporan_praktikum_tls.html")

    https_data, http_data, ecommerce_analysis = ecommerce_data
    msg, enc, dec, hash_val, email_analysis = email_data

    html = f"""
    <html>
    <head>
        <title>Laporan Praktikum TLS & E-Commerce</title>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
            th {{ background-color: #f0f0f0; }}
            ul {{ margin-top: 10px; }}
            pre {{ background: #fafafa; padding: 10px; overflow-x: auto; }}
        </style>
    </head>
    <body>

    <h1>Laporan Praktikum Keamanan Jaringan</h1>

    <h2>Langkah 1 — Analisis SSL/TLS</h2>
    <table>
        <tr>
            <th>Website</th><th>Issuer CA</th><th>Valid From</th><th>Valid Until</th>
            <th>TLS Version</th><th>Cipher Suite</th><th>Encryption</th><th>Key Length</th>
        </tr>
    """

    for r in tls_results:
        html += f"""
        <tr>
            <td>{r['Website']}</td>
            <td>{r['Issuer CA']}</td>
            <td>{r['Valid From']}</td>
            <td>{r['Valid Until']}</td>
            <td>{r['TLS Version']}</td>
            <td>{r['Cipher Suite']}</td>
            <td>{r['Encryption']}</td>
            <td>{r['Key Length']}</td>
        </tr>
        """

    html += f"""
    </table>

    <h2>Langkah 2 — Studi Kasus E-Commerce</h2>
    <p><b>HTTPS (dengan TLS):</b></p>
    <pre>{https_data}</pre>

    <p><b>HTTP (tanpa TLS):</b></p>
    <pre>{http_data}</pre>

    <h3>Analisis Langkah 2</h3>
    <ul>
    {''.join(f"<li>{point}</li>" for point in ecommerce_analysis)}
    </ul>

    <h2>Langkah 3 — Analisis Etika & Privasi</h2>
    <p><b>Pesan Asli:</b> {msg}</p>
    <p><b>Pesan Terenkripsi (simulasi):</b> {enc}</p>
    <p><b>Pesan Terdekripsi:</b> {dec}</p>
    <p><b>Hash Integritas (SHA-256):</b> {hash_val}</p>

    <h3>Analisis Langkah 3</h3>
    <ul>
    {''.join(f"<li>{point}</li>" for point in email_analysis)}
    </ul>

    </body>
    </html>
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("\nLaporan berhasil dibuat:")
    print(file_path)

# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":
    websites = [
        "www.tokopedia.com",
        "www.shopee.co.id",
        "www.bukalapak.com"
    ]

    tls_results = [analyze_tls_certificate(w) for w in websites]
    ecommerce_data = ecommerce_transaction_simulation()
    email_data = encrypted_email_simulation()

    export_to_html(tls_results, ecommerce_data, email_data)
