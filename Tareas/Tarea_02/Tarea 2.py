##Tarea 2

#Ejercicio 1
for x in range(100):
  print(x + 1)

#Ejercicio 2
for x in range(100):
  if(x + 1) % 3 == 0:
    print(x + 1)

#Ejercicio 3
numero_1 = int(input("Ingrese un número"))
numero_2 = 5
suma= numero_1 + numero_2
resultado= ""

if(suma<100):
  resultado= "menor a 100"
elif(suma>=100 and suma<150):
  resultado= "mayor a 100"
elif(suma>=150):
  resultado= "mayor a 150"
print(resultado)

#Ejercicio 4 
edad = int(input("Ingrese edad"))
gustar_programación = (input("Responder Si o No "))


if (edad>18 and gustar_programación == Si):
  promedio = "Eres mayor de edad y te gusta programar"
if (edad>18 and gustar_programación == No):
  promedio = "Eres mayor de edad y no gusta programar"

if (edad<18 and gustar_programación == Si):
  promedio = "No eres mayor de edad o no te gusta programar"
if (edad<18 and gustar_programación == No):
  promedio = "No eres mayor de edad y si te gusta programar"

print(promedio)