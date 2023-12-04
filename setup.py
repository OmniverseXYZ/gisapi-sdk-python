from setuptools import setup, find_packages

setup(
    name='GISAPI-SDK',
    version='0.1.2',
    author='Parker Dinkins',
    author_email='parkerdinkins@gmail.com',
    description='GISAPI SDK enabling geospatial data search and discovery',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OmniverseXYZ/gisapi-sdk-python',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='gis api sdk',
    packages=find_packages(),
    install_requires=[
        'requests',
    ], 
    python_requires='>=3.6',
)

