

class User:
    def __init__(self,username,password,userId):
        self.username = username
        self.password = password
        self.userId = userId
    def showNode(self): 
        print("username:", self.username)
        print("password:", self.password)
        print("userId:", self.userId)



class Users(User):
    def __init__(self, username, password, userId) -> None:
        super().__init__(username, password, userId)

newUser = Users(username="talha",password="cft1903cft",userId="210717058")

print(newUser.showNode())