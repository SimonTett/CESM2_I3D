#!/usr/bin/env sh
# Change a CESM case to use AMIP SSTs
# specific to particualr file.
./xmlchange --id SSTICE_YEAR_ALIGN --val 2015
./xmlchange --id SSTICE_YEAR_START --val 2015
./xmlchange --id SSTICE_YEAR_END --val 2016
./xmlchange --id SSTICE_DATA_FILENAME --val '$DIN_LOC_ROOT/atm/cam/sst/blend_test.nc'
# NB use of ' so shell does not expand $DIN_LOC_ROOT
# show what we have changed
./xmlquery SSTICE_YEAR_START,SSTICE_YEAR_ALIGN,SSTICE_YEAR_END,SSTICE_DATA_FILENAME
