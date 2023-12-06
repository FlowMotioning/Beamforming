# Import PyBF library
import numpy as np
from scipy import signal as ss
'''
import sys, os
look here if below import doesn't work: https://stackoverflow.com/questions/7505988/importing-from-a-relative-path-in-python
'''
from ..juypter.pybf.scripts.beamformer_cartesian_realtime import BFCartesianRealTime
from ..juypter.pybf.pybf.transducer import Transducer
from ..juypter.pybf.pybf.visualization import plot_image
from ..juypter.pybf.pybf.image_settings import ImageSettings

# Load raw RF data
rf_data = np.genfromtxt('raw_data_beamforming.csv', delimiter=',')

### Specify Trancducer settings and create transducer object ###

# Transducer sttings
F_CENTRAL = 5.13 * 10 ** 6
X_ELEM = 128
X_PITCH = 0.0003
X_WIDTH = 0
Y_ELEM = 1
Y_PITCH = 0
Y_WIDTH = 0

# Set all transducer elements (channels) to be active by default
active_elements = np.arange(X_ELEM)

# Select every 2nd channels to be active
#active_elements = active_elements[::2]

#Select 64 central channels to be active
#active_elements = active_elements[32:96]

# Select 64 central channels to be active
#active_elements = active_elements[48:80]

trans = Transducer(num_of_x_elements=X_ELEM,
                   num_of_y_elements=Y_ELEM,
                   x_pitch=X_PITCH,
                   y_pitch=Y_PITCH,
                   x_width=X_WIDTH,
                   y_width=Y_WIDTH,
                   f_central_hz=F_CENTRAL,
                   bandwidth_hz=F_CENTRAL,
                   active_elements=active_elements)


### Specify Image settings and create corresponding object ###
img_res = [400, 600]
image_x_range = [-0.018, 0.018]
image_z_range = [0.000, 0.1]

LATERAL_PIXEL_DENSITY_DEFAULT = 5

img_config = ImageSettings(image_x_range[0],
                           image_x_range[1],
                           image_z_range[0],
                           image_z_range[1],
                           LATERAL_PIXEL_DENSITY_DEFAULT,
                           trans)

### Specify preprocessing parameters for RF data ###

decimation_factor = 1
interpolation_factor = 10

### Specify TX strategy and Apodization parameters ###

start_time = 0
correction_time_shift = 0

alpha_fov_apod = 40

# 1 Plane waves with inclination angle 0
tx_strategy = ['PW_1_0', [0]]

### Specify Sampling Frequency ###

SAMPLING_FREQ = 20.832 * (10 ** 6)

bp_filters_params = [1 * 10 **6, 8 * 10 **6, 0.5 * 10 **6]

# Create an instance of beamformer
bf = BFCartesianRealTime(SAMPLING_FREQ,
                         tx_strategy,
                         trans,
                         decimation_factor,
                         interpolation_factor,
                         img_res,
                         img_config,
                         start_time=start_time,
                         correction_time_shift=correction_time_shift,
                         alpha_fov_apod=alpha_fov_apod,
                         bp_filter_params=bp_filters_params)

# Run beamformer
img_data = bf.beamform(rf_data[active_elements])

# Plot image and save it.
plot_image(np.abs(img_data), 
           scatters_coords_xz=None,
           elements_coords_xz=trans.elements_coords,
           framework='matplotlib',
           title='Sample Image',
           image_x_range=image_x_range,
           image_z_range=image_z_range,
           db_range=80,
           colorscale='Greys',
           save_fig=False, 
           show=True,
           path_to_save='.')

