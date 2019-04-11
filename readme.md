# Configurations

Defining Development and Production classes

Note: **os.getenv()** calls Environment Variables. Environment Variables allow us to hide secret stuff on our machines, and use them in our code. This is useful when we want to store a secret key or even to an online account. Environment variables allow us to plug variables on our machines and be accessed late on.

```python
class Development(object):
    '''
    Development Environment config
    '''
    DEBUG = True
    TESTING = True
    JWT_SECRET_KEY =os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
```

```bash
export FLASK_ENV=development  
export JWT_SECRET_KEY=thisIsYourSecretKey
export DATABASE_URL=postgres://{username}:{password}@localhost/flask_blog
# IE: postgres://postgres:@localhost/flask_blog
```