import os
from django.core.exceptions import ValidationError

def valid_file(value):
    valid_extensions = ['.png', '.jpeg', '.jpg']
    extension = os.path.splitext(value.name)[1]

    if  not extension.lower() in valid_extensions:
        raise ValidationError('The file must be a valid image with one of the following extensions:'+str(valid_extensions))
