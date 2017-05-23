# seekanddestroy.deb 

Pour ce challenge, une archive debian (.deb) nous était fournis : [seekanddestroy.deb](seekanddestroy.deb)

## Solution 1 

ouvrir avec le gestionnaire d'archive et naviguez vers usr/share/man/fr/man1/seekanddestroy.1 

![deb1.png](deb1.png)

Ensuite il suffit de l'ouvrir et le flag apparait à la fin

![deb2.png](deb2.png)

## Solution 2 

Utiliser binwalk et lire le contenu des fichiers présents:

![dpkg1.png](dpkg1.png)

![dpkg2.png](dpkg2.png)

==> thx2RTFM
