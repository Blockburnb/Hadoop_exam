# Examen Hadoop MapReduce - Dataset MovieLens 25M

**Lien GitHub :** https://github.com/Blockburnb/Hadoop_exam  
**Environnement :** Sandbox Hortonworks HDP 2.6.5  
**Outil :** Python 2.7 avec la bibliothèque `mrjob`

---

## Question 1 : Nombre de tags par film
**Objectif :** Calculer combien de tags chaque film a reçu au total.

### Aperçu des résultats :
```text
"1"     697
"10"    137
"100"   18
"1000"  10
"100001"        1
"100003"        3
"100008"        9
"100017"        9
"100032"        2
"100034"        19
```

---

## Question 2 : Nombre de tags par utilisateur
**Objectif :** Calculer le nombre total de tags introduits par chaque utilisateur.

### Aperçu des résultats :
```text
"100001"        9
"100016"        50
"100028"        4
"100029"        1
"100033"        1
"100046"        133
"100051"        19
"100058"        5
"100065"        2
"100068"        19
```

---

## Question 3 : Analyse des Blocs HDFS
**Commande :** `hdfs fsck /user/maria_dev/tags_default.csv -files -blocks`

### Résultats techniques :
- **Taille du fichier :** 38 810 332 octets (~37 Mo)
- **Nombre de blocs :** 1 block(s)
- **Status :** HEALTHY

### Analyse :
Le fichier `tags.csv` a une taille réelle de 38.8 Mo. Dans HDFS, la taille de bloc par défaut est de 128 Mo. Comme la taille du fichier est inférieure à ce seuil (ainsi qu'au seuil de 64 Mo testé durant le TP), le système de fichiers n'a pas besoin de le fragmenter. Le fichier est donc stocké dans **un seul bloc**.

---

## Question 4 : Occurrences de chaque Tag
**Objectif :** Identifier combien de fois chaque tag spécifique a été utilisé globalement.

### Aperçu des résultats :
```text
" Alexander Skarsg\u00e5rd"     1
" Difficult to find it" 1
" Filmes Antigos "      2
" Filmes Antigos"       2
" Kartik Aaryan"        1
" Kriti Sanon"  1
" Laurel Canyon"        1
" Luis Brandoni"        1
" Masami Nagasawa"      1
" O'Shea Jackson Jr."   1
```

---

## Question 5 : Tags par couple (Film, Utilisateur)
**Objectif :** Pour chaque film, déterminer combien de tags un utilisateur spécifique a ajouté.

### Aperçu des résultats (Format: "MovieID,UserID" Count) :
```text
"1,100538"      4
"1,10231"       2
"1,102568"      4
"1,102901"      1
"1,103368"      1
"1,103371"      1
"1,103883"      3
"1,104394"      9
"1,1048"        1
"1,105717"      1
```

---

## Commandes d'exécution
Tous les scripts ont été lancés avec la syntaxe suivante :
```bash
python script.py -r hadoop \
--hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
hdfs:///user/maria_dev/tags_default.csv \
-o /user/maria_dev/reponse_qx
```
