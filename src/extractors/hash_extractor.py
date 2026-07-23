
import hashlib #Importation du module standard de Python dédiée aux hachages

class HashExtractor:
    def __init__(self, attachments):
        self.attachments = attachments
        
    def extract_hashes(self):
        hashes = []
        for attachment in self.attachments:
            content = attachment.get("content")
            
            if content:
                hashes.append({
                    "filename": attachment["filename"],
                    "md5": hashlib.md5(content).hexdigest(),
                    "sha1": hashlib.sha1(content).hexdigest(),
                    "sha256": hashlib.sha256(content).hexdigest()
                })  
        return hashes           