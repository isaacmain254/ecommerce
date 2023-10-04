# import celery to use it in django project
from .celery import app as celery_app

__all__ = ['celery_app']