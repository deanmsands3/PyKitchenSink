__author__ = 'Dean M. Sands, III (deanmsands3@gmail.com)'
__version__ = '0.0.1a'
from setuptools import setup
package_name = 'kitchensink'


setup(
    name=package_name,
    author=__author__,
    version=__version__,
    packages=[package_name],
    license='Unlicense',
    description='A "Kitchen Sink" collection of assorted modules and classes I\'ve collected',
    include_package_data=True
)


