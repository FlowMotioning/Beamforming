# Concept Note: PyBF (Python Beamformer)

## Overview
<!-- Provide a brief overview of the concept, highlighting its purpose and significance.-->
Library by [GitHub Link](https://github.com/Sergio5714/pybf/tree/master) to implement beamforming in python. The library implements several different beamforming algorithms to reconstruct ultrasound images from B-mode raw data with $n$ transducers.

## Key Features
<!-- Enumerate the key features or characteristics of the concept.-->

See [Structure of the repository](https://github.com/Sergio5714/pybf/tree/master#structure-of-the-repository) to get overview of the package:
- `pybf` contains low level routines
- `scripts`: here are the functions that implement even entire pipeline for image reconstruction
- `tests`: some testing functions to determine the quality and performance of the data/algorithms. There are tests that use an adapted version of **PICMUS** dataset.
    - mentioned dataset is an adapted version of the PICMUS dataset. Below in "Implementations" the example code from PyBF uses this version, not the original dataset files from PICMUS website. 
    - IMPORTANT: put folder `Picmus` into the pybf library, such that the path is `Beamforming/juypter/pybf/tests/data/Picmus`

## Implementation
<!-- Outline the steps or process required to implement the concept.-->
"All code necessary to acquaint oneself with the pybf library's different beamformers is located under `tests/code/`" (from README.md of PyBF)

- [io_interfaces.py](../juypter/pybf/pybf/io_interfaces.py) contains two classes: `DataLoader`and `ImageLoader`
    - **DataLoader**: loads required data from the **.hdf5** files. The functions are loading data from defined paths within .hdf5 files. Please use the mentioned *adapted dataset* provided by the PyBF maintainers. 
        - Code will have to be adapted to handle PICMUS itself
        - Are there even all the required data categories in the datasets provided by PICMUS?