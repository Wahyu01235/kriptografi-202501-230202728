from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta, timezone

# GENERATE PRIVATE KEY (CA)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# IDENTITAS SERTIFIKAT
# (Self-Signed Certificate)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, "UPB Root CA"),
])

# MEMBANGUN SERTIFIKAT DIGITAL
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
    .add_extension(
        x509.BasicConstraints(ca=True, path_length=None),
        critical=True
    )
    .sign(private_key, hashes.SHA256())
)

# SIMPAN PRIVATE KEY
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# SIMPAN SERTIFIKAT
with open("certificate.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

print("Self-signed certificate berhasil dibuat.")
print("File tersimpan: private_key.pem dan certificate.pem")
