#!/usr/bin/env sh
# Change a CESM case to use AMIP SSTs
# specific to particular file.
./xmlchange --id SSTICE_YEAR_ALIGN --val 2010
./xmlchange --id SSTICE_YEAR_START --val 2010
./xmlchange --id SSTICE_YEAR_END --val 2021
./xmlchange --id SSTICE_DATA_FILENAME --val '$DIN_LOC_ROOT/atm/cam/sst/bcs_input4MIPs_SSTsAndSeaIce_CMIP_PCMDI-AMIP-1-1-8_gn_201001-202112_0.9x1.25.nc'
# NB use of ' so shell does not expand $DIN_LOC_ROOT
# show what we have changed
./xmlquery SSTICE_YEAR_START,SSTICE_YEAR_ALIGN,SSTICE_YEAR_END,SSTICE_DATA_FILENAME
