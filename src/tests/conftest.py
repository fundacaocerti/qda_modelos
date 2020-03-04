import pytest
import rasterio as rio


@pytest.fixture()
def setup_bands():
    prefix_20m = "tests/assets/20m/"
    suffix_20m = "_20m_20181224.tif"
    prefix_10m = "tests/assets/10m/"
    suffix_10m = "_10m_20181224.tif"

    band_01_20m = rio.open(prefix_20m + "B1" + suffix_20m).read()
    band_02_20m = rio.open(prefix_20m + "B2" + suffix_20m).read()
    band_03_20m = rio.open(prefix_20m + "B3" + suffix_20m).read()
    band_04_20m = rio.open(prefix_20m + "B4" + suffix_20m).read()
    band_05_20m = rio.open(prefix_20m + "B5" + suffix_20m).read()
    band_06_20m = rio.open(prefix_20m + "B6" + suffix_20m).read()
    band_08_20m = rio.open(prefix_20m + "B8" + suffix_20m).read()
    band_8a_20m = rio.open(prefix_20m + "B8A" + suffix_20m).read()

    band_01_10m = rio.open(prefix_10m + "B1" + suffix_10m).read()
    band_02_10m = rio.open(prefix_10m + "B2" + suffix_10m).read()
    band_03_10m = rio.open(prefix_10m + "B3" + suffix_10m).read()
    band_04_10m = rio.open(prefix_10m + "B4" + suffix_10m).read()
    band_05_10m = rio.open(prefix_10m + "B5" + suffix_10m).read()
    band_08_10m = rio.open(prefix_10m + "B8" + suffix_10m).read()

    bands = {
        "20m": {
            "B01": band_01_20m,
            "B02": band_02_20m,
            "B03": band_03_20m,
            "B04": band_04_20m,
            "B05": band_05_20m,
            "B06": band_06_20m,
            "B08": band_08_20m,
            "B8A": band_8a_20m,
        },
        "10m": {
            "B01": band_01_10m,
            "B02": band_02_10m,
            "B03": band_03_10m,
            "B04": band_04_10m,
            "B05": band_05_10m,
            "B08": band_08_10m,
        },
    }

    return bands
