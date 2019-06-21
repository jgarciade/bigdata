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
 db.data.aggregate([ {$match: {"experience_range" : {$in: ["0-2"]} }}, {$group: { _id: '$age_range' }} ])
```
6. Cuantas mujeres programan en python?

```
db.data.find({"programming_languages" : {$in: ["python", "Python"]}, 'gender': {$in: ['Female', 'female']}}).count()
```

7. En que lenguajes se sienten más insatisfechos los programadores?


8. Cuál es el rango de salario por lenguaje?


9. Diferencia de salario entre hombres y mujeres


10. Cuantas personas trabajaban en start up en 2017?

Se asume que una startup tiene menos de 25 empleados

```
db.survey2017.find({'company_size_range': '1-25'}).count()
```

11. Evolucion del numero de programadores por tamaño de la compañia?

```
var s11 = db.survey2011.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s12 = db.survey2012.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s13 = db.survey2013.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s14 = db.survey2014.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s15 = db.survey2015.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s16 = db.survey2016.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
var s17 = db.survey2017.aggregate([ {$group: {_id: '$company_size_range', total: {$sum: 1}}} ])
```

12. Cual es el lenguaje que utilizan las grandes compañias?
13. Numero de programadores por lenguaje en 2017
14. En que pais se paga mejor por programar en python?

```
db.data.aggregate([ {$match: {'programming_languages': {$in: ['Python', 'python']}, 'salary_range': '>140k'}}, {$group: {_id: '$region'}}])
```

15. Cual es el promedio de lenguajes que los programadores han utilizado?

```
import pandas as pd
import numpy as np

df = pd.read_json('queries/clean_files/data.json')

df['programming_languages_lenght'] = df['programming_languages'].apply(lambda x: len(x) if x is not None else None)
df['programming_languages_lenght'].mean()
```
