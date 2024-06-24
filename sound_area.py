import glm
import pygame as pg


class SoundArea:
    def __init__(self, position, radius, sound_file, key):
        self.position = glm.vec3(position)
        self.radius = radius
        self.sound_file = sound_file
        self.key = key  # La tecla específica para reproducir el sonido
        self.sound = None
        self.stop_after_playback = False
        self.is_playing = False  # Estado de reproducción

    def load_sound(self):
        self.sound = pg.mixer.Sound(self.sound_file)
        self.sound.set_volume(0)

    def play(self):
        if not self.is_playing:
            self.sound.play(loops=-1)
            self.is_playing = True

    def stop(self):
        if self.is_playing:
            self.sound.stop()
            self.is_playing = False

    def set_volume(self, volume):
        self.sound.set_volume(volume)

    def check_and_play(self, cam_pos, key_pressed):
        distance = glm.distance(cam_pos, self.position)
        print(f'Distance to sound area: {distance}')
        if distance < self.radius:
            if key_pressed[self.key]:
                volume = 1 - (distance / self.radius)
                print(f'Setting volume: {volume}')
                self.set_volume(volume)
                self.play()
            else:
                print('Stopping sound')
                self.stop_after_playback = True
                self.set_volume(0)
                self.stop()
        else:
            print('Out of range, stopping sound')
            self.set_volume(0)
            self.stop()
