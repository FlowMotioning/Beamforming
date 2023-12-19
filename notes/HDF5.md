# Concept Note: Hierarchical Data Format

## Overview
<!-- Provide a brief overview of the concept, highlighting its purpose and significance.-->
Database for storing large quantities of numerical values for scientific and engineering work. See [HDF5 Documentation](https://support.hdfgroup.org/HDF5/doc/index.html) for technical details. 

## Key Features
<!-- Enumerate the key features or characteristics of the concept.-->
- [An Introduction to HDF5 - YouTube](https://www.youtube.com/watch?v=S74Kc8QYDac)
    - hierarchical "tree"-like database-ish saving of multiple datatype in one .hdf5 file!
    - often operations need to be done on only a fraction of data. HDF5 allows to load only required rows into memory, instead of the whole file like in .csv
    - sharable format, many programming environments (python, matlab) use HDF5 API packages

## Implementations

The HDF Group is an open source project, that updates these offline database-filesystems. Check their website from *overview*. To visualize the database use either [myHDF5](https://myhdf5.hdfgroup.org/) on the internet which can open local files, or the VSCode extension [H5Web](https://marketplace.visualstudio.com/items?itemName=h5web.vscode-h5web)