import uuid
from django.db import models


"""This file will prove basic django abstract model templates to alleviate duplicating the development efforts. 
Abstract models do not create tables in the databse.See https://docs.djangoproject.com/en/3.1/topics/db/models/#abstract-base-classes for more info.
Templates will be created based on the models purpose and audience (end-user,system level).
Good pratice is to create UUID in every model."""


class StandardModel(models.Model):

    """created_date: generates the date a record was created.
    last_modified: updates whenever a record is modified."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
