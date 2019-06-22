1. Cuál es la edad de los programadores senior en Alemania y en ?

Se considera senior un ingeniero que tenga al menos seis años de experiencia

```
db.data.aggregate([ {$match: {"experience_range" : {$in: ["6-10","10-15","15-20", "20-90"]} , 'region': 'Germany'}}, {$group: { _id: '$age_range' }}, {$out: 'q1'}])
```

To export the result

```
mongoexport --db stackoverflow --collection q1 --out q1.json
```

2. Cuáles son los 5 paises que mas tienen programadores?

```
db.data.aggregate([
    {$group: {_id: '$region', total: {$sum: 1}}},
    {$sort: {'total':-1}},
    {$limit: 6},
    {$out: 'q2'}
])
```

To export the result

```
mongoexport --db stackoverflow --collection q2 --out q2.json
```

3. Top 3 lenguajes más populares por año


4. Cuál es el sistema operativo que usan los programadores de C#?

5. Cuál es el rango de edad de los programadores junior?

```
 db.data.aggregate([ {$match: {"experience_range" : {$in: ["0-2"]} }},
                     {$group: { _id: '$age_range', total: {$sum: 1} }},
                     {$out: 'q5'} ])
```

```
mongoexport --db stackoverflow --collection q5 --out q5.json
```

6. Cuantas mujeres programan en python, javascript y sql?

Using bash:

```
mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["python", "Python"]}, 'gender': {$in: ["Female","female"]}}).count())' | xargs -o -I {} echo "{python:" {} "}" > question_answers_json/q6_python.json


mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["javascript", "Javascript"]}, 'gender': {$in: ["Female","female"]}}).count())' | xargs -o -I {} echo "{javascript:" {} "}" > q6_python.json

mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["sql", "SQL"]}, 'gender': {$in: ["Female","female"]}}).count())' | xargs -o -I {} echo "{sql:" {} "}" > q6_python.json
```

7. En que lenguajes se sienten más insatisfechos los programadores?


8. Cuál es el rango de salario por lenguaje?


9. Cuantos hombres programan en python, javascript y sql?

Using bash:

```
mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["python", "Python"]}, 'gender': {$in: ["male","Male"]}}).count())' | xargs -o -I {} echo "{python:" {} "}" > question_answers_json/q9_python.json

mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["javascript", "Javascript"]}, 'gender': {$in: ["male","Male"]}}).count())' | xargs -o -I {} echo "{javascript:" {} "}" > question_answers_json/q9_javascript.json

mongo --quiet stackoverflow --eval 'printjson(db.data.find({"programming_languages" : {$in: ["sql", "SQL"]}, 'gender': {$in: ["male","Male"]}}).count())' | xargs -o -I {} echo "{sql:" {} "}" > question_answers_json/q9_sql.json
```

10. Cuantas personas trabajaban en start up en el 2011, 2012 y 2013?

Se asume que una startup tiene menos de 25 empleados

```
mongo --quiet stackoverflow --eval 'printjson(db.survey2011.find({"company_size_range": "1-25"}).count())' | xargs -o -I {} echo "{count:" {} "}" > q10_2011.json
```

```
mongo --quiet stackoverflow --eval 'printjson(db.survey2012.find({"company_size_range": "1-25"}).count())' | xargs -o -I {} echo "{count:" {} "}" > q10_2012.json
```

```
mongo --quiet stackoverflow --eval 'printjson(db.survey2013.find({"company_size_range": "1-25"}).count())' | xargs -o -I {} echo "{count:" {} "}" > q10_2013.json
```

11. Evolucion del numero de programadores por tamaño de la compañia?

```
mongo --quiet stackoverflow --eval 'db.survey2011.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2011.json

mongo --quiet stackoverflow --eval 'db.survey2012.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2012.json

mongo --quiet stackoverflow --eval 'db.survey2013.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2013.json

mongo --quiet stackoverflow --eval 'db.survey2014.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2014.json

mongo --quiet stackoverflow --eval 'db.survey2015.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2015.json

mongo --quiet stackoverflow --eval 'db.survey2016.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2016.json

mongo --quiet stackoverflow --eval 'db.survey2017.aggregate([ {$group: {_id: "$company_size_range", total: {$sum: 1}}} ])' | xargs -o -I {} echo  {} > question_answers_json/q11_2017.json
```

12. Cual es el lenguaje que utilizan las grandes compañias?


13. Numero de programadores por lenguaje en 2017


14. En cuales se paga mejor por programar en python?

```
mongo --quiet stackoverflow --eval 'db.data.aggregate([ {$match: {'programming_languages': {$in: ['Python', 'python']}, 'salary_range': '>140k'}}, {$group: {_id: '$region'}}])' | xargs -o -I {} echo  {} > question_answers_json/q14.json
```

15. Cual es el promedio de lenguajes que los programadores han utilizado?

```
import pandas as pd
import numpy as np

df = pd.read_json('queries/clean_files/data.json')

df['programming_languages_lenght'] = df['programming_languages'].apply(lambda x: len(x) if x is not None else None)
df['programming_languages_lenght'].mean()
```
