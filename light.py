import glm

class Light:
    def __init__(self, position=(30, 30, 10), color =(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        # intensidades de los elementos del modelo de Phong para calcular la iluminación
        self.Ia = 0.6 * self.color # ambiental
        self.Id = 0.8 * self.color # difusa
        self.Is = 1.0 * self.color # especular
        