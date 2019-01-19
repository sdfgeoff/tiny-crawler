tup.creategitignore()

outs = tup.foreach_rule('*.stl.blend', blender .. '%f -b --python $(TOP)/export_stl.py -- --outfile %o', '$(STL_FOLDER)/%B')
tup.foreach_rule(outs, blender .. ' -b --python $(TOP)/import_stl.py -- --infile %f --outfile %o', '$(GEN_BLEND_FOLDER)/%B.blend')
