from distutils.core import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst")) as f:
    long_description = f.read()

setup(
    name="qda_modelos",
    packages=["qda_modelos"],
    version="1.0.4",
    license="BSD",
    description="Implement bio-optic models to evaluate water quality indexes with satellite images.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="CERTI Foundation",
    author_email="qda-pypi@certi.org.br",
    url="https://github.com/fundacaocerti/qda_modelos",
    download_url="https://github.com/fundacaocerti/qda_modelos/archive/v1.0.4.tar.gz",
    keywords=[
        "bio-optic models",
        "water quality",
        "indexes",
        "satellite image",
        "reservoir",
        "lake",
        "water",
        "remote sensing",
    ],
    install_requires=["numpy", "qda_modelos"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
