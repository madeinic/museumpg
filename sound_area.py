import glm
import pygame as pg

class SoundArea:
    def __init__(self, position, radius, sound_file):
        self.position = glm.vec3(position)
        self.radius = radius
        self.sound_file = sound_file
        self.sound = None

    def load_sound(self):
        self.sound = pg.mixer.Sound(self.sound_file)
        self.sound.set_volume(0)

    def play(self):
        if not self.sound.get_num_channels():
            self.sound.play(loops=-1)

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume):
        self.sound.set_volume(volume)

    def check_and_play(self, cam_pos):
        distance = glm.distance(cam_pos, self.position)
        print(f'Distance to Sound Area: {distance}, Radius: {self.radius}')  # Registro de depuración

        if distance < self.radius:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:  # Cambia `self.key` por `pg.K_SPACE` o la tecla que desees usar
                volume = 1 - (distance / self.radius)
                print(f'Volume: {volume}')  # Registro de depuración
                self.set_volume(volume)
                self.play()
            else:
                self.set_volume(0)
                self.stop()
        else:
            self.set_volume(0)
            self.stop()
