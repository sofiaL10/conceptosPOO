import random    # siempre dejar 2 espacios para que funcione #


class Materia:

    def __init__(self, nombre: str, creditos: int):
        self.nombre: str = nombre
        self.creditos: int = creditos



class Estudiante:

    # atributo de instacia = init y self #

    def __init__(self, nombre: str, edad: int, nota_promedio: float):
        self.nombre: str = nombre
        self.edad: int = edad
        self.nota_promedio: float = nota_promedio
        self.materias: list[Materia] = []          # manera de relacionar dos clases #

    # manera de crear una lista #

    def matricular_materia(self, nombre_materia: str, creditos: int):
        materia: Materia = Materia(nombre_materia, creditos)
        self.materias.append(materia)


# para agregar metodos #                  # siempre con verbos. ej. cambiar #

    def cambiar_nota(self):
        n = random.randint(1, 10)
        if n > 5:
            self.nota_promedio += 0.5
        else:
            self.nota_promedio -= 0.5


if __name__ == "__main__":
    e1: Estudiante = Estudiante("pedro", 18, 3.5)
    e2: Estudiante = Estudiante("maria", 15, 3.5)
    e3: Estudiante = Estudiante("luisa", 20, 2.8)

    

    # para agregar el metodo, en esta ocacion fue cambair la nota #

#    print(e2.nota_promedio)
#    e2.cambiar_nota()
#    print(e2.nota_promedio)

#    print(e1.nombre) #
#    print(e2.nombre) #  # accede a los valores de un atributo #
#    print(e3.nombre) #

#    e1.nombre = "carlos"  # cambia el valor del atributo #

#    print(e1.nombre)
#    print(e2.nombre)
#    print(e3.nombre)
