#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:36:19 2024

@author: tetts_ta167
Plot the discolved inorganic, disolved organinc and total dissolved carbon in the ocean. 
Values are all converted to Pg in each model layer.
"""

import xarray
import matplotlib.pyplot as plt
import pathlib

tot=dict() # where we store the totals
# read in an ocean file.
file = pathlib.Path('/work/ta167/ta167/tetts_ta167/cesm/archive/SSP585_example/ocn/hist/SSP585_example.pop.h.2024.nc')
ds= xarray.open_dataset(file)
z = ds.z_t/100 # convert to m

# wts are converted from cm^3 to m^3
wts = ds.TAREA*ds.dz/1e6
# and to convert to g multiplied by 12.01e-3 as Units are *I think* mmol C per m^3
mass_c = 12.0e-3/1e15 # conversion for mmol C to petagrams C
total_dic = ds.DIC.weighted(wts).sum(['nlat','nlon'])*mass_c # Disolved inorganic carbon. 
total_doc =ds.DOC.weighted(wts).sum(['nlat','nlon'])*mass_c
total_dic = total_dic.assign_coords(z_t=z) # overwrite the cm corrds with meter coords
total_doc = total_doc.assign_coords(z_t=z) # overwrite the cm corrds with meter coords
total_dc = total_dic+total_doc
tot['DIC']=float(total_dic.sum())
tot['DOC']=float(total_doc.sum())
tot['total_ocean_carbon']=float(total_dc.sum())
fig,ax = plt.subplots(nrows=1,ncols=1,num='Ocean_carbon',layout='constrained',clear=True)
total_dic.plot(y='z_t',yincrease=False,label=f'DIC {total_dic.sum():5.0f} Pg',ax=ax)
total_doc.plot(y='z_t',yincrease=False,label=f'DOC  {total_doc.sum():5.0f} Pg',ax=ax)
total_dc.plot(y='z_t',yincrease=False,label=f'DC  {total_dc.sum():5.0f} Pg',ax=ax)
ax.set_ylabel('Depth (m)')
ax.legend()
ax.set_title(f'Total Carbon (Pg)')
ax.set_xlabel('Pg Carbon')
fig.show()
## then get the land carbon.
# In the h4 files land is 'packed' -- only land units are shown
# so we need to convert the area to that which do by selection
# and then weight by landunit


land_file = pathlib.Path('/work/ta167/ta167/tetts_ta167/cesm/archive/SSP585_example/lnd/hist/SSP585_example.clm2.h4.2025-01-01-00000.nc')
ds_land= xarray.open_dataset(land_file)
total_carbon = 0.0
area = ds_land.area.fillna(0.0)*1e6
lon = ds_land.land1d_lon
lat = ds_land.land1d_lat
wt = area.sel(lon=lon,lat=lat,method='nearest',tolerance=1e-3) 

for var in ['TOTLITC','TOTSOMC','TOTVEGC']:
    # convert to total pG. Scale by area in km2 * 1e6/1e15 (units are gC/m^2)
    total_carbon += ds_land[var]
    tot[var]=float(ds_land[var].weighted(wt).sum(['landunit']))/1e15 

tot['total_land_carbon']=float(total_carbon.weighted(wt).sum('landunit')/1e15)
for key,value in tot.items():
    print(f'{key}: {value:5.0f} PgC')


