#!/usr/bin/env python3.6

from user import User, Credentials


def create_newUser(userName, password):
    '''
    function to create a new user
    '''
    new_user = User(userName, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()


def display_user():
    '''
    Function to display existing user
    '''
    return User.display_user()

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generate_password()
    return auto_password

def create_credential(account, userName, email, password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credentials(account, userName, email, password)
    return new_credential

def save_credential(credential):
    """
    Function to save Credentials to the credential_list
    """
    credential. save_credential()

def delete_credential(credential):
    """
    Function to delete a Credentials from credentials list

    """
    credential.delete_credential()


def credential_exists(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.credential_exists(account)


def password_locker():
    print("Hello there, Welcome to Password Locker.\n \n please enter any of this shotcodes to navigate: \n ca ---  Create New Account  \n ha ---  Already Have An Account  \n")
    short_code=input("").strip()
    
    
    if short_code == "ca":
        print("sign up")
        print("*" *60)
        userName = input("User name: ")
        




if __name__ == '__main__':

    password_locker()
