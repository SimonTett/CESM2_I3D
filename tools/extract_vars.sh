#!/bin/bash
# extract variables from input list of files.
# Time coords are shifted to the 15th of the month rather than the end of the
# month as CAM generates them. Technically this should be the middle of the month which means time-dependant shifts.
module load cdo
root_name=$1; shift
files=$*
# variables to extract.
variables="ACTREI ACTREL AODVIS CLOUD  DMS FLNT FSNT H2O PRECT RELHUM SO2 T U10 TREFHT TREFHTMX TREFHTMN" 
for variable in $variables
do
    output_file=$root_name"_"$variable".nc"
    echo "Processing $variable and sending it to $output_file"
    cmd="cdo -w shifttime,15days -shifttime,-1months -select,name=$variable $files $output_file"
    result=$($cmd)
    status=$?
    if [[ $status != 0 ]]
    then
	echo "Cmd $cmd failed with status $status and result $result"
	exit 1
    fi
done
    
