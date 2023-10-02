#!/usr/bin/env sh
# changes to a SST forced "HIST" case to give it 1850 forcings
# land changes needed for CLM
./xmlchange --id CLM_NML_USE_CASE --val 1850_control
# CAM changes
./xmlchange --id CAM_NML_USE_CASE --val 1850_cam6 
./xmlchange --id CAM_NAMELIST_OPTS  --val "co2_cycle_rad_passive=.true."
echo "remember to set start date etc appropriately"

# show what we have changed
./xmlquery CLM_NML_USE_CASE,CLM_BLDNML_OPTS,CAM_NML_USE_CASE,CAM_NAMELIST_OPTS

