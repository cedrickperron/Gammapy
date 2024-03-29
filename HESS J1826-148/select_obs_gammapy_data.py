
import astropy.units as u
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.time import Time
from regions import CircleSkyRegion
from astropy.coordinates import Angle

import logging

log = logging.getLogger(__name__)


from gammapy.data import DataStore
from gammapy.datasets import SpectrumDataset
from gammapy.modeling.models import PowerLawSpectralModel, SkyModel
from gammapy.maps import MapAxis
from gammapy.estimators import LightCurveEstimator
from gammapy.makers import (
    SpectrumDatasetMaker,
    ReflectedRegionsBackgroundMaker,
    SafeMaskMaker,
)


data_store = DataStore.from_dir("GAMMAPY/Gammapy-data/gammapy-datasets/hess-dl3-dr1/")


target_position = SkyCoord(
    329.71693826 * u.deg, -30.2255890 * u.deg, frame="icrs"
)
selection = dict(
    type="sky_circle",
    frame="icrs",
    lon=target_position.ra,
    lat=target_position.dec,
    radius=2 * u.deg,
)
obs_ids = data_store.obs_table.select_observations(selection)["OBS_ID"]
observations = data_store.get_observations(obs_ids)
print(obs_ids)
print(f"Number of selected observations : {len(observations)}")


t0 = Time("2006-07-29T20:30")
duration = 3* u.min
n_time_bins = 35
times = t0 + np.arange(n_time_bins) * duration
time_intervals = [
    Time([tstart, tstop]) for tstart, tstop in zip(times[:-1], times[1:])
]
#print(time_intervals[0].mjd)

#short_observations = observations.select_time(time_intervals)
"""
# check that observations have been filtered
print(
    f"Number of observations after time filtering: {len(short_observations)}\n"
)

# Target definition
e_reco = MapAxis.from_energy_bounds(0.4, 20, 10, "TeV")
e_true = MapAxis.from_energy_bounds(0.1, 40, 20, "TeV", name="energy_true")

on_region_radius = Angle("0.11 deg")
on_region = CircleSkyRegion(center=target_position, radius=on_region_radius)

dataset_maker = SpectrumDatasetMaker(
    containment_correction=True, selection=["counts", "exposure", "edisp"]
)
bkg_maker = ReflectedRegionsBackgroundMaker()
safe_mask_masker = SafeMaskMaker(methods=["aeff-max"], aeff_percent=10)

datasets1 = []

dataset_empty = SpectrumDataset.create(
    e_reco=e_reco, e_true=e_true, region=on_region
)

for obs in observations:
    dataset = dataset_maker.run(dataset_empty.copy(), obs)

    dataset_on_off = bkg_maker.run(dataset, obs)
    dataset_on_off = safe_mask_masker.run(dataset_on_off, obs)
    datasets1.append(dataset_on_off)

spectral_model = PowerLawSpectralModel(
    index=3.4, amplitude=2e-11 * u.Unit("1 / (cm2 s TeV)"), reference=1 * u.TeV
)
spectral_model.parameters["index"].frozen = False

sky_model = SkyModel(
    spatial_model=None, spectral_model=spectral_model, name="pks2155"
)

for dataset in datasets:
    dataset.models = sky_model

"""


