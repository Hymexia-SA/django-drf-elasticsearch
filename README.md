# Django DRF Elasticsearch

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-drf-elasticsearch/).

## Want to use this project?

1. update git submodule

    ```sh
    git submodule udate
    ```

2. Install Elasticsearch

    ```sh
    cd ELK-Docker-compose && docker-compose up -d
    cd ..
    ```

3. Create and activate a virtual environment:

    ```sh
    $ python3 -m poetry shell
    ```

4. Install the requirements:

    ```sh
    poetry install
    ```

5. Apply the migrations:

    ```sh
    python manage.py migrate
    ```

6. Populate the database with some test data by running the following command:

    ```sh
    python manage.py populate_db
    ```

7. Create and populate the Elasticsearch index and mapping:

    ```sh
    python manage.py search_index --rebuild
    ```

8. Create the first super user

    ```sh
    python manage.py createsuperuser
    ```

8. Run the server

    ```sh
    python manage.py runserver
    ```

9. Test Elasticsearch with the following queries:

     - [http://127.0.0.1:8000/search/user/mike/](http://127.0.0.1:8000/search/user/mike/) - should find the user 'mike13'
     - [http://127.0.0.1:8000/search/user/jess_/](http://127.0.0.1:8000/search/user/jess_/) - should find the user 'jess_'
     - [http://127.0.0.1:8000/search/category/seo/](http://127.0.0.1:8000/search/category/seo/) - should find the category 'SEO optimization'
     - [http://127.0.0.1:8000/search/category/progreming/](http://127.0.0.1:8000/search/category/progreming/) - should find the category 'Programming' (:warning: notice the typo)
     - [http://127.0.0.1:8000/search/article/linux/](http://127.0.0.1:8000/search/article/linux/) - should find the article 'Installing the latest version of Ubuntu'
     - [http://127.0.0.1:8000/search/article/java/](http://127.0.0.1:8000/search/article/java/) - should find the article 'Which programming language is the best?'
