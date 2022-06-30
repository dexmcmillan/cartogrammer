from setuptools import find_packages, setup
from pathlib import Path

# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.rst").read_text()

setup(
    name='cartogrammer',
    packages=find_packages(include=["cartogrammer"]),
    version='0.0.2',
    # url='https://github.com/dexmcmillan/datawrappergraphics',
    description='A package for bootstrapping cartographic grid maps from shapefiles.',
    # long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dexter McMillan',
    license='MIT',
    install_requires=[
        "pandas",
        "geopandas",
        ],
    setup_requires=[
        'pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-runner'],
    test_suite='tests',
)