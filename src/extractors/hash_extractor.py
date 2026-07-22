
import hashlib #Importation du module standard de Python dédiée aux hachages

def calculate_hashes(file_bytes):#Declaration de la foncion qui récupere le fichier btutes en entrée
    
   # Calcule les empreintes MD5, SHA-1 et SHA-256 à partir des octets bruts d'un fichier/pièce jointe.
    
    if not file_bytes:#Au cas ou la pièce jointes n'as pas pu etre lu ou il est vide.
        return {
            "md5": None,
            "sha1": None,
            "sha256": None
        }#Il retourne none ce qui évite l'exécution du reste du code.

    # Calcul des hashs sur le contenu binaire.Il prend le contenu brut du fichier et applique les algorithmes de chaque hachages disponible dans la biblio et le transforme en signature binaire ensuite hexddigest le transforme en chaine hexadécimale  
    md5_hash = hashlib.md5(file_bytes).hexdigest()
    sha1_hash = hashlib.sha1(file_bytes).hexdigest()
    sha256_hash = hashlib.sha256(file_bytes).hexdigest()

    return {#Il renvoie les trois empreintes dans un dictionnaire intégrée.
        "md5": md5_hash,
        "sha1": sha1_hash,
        "sha256": sha256_hash
    }