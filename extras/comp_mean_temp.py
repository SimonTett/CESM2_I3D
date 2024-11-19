# make a plot of temperatures from CESM cases.
# Will also plot carbon...

import xarray
import numpy as np
import matplotlib.pyplot as plt
import pathlib

# get the cases
file='TREFHT.nc'
vars = ['TREFHT','SO2_SRF','SFCO2']
dir_path = pathlib.Path('/work/ta167/ta167/tetts_ta167/extract_data')
fig,axs = plt.subplots(nrows=1,ncols=len(vars),clear=True,
                           layout='constrained',figsize=(8,6),num='cesm_ts')


for var,ax in zip(vars,axs.flatten()):
    noso2_files=list(pathlib.Path().\
                     glob(f'noso2_*/*_{var}.nc'))
    ssp585_files=list(dir_path.glob(f'SSP585_example_[0-9]_{var}.nc'))
    noso2_files=list(dir_path.glob(f'SSP585_noso2_[0-9]_{var}.nc'))
    ds_noso2=xarray.open_mfdataset(noso2_files,combine='nested',
                                   concat_dim='ensemble')
    ds_ssp585=xarray.open_mfdataset(ssp585_files,combine='nested',
                                    concat_dim='ensemble')
    wts = np.cos(np.deg2rad(ds_noso2.lat))
    ts_noso2=ds_noso2[var].weighted(wts).mean(['lon','lat']).resample(time='YS').mean().load()
    ts_ssp585=ds_ssp585[var].weighted(wts).mean(['lon','lat']).resample(time='YS').mean().load()
    if var in ['SO2']:
        ts_noso2=ts_noso2.isel(lev=-1)# bottom level
        ts_ssp585=ts_ssp585.isel(lev=-1)# bottom level

    ts_noso2.plot.line(ax=ax,x='time',linewidth=2,label='NoSO2')
    ts_ssp585.plot.line(ax=ax,x='time',linestyle='dashed',linewidth=2,label='SSP585')
    ax.set_title(f'{var}')
fig.show()
fig.savefig('results.png')


print(noso2_files)


