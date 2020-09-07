#!/usr/bin/env python3.6

"""
user can:
- Add credentials account
- Delete credentials Account,
- view all credentials account
- view specific credentials account
- login
- logout
- register
- Generate password and sepcify password length- 
"""
from user import User, Credentials

user =User('userName','password')
cr = Credentials('account','userName','email','password')
def create_newUser(userName, password):
    '''
    function to create a new user
    '''
    new_user = User(userName, password)
    return new_user

def login_user(first_name, password):
    '''
    Function that verifies if user exists.
    '''
    enter_user = user.login(first_name, password)
    return enter_user

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

def add_account():
   account = input()
   password = input()
   username = input()
   email = input ()
   Credentials('account','userName','email', 'password').save_credential(account,username,email,password)

def password_locker():
    print("Hello there, Welcome to Password Locker.\n \n please enter any of this shotcodes to navigate: \n ca ---  Create New Account  \n ha ---  Already Have An Account  \n")
    short_code=input("").strip()
    
    
    if short_code == "ca":
        print("sign up")
        print("*" *60)
        userName = input("User name: ")
        password = None
        while True:
            print("tp - To type your own pasword:\n gp - To generate random Password")
            password_Choice = input().strip()

            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break

            elif password_Choice == 'gp':
                password = generate_Password()
                break
 
            else:
                print("Invalid password please try again")
                break
        user.save_user(userName,password)
        print("*"*70)
        print(f"Hello {userName}, Your account has been created succesfully! Your password is: {password}")
        print("*"*70)


    elif short_code == 'ha':
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)

        userName = input("userName: ")
        password = input("password: ")
        login = user.login(userName,password)

        if login:
            print(f"Hello {userName}.Welcome To PassWord Locker Manager")  
            print('\n')
        else:
            print("Error")

    while True:
        print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n gp - Generate A randomn password \n d - Delete credential \n ex - Exit the application \n")
        short_code = input().strip()

        if short_code == "cc":
            print("Create New Credential")
            print("."*30)
            print("Account name ....")
            account = input()
            print("Your Account email")
            email = input()
            print("Your Account username")
            userName = input()
            while True:
                print(" cp - To type your own pasword if you already have an account:\n gp - To generate random Password")
                password_Choice = input().strip()
                password = None

                if password_Choice == 'cp':
                    password = input("Enter Your Own Password\n")
                    break

                elif password_Choice == 'gp':
                    password = generate_Password()
                    break

                else:
                    print("Invalid password, please try again")
            cr.save_credential(account,userName,email,password)
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')

        if short_code == "dc":
            if len(cr.credential_list):

                for cred in cr.credential_list:
                    print(cred)
                    print('\n')
            else:
                print("You don't have any credentials saved yet..........")
       
        if short_code == "fc":
            print("Enter the Account Name you want to search for")
            account= input()
            print(cr.search_credential(account))

        
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            account = input()
            if cr.delete_credential(account):
                print("Account Deleted successfully")
            else:
                return "Error occured"


        



if __name__ == '__main__':

    password_locker()
