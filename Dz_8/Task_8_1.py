import re

RE_EMAIL = re.compile(r'(?P<username>[a-zA-Z0-9.-]{1,30})@(?P<domain>[a-z.]{2,255})')


def email_parse(email_address):
    if RE_EMAIL.match(email_address):
        print(RE_EMAIL.match(email_address).groupdict())
    else:
        raise ValueError(f'wrong email: {email_address}')


if __name__ == "__main__":
    try:
        email_parse(input("Введите адрес электронной почты: "))
    except ValueError as error:
        print(error)
