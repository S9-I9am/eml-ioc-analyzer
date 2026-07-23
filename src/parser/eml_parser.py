from email import policy
from email.parser import BytesParser
import hashlib
import os


class EMLParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, "rb") as file:
            message = BytesParser(
                policy=policy.default
            ).parse(file)

        return {
            "subject": message.get("Subject"),
            "from": message.get("From"),
            "to": message.get("To"),
            "date": message.get("Date"),
            "body": self.extract_body(message),
            "attachments": self.extract_attachments(message)
            
        }
    def extract_body(self, message):
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_content()
        else:
            return message.get_content()
        return ""
    
     
    def extract_attachments(self, message):
        """
        Extraction des informations sur les pièces jointes
        """

        attachments = []

        if message.is_multipart():

            for part in message.walk():

                if part.get_content_disposition() == "attachment":

                    filename = part.get_filename()

                    if filename:

                        payload = part.get_payload(decode=True)

                        attachment = {
                            "filename": filename,
                            "content_type": part.get_content_type(),
                            "size": len(payload),
                            "extension": os.path.splitext(filename)[1],
                            "sha256": hashlib.sha256(payload).hexdigest()
                        }

                        attachments.append(attachment)

        return attachments
      
                            