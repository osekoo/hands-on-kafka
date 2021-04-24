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
Le code source de cette partie est disponible dans ce repository. Vous pouvez le récupérer en utilisant [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git) ou en téléchargeant l'archive.  
Nous allons étudier deux cas:
- <b>get_started</b>: une application simple d'écriture et de lecture de données. Il permet de comprendre les différents mécanismes de Kafka (producers, consumers, consumer group, etc).
- <b>dico</b>: une application plus ou moins évoluée qui implémente la recherche de définition des mots sur internet (dictionaire). L'application support le Français et l'Anglais.

## Cluster Kafka
Nous allons utiliser les images bitnami de Kafka pour exécuter Kafka sur notre machine locale.  
Le fichier `./docker-compose.yaml` contient le script pour lancer localement Kafka.  Il suffit d'exécuter la ligne de commande `docker-compose up` pour lancer le broker kafka.
Le fichier contient également un service nomé `kafkaui` qui permet d'accéder au dashboard de kafka. L'accès à ce dashboard se fait via un browser à l'adresse http://localhost:8080. Nous verrons ensemble les informations disponibles sur ce dashboard.  

## Le programme `get_started`
Le module `get_started` permet publier et lire des messages. Il contient 3 fichiers:
- `config.py`: contient les variables/constantes globales.
- `producer.py`: permet de publier une série de messages dans le bus Kafka. Dans Pycharm, cliquez sur la flèche verte à côté de la ligne `if __name__ == "__main__":` pour exécuter le producer.
- `consumer.py`: permet de lire les messages publiés par le consumer.

Après exécution de ces deux fichiers, vous pouvez analyser les informations affichées sur le dashboard.  

## Le programme `dico`
Le module `dico` permet de chercher la définition des mots sur Internet. Il support le Français (le Robert) et l'Anglais (dictionary.com). Ce module contient 5 fichiers:
- `config.py`: contient les variables globales.
- `crawler.py`: permet de chercher la définition des mots sur Internet en Français (`CrawlerFR`) et en Anglais (`CrawlerEN`).
- `worker.py`: lit les requêtes de recherche postées dans le bus Kafka (consumer), effectue la recherche en utilisant le crawler (processor) et republie le résultat dans Kafka (producer). Il faut cliquer sur la flêche verte à côté de `if __name__ == "__main__":` pour exécuter le worker. Vous devez spécifier la langue de recherche (`fr` pour Français ou `en` pour Anglais).
- `client.py`: publie dans Kafka la requête de recherche de définition (producer) et lit au retour la réponse (consumer). Il faut cliquer sur la flêche verte à côté de `if __name__ == "__main__":` pour exécuter le client. Vous devez spécifier votre pseudonyme (utilisé pour créer le topic qui servira à lire les réponses) et la langue de recherche (`fr` pour Français ou `en` pour Anglais).
- `kafka_data.py`: implémente les structures de données échanger entre les clients et les workers à travers Kafka.




