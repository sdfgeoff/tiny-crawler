tup.creategitignore()

tup.foreach_rule('*.stl.blend', blender .. '%f -b --python $(TOP)/export_stl.py -- --outfile %o', '$(STL_FOLDER)/%B')
