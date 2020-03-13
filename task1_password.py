import itertools
import string
from zipfile import ZipFile

zip_object = ZipFile('lesson6.zip', 'r')


def generator(alphabet=string.ascii_lowercase):
    for pwd in itertools.product(alphabet, repeat=3):
        yield ''.join(pwd)


success = False
for password in generator():
    try:
        zip_object.extractall(pwd=password.encode('utf-8'))
        print('PASSWORD FOUND: {}'.format(password))
        success = True
        break
    except Exception:
        print('----fail---- {}'.format(password))
        continue
