#!/usr/bin/env python3.6

# Note that this file should be called from either of the launch files in the module

import rospy
import sys
import os


rospy.sleep(1)  # so that launch script can finish running

# Load these parameters that have been defined in the yaml or launch file
yaml_name_space = sys.argv[1]
parameter_paths = [
    yaml_name_space + '/' + 'my/param/str',
    yaml_name_space + '/' + 'my/param/int',
    yaml_name_space + '/' + 'my/param/float',
    "from_launchfile/my/param/is_overridden",
]
parameter_values = [rospy.get_param(p) for p in parameter_paths]


# Add a parameter that hasn't been assigned yet by supplying a default
foo_path = 'not/a/path/to/a/valid/parameter'
parameter_paths.append(foo_path)
try:
    rospy.get_param(foo_path)
except KeyError as e:
    pass
parameter_values.append(
    rospy.get_param(foo_path, default="Default value set in '{}'".format(os.path.basename(__file__)))
)

# Print loaded parameters
assert len(parameter_values) == len(parameter_paths)
print()
for i in range(len(parameter_values)):
    print(
        "\t{path}  ==>  {value}, {type}".format(
            path=parameter_paths[i],
            value=parameter_values[i],
            type=type(parameter_values[i])
        )
    )
print()

