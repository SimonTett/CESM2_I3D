
import matplotlib.pyplot as plt # matplotlib library
import xarray # xarray
import numpy as np # numpy
import cartopy.crs as ccrs # cartopy projections

xarray.set_options(keep_attrs=True) # keep attributes when doing arithmetic. 

file="/work/ta167/ta167/tetts_ta167/cesm/archive/SSP585_example/atm/hist/SSP585_example.cam.h1.2024-01-01-00000.nc"
ds=xarray.open_dataset(file) # daily data -- open => only have metadata


levels = np.arange(940,1038.,8) # levels for plotting. 2x normal pressure diffs

 
fig = plt.figure(figsize=[11,8],clear=True,num='pressure')

time_index = [0,9] # 1st day and 9th day
ntime= len(time_index)
for count_time,time_indx in enumerate(time_index): 
    dataArray=ds.PSL.isel(time=time_indx).load()
    # get a sea level pressure field. 
    projections=[ccrs.PlateCarree(),ccrs.NorthPolarStereo()] # projections to use.
    nproj = len(projections)
    for count,proj in enumerate(projections):
        ax=fig.add_subplot(ntime,2,(count+1)+count_time*nproj,projection=proj)
        if isinstance(proj,ccrs.NorthPolarStereo):
        # Limit the map to 30 degrees latitude and above
            ax.set_extent([-180, 180, 30, 90], ccrs.PlateCarree())
        cm=(dataArray/100.).plot(levels=levels, ax=ax,transform=ccrs.PlateCarree(),
                                 cbar_kwargs=dict(orientation='horizontal'),
                                 # make colour bar horizontal
                             ) 
        cs=(dataArray/100.).plot.contour(levels=levels, 
                                         linestyles='solid',colors='white',
                                         ax=ax,transform=ccrs.PlateCarree(),)
        # make colour plot
        # overlay contours
        ax.clabel(cs,cs.levels,inline=True,fmt="%d",fontsize=8) # add contour labels
        ax.gridlines()
        ax.coastlines(linewidth=2,color='red')
fig.show()
fig.savefig("pressure.png")
