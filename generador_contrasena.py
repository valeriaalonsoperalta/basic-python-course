import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['/', '@', '_', '?', '!', '#', '()']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    carateres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    
    
    for i in range(15):
        carater_radom = random.choice(carateres)
        contrasena.append (carater_radom)
    
    contrasena = "". join(contrasena)
    return contrasena
    
    
  


    
def run():
    contrasena = generar_contrasena()

    print("Tu nueva contraseña es: " + contrasena)



if __name__ == '__main__':
    run()
