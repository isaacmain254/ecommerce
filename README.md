ECOMMERCE 
----------

To run the project locally: clone this repository on your computer

```
    cd  #to your preferred directory
    git clone https://github.com/isaacmain254/ecommerce
    cd ecommerce
```

create a virtual environment and install all packages from **requirements.txt**.

 Make sure you are in the `$ ... ecommerce ` directory

```python
    #create a virtual environment
    python -m venv venv

    #Activate the virtual environment, for Linux users
    # For Windows users search on how to activate a virtual environment
    source venv/bin/activate

    pip install -r requirements.txt
```

Next makemigrations

```python
    #makemigrations
    python manage.py makemigrations

    #migrate
    python manage.py migrate

    #create a super user
    python manage.py createsuperuser
    
    #start the development server
    python manage.py runserver
```
Install RabbitMQ, you can use docker or install it natively on your machine, then start the RabbitMQ server.

Open another shell and start the Celery worker from your project directory with the following command:

```
    celery -A myshop worker -l info
```
Create a stripe account. After successful registration add an account name to process payments. To add stripe to your project, add the following settings to the settings.py file of your project:

```
    # Stripe settings
    STRIPE_PUBLISHABLE_KEY = '' # Publishable key
    STRIPE_SECRET_KEY = ''  # Secret key
    STRIPE_API_VERSION = '2022-08-01'
```

 Replace the **STRIPE_PUBLISHABLE_KEY** and **STRIPE_SECRET_KEY** values with the test Publishable key and the Secret key provided by Stripe

Open an additional shell and execute the following command to forward Stripe events to your local webhook URL:

```
    stripe listen --forward-to localhost:8000/payment/webhook/
```

Now create a superuser for your site using the following command:
```python
    python manage.py createsuperuser
```

Open http://127.0.0.1:8000/admin/ in your browser to add a new category and product using the administration interface.

Run the development server with the following command and open http://127.0.0.1:8000/ in your browser.
```
python manage.py runserver
```
