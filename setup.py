__author__ = 'Dean M. Sands, III'
__author_email__ = 'deanmsands3@gmail.com'
__home_page__ = 'https://github.com/deanmsands3'
__url__ = __home_page__ + '/PyKitchenSink'
from setuptools import setup
import json
package_name = 'kitchensink'

with open('__version__.json') as f:
    v = json.load(f)
    __version__ = "{}.{}.{}+{}".format(v['Major'], v['Minor'], v['Patch'], v['Timestamp'])


setup(
    name=package_name,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    version=__version__,
    packages=[package_name],
    license='Unlicense',
    description='A "Kitchen Sink" collection of assorted modules and classes I\'ve collected',
    include_package_data=True
)


