mcmat
=====

Converting materials to Blender Cycles for objects exported from Minecraft.

Features
--------
* Generate material nodes of Cycles with image textures.
* Alpha channel is used to mix diffuse shader with transparent shader, which makes the rendering of something like flowers and leaves to be correct.
* Emission shader is used for torch, glowstone, lava, etc.
* Glossy shader is mixed for glass and water.

Prerequisite
------------

* [Minecraft](https://minecraft.net) (1.7.5)
* [Jmc2Obj](http://www.jmc2obj.net) (0.2-dev303)
* [Blender](http://www.blender.org) (2.70)

The versions listed above are what I am using at present. Other versions may also work. 

Usage
-----

You have the directory `world` or other worlds you have played in with Minecraft. Export the regions you want using jMc2Obj. Note that

1. Do not create separate objects for anything.
2. Do not use single material.
3. Set `Pre-scale textures` to 16x, so that the final outcome will look more like pixels instead of being smoothed.
4. The textures should be exported in a subdirectory named `tex` within the one that the obj file will be exported to.

In Blender, import the object through `File` > `Import` > `Wavefront (.obj)`. Select the minecraft object, and make sure it is the only object selected. Open the script `mcmat.py` of this repository in the text editor of Blender and run it. Then all materials should be ready to render.
