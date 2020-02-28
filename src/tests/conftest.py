import pytest
import rasterio as rio


@pytest.fixture()
def setup_bands():
    prefix_20m = "tests/assets/20m/"
    suffix_20m = "_20m_20181224.tif"
    prefix_10m = "tests/assets/10m/"
    suffix_10m = "_10m_20181224.tif"

    B01_20m = rio.open(prefix_20m + "B1" + suffix_20m).read()
    B02_20m = rio.open(prefix_20m + "B2" + suffix_20m).read()
    B03_20m = rio.open(prefix_20m + "B3" + suffix_20m).read()
    B04_20m = rio.open(prefix_20m + "B4" + suffix_20m).read()
    B05_20m = rio.open(prefix_20m + "B5" + suffix_20m).read()
    B06_20m = rio.open(prefix_20m + "B6" + suffix_20m).read()
    B08_20m = rio.open(prefix_20m + "B8" + suffix_20m).read()
    B8A_20m = rio.open(prefix_20m + "B8A" + suffix_20m).read()

    B01_10m = rio.open(prefix_10m + "B1" + suffix_10m).read()
    B02_10m = rio.open(prefix_10m + "B2" + suffix_10m).read()
    B03_10m = rio.open(prefix_10m + "B3" + suffix_10m).read()
    B04_10m = rio.open(prefix_10m + "B4" + suffix_10m).read()
    B05_10m = rio.open(prefix_10m + "B5" + suffix_10m).read()
    B08_10m = rio.open(prefix_10m + "B8" + suffix_10m).read()

    bands = {
        "20m": {
            "B01": B01_20m,
            "B02": B02_20m,
            "B03": B03_20m,
            "B04": B04_20m,
            "B05": B05_20m,
            "B06": B06_20m,
            "B08": B08_20m,
            "B8A": B8A_20m,
        },
        "10m": {
            "B01": B01_10m,
            "B02": B02_10m,
            "B03": B03_10m,
            "B04": B04_10m,
            "B05": B05_10m,
            "B08": B08_10m,
        },
    }

    return bands
