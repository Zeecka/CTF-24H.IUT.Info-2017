# Réseau 1 dorian.pcapng

Sur ce challenge, on dispose d'une trame réseau au format pcapng : [Epreuve-reseau-1-dorian.pcapng](Epreuve-reseau-1-dorian.pcapng)

On utilise l'outil Wireshark afin de lire le traffique.

[!wireshark1.png](wireshark1.png)

On observe tout au long de la trame des requetes HTTP. On va donc filtrer la trame à la recherche de requete "POST", plus probable de transporter un pot de passe qu'un GET.

[!wireshark2.png](wireshark2.png)

Bingo on retrouve le mot de passe ! 

==> attrapemoisitupeux

Afin d'aller plus loin on peut également s'amuser à extraire les fichiers capturés:

[!wireshark3.png](wireshark3.png)
