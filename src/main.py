import argparse
import os

# On importe directement le parser existant
from EMLParser import EMLParser


def verif_mail(file_path):
    #Utilise le emlParser pour extraire et afficher les données.
    try:
        # le parser fait tout le travail ici 
        parser = EMLParser(file_path)
        data = parser.parse()

        print("=" * 60)
        print(f"FICHIER         : {os.path.basename(file_path)}")
        print("=" * 60)
        print(f"De (From)       : {data.get('from')}")
        print(f"À (To)          : {data.get('to')}")
        print(f"Sujet (Subject) : {data.get('subject')}")
        print(f"Date            : {data.get('date')}")
        print("=" * 60)

        print("--- CORPS DU MESSAGE ---")
        print(data.get("body") or "[Aucun texte brut trouvé]")

        if data.get("attachments"):
            print("\n--- PIÈCES JOINTES ---")
            for att in data["attachments"]:
                print(
                    f"- {att['filename']} ({att['size']} octets) | SHA256: {att['sha256'][:10]}..."
                )
        print("\n")

    except Exception as e:
        print(f"Erreur lors de la lecture de {file_path} : {e}\n")


def verif_dossier_mail(folder_path):
    #Parcourt un dossier et passe chaque fichier .eml au parser.
    if not os.path.exists(folder_path):
        print(f"Le dossier '{folder_path}' n'existe pas.")
        return

    files_eml = [f for f in os.listdir(folder_path) if f.endswith(".eml")]

    if not files_eml:
        print(f"Aucun fichier .eml trouvé dans '{folder_path}'")
        return

    print(f"{len(files_eml)} fichier(s) mail trouvé(s) dans '{folder_path}'\n")

    for nom_file in files_eml:
        complete_path = os.path.join(folder_path, nom_file)
        verif_mail(complete_path)


if __name__ == "__main__":
    parser_cli = argparse.ArgumentParser(
        description="Analyseur de fichiers .eml"
    )
    parser_cli.add_argument(
        "chemin",
        nargs="?",
        default="sample",
        help="Chemin vers un fichier .eml ou un dossier (par défaut: 'sample')",
    )
    args = parser_cli.parse_args()

    if os.path.isfile(args.chemin):
        verif_mail(args.chemin)
    elif os.path.isdir(args.chemin):
        verif_dossier_mail(args.chemin)
    else:
        print(f"Chemin invalide : '{args.chemin}'")