import uuid
from django.db import models
from natic_templates.model_templates import StandardModel


# Create your models here.
class Customer(StandardModel):

    """A customer represents a single user in the natic core. This model inherits from the
    natic template StandardModel"""

    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    name = models.CharField(blank=True, null=True, max_length=255)

    @property
    def full_name(self):
        "Returns the customers's full name."
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):

        """Save method. Checks if there is a first and last name. Implying the customer
        is a person."""

        if self.first_name and self.last_name:
            self.name = self.full_name

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "customer"
