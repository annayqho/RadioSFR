""" 
From the SFR of a galaxy, estimate the radio luminosity
at any frequency in GHz

Equation from Murphy et al. (2011)
"""

import numpy as np


def get_lum(sfr, nu):
    """ 
    sfr: solar masses per year
    nu: frequency of observation in GHz
    """
    # 1.4 GHz luminosity
    L_14GHz = 1.57E28 * (sfr)

    # assuming spectral index of -0.7
    lum = L_14GHz * (nu/1.4)**(-0.7)

    return lum
