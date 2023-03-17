import json

class User:
    def __init__(self, id, password, name, surname, role):
        self.id = id
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role   

    def __str__(self):
        return f"{self.surname}, {self.name}"
    
    def load_users():
        with open('users.json', "r") as usersfile:
            users = []
            for line in usersfile:
                if line.strip():  
                    user_dict = json.loads(line)
                    users.append(user_dict)
            return users
        
    def user_exists(id, password):
        users = User.load_users()
        for user in users:
            if user["id"] == id and user["password"] == password:
                return True
            else:
                return False   
    
    def check_for_usrname(id):
        users = User.load_users()
        for user in users:
            if user["id"] == id:
                return False
        return True

    def save_usr(self):
        if User.check_for_usrname(self.id):
            with open('users.json', 'a') as usersfile:
                users = {"id": self.id, "password": self.password, "name": self.name, "surname": self.surname, "role": self.role}
                user_str = json.dumps(users)
                usersfile.write(user_str + '\n')
            return True
        else:
            print("El usuario no está disponible. Prueba otra vez.")
            return False    
