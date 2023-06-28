class User:
    def __init__(self,name):
        self.name=name
        self.__password='abc'

    #how to get a name:
    @property
    def password(self):
        return self.__password

    # how to change a secret name:
    @password.setter
    def password (self, value):
        print('set password =', value)
        self.__password = hash(value)

u=User('John')
print(u.name,u.password)
print(u.__dict__) #{'name': 'John', '_User__password': 'abc'}
print(u._User__password) #abc

u.password='secret'
print(u.name,u.password)
print(u.__dict__)