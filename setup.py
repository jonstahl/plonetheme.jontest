from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.0.1'

setup(
    author='Jon Stahl',
    author_email='None',
    classifiers=(
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
    ),
    description='An installable Diazo theme for Plone 4.2',
    entry_points = {
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    long_description=(open('README.txt').read() +
        open(os.path.join('docs', 'HISTORY.txt')).read()),
    name='plonetheme.jontest',
    namespace_packages=(
        'plonetheme',
    ),
    packages=find_packages(),
    url='https://github.com/jonstahl/plonetheme.jontest',
    version=VERSION,
)
