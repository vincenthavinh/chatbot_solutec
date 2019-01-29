# PISTL 2018 : Chatbot Q&A SOLUTEC

### Dossiers de ce repo:

- **data/**, constitué de :
  + .json contenant les logs des conversations des utilisateurs.
  + .json contenant des sauvegardes de la logique de l'IA du Chatbot.
  + un dossier solutec.fr qui est une extraction des informations des pages du site solutec.fr.
  
- **resources/**, un dossier utile au fonctionnement des scripts python du dossier WIP_clean_data. Il contient :
  + le driver 'geckodriver' pour l'utilisation du framefork de test automatique web 'selenium".
  + des fichiers stopwords.txt et verbsToKeep.txt 

- **secret/**, un dossier pour stocker les informations à ne pas versionner, comme les clefs d'api. Lire le README.md se situant dedans pour plus d'informations.

- **src/**, qui contient :
  + export_chatbot_logic.py, script qui récupère la version la plus récente de la logique de notre IA sur les serveurs IBM et la stocke en .json dans notre dossier data/chatbot/.
  + export_users_conversations_log.py, script qui récupère les 1000 derniers messages utilisateurs sur les serveurs IBM et les stocke en .json dans le dossier data/chatbot/.
  + WIP_clean_data, un dossier contenant des scripts pour cibler les données utiles à partir d'un texte.\
  **Les scripts de ce dossier ne sont pas finis. C'est un Work-In-Progress**.


### Fichiers dans ce repo:

- ce **README.md**

- **.gitignore** pour ne pas versionner les fichiers temporaires et de cache.

- **requirements.txt**, indiquant les dépendances nécessaires au fonctionnement des scripts python de ce projet.
  + Pour mettre à jour requirements.txt durant le projet :\
Depuis l'IDE PyCharm, sélectionner le projet, ouvrir la fenêtre Terminal, et entrer la commande "pip freeze > requirements.txt"