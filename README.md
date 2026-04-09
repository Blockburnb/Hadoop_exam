# Examen Hadoop MapReduce

**Lien GitHub :** https://github.com/Blockburnb/Hadoop_exam

### Démarche suivie
1.  **Préparation des données** : Chargement du fichier local `ml-25m/tags.csv` sur HDFS pour permettre le traitement distribué.
2.  **Développement des scripts** : Écriture de scripts Python utilisant la bibliothèque `mrjob`. Conformément aux consignes, chaque mapper inclut un bloc `try...except` pour ignorer les lignes mal formées.
3.  **Analyse HDFS** : Utilisation de la commande `fsck` pour comparer l'impact des tailles de blocs sur le stockage du fichier.
4.  **Exécution MapReduce** : Lancement des jobs sur le cluster Hadoop avec l'option `-o` pour forcer l'écriture des résultats sur HDFS et éviter la saturation du terminal.

### Commandes utilisées
```bash
# Chargement du fichier sur HDFS
hdfs dfs -put ml-25m/tags.csv /user/maria_dev/tags_default.csv

# Vérification des blocs (Q3)
hdfs fsck /user/maria_dev/tags_default.csv -files -blocks

# Exécution des jobs (Exemple pour Q1, répétée pour Q2, Q4, Q5)
python q1_tags_per_movie.py -r hadoop \
--hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
hdfs:///user/maria_dev/tags_default.csv \
-o /user/maria_dev/reponse_q1

# Récupération des résultats en local
hdfs dfs -get /user/maria_dev/reponse_q1/part-00000 resultat_q1.txt
```

### Résultats obtenus

**Q1. Combien de tags chaque film possède-t-il ?**
*(45 251 films traités au total)*
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

**Q2. Combien de tags chaque utilisateur a-t-il ajoutés ?**
*(14 592 utilisateurs traités au total)*
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

**Q3. Combien de blocs le fichier occupe-t-il dans HDFS ?**
Le fichier `tags.csv` pèse 38,8 Mo.
- **Config par défaut (128 Mo) :** 1 bloc.
- **Config 64 Mo :** 1 bloc.
*Explication : Le fichier étant plus petit que 64 Mo, il n'est jamais fractionné.*

**Q4. Combien de fois chaque tag a-t-il été utilisé ?**
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

**Q5. Pour chaque film, combien de tags le même utilisateur a-t-il introduits ?**
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
