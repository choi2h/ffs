class AuthenticationException(Exception):
    message = "토큰이 유효하지 않습니다."

class NotAuthorizedException(Exception):
    message = "검증되지 않은 사용자입니다."

class UserNotFoundException(Exception):
    message = "사용자 정보를 찾을 수 없습니다."

class InvalidLoginException(Exception):
    message = "아이디 혹은 비밀번호가 올바르지 않습니다."