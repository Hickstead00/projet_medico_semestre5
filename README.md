- BODIN Virgile L3 MIAGE virgile.bodin@etu.univ-orleans.fr 
- Gomes Cardoso Rui Pedro L3 MIAGE rui-pedro.gomes-cardoso@etu.univ-orleans.fr
- AMGHAR Gassien L3 MIAGE gassien.amghar@etu.univ-orleans.fr
- Faure-Bignolas Guerric L3 MIAGE guerric.faure-bignolas@etu.univ-orleans.fr

**QUESTION 1 (BODIN VIRGILE)**
Une fois les fichier docker récupérés et placé dans le dossier, les commandes suivantes ont été utilisés :

USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker compose up -d
*afin d'initialiser le container*

django-admin startproject cc .
*afin d'initialiser le projet*

python manage.py startapp medico
*afin de créer l'application medico*


