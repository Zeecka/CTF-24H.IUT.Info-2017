Pour ce Challenge on disposait de l'archive [JeudeCesar.zip](JeudeCesar.zip)

Celle-ci contient un fichier "Passphrase.txt" et une autre archive "[Ladies.zip](Ladies.zip)"

Le fichier txt contient la chaine :
"KT SGXZOTOWAK OR E G RK YURKOR, RKY VRGMKY, RKY LORRKY, R'GRIUUR... KZ RK SUZ JK VGYYK JK R'GXINOBK WAO KYZ RKYLKSSKYKTHOQOTOEGXOKTJKVRAYHKGA G XKIXEVZKX KT IUJK JK IKYGX GBKI IUSSK IRK S"

L'archive [Ladies.zip](Ladies.zip) quand à elle est protégée par un mot de passe.

On effectue un [Chiffre de Cesar](http://www.dcode.fr/chiffre-cesar) avec une attaque par bruteforce sur le fichier text afin de le décoder : la solution s'avère être un décalage de +6

"EN MARTINIQUE IL Y A LE SOLEIL, LES PLAGES, LES FILLES, L'ALCOOL... ET LE MOT DE PASSE DE L'ARCHIVE QUI EST LESFEMMESENBIKINIYARIENDEPLUSBEAU A RECRYPTER EN CODE DE CESAR AVEC COMME CLE M"

La lettre A correspondant à un décalage de 0, B => 1, C=>2, un décalage de M correpond à un décalage de +12

"LESFEMMESENBIKINIYARIENDEPLUSBEAU" (+)12 ==> "XQERQYYQEQZNUWUZUKMDUQZPQBXGENQMG"

On a donc récupéré le flag avec 2 chiffres de césar !

L'archive quand à elle contient un lien vers la vidéo : [https://www.youtube.com/watch?v=BoAba8Rl0M0](https://www.youtube.com/watch?v=BoAba8Rl0M0)
