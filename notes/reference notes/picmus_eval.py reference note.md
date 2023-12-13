# Reference Note: Of code in [picmus_eval.py](../../juypter/pybf/scripts/picmus_eval.py)

- one single class: `PicmusEval`
- function `evaluate_FWHM`: evaluates the full width at half maximum
- function `evaluate_circ_contrast`: obtains the CNS (contrast to noise ratio) from defined circles. 
    - argument `cirles` is numpy array defining the center and radius of circles
- function `evaluate_rect_contrast`: does what upper function does, but with rectangles
- function `_resolution_el`: helper function that does all the "backstage" work to obtain the two numbers for FWHM in x and in y direction