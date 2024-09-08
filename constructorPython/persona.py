## Los objetos por sí mismos no tienen ninguna propiedad. Las propiedades debemos definirlas en un método creado para las clases llamado init. Este método nos permite definir los valores iniciales del objeto que será creado a partir de la clase. La función init es el constructor de la clase. El constructor siempre se ejecuta cuando se crea el objeto. Para nuestra clase Persona vamos a crear el método init. Reemplazamos el pass por «def __init__(self):». El constructor de la clase y todas las funciones de la clase reciben como primer parámetro el self. Esta variable representa la instancia de la clase y, a través de ella, se pueden acceder a las propiedades y funciones de la clase

class Persona:
    def __init__(self):
        print("estoy en el constructor")

        paco=Persona()