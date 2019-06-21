#!/usr/bin/bash

mongoimport --db stackoverflow --collection survey2011 --file ../queries/clean_files/2011.json --jsonArray
mongoimport --db stackoverflow --collection survey2012 --file ../queries/clean_files/2012.json --jsonArray
mongoimport --db stackoverflow --collection survey2013 --file ../queries/clean_files/2013.json --jsonArray
mongoimport --db stackoverflow --collection survey2014 --file ../queries/clean_files/2014.json --jsonArray
mongoimport --db stackoverflow --collection survey2015 --file ../queries/clean_files/2015.json --jsonArray
mongoimport --db stackoverflow --collection survey2016 --file ../queries/clean_files/2016.json --jsonArray
mongoimport --db stackoverflow --collection survey2017 --file ../queries/clean_files/2017.json --jsonArray
mongoimport --db stackoverflow --collection data --file ../queries/clean_files/data.json --jsonArray
