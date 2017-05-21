# 5 inscriptions en 10 secondes

5 incription en 10 secondes, avec un "captcha" ? C'est qu'indique la page "Aide" du challenge.

Le site proposait en effet un formulaire d'inscription avec à remplir:
* Un Nom
* Un Prénom
* Un EMail
* Un "Captcha"

Le formulaire contient également un champ caché : formulaire=1

Il faut donc réaliser une série de 5 inscriptions sur ce formulaire, tout en prenant soin de bien compléter le captcha.

Ce captcha nous demandait de rentrer le nombre de lignes verticales et horizontales présentes sur l'image.
Le nombre de lignes horizontales / verticales variait entre 1 et 10 pour chaque axe ce qui générait des captcha de cette forme :

[Captcha](captcha.png)

Le captcha ci dessu demandait donc à l'utilisateur de rentrer la valeur 75 puisqu'il y a 7 lignes verticales et 5 horizontales.


Pour réaliser cet exploit, j'ai donc développé un script python 3 qui va inscrir à notre place 5 personnes, et résoudre le captcha à chaque fois ! 


La résolution du captcha utilise le plugin "PIL" (comme indiqué dans l'aide du site il me semble). Celle ci va compter le nombre de pixels noir sur la première lignes puis la première colone.

Voici le script utilisé pour résoudre l'épreuve :

[SolveInscriptionCaptcha.py]("SolveInscriptionCaptcha.py")

Je n'ai malheureusement plu le flag en tête mais l'execution du script renvoyait un phrase avec le flag ;) .
