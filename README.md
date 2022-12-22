# IMDBpractice
A great way to practice some more with a database schema you have not encountered yet.

## Setup
You can either use the database in this repo, or set up an environment to create a database yourself.
This can be done by: 
### Scraping the web
1. Install a version of python3.8.x+ 
2. Install the following libraries {SSL,urllib.request,bs4}
3. run the main file (You can alter the number of pages visited, thus make the number of entries in the database less. Note: It is not adviced to increase the number of pages.) 

```console
python3 main.py
```
### Use a csv file
You can also use the CSVtoSQL file for a CSV file and a schema of your choice.
1. Install a version of python3.8.x+ 
2. Install the following libraries {pandas}
3. Find a csv file of your choice
4. run the CSVtoSQLfile 
```console
python3 CSVtoSQL.py --input <CSV-file> --table table1 table2 table3
```
A new .sql file will be made, called table.sql

## Using the .sql file 
To use the sql file in sqlite3. 
1. Open duckdb/sqlite
2. Enter the command:
```console
  .read <file.sql>
  ```
 3. To check whether it worked, enter the following command:
 ```console
  .tables
  ``` 
  If you see the table names, you can start practicing.
  
  ## HAVE FUN :) 
  From your TA, Kevin
