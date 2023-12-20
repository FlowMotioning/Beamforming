# Import PyBF library
import numpy as np
import sys, os
'''
import sys, os
look here if below import doesn't work: https://stackoverflow.com/questions/7505988/importing-from-a-relative-path-in-python
'''
# sys.path.append('../jupyter')
sys.path.append('../jupyter/')
from pybf.pybf.io_interfaces import DataLoader
from pybf.scripts.beamformer_DAS_ref import BFCartesianReference
from pybf.scripts.beamformer_mvbf_spatial_smooth import BFMVBFspatial
from pybf.scripts.beamformer_mvbf_DCR import BFMVBFdcr
from pybf.pybf.image_settings import ImageSettings
from pybf.pybf.visualization import plot_image
from pybf.scripts.picmus_eval import PicmusEval

data_loader_obj = DataLoader('./pybf/tests/data/Picmus/resolution_distorsion/rf_dataset.hdf5')

def create_beamformer(tx_strategy):
    """
    Creates a beamformer for the active elements and the specified transmission strategy.

    Args:
        tx_strategy (list): Transmission strategy.

    Returns:
        object: Beamformer object.

    Pre-conditions:
        - The tx_strategy is a valid transmission strategy.

    Post-conditions:
        - The returned beamformer object is initialized with the specified active elements and transmission strategy.
    """

    # set active transducer elements
    # data_loader_obj.transducer.set_active_elements(active_elements_list)
    img_res = [400, 600]
    image_x_range = [-0.019, 0.019]
    image_z_range = [0.005, 0.05]

    db_range = 50

    LATERAL_PIXEL_DENSITY_DEFAULT = 5

    img_config = ImageSettings(image_x_range[0],
                               image_x_range[1],
                               image_z_range[0],
                               image_z_range[1],
                               LATERAL_PIXEL_DENSITY_DEFAULT,
                               data_loader_obj.transducer)

    ### Specify preprocessing parameters for RF data ###
    decimation_factor = 1
    interpolation_factor = 10

    ### Specify TX strategy and Apodization parameters ###
    start_time = 0
    correction_time_shift = 0

    alpha_fov_apod = 40

    # tx_strategy = 
    rf_data_shape = (len(tx_strategy[1]),) + data_loader_obj.get_rf_data(0, 0).shape
    rf_data = np.zeros(rf_data_shape)
    inclin_index = np.asarray(list(range(len(tx_strategy[1]))))
    # return print(rf_data.shape)
    for i in range(rf_data.shape[0]):
        rf_data[i, :, :] = data_loader_obj.get_rf_data(0, inclin_index[i])

    SAMPLING_FREQ = data_loader_obj.f_sampling

    filters_params = [1 * 10 **6, 8 * 10 **6, 0.5 * 10 **6]

    bf = BFCartesianReference(SAMPLING_FREQ,
                             tx_strategy,
                             data_loader_obj.transducer,
                             decimation_factor,
                             interpolation_factor,
                             img_res,
                             img_config,
                             start_time=start_time,
                             correction_time_shift=correction_time_shift,
                             alpha_fov_apod=alpha_fov_apod,
                             bp_filter_params=filters_params,
                             envelope_detector='I_Q',
                             picmus_dataset=True,
                             channel_reduction=32)

    return bf, rf_data

def run_beamformer(bf, rf_data, active_elements):
    """
    Runs the beamformer on the specified RF data.

    Args:
        bf (object): Beamformer object.
        rf_data (numpy.ndarray): RF data.
        active_elements (list): List of active transducer elements.

    Returns:
        numpy.ndarray: Beamformed image.

    Pre-conditions:
        - The bf object is a valid beamformer object.
        - The rf_data is a valid numpy array.
        - The active_elements is a valid list of transducer elements.

    Post-conditions:
        - The returned image is the beamformed image of the specified RF data.
    """

    # Run beamformer
    img_data = bf.beamform(rf_data[:,active_elements])

    return img_data