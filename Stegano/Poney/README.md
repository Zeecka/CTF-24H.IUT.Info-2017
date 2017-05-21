# Poney

L'épreuve proposait l'image d'un magnifique poney :

![poney](poney.jpg)

Pour commencer l'épreuve on fait un "file" de l'image pour vérifier de quel type il s'agit.

![Poney1](Poney1.png)

On utilise l'outil "binwalk" pour vérifier si'il existe des fichiers cachés dans l'image. L'option -e permet d'extraire ces fichiers.

![Poney2](Poney2.png)

Enfin on liste les fichier présents. Il y a un fichier "flag" et une archive qui contient elle aussi ce même fichier flag. On change l'extention du fichier flag en flag.pdf et on l'ouvre ! 

![Poney3](Poney3.png)

==> zolipon3y!yaf0undMeh
