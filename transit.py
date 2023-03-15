import pandas as pd
import random

namesList = []
dniList = []
medic = []
try:
    while True:
        name = input("Nombre y apellido: \n")
        namesList.append(name)
        dni = input("DNI: \n")
        dniList.append(dni)
        booList = bool(random.getrandbits(1))
        medic.append(booList)

        if len(namesList) > 2 and len(dniList) > 2:
            data = {
                "Nombre": namesList,
                "DNI": dniList,
                "Medico": medic
            }
            newdf = pd.DataFrame(data)
            print(newdf)
        newone = input("Quieres agregar a alguien mas? Y/y o N/n\n")
        newone = newone.lower()
        while True:
            if newone == "y":
                break
            elif newone == "n":
                newdf.to_excel(r'C:\Users\Almirante Brown\Saved Games\c\transit-csv\transito.xlsx', index=False)
                print(newdf)
                break
            else: 
                print("Error, para si escriba Y o y, para NO, escriba N o n")
        
except:
    print("Error, ha salido")