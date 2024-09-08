## La herencia de clases permite que una clase sea creada a partir de otra. En la programación orientada a objetos, usamos clases padre y clases hijo cuando hablamos de herencia, ya que existe una clase principal, conocida como la clase padre, y una clase secundaria que recibe el nombre de clase hija. Esa clase hija hereda atributos o métodos de la clase padre. Cuando decimos que una clase hereda algo, hacemos referencia a que la clase secundaria aproveche atributos o métodos de la principal para reutilizar código ya existente.
class Persona:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anios(self):
        self.edad+=1
        print(f"Feliz cumpleaños #{self.edad} #{self.nombre}")

class Empleado(Persona):
    def __init__(self,horas_totales,nombre,edad):
        super(Empleado,self).__init__(nombre,edad)
        self.horas_totales=horas_totales
        
    def trabajar(self,horas_trabajadas):
        self.horas_totales+=horas_trabajadas

        print(f"usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales {self.horas_totales}")



paco=Empleado(nombre="paco",edad=20,horas_totales=30 )
paco.trabajar(horas_trabajadas=8)
paco.cumplir_anios()