from django.core.exceptions import ValidationError


def validate_users_mail(value):
    if '@' in value:
        return value
    else:
        raise ValidationError('Please provide a valid email')