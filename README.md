# AVL

My implementation of an AVL tree in python.

About AVL : https://en.wikipedia.org/wiki/AVL_tree

#Output

```
| Test de rotation droite |
===========================

Avant :
-------

   |-->F
-->D
   |   |-->C
   |-->B
   |   |-->A

Apres :
-------

   |   |-->F
   |-->D
   |   |-->C
-->B
   |-->A

| Test de rotation gauche |
===========================

Avant :
-------

   |   |-->F
   |-->D
   |   |-->C
-->B
   |-->A

Apres :
-------

   |-->F
-->D
   |   |-->C
   |-->B
   |   |-->A

| Test de rotation gauche droite |
==================================

Avant :
-------

   |-->G
-->F
   |   |   |-->E
   |   |-->D
   |   |   |-->C
   |-->B
   |   |-->A

Apres :
-------

   |   |-->G
   |-->F
   |   |-->E
-->D
   |   |-->C
   |-->B
   |   |-->A

| Test de rotation droite gauche |
==================================

Avant :
-------

   |   |-->G
   |-->F
   |   |   |-->E
   |   |-->D
   |   |   |-->C
-->B
   |-->A

Apres :
-------

   |   |-->G
   |-->F
   |   |-->E
-->D
   |   |-->C
   |-->B
   |   |-->A

| Test d'insertion |
====================
   |   |   |   |-->Z
   |   |   |-->Y
   |   |-->X
   |   |   |   |-->W
   |   |   |-->V
   |   |   |   |-->U
   |-->T
   |   |   |-->S
   |   |-->R
   |   |   |-->Q
-->P
   |   |   |   |-->O
   |   |   |-->N
   |   |   |   |-->M
   |   |-->L
   |   |   |   |-->K
   |   |   |-->J
   |   |   |   |-->I
   |-->H
   |   |   |   |-->G
   |   |   |-->F
   |   |   |   |-->E
   |   |-->D
   |   |   |   |-->C
   |   |   |-->B
   |   |   |   |-->A
```
