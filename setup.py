from setuptools import setup, find_packages
from os import path


VERSION = '1.0.0'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="mkdocs-semantic",
    version=VERSION,
    url='http://mkdocs-semantic.alazy.dev/',
    license='MIT',
    description='Semantic-UI Theme for MkDocs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='https://github.com/cryocaustik',
    author_email='alex@alazy.dev',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'semantic = semantic',
        ]
    },
    zip_safe=False
)