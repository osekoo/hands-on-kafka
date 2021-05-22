![image](https://user-images.githubusercontent.com/49156499/115967379-9e6fb180-a532-11eb-8142-428a455a6454.png)

# Objectifs  

Dans cette session pratique, nous allons: 
- comprendre le fonctionnement de Kafka et ses différentes terminologies
- déployer et configurer un cluster Kafka
- mettre en oeuvre une application de traitement de données en Python
- ...


# Pré-requis
_A faire avant la session pratique._

## PyCharm
[PyCharm](https://www.jetbrains.com/pycharm/download/) est un IDE permettant de développer des applications en Python.
Nous allons l'utiliser lors de cette session pratique car il intègre plusieurs outils qui facilitent et accélèrent le développement des applications.  
  
La version PyCharm Community est disponible [ici](https://www.jetbrains.com/pycharm/download/).  
Téléchargez et installez la version compatible avec votre machine.
Commande spéciale pour Ubuntu 16.04 ou plus:
```
sudo snap install pycharm-community --classic
```
Note: votre compte étudiant de Dauphine vous donne accès gratuitement à la version Ultimate. Pour cela, il suffit de vous enregistrer avec votre adresse mail de Dauphine et de valider l'inscription.

Je vous invite à prendre en main PyCharm avec ce [tutoriel](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#create-file).
  
## Docker et docker-compose
Lors de cette session nous allons exécuter et gérer le cluster Kafka en utilisant docker et docker-compose.  
Vous pouvez ignorer cette section si vous avez déjà ces deux outils installés sur votre machine.  
Le tutoriel pour installer/configurer ces deux outils sont disponibles [ici](https://github.com/osekoo/hands-on-spark-scala#pr%C3%A9requis).  

# Lab Session
Le code source de cette partie est disponible dans ce [repository](https://github.com/osekoo/hands-on-kafka). Vous pouvez le récupérer en utilisant [git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git) ou en téléchargeant l'archive.  
![image](https://user-images.githubusercontent.com/49156499/115967302-3325df80-a532-11eb-825c-58343a02118b.png)

Nous allons étudier deux cas:
- <b>get_started</b>: une application simple d'écriture et de lecture de données. Il permet de comprendre les différents mécanismes de Kafka (producers, consumers, consumer group, etc).
- <b>dico</b>: une application asynchrone de recherche de définition des mots sur internet (dictionnaire).  

## Cluster Kafka
Nous allons utiliser les images bitnami de [Kafka](https://github.com/bitnami/bitnami-docker-kafka) pour exécuter Kafka sur notre machine locale.  
Le fichier `./docker-compose.yaml` (disponible à la racine) contient le script pour lancer localement Kafka.  Il suffit d'exécuter la ligne de commande `docker-compose up` pour lancer le broker kafka.
Le fichier contient également un service nommé `kafkaui` ([kafdrop](https://github.com/obsidiandynamics/kafdrop) qui permet d'accéder au dashboard de kafka. L'accès à ce dashboard se fait via un browser à l'adresse http://localhost:8080. Nous verrons ensemble les informations disponibles sur ce dashboard.  

## Le module `get_started`
Le module `get_started` permet de publier et de lire des messages. Il contient 3 fichiers:
- `config.py`: contient les variables/constantes globales.
- `producer.py`: permet de publier une série de messages dans le bus Kafka. Dans Pycharm, cliquez sur la flèche verte à côté de la ligne `if __name__ == "__main__":` pour exécuter le producer.
- `consumer.py`: permet de lire les messages publiés par le consumer.

Après exécution de ces deux fichiers, vous pouvez analyser les informations affichées sur le [dashboard](http://localhost:8080).  

![image](https://user-images.githubusercontent.com/49156499/115967255-da564700-a531-11eb-9a5d-de7ac64d5e67.png)


## Le module `dico`
Le module `dico` permet de chercher la définition d'un mot sur Internet. Il supporte le français (lerobert.com) et l'anglais (dictionary.com). Ce module contient 5 fichiers:
- `config.py`: contient les variables globales (noms des topics, noms des dictionnaires, etc.).
- `crawler.py`: permet de chercher la définition des mots sur Internet en français (`CrawlerFR`) et en anglais (`CrawlerEN`). Cette classe extrait la définition des en parsant la source HTML du résultat de recherche. Le parsing peut parfois échoué si la structure HTML de la page change.
- `worker.py`: contient une class (`Worker`) qui permet de lire les requêtes de recherche postées dans le bus Kafka (en mode `consumer`), effectue la recherche en utilisant le crawler (`data processing`) et republie le résultat dans Kafka (en mode `producer`). Il faut cliquer sur la flèche verte à côté de `if __name__ == "__main__":` pour exécuter le worker. Vous devez spécifier la langue de recherche (`fr` pour français ou `en` pour anglais) à l'invite commande.
- `client.py`: publie dans Kafka la requête de recherche de définition (en mode `producer`) et lit au retour la réponse (en mode `consumer`). Il faut cliquer sur la flèche verte à côté de `if __name__ == "__main__":` pour exécuter le client. Vous devez spécifier votre pseudonyme (utilisé pour créer le topic qui servira à lire les réponses) et la langue de recherche (`fr` pour français ou `en` pour anglais).
- `kafka_data.py`: implémente les structures de données (`KafkaRequest`, `KafkaResponse`) échanger entre les clients et les workers à travers Kafka.

![image](https://user-images.githubusercontent.com/49156499/115967493-2f468d00-a533-11eb-86c4-fa82c7ec9f3d.png)


## Pour aller plus loin
_à faire chez vous_  

Implémentez une application de data pipeline ayant les fonctionnalités suivantes:
- un utilisateur envoie sur un topic Kafka une URL d'un site Internet contenant du texte,
- un premier groupe de consumers lit l'URL, récupère le contenu de l'URL et réalise un WordCount sur ce contenu. Il publie ensuite le résultat de wordCount (liste de mots et leur occurrence) dans Kafka,
- un deuxième groupe de consumers lit le résultat de wordCount et cherche la définition de chaque mot. Il renvoie ensuite au client la liste des mots avec leur occurrence et leur définition.
- l'utilisateur lit ce résultat et... l'enregistre dans une base de données!
- Vous pouvez rajoutez d'autres langues (espagnol, allemand, chinois, etc.)

L'application doit supporter au moins deux langues.

Quelles sont les applications possibles d'un tel programme?

![image](https://user-images.githubusercontent.com/49156499/119236141-1af7af00-bb36-11eb-9a5e-66f34806108f.png)
