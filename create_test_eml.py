from email.message import EmailMessage
import mimetypes


message = EmailMessage()

message["From"] = "attacker@example.com"
message["To"] = "victim@example.com"
message["Subject"] = "Test avec pièce jointe"
message["Date"] = "Mon, 20 Jul 2026 10:30:00 +0100"


message.set_content(
    """
Bonjour,

Voici le document demandé.

Cordialement
"""
)


# Création d'une fausse pièce jointe
filename = "malware.exe"

file_content = b"This is a fake malware file"


message.add_attachment(
    file_content,
    maintype="application",
    subtype="octet-stream",
    filename=filename
)


with open("test_attachment.eml", "wb") as file:
    file.write(bytes(message))


print("Fichier EML créé avec succès")