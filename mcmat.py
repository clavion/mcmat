
import bpy

bpy.context.scene.render.engine = 'CYCLES'

emissionNames = [
    'torch_flame',
    'fire',
    'lava',
    'lava_flowing',
    'glowstone',
    'redstone_wire_on'
]

for matslot in bpy.context.active_object.material_slots:
    mat = matslot.material
    image = mat.texture_slots[0].texture.image
    mat.use_nodes = True
    mat.node_tree.nodes.clear()
    links = mat.node_tree.links
    nodes = mat.node_tree.nodes
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (0, 0)
    mix = nodes.new('ShaderNodeMixShader')
    mix.location = (-200, 0)
    transparent = nodes.new('ShaderNodeBsdfTransparent')
    transparent.inputs[0].default_value = (1,1,1,1)
    transparent.location = (-400, 100)
    if(mat.name in emissionNames):
        mainNode = nodes.new('ShaderNodeEmission')
        mainNode.inputs[1].default_value = 3.0
    else:
        mainNode = nodes.new('ShaderNodeBsdfDiffuse')
        mainNode.location = (-400, -50)
    teximg = nodes.new('ShaderNodeTexImage')
    teximg.location = (-600, -50)
    teximg.image = image
    links.new(transparent.outputs[0], mix.inputs[1])
    links.new(teximg.outputs[0], mainNode.inputs[0])
    links.new(mainNode.outputs[0], mix.inputs[2])
    links.new(teximg.outputs[1], mix.inputs[0])
    if(mat.name.startswith('glass') or mat.name.startswith('water')):
        mix2 = nodes.new('ShaderNodeMixShader')
        if(mat.name.startswith('glass')):
            mix2.inputs[0].default_value = 0.5
        else:
            mix2.inputs[0].default_value = 0.3
        mix2.location = (0, 0)
        output.location = (200, 0)
        glossy = nodes.new('ShaderNodeBsdfGlossy')
        glossy.inputs[1].default_value = 0.0
        glossy.location = (-200, -150)
        links.new(mix.outputs[0], mix2.inputs[1])
        links.new(glossy.outputs[0], mix2.inputs[2])
        links.new(mix2.outputs[0], output.inputs[0])
    else:
        links.new(mix.outputs[0], output.inputs[0])
