import re

def extract_emails(text):
    
    #Extrait toutes les adresses e-mail uniques présentes dans un texte.
    
    if not text:
        return []

    # Definition de la variable email pattern qui est la structure standard d'une adresse email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # On recherche tt les adresses emails dans le texte en fonction de email pattern
    emails = re.findall(email_pattern, text)

    # On sort une liste de tt les adresses emails chacuns différents c'est à dire sans doublon
    return list(set(emails))