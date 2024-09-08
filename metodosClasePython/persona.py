## Los métodos de la clase son funciones que se definen dentro de una clase. Cada uno de los objetos creados a partir de una misma clase puede acceder a sus métodos. Los métodos de las clases se definen tal como las funciones, con la diferencia de que los métodos deben recibir como primer atributo la variable self. Esta variable representa la instancia de la clase y, a través de ella, se puede acceder a las propiedades y funciones de la clase. Vamos a crear un método en nuestra clase Persona, que se llama cumplir años. Este método no recibirá ningún parámetro, pero modificará el atributo de la edad e imprimirá un mensaje. 

class Persona:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anios(self):
        self.edad+=1
        print(f"Feliz cumpleaños #{self.edad} #{self.nombre}")

paco=Persona(nombre="paco",edad=20)
paco.cumplir_anios()

