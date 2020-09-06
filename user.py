import pyperclip
import random
import string

class User:
    '''
    Class User generate a instances of user cridentials.
    '''

    user_list = []

    def __init__(self, user_name, password):

        '''
        __init__ method that defines the properties for user objects 
        '''
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        user method that saves the objects in the user_list 
        '''
         
        User.user_list.append(self)


        

