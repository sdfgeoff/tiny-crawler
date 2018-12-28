import bpy
import argparse
import sys
import traceback
import os

SCALE = 0.1

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--outfile', help="Additional Dependencies", required=True)

    config = parser.parse_args(args)

    bpy.ops.object.duplicates_make_real()

    bpy.ops.export_mesh.stl(
        filepath=config.outfile,
        check_existing=True,
        axis_forward='Y',
        axis_up='Z',
        filter_glob="*.stl",
        use_selection=False,
        global_scale=10.0,
        use_scene_unit=False,
        ascii=False,
        use_mesh_modifiers=True,
        batch_mode='OFF'
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
