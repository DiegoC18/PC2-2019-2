import os
os.system("cls")

print ("-----Bienvenidos al programa de inscripcion del curso de natacion-----")

n_alumn = 0
l_nombres=[]
l_sexo=[]
l_edad=[]
n_hombres = 0
n_mujeres = 0
promedio=0

while n_alumn < 5:
    nombre = input("ingrese su nombre: ")
    l_nombres.append(nombre)
    while True:
        sexo = input("¿eres hombre o mujer?: ")
        if sexo.lower() == "hombre":
            n_hombres += 1
            l_sexo.append("hombre")
            break
        elif sexo.lower() == "mujer":
            l_sexo.append("mujer")
            n_mujeres += 1

            break
        else:
            sexo=input("ingrese dato valido: ")        
    
    while True :
        edad = int(input("ingrese su edad: "))
        if edad<5 or edad>17:
            edad = int(input("edad no valida, ingrese una validad: "))
        if edad>5 or edad<17:
            l_edad.append(edad)
            promedio += edad
            break    
    
    n_alumn += 1


for i in range(0,n_alumn):
    print("alumno", i+1)
    print("nombre: ", l_nombres[i])
    print("sexo: ", l_sexo[i])
    print("edad: ",l_edad[i])
    print("-------------------------")

print("numero de hombre: ",n_hombres)
print("numero de mujeres: ", n_mujeres)
print(promedio/5)    

