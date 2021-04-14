# Objectifs  

Dans cette session pratique, nous allons: 
- comprendre le fonctionnement de Kafka et ses différentes terminologies
- déployer un cluster Kafka
- metre en oeuvre une application Python de traitement de données en mode streaming
- écrire et lire des donnnées
- ...


# Pré-requis
_A faire avant la session pratique._

## PyCharm
[PyCharm](https://www.jetbrains.com/pycharm/download/) est un IDE permettant de développer des applications en Python.
Nous allons l'utiliser lors de cette session pratique car il intègre plusieurs outils qui facilitent et accélèrent le développement des applications Python.  
  
La version PyCharm Community est disponible [ici](https://www.jetbrains.com/pycharm/download/).  
Téléchargez et installez la version compatible avec votre machine.
Commande spéciale pour Ubuntu 16.04 ou plus:
```
sudo snap install pycharm-community --classic
```
Note: votre compte étudiant de Dauphine vous donne accès gratuitement à la version Ultimate. Pour cela, il suffit de vous enregistrer avec votre adresse mail de Dauphine et de valider l'inscription.

Je vous invite à prendre en main PyCharm avec cet excelent [tutorial](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#create-file)
  
## Docker et docker-compose
Lors de cette session nous allons lancer et gérer le cluster Kafka via docker et docker-compose.  
Vous pouvez ignorer cette section si vous avez déjà ces deux outils installés sur votre machine.  
Le tutorial pour installer/configurer ces deux outils sont disponibles [ici](https://github.com/osekoo/hands-on-spark-scala#pr%C3%A9requis).  

# Lab Session
## Cluster Kafka
Nous allons utiliser les images bitnami de Kafka pour exécuter Kafka sur notre machine locale.  
Le fichier [docker-compose.yaml]() contient le script pour lancer localement Kafka.  
