<div align="center">
<h1 >🏢 Exotic Animals Museum 🏢</h1>
</div>

![Museum Gallery](https://github.com/madeinic/museumpg/blob/main/Documentation/Screenshots/interior%201.jpg)

# Introduction

Exotic Animals Museum is a program developed with Python, Pygame and OpenGL that allows users to explore a three-dimensional space to view various models of animals on display in the museum. Users can use the keyboard and mouse to move the camera and view informative posters with details about each animal on display. In addition, the keyboard allows users to hear the sounds of some of the animals, providing a more immersive experience.




### How to run the program

```
pip install -r requirements.txt 
```

```
env/Scripts/Activate 
```

```
python main.py
```

### How to use the program

Use the W A S D keys to move in the environment and press LShift while moving to run. Also move the mouse to change the direction in which the camera points. When you are close to an animal, hold down the F key to play an audio of the animal's sound.



## Screenshots

![Museum Exhibition](https://github.com/madeinic/museumpg/blob/main/Documentation/Screenshots/interior%202.jpg)

![Museum Exhibition](https://github.com/madeinic/museumpg/blob/main/Documentation/Screenshots/interior%203.jpg)

# How it's made


Cubes were used using cycles to create the roof, walls and floor of the museum and appropriate textures were added according to the type of structure they formed. Created a Skybox using global coordinates to apply the textures to a cube and used Pygame's transformation function to rotate the textures so that they display correctly.

For sounds, such as background music and sound areas, the Pygame mixer module was used. This module allows looped background music and animal sounds to be played when the user approaches a specific area and holds down a certain key.

Several animal models were downloaded and imported to be exhibited in the museum. In addition, some decorative models were used to set the mood of the exhibits according to the environment of the animals presented. All models were placed in such a way that they are easy to appreciate, and the decorative models were arranged to decorate the exhibits and enhance the visual experience.


The camera class is configured to allow the user to move through the three-dimensional space at a fixed height using the keyboard. In addition, boundary zones were implemented on the models and the camera to ensure that the user does not walk through the models or move away from the museum area.


### Documentation:

- [Documentation (Spanish)](<https://github.com/madeinic/museumpg/blob/main/Documentation/PaseoVirtualMuseo.pdf>)



## Built With

- [Moderngl](https://moderngl.readthedocs.io/en/5.8.2/) 
- [Numpy](https://numpy.org/) 
- [Pygame](https://www.pygame.org/news) 
- [PyOpenGL](https://pyopengl.sourceforge.net/) 
- [PyGLM](https://pypi.org/project/PyGLM/) 
- [PyWavefront](https://pypi.org/project/PyWavefront/) - Model

## Authors

- * David Soza** - [Doxir010](https://github.com/Doxir010)

- * **Madeling Cabrera** - [madeinic](https://github.com/madeinic)

- * **Javier Romero** - [Courier05](https://github.com/madeinic)

- * **Madeling Cabrera**  - [madeinic](https://github.com/madeinic)

## Acknowledgments
The project was inspired by [aagyo](https://github.com/aagyo/OpenGL-Museum?tab=readme-ov-file)'s project and [StanislavPetrovV](https://www.youtube.com/watch?v=eJDIsFJN4OQ&list=LL&index=22)'s videos.

Models provided by [printable_models](https://free3d.com/user/printable_models)

## Video link:
https://youtu.be/QODSXA7jR2M
