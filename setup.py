import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='npm',
    author="Anuj Pasricha",
    author_email='anuj.pasricha@colorado.edu',
    version='1.0.0',
    description='Base project for all things NPM.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HIRO-group/npm',
    packages=setuptools.find_packages(where='npm*'),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
