#!/usr/bin/env sh
# changes to a SST forced "HIST" case to make it a SST forced SSP run.
# land changes needed for CLM
./xmlchange --id CLM_NML_USE_CASE --val 1850-2100_SSP5-8.5_transient
./xmlchange --id CLM_BLDNML_OPTS  --val "-bgc bgc -crop"
# CAM changes
./xmlchange --id CAM_NML_USE_CASE --val ssp585_cam6 
./xmlchange --id CAM_NAMELIST_OPTS  --val "co2_cycle_rad_passive=.true."
echo "remember to set start date etc appropriately"

# show what we have changed
./xmlquery CLM_NML_USE_CASE,CLM_BLDNML_OPTS,CAM_NML_USE_CASE,CAM_NAMELIST_OPTS

