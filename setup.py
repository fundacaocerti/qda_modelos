from distutils.core import setup

setup(
    name="qda_modelos,",
    packages=["qda_modelos"],
    version="0.1",
    license="BSD",
    description="Implement bio-optic models to evaluate water quality indexes with satellite images.",
    author="CERTI Foundation",
    author_email="qda-pypi@certi.org.br",
    # Editar o "url" e o "download_url" quando já estiver inserido no GitHub
    url="https://github.com/user/qda_modelos",
    # Para o "download_url, é necessário "Create a new release" pelo GitHub
    download_url="https://github.com/user/qda_modelos/archive/v_01.tar.gz",
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
