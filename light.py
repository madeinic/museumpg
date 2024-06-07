import glm

class Light:
    def __init__(self, position=(30, 30, 10), color =(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensidades de los elementos del modelo de Phong para calcular la iluminación
        self.Ia = 0.6 * self.color # ambiental
        self.Id = 0.8 * self.color # difusa
        self.Is = 1.0 * self.color # especular
        #view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
    