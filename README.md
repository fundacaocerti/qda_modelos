# Bio-Optical Models for Water Quality Analysis  


This repository has the implementation and tests of benchmarked bio-optic models that evaluates some water quality indexes by analyzing satellite images.
  

## Table of contents  

* [General Info](#general-info)
* [Getting Started](#getting-started)
* [Testing](#testing)
* [Contributing](#contributing)
* [Links](#links)
* [Authors and Contributors](#authors-and-contributors)
* [License](#license)



## General Info  

In order to analyze the water quality of reservoirs by remote sensing, such as satellites, bio-optical models were used. Those models are mathematical and statistical algorithms that generate information about water bodies.

Currently, this project performs calculations for models that estimate the concentration of chlorophyll-a, suspended solids, water transparency, turbidity, cyanobacteria and macrophytes in aquatic environments.

  
  
## Getting Started  

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
  
  
### Technologies

To execute this project, you'll need the following technologies:
  
- 32- or 64-bit computer
- [Python 3](https://www.python.org/downloads/)


### Development

To start the development, it is necessary to clone or download Bitbucket repository in a directory of your choice:  
  
  
```git clone https://user@bitbucket.org/certi_repos/qda_modelos.git```


### Usage

This repository can be used as a complementary library for a main project and its modules can be used whenever they are necessary. 
All dependencies are listed in requirements.txt.

To install dependencies use the following command:  
  
```python3 -m pip install -r requirements.txt```

You can install dependencies directly in your machine or in a virtual environment of your choice, such as [VirtualEnv](https://virtualenv.pypa.io/en/latest/) or [Conda](https://docs.conda.io/en/latest/).



## Testing

This repository implementations can be tested by running **pytest** command in **src** folder.  
  
```python3 -m pytest```
  

## Contributing


Contributions are always welcome!
To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (```git checkout -b improve-feature```)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (```git commit -am 'Improve feature'```)
- Push to the branch (```git push origin improve-feature```)
- Create a Pull Request


While contributing, remember to add tests to the new developed methods.



## Links 

- [A Comprehensive Review on Water Quality Parameters Estimation Using Remote Sensing Techniques](https://www.researchgate.net/publication/306240486_A_Comprehensive_Review_on_Water_Quality_Parameters_Estimation_Using_Remote_Sensing_Techniques)
- [Bio-optical Modeling and Remote Sensing of Inland Waters](https://www.sciencedirect.com/book/9780128046449/bio-optical-modeling-and-remote-sensing-of-inland-waters)



## Authors & Contributors

(Não sei se entra)



## License

BSD 3-Clause License

Copyright (c) 2020, CERTI Foundation All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

    Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.