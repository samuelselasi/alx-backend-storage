# 0x00. MySQL advanced
#### `Back-end` `SQL` `MySQL`
![fi_coding-013](https://github.com/samuelselasi/alx-backend-storage/assets/85158665/c5762273-0a24-4f06-b608-2f2aa79434d6)

## Resources
### Read or watch:

* [MySQL cheatsheet](https://devhints.io/mysql)
* [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
* [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
* [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
* [Views](https://www.w3resource.com/mysql/mysql-views.php)
* [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
* [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
* [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
* [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
* [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
* [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Requirements
### General
* All your files will be executed on Ubuntu `18.04` LTS using MySQL `5.7` (version `5.7.30`)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
* A `README.md` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using `wc`

## More Info

## Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Use “container-on-demand” to run MySQL
* Ask for container `Ubuntu 18.04 - Python 3.7`
* Connect via `SSH`
* Or via the `WebTerminal`
* In the container, you should start MySQL before playing with it:
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
### In the container, credentials are `root/root`

## How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks

[0. We are all unique!](./0-uniq_users.sql)

Write a SQL script that creates a table `users` following these requirements:

* With these attributes:
	* `id`, integer, never null, auto increment and primary key
	* `email`, string (255 characters), never null and unique
	* `name`, string (255 characters)
* If the table already exists, your script should not fail
* Your script can be executed on any database

**Context**: *Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application*
```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 
```

[1. In and not out](./1-country_users.sql)

Write a SQL script that creates a table `users` following these requirements:

* With these attributes:
        * `id`, integer, never null, auto increment and primary key
        * `email`, string (255 characters), never null and unique
        * `name`, string (255 characters)
	* `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
* If the table already exists, your script should not fail
* Your script can be executed on any database
```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$
```

[2. Best band ever!](./2-fans.sql)

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) `fans`

### Requirements:

* Import this table dump: [metal_bands.sql](./metal_bands.sql)
* Column names must be: `origin` and `nb_fans`
* Your script can be executed on any database

**Context**: *Calculate/compute something is always power intensive… better to distribute the load!*
```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 
```

[3. Old school band](./3-glam_rock.sql)

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their `longevity`

### Requirements:

* Import this table dump: [metal_bands.sql](./metal_bands.sql)
* Column names must be: `band_name` and `lifespan` (in years until `2022` - please use `2022` instead of `YEAR(CURDATE()`))
* You should use attributes formed and `split` for computing the `lifespan`
* Your script can be executed on any database
```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$
```
