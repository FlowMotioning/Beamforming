This archive contains the data-sets and code to get started with the data format of the PICMUS challenge. 
The architecture is organized as follows.

archive_to_download
  - code
      * evaluation
      * image_reconstruction_das
      * src
  - database
      * experiments
          contrast_speckle
          resolution_distorsion
      * simulation
          contrast_speckle
          resolution_distorsion
  - evaluation
      * contrast_speckle
      * resolution_distorsion
  - reconstructed_image
      * experiments
          contrast_speckle
          resolution_distorsion
      * simulation
          contrast_speckle
          resolution_distorsion

The pre_beamformed data-sets to beamform are in /database. They correspond to experiments and simulations for both contrast (with speckle quality testing) and resolution (with distorsion testings). All data are stored in .hdf5 files. You will find IQ and RF data. The _scan file includes the grid where to beamform and the  _phantom file includes information necessary to evaluate the different metrics.

An exemple that handles the data-sets and that produces the beamformed image and saves it in the right format is included in /code/images_reconstruction_das. This script calls the beamformer function included in /code/src/beamformers. The reconstructed images are automatically saved in the corresponding folder in /reconstructed_image.

The script that evaluates the metrics is in /code/evaluation. Based on the images and on the phantom information, this script calculates automatically the values of the different metrics and saves the results as text files in the corresponding folder in /evaluation.

For both the image reconstruction example and the metric evaluation, the user can change the parameters at the beginning of the script according to his objective.








    
  
