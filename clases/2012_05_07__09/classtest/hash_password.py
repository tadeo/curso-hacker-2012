'''
Created on Aug 31, 2010

@author: tadeo
'''
import sys, os, getpass

SITE_ROOT = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.insert(0, SITE_ROOT)
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

def hash_password(raw_password):
    import random
    from django.contrib.auth.models import get_hexdigest
    algo = 'sha1'
    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
    hsh = get_hexdigest(algo, salt, raw_password)
    return '%s$%s$%s' % (algo, salt, hsh)

if __name__ == '__main__':
    password = getpass.getpass('Password to hash: ')
    while password != getpass.getpass('Confirm password to hash: '):
        print 'Password doesn\'t match, try again.'
    print 'The hashed password is: ' + hash_password(password)