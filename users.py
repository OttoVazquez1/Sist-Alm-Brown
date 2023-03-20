import json
import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="nueva_database"
)

myCursor = mydb.cursor(dictionary = True)

class User:
    def __init__(self, id, password, name, surname):
        self.id = id
        self.password = password
        self.name = name
        self.surname = surname
        

    def __str__(self):
        return f"{self.surname}, {self.name}"
    
    def load_users():
        #With JSON
        """with open('users.json', "r") as usersfile:
            users = []
            for line in usersfile:
                if line.strip():  
                    user_dict = json.loads(line)
                    users.append(user_dict)
            return users"""
        #WITH MYSQL
        myCursor.execute("SELECT * FROM usuarios")
        usuarios = myCursor.fetchall()
        return usuarios

        
    def user_exists(id, password):
        users = User.load_users()
        for user in users:
            username = user["username"]
            pw = user["pass"]
            if username == id and pw == password:
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
            #JSON
            """with open('users.json', 'a') as usersfile:
                users = {"id": self.id, "password": self.password, "name": self.name, "surname": self.surname}
                user_str = json.dumps(users)
                usersfile.write(user_str + '\n')"""
            
            #MYSQL
            sql = "INSERT INTO usuarios (username, pass, nombre, apellido) VALUES (%s, %s, %s, %s)"
            val = (self.id, self.password, self.name, self.surname)
            myCursor.execute(sql, val)
            mydb.commit()
            return True
        else:
            print("El usuario no está disponible. Prueba otra vez.")
            return False    

    def get_usr(id, password):
        users = User.load_users()
        for user in users:
            username = user["username"]
            pw = user["pass"]
            if username == id and pw == password:
                return user
        else:
            return False
