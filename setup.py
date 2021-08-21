import os
from setuptools import setup, find_packages
from extruder_turtle import __version__

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='extruder-turtle',
    version=__version__,
    description='A Python package that uses the principles of Turtle Geometry to generate GCODE for 3d-printed solids.',
    author='Franklin Pezzuti Dyer',
    author_email='franklin+extruderturtle@dyer.me',
    packages=find_packages(exclude=('docs', 'tests')),
    include_package_data=True,
    package_requires=[
        'math',
        'os',
        'rhinoscriptsyntax'
    ]
    )
