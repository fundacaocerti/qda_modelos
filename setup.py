from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="qda_modelos",
    packages=["qda_modelos"],
    version="1.0.0",
    license="BSD",
    description="Implement bio-optic models to evaluate water quality indexes with satellite images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    install_requires=["numpy", "qda_modelos" "rasterio",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
