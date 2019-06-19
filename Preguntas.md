1. Cuál es la edad de los programadores senior en Alemania?

Se considera senior un ingeniero que tenga al menos seis años de experiencia

```
db.data.aggregate([ {$match: {"experience_range" : {$in: ["6-10","10-15","15-20", "20-90"]} , 'region': 'Germany'}}, {$group: { _id: '$age_range' }} ])
```

2. Cuáles son los 5 paises que mas tienen programadores?

```
db.data.aggregate([
    {$group: {_id: '$region', total: {$sum: 1}}},
    {$sort: {'total':-1}},
    {$limit: 6}
])
```

3. Top 3 lenguajes más populares por año


4. Cuál es el sistema operativo que usan los programadores de C#?

5. Cuál es el rango de edad de los programadores junior?

```
 db.data.aggregate([ {$match: {"experience_range" : {$in: ["0-2"]} }}, {$group: { _id: '$age_range' }} ])
```
6. Cuantas mujeres programan en python?
7. En que lenguajes se sienten más insatisfechos los programadores?
8. Cuál es el rango de salario por lenguaje?
9. Diferencia de salario entre hombres y mujeres
10. Cuantas personas trabajaban en start up en 2017?
11. Evolucion del numero de programadores por tamaño de la compañia?
12. Cual es el lenguaje que utilizan las grandes compañias?
13. Numero de programadores por lenguaje en 2017
14. En que pais se paga mejor por programar en python?
15. Cual es el promedio de lenguajes que los programadores han utilizado?
