- BODIN Virgile L3 MIAGE virgile.bodin@etu.univ-orleans.fr 
- Gomes Cardoso Rui Pedro L3 MIAGE rui-pedro.gomes-cardoso@etu.univ-orleans.fr
- AMGHAR Gassien L3 MIAGE gassien.amghar@etu.univ-orleans.fr
- Faure-Bignolas Guerric L3 MIAGE guerric.faure-bignolas@etu.univ-orleans.fr

**QUESTION 1 (BODIN VIRGILE)**
Une fois les fichier docker récupérés et placé dans le dossier, les commandes suivantes ont été utilisés :

- USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker compose up -d
 *afin d'initialiser le container*

- django-admin startproject cc .
 *afin d'initialiser le projet*

- python manage.py startapp medico
 *afin de créer l'application medico*


**QUESTION 2 (AMGHAR Gassien)**

- **Modification** du fichier settings afin lier l'application

- **Ajout** de l'url général de l'application

- **Ajout** de l'url pour la page about

- **Ajout** du dossier templates ainsi que du template about

- **Ajout** de la vue about


**QUESTION 3 (GOMES CARDOSO Rui)**

- **Création** du modèle consultation

- **Migrations** effectuées sur le modèle (*python manage.py makemigrations* , *python manage.py migrate*)

- **Test** de la creation via le shell (*python manage.py shell*)

**QUESTION 4 (FAURE-BIGNOLAS Guerric)**

- **Création** d' examples.json afin de simuler une base de données avec des consultations

- **Test** de la commande python manage.py loadata examples

**QUESTION 5 (BODIN VIRGILE)**

- **Création** de la view consultation

- **Création** du template consultation.html correspondant

- **Ajout** de l'url pour y accéder


**QUESTION 6 (AMGHAR Gassien)**

- **Création** de la vue consultations

- **Création** du template list_consultations.html pour afficher la liste des consultations

- **Ajout** de l'url lié à la page de la liste des consultations.

**QUESTION 7 (GOMES CARDOSO Rui)**

- **Créations** de la vue pour les nouvelles consulations

- **Créations* du fichier forms + **Ajout** d'un formulaire pour créer une nouvelle consultation

- **Créations** d'un template pour pouvoir afficher le formulaire

- **Ajout** de l'url pour accéder à la page du formulaire de nouvelle consultation

**QUESTION 8 (FAURE-BIGNOLAS Guerric)**

- **Créations** de la vue pour effacer une consultations

- **Créations** d'un formulaire pour effacer la consultation 

- **Ajout** d'un template page de suppression de consultation

- **Ajout** sur la liste des consultations du lien qui envoie sur la page de suppression associé à la consultation


**QUESTION 9 (AMGHAR Gassien)** :

- **Créations** de la page pour modifier les consultations

- **Ajout** de la vue pour modifier les consultations

- **Ajout** d'un template pour la modification d'une consultation

- **Ajout** d'un bouton pour modifier une consultation directement sur la page de toutes les consultations. 








