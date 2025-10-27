import re

from django.core.exceptions import ValidationError

def validate_phone_number(phone: str):
    if not re.match(r'^010[0-9]{8}$', phone):
        return ValidationError(
            ' (ex.01011112222)',
            params={'phone': phone},
        )
    if '-' in phone:
        return ValidationError(
            ''
        )
    return None

def validate_password(password: str):
    if not re.match(r'^.{8,}$', password):
        return ValidationError('비밀번호는 8자 이상 입력해주세요.')

    return None
