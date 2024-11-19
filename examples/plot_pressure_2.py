# plot SLP from two ensembles and the RMS difference between them.
import matplotlib.pyplot as plt # matplotlib library
import xarray # xarray
import numpy as np # numpy
import cartopy.crs as ccrs # cartopy projections

xarray.set_options(keep_attrs=True) # keep attributes when doing arithmetic. 
base_dir="/work/ta167/ta167/tetts_ta167/cesm/archive/" 
file=base_dir+"SSP585_example/atm/hist/SSP585_example.cam.h1.2024-01-01-00000.nc"
file2=base_dir+"SSP585_case_a/atm/hist/SSP585_case_a.cam.h1.2024-01-01-00000.nc"

ds1=xarray.open_dataset(file) # daily data -- open => only have metadata
ds2=xarray.open_dataset(file2) # daily data -- open => only have metadata

levels = np.arange(940,1038.,8) # levels for plotting. 2x normal pressure diffs
time_index = [0,9] # 1st day and 10th day
dataArray = xarray.concat([ds1.PSL,ds2.PSL],dim='ensemble')
# facet plot.
facet = (dataArray.isel(time=time_index)/100.).plot(
               x='lon',y='lat',
               figsize=[11,8],
               row='ensemble',col='time',
               add_colorbar=True,
               cbar_kwargs=dict(orientation='horizontal',
                                fraction=0.075,pad=0.05,shrink=0.75),
               levels=levels,
               transform=ccrs.PlateCarree(),
               subplot_kws=dict(projection=ccrs.NorthPolarStereo()))
# makes a "facet plot" of pressure.
# Now to add contours, coastlines and focus on NH mid-lats
# add contour lines
fg=facet.map_dataarray(xarray.plot.contour,levels=levels,
                       x='lon',y='lat',
                       add_colorbar=False,
                       transform=ccrs.PlateCarree(),
                       colors='white',linestyles='solid')
for ax in facet.axs.flatten(): # iterate over all axes.
    ax.set_extent([-180, 180, 30, 90], ccrs.PlateCarree())
    ax.gridlines()
    ax.coastlines(linewidth=2,color='red')


# put a colour bar on the entire figure (as all levels the same)
#facet.add_colorbar(orientation='horizontal')
facet.fig.show()
facet.fig.savefig("pressure2.png")


# plot RMS difference which is the weighted std dev
ts=((ds1.PSL-ds2.PSL)/100).weighted(ds1.gw).std(['lon','lat']).load()

fig=plt.figure(num='pressure_rms')
ts.plot()
plt.title("RMS pressure difference")
fig.show()
fig.savefig("pressure_rms.png")
