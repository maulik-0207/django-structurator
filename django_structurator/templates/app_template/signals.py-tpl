"""
---> Model Signals <---
    
    Args:
        sender (Model): The model class.
        instance (Model instance): The instance being saved.
        created (in post_save only)(bool): True if a new instance was created, False if updated.
        kwargs: Additional keyword arguments.
    
@receiver(pre_save, sender = MyModel) #or pre_delete, post_delete 
def pre_save_handler(sender, instance, **kwargs):
    pass


@receiver(post_save, sender = MyModel)
def post_save_handler(sender, instance, created, **kwargs):
    pass
"""
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
)
from django.dispatch import receiver
from .models import *
# Create your Signals here.

