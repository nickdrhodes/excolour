import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='excolour',
    version='0.1',
    description='Simple Python package which colours exception traces using iPython',
    author='Nick Rhodes',
    author_email='nicholasdrhodes@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickdrhodes/excolour",
    packages=setuptools.find_packages(),
    install_requires=['ipython']
)
