import glm
import pygame as pg
from time import sleep

FOV = 50  # deg
NEAR = 0.1
FAR = 110
BASE_SPEED = 0.005
BOOSTED_SPEED = 0.10  # Velocidad aumentada al presionar Shift
SENSITIVITY = 0.04

class Camera:
    def __init__(self, app, position=(0, 1, 0), yaw=-90, pitch=0, min_height=3.1, max_height=3.1):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        #obtener altura maxima y minima
        self.min_height = min_height
        self.max_height = max_height
        # view matrix
        self.m_view = self.get_view_matrix()
 # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = BASE_SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        # Ajustar velocidad si se presiona Shift
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            velocity = BOOSTED_SPEED * self.app.delta_time
        
        #variable para obtener la posicion que se usara para detectar colisiones
        potential_position = glm.vec3(self.position)

        if keys[pg.K_w]:
            potential_position += self.forward * velocity
        if keys[pg.K_s]:
            potential_position -= self.forward * velocity
        if keys[pg.K_a]:
            potential_position -= self.right * velocity
        if keys[pg.K_d]:
            potential_position += self.right * velocity
        if keys[pg.K_q]:
            potential_position += self.up * velocity
        if keys[pg.K_e]:
            potential_position -= self.up * velocity

        
        if not self.detect_collision(potential_position):
            self.position = potential_position

        # Limitar la altura de la cámara
        self.position.y = max(self.min_height, min(self.max_height, self.position.y))

    #funciona para verificar si la camara esta tocando una caja delimitadora
    def detect_collision(self, new_position):
        for obj in self.app.scene.objects:
            min_corner, max_corner = obj.bounding_box
            if (min_corner.x <= new_position.x <= max_corner.x and
                min_corner.y <= new_position.y <= max_corner.y and
                min_corner.z <= new_position.z <= max_corner.z):
                return True
        return False

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
