import getpass
import sys

from ..models.base import Base, get_session, get_engine
from ..modules.misc import get_input


def initialize(salt):
    """
        Vault setup
    """

    print('Welcome to Vault. Please choose a secure secret key.')
    print()

    while True:
        if get_key_input():
            # Create db
            create_db()

            print()
            print("Your vault has been created and encrypted with your master key.")
            print("Your unique salt is: %s " % (salt))
            print(
                "Write it down. If you lose your config file you will need it to unlock your vault.")

            return True


def create_db():
    """
        Create db
    """

    session = get_session()
    Base.metadata.create_all(get_engine())
    session.commit()

    return True


def get_key_input():
    """
        Prompt user for a master key
    """

    key = get_input(message='Please choose a master key:', secure=True)
    repeat = get_input(message='Please confirm your master key:', secure=True)

    # Ensure that the key was correctly typed twice and is valid
    if check_key_and_repeat(key, repeat) and is_key_valid(key):
        return True

    return False


def is_key_valid(key):
    """
        Return True if a key is valid
    """

    if len(key) < 8:
        print()
        print('The master key should be at least 8 characters. Please try again!')
        print()

        return False

    return True


def check_key_and_repeat(key, repeat):
    """
        Ensure that the key was correctly typed twice
    """

    if key != repeat:
        print()
        print('The master key does not match its confirmation. Please try again!')
        print()

        return False

    return True
