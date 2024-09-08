## En programación, un objeto es la representación de un elemento. Los objetos nos permiten representar elementos de la vida real, por ejemplo, una persona puede ser representada por un objeto, pero este objeto debe definirse a partir de un plano o un molde.
class Persona:
    pass

pedro=Persona()
print(type(pedro))

paco= Persona()
print(type(paco))

print(pedro== paco)
## los objetos son diferentes. Esto sucede porque son objetos de igual tipo, pero cada uno de ellos ocupa una posición diferente en la memoria del computador, por lo tanto, no son el mismo objeto. 
