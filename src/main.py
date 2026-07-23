import argparse
import os
from email import policy
from email.parser import BytesParser
import json
def verif_mail(file_path):
      if not os.path.exists(file_path):
         print(f"Le mail {file_path} n'existe pas")
         return
      with open(file_path,'rb') as f:
         msg =BytesParser(policy=policy.default).parse(f)
      print("=" * 60)
      print(f"FICHIER: {os.path.basename(file_path)}")
      print("=" * 60)
      print(f"De(From)             : {msg['FROM']}")
      print(f"A (To)               : {msg['to']}")
      print(f"Sujet(Subject)       : {msg['subject']}")
      print(f"Date                 : {msg['date']} ")
      print("=" * 60)
      
      corps = ""
      if msg.is_multipart():
         for partie in msg.walk():
            if partie.get_content_type() == 'text/plain':
                corps = partie.get_content()
                break 
                
      else:
        corps = msg.get_content()

      if corps:
        print("--- CORPS DU MESSAGE ---")
        print(corps.strip())
      else:
        print("[Aucun texte brut trouvé dans ce mail]")
      print(" \n") 
def verif_dossier_mail(folder_path):
      """Parcourt un dossier et analyse tous les fichiers email qu'il contient."""
      if not os.path.exists(folder_path):
         print(f"Le dossier {folder_path} n'existes pas")
         return
      files = os.listdir(folder_path)
      files_eml = [f for f in files if f.endswith('.eml')]
      if not files_eml :
         print(f"Aucun fichier mail trouver dans le dossier '{folder_path}'")
         return
         print(f"{len (files_eml)} fihiers mail trouvées dans le '{folder_path}'\n")
      for nom_files in files_eml :
         complete_path =os.path.join(folder_path,nom_files)
         try:
            verif_mail(complete_path)
         except Exception as e:
            print (f"Erreur lors de la lecture du {nom_files}: {e}\n")
if __name__ == "__main__":
      dossier_samples = "sample"
      verif_dossier_mail(dossier_samples)

