import bpy
import argparse
import sys
import traceback
import os

SCALE = 0.1

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', help="Path to the main latex file", required=True)
    parser.add_argument('--outfile', help="Additional Dependencies", required=True)

    config = parser.parse_args(args)

    while bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[0])
    bpy.ops.import_mesh.stl(filepath=config.infile, global_scale=SCALE)

    mat = bpy.data.materials.new(name="STLDefaultMaterial")
    group_name = os.path.basename(config.infile).split('.', 1)[0]
    group = bpy.data.groups.new(group_name)
    for obj in bpy.data.objects:
        obj.game.physics_type = "NO_COLLISION"
        obj.data.materials.append(mat)
        group.objects.link(obj)

    bpy.ops.wm.save_mainfile(
        filepath=config.outfile,
        compress=True
    )


def run_function_with_args(function):
    arg_pos = sys.argv.index('--') + 1
    try:
        function(sys.argv[arg_pos:])
    except:
        print("ERROR")
        traceback.print_exc()
        sys.exit(1)

    print("SUCCESS")
    sys.exit(0)


run_function_with_args(main)
