    """
    If you have xarray package installed on your machine this should be pretty straight foreward.
    If not you can run `conda install xarray` or `pip install xarray`

    Put the netcdf files in a folder named data in the same folder as this one.
    """

import xarray as xr # This is the only package that needs to be imported

# Load Data #
fname = "./data/m1_ocr_Ed10_std.nc"
ds = xr.open_dataset(fname)
print(ds) # View the dataset if using a jupyter notebook

# The downwelling data has some extra dimensions: latitude, longitude, depth, which are all fixed, so we want to flattened them.
ds_short = ds.isel(latitude=0,longitude=0,depth=0) # This just squeezes the data from (n, 1, 1, 1, m) to (n, m)
ds_short['ocean_downwelling_irradiance_10m'].isel(time=0).plot() # plot the first time for sanity

# Convert the data to a pandas data_frame
df = ds_short['ocean_downwelling_irradiance_10m'].to_pandas()
print(df.head())

# Write the data to a csv
df.to_csv("m1_downwelling_std.csv")