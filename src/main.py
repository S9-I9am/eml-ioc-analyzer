import os

# On importe directement le parser existant
from parser.eml_parser import EMLParser
from ioc.extractor import IOCExtractor


def verif_mail(file_path):
    """
    Analyse un fichier .eml :
    - Parsing du mail
    - Extraction des IOC
    - Affichage des résultats
    """

    try:

        # -------------------------
        # Parsing du fichier EML
        # -------------------------

        parser = EMLParser(file_path)
        data = parser.parse()


        # -------------------------
        # Extraction des IOC
        # -------------------------

        extractor = IOCExtractor(data)
        results = extractor.extract_all()



        # -------------------------
        # Informations du mail
        # -------------------------

        print("=" * 60)
        print(f"FICHIER         : {os.path.basename(file_path)}")
        print("=" * 60)

        print(f"De (From)       : {data.get('from')}")
        print(f"A (To)          : {data.get('to')}")
        print(f"Sujet           : {data.get('subject')}")
        print(f"Date            : {data.get('date')}")

        print("=" * 60)



        # -------------------------
        # Corps du message
        # -------------------------

        print("\n--- CORPS DU MESSAGE ---")

        print(
            data.get("body")
            or "[Aucun texte trouvé]"
        )



        # -------------------------
        # Pièces jointes
        # -------------------------

        if data.get("attachments"):

            print("\n--- PIECES JOINTES ---")

            for attachment in data["attachments"]:

                print(
                    f"- {attachment['filename']} "
                    f"({attachment['size']} octets)"
                )



        # -------------------------
        # IOC détectés
        # -------------------------

        print("\n" + "=" * 60)
        print("IOC EXTRAITS")
        print("=" * 60)



        print("\n[URLS]")

        for url in results["urls"]:
            print(f"- {url}")



        print("\n[ADRESSES IP]")

        for ip in results["ips"]:
            print(f"- {ip}")



        print("\n[DOMAINES]")

        for domain in results["domains"]:
            print(f"- {domain}")



        print("\n[EMAILS]")

        for email in results["emails"]:
            print(f"- {email}")



        print("\n[HASHES]")

        for hash_data in results["hashes"]:

            print(
                f"- Fichier : {hash_data['filename']}"
            )

            print(
                f"  MD5     : {hash_data['md5']}"
            )

            print(
                f"  SHA1    : {hash_data['sha1']}"
            )

            print(
                f"  SHA256  : {hash_data['sha256']}"
            )


        print("\n")



    except Exception as error:

        print(
            f"Erreur lors de l'analyse de {file_path} : {error}"
        )



def verif_dossier_mail(folder_path):
    """
    Analyse tous les fichiers .eml présents dans un dossier.
    """

    if not os.path.exists(folder_path):

        print(
            f"Le dossier '{folder_path}' n'existe pas."
        )

        return



    files_eml = [
        file
        for file in os.listdir(folder_path)
        if file.endswith(".eml")
    ]



    if not files_eml:

        print(
            f"Aucun fichier .eml trouvé dans '{folder_path}'"
        )

        return



    print(
        f"{len(files_eml)} fichier(s) trouvé(s)\n"
    )



    for file in files_eml:

        file_path = os.path.join(
            folder_path,
            file
        )

        verif_mail(file_path)



if __name__ == "__main__":

    dossier_samples = "samples"

    verif_dossier_mail(dossier_samples)