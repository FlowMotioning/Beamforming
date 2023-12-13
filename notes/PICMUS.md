# Concept Note: PICMUS Dataset

## Overview
<!-- Provide a brief overview of the concept, highlighting its purpose and significance.-->
Challenge from 2016 that provided sample data and requested the participants to develop **beamforming algorithms** which would then be compared to each other.

Data format is **.hdf5**. See [HDF5 note](HDF5.md) for overview and tools to visualize.

## Key Features
<!-- Enumerate the key features or characteristics of the concept.-->

Contrast Speckles of Phantom in PICMUS dataset ([contrast_speckle_expe_dataset_rf.hdf5](../archive_to_download/database/experiments/contrast_speckle/contrast_speckle_expe_dataset_rf.hdf5)) have following entries in the real and imag matrices:
- channels 0-127 (128 total transducers)
- 3328 entries (this is frames? Or raw frames?)
- 75 degrees (these are the degrees of the beams that are going into the tissue, this is useful when trying to do Compound Imaging)

## Implementation
<!-- Outline the steps or process required to implement the concept.-->
[Python Beamformer library](<PyBF Library.md>) has already functionality to load PICMUS datasets. 

Resolution example is here: [main_resolution.ipynb](../juypter/pybf/tests/code/low_ch_mvbf_jupyter/main_resolution.ipynb)
- example compares the resolution of two beamformers (DAS and MVDR) in a jupyter notebook

Contrast example is here: [main_contrast.ipynb](../juypter/pybf/tests/code/low_ch_mvbf_jupyter/main_contrast.ipynb)

## Challenges
<!-- Identify any potential challenges or obstacles that may arise during the implementation of the concept.-->

- Getting the PyBF code to handle the actual dataset and not data from [Beamforming/juypter/pybf/tests/data/Picmus/contrast_speckle/rf_dataset.hdf5](../juypter/pybf/tests/data/Picmus/contrast_speckle/rf_dataset.hdf5)