from email import policy
from email.parser import BytesParser


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
            "body": self.extract_body(message)
            
        }
    def extract_body(self, message):
        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
        else:
            return message.get_content()
        return None        
                    