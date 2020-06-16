from distutils.core import setup

setup(
    name="qda_modelos,",
    packages=["qda_modelos"],
    version="1.0.0",
    license="BSD",
    description="Implement bio-optic models to evaluate water quality indexes with satellite images.",
    author="CERTI Foundation",
    author_email="qda-pypi@certi.org.br",
    url="https://github.com/fundacaocerti/qda_modelos",
    download_url="https://github.com/fundacaocerti/qda_modelos/archive/v1.0.0.tar.gz",
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
    install_requires=[
        "numpy",
        "qda_modelos"
        "rasterio",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clause License,
        "Operating System :: OS Independent",
    ],
)
