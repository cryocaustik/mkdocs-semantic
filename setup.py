from setuptools import setup, find_packages
from os import path


VERSION = '0.0.4'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="mkdocs-semantic",
    version=VERSION,
    url='https://github.com/cryocaustik/mkdocs-semantic',
    license='MIT',
    description='Semantic-UI Theme for MkDocs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='https://github.com/cryocaustik',
    author_email='cryocaustik@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'semantic = semantic',
        ]
    },
    zip_safe=False
)