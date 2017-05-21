# CaptureHTTP

Le challenge proposait un fichier txt: [CaptureHTTP.txt](CaptureHTTP.txt)

Après ouverture sous notepad++, le fichier montrait l'enregistrement d'un trafic web.
(Le fichier comprenait des retours à la ligne non pris en compte sous blocnote)

La méthode utilisée lors de l'évènement consistait à chercher une trame "POST" généralement utilisé pour cacher un mot de passe lors de la soumission d'un formulaire.

On pouvait donc clairement identifier la trame :

> POST /stats/ HTTP/1.1<br>
> Host: litle.jimdo.com<br>
> User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0<br>
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8<br>
> Accept-Language: en-US,en;q=0.5<br>
> Accept-Encoding: gzip, deflate<br>
> Referer: http://litle.jimdo.com/protected/?comeFrom=http%3A%2F%2Flitle.jimdo.com%2Fstats%2F&<br>
> Cookie: PHPSESSID=f09f0b0e2a14f37339c9fb57dfdbe2fe; gads=ID=e733be4c78b5bec0:T=1395916271:S=ALNI_MbeNOeJztRkL-WRywwcG97J4blB8g; servicewb[91914]=1395919546<br>
> Connection: keep-alive<br>
> Content-Type: application/x-www-form-urlencoded<br>
> Content-Length: 58<br>
> P@ssWord=PasdemeufaMaubeuge&do_L0gin=yes&Submit=Connexion+<br>

Ici la dernière ligne nous interessait puisqu'il s'agit des informations transmises en POST.

On peut ainsi clairement identifier le pass qui s'est avéré être le flag : PasdemeufaMaubeuge
