# class User:
#     pass

# user_1 = User()
# user_1.id="001"
# user_1.username="angela"

# print(user_1.username)

# user_2= User()
# user_2.id="002"
# user_2.username="Jack"
# print(user_2.username)





class User:
    def __init__(self,user_id,username):
        self.id= user_id
        self.username=username

user_1 = User("001","angela")
user_2=User("002","Jack")
print(user_1.id)
print(user_1.username)
print(user_2.id)
print(user_2.username)