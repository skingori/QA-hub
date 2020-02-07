===================
QA TOOL
===================

Quick Start
-----------
1. Switch to postgres user
    ``` python
    sudo su postgres
    ```
2. Enter the the interactive terminal for working with Postgres
    ``` sql
    psql
    ```
3. Create the database (change database_name)
    ``` sql
    CREATE DATABASE database_name;
    ```
4. Create user (change my_username and my_password)
    ``` sql
    CREATE USER my_username WITH PASSWORD 'my_password';
    ```
5. Grant privileges on database to user
    ``` sql
    GRANT ALL PRIVILEGES ON DATABASE "database_name" to my_username;
    ```

**Migrate data from SQLite to PostgreSQL**

* Dump existing data:
    ``` python
    python3 manage.py dumpdata > datadump.json
    ```
* Make sure you can connect on PostgreSQL. Then:
    ``` python
    python3 manage.py migrate --run-syncdb
    ```
* Run this on Django shell to exclude contentype data

    ``` python
    python3 manage.py shell
    ```

    ``` python
    >>>from django.contrib.contenttypes.models import ContentType
    >>>ContentType.objects.all().delete()
    >>>quit()
    ```

* Finally, run following command to load the json data:
    ``` python
    python3 manage.py loaddata datadump.json
    ```
**Django - Caching**
* Setting up the cache

    ``` python
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
        }
    }
    ```

* Creating the cache table
    > Before using the database cache, you must create the cache table with this command:

    ``` python
    python manage.py createcachetable
    ```