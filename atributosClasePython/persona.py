## Cada objeto que creamos a partir de una clase en Python puede tener atributos. Los atributos son las propiedades de la clase, es decir, las variables que definen las características del objeto. Las clases tienen dos tipos de atributos: los atributos de instancia y los atributos de la clase. 

class Persona:



##los atributos de la clase son variables que se definen por fuera del constructor y tienen el mismo valor para todos los objetos que se crean a partir de esa clase.  
    atributo=123




    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

paco=Persona("Paco",20)
print(paco.nombre,paco.edad)

print(paco.atributo)