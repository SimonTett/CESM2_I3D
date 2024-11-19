# plot SLP from two ensembles and the RMS difference between them.
import matplotlib.pyplot as plt # matplotlib library
import xarray # xarray
import numpy as np # numpy
import cartopy.crs as ccrs # cartopy projections
import pathlib

xarray.set_options(keep_attrs=True) # keep attributes when doing arithmetic. 
base_dir=pathlib.Path("/work/ta167/ta167/tetts_ta167/cesm/archive/")
files1=sorted((base_dir/"SSP585_example/atm/hist/").glob("SSP585_example.cam.h1.2024*.nc"))
files2=sorted((base_dir/"SSP585_case_a/atm/hist/").glob("SSP585_case_a.cam.h1.2024*.nc"))
# show open_mfdataset -- multiple files
ds1=xarray.open_mfdataset(files1) # daily data -- open => only have metadata
ds2=xarray.open_mfdataset(files2) # daily data -- open => only have metadata

# compute mean square difference -- variance
delta=((ds1.PSL-ds2.PSL)/100).weighted(ds1.gw).var(['lon','lat']).load()
# compute square root of 10 day rolling mean
ts=np.sqrt(delta.rolling(time=10,center=True).mean())
# compute monthly-mean over all months using groupby.
ts_mm = np.sqrt(delta.groupby('time.month').mean())
fig,axes=plt.subplots(nrows=2,ncols=1,num='pressure_rms',
                    clear=True,figsize=[8,11])
ts.plot(ax=axes[0])
ts_mm.plot(ax=axes[1])
fig.suptitle("RMS pressure difference")
fig.show()
fig.savefig("pressure_rms_!0day.png")

