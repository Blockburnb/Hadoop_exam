# Examen Hadoop MapReduce

**Lien GitHub :** https://github.com/Blockburnb/Hadoop_exam

### Q1. Combien de tags chaque film possède-t-il ?
Il y a **45 251 films** recensés avec leurs nombres de tags respectifs dans le fichier `resultat_q1.txt`.
```text
"1"     697
"10"    137
"100"   18
"1000"  10
"100001"        1
```

### Q2. Combien de tags chaque utilisateur a-t-il ajoutés ?
Le fichier `resultat_q2.txt` dénombre **14 592 utilisateurs** ayant contribué.
```text
"100001"        9
"100016"        50
"100028"        4
"100029"        1
"100033"        1
```

### Q3. Combien de blocs le fichier occupe-t-il dans HDFS ?
- **Configuration 128 Mo :** 1 bloc.
- **Configuration 64 Mo :** 1 bloc.
Le fichier `tags.csv` (38.8 Mo) est inférieur aux deux seuils de taille de bloc, il n'est donc pas fractionné.

### Q4. Combien de fois chaque tag a-t-il été utilisé ?
Les occurrences globales par tag sont disponibles dans `resultat_q4.txt`.
```text
" Alexander Skarsg\u00e5rd"     1
" Difficult to find it" 1
" Filmes Antigos "      2
" Filmes Antigos"       2
" Kartik Aaryan"        1
```

### Q5. Pour chaque film, combien de tags le même utilisateur a-t-il introduits ?
Le fichier `resultat_q5.txt` contient les comptes par couple (FilmID, UserID).
```text
"1,100538"      4
"1,10231"       2
"1,102568"      4
"1,102901"      1
"1,103368"      1
```
