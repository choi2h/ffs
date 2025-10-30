import re
import logging

from django.core.exceptions import ValidationError

logger = logging.getLogger('django.server')

def validate_phone_number(phone: str):
    logger.debug('Validate phone number. phone={}'.format(phone))
    if not re.match(r'^010[0-9]{8}$', phone):
        raise ValidationError(
            message='전화번호 형식이 올바르지 않습니다. (ex.01011112222)',
            params={'phone': phone},
        )
    if '-' in phone:
        raise ValidationError(
            ''
        )
    return None

def validate_password(password: str):
    if not re.match(r'^.{8,}$', password):
        raise ValidationError('비밀번호는 8자 이상 입력해주세요.')

    return None

def validate_email(email: str):
    if not re.match(
        r'^[a-zA-Z0–9][a-zA-Z0–9._]+[@][a-zA-Z][A-Za-z.]+[.]\w{2,\}', email):
        raise ValidationError('이메일 형식이 올바르지 않습니다.')

    return None