from sympy import *
#Pedro Escobar

#punto1
n=int(input("Ingrese el valor de n: "))
arreglo=[]
matriz=[]
for j in range(0, n):
  for i in range(0, n):
    arreglo.append(int(input("Ingrese valor")))
  matriz.append(arreglo)
  arreglo=[]
print("Matriz insertada:")
for j in range(0, n):
  for i in range(0, n):
    print(matriz[j][i]," ", end='')
  print("")
suma=0
value=0
val2=0
contador=1

#Metodo para sumar los valores de la submatriz triangular superior, notación O()
while(value<n):
  if(val2==n):
    val2=contador
    contador=contador+1
  suma=suma+matriz[value][val2]
  val2=val2+1
  if(val2==n):
    value=value+1
    print("Suma por fila acumulada: ",suma)

print("f(n): ",suma)




#punto2
def recursion(ec1, ec2, x, xanterior):
  print(solve(ec1,x))
  print(solve(ec2,x))
  if(solve(ec1,x)==solve(ec2,x)):
    return x
  else:
    return recursion(ec1,ec2,round(x-((solve(ec1,x)*(x-xanterior))/(solve(ec1,x)-(solve(ec1,xanterior)))),7),x)

ecu="ln(x+2)"
ecu2 = "sin(x)"
x=1
print("Intersección en x= ",recursion(ecu,ecu2,x, 0),"+- 1e-07")




#punto3
def newton(ecuaciones, intervalo1, intervalo2):
    if(solve(ecuaciones[0], 1)==3or solve(ecuaciones[0], 2)==4):
        
        variables=[]
        derivadas=[]
        cont=0
        for k in range (0, len(ecuaciones)):
            for i in range(0, len(ecuaciones[k])):
                ec=ecuaciones[k]
                if(ec[i].isalpha()):
                    if(ec[i] not in variables):
                        variables.append(ec[i])
                        variables[cont]=symbols(variables[cont])
                        cont=cont+1
        for k in range (0, len(ecuaciones)):
            for i in range (0, len(variables)):
                derivadas.append(diff(ecuaciones[k], variables[i]))



        return "exito"
        
    return "no tiene solucion"

polinomio=[3,4,5,6,7]
ecuaciones=["a+(a*x+b)*e**(a*x+b)", "1", "4"]
intervalo1=1
intervalo2=4
print("Coeficientes hallados: ",newton(ecuaciones, intervalo1, intervalo2))

