# Concept Note: PyBF (Python Beamformer)

## Overview
<!-- Provide a brief overview of the concept, highlighting its purpose and significance.-->
Library by Sergei [GitHub Link](https://github.com/Sergio5714/pybf/tree/master) to implement beamforming in python. There are 3 different algorithms available (Delay and Sum, two other) to reconstruct ultrasound images from B-mode raw data with $n$ transducers. 

## Key Features
<!-- Enumerate the key features or characteristics of the concept.-->

See [Structure of the repository](https://github.com/Sergio5714/pybf/tree/master#structure-of-the-repository) to get overview of the package:
- `pybf` contains low level routines
- `scripts`: here are the functions that implement even entire pipeline for image reconstruction
- `tests`: some testing functions to determine the quality and performance of the data/algorithms. There are tests that use the **PICMUS** dataset. IMPORTANT: put the folder `Picmus` into the pybf library, such that the path is `Beamforming/juypter/pybf/tests/data/Picmus`

## Implementation
<!-- Outline the steps or process required to implement the concept.-->
"All code necessary to acquaint oneself with the pybf library's different beamformers is located under `tests/code/`" (from README.md of PyBF)

- [io_interfaces.py](../juypter/pybf/pybf/io_interfaces.py) contains two classes: `DataLoader`and `ImageLoader`
    - **DataLoader**: loads required data (from [this README](../juypter/pybf/tests/data/README.md)) out of the **.hdf5** file that can be downloaded from the polybox link. Code must be adapted to handle PICMUS itself
        - Are there even all the required data categories in the datasets provided by PICMUS?