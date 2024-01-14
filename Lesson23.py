class User:
    def __init__(self, user_id, user_name):
        self.id=user_id
        self.username= user_name
        self.followers=0
        self.followings=0
    
    def follow(self, user):
        user.followers+=1
        self.followings+=1



user_1=User('001','kristina')

# print(user_1.id)
# print(user_1.username)

user_2= User('002', 'nursaule')

user_1.follow(user_2)
print(user_1.followings)
print(user_2.followers)
# print(user_2.id)
# print(user_2.username)
