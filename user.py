import pyperclip
import random
import string


class User:
    '''
    Class User generate a instances of user credentials.
    '''

    user_list = []

    def __init__(self, userName, password):
        '''
        __init__ method that defines the properties for user objects
        '''

        self.userName = userName
        self.password = password
        self.isLoggedIn = False

    def login(self,userName,password):
        if userName == self.userName and password in self.password:
            self.isLoggedIn= True
            print( "Login Successfully!")
            return True
        else:
            print( "Incorrect Username/ Password")
            return False

    def save_user(self,userName,password):            
        '''
        user method that saves the objects in the user_list
        '''
        self.userName = userName
        self.password = password
        self.isLoggedIn= True
        print("Account Created Successfully")
        self.user_list.append({'username':userName,'password':password})
        return True

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        method that deletes a saved account from the list
        '''
        User.user_list.remove(self)

class Credentials:
    '''
    class credentials creates new object of creadentials
    '''
    credential_list = []


    def __init__(self, account, userName, email, password):
        '''
        method that defines user credentials
        '''
        self.account = account
        self.userName = userName
        self.email = email
        self.password = password

    def save_credential(self,account,userName,email,password):
        '''
        method that saves the objects in the credential_list
        '''
        account = {'account':account,'username':userName,'email':email,'password':password}
        self.credential_list.append(account)
        print("Account created successfully!")
        return self.credential_list


    def delete_credential(self,account):
        '''
        method that deletes an account
        '''
        if self.account:
            if (acc['account']==account for acc in self.account):

                # new_acc = []
                # for acc in self.account:
                #     if not(acc['account'] ==account):
                #         new_acc.append(acc)
                # self.account = new_acc
                self.credential_list = [acc for acc in self.credential_list if not(acc.get('account')==account)]
                
                return True
            else:
                return False
        else:
            return "You don't ave any account yet"

   

    @classmethod
    def search_credential(cls, account):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.

        '''
        for credential in cls.credential_list:
            if credential['account'] == account:
             return credential
        return "Not Found"

    @classmethod
    def credential_exists(cls, account):
        '''
        Method that checks if a credential exists from the credential list and returns true or false depending on whether the credential exists.
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False
     
    @classmethod
    def display_credentials(cls):
        '''
        Method that returns all items in the credentials list
        '''
        return cls.credential_list
    
    def login_user_credentials(self):
        '''
        metthod that logs in the user
        '''
        Credentials.credential_list.append(self)
        

    # @classmethod
    # def copy_credential(cls, site_name):
    #     '''
    #     Class method that copies a credentials details after the credentials site_name has been entered
    #     '''
    #     find_credential = Credentials.find_by_account(account)
    #     return pyperclip.copy(find_credential.password)

    @classmethod
    def generate_password(self,stringLength=8):
        '''
        Generate a random password string of letters and digits and special characters
        '''
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))


    




        
# c =User('John','Doe')
# print(c.login('John','Doiiiioioie'))
# print(Credentials())
cr = Credentials('aa','b','asas','sdsfd')
cr.save_credential('add','asdadsad','dsadsad','asdasdad')
cr.save_credential('ig','asdadsad','dsadsad','asdasdad')
# print(cr.save_credential('add','asdadsad','dsadsad','asdasdad'))


     
print(cr.delete_credential('add'))