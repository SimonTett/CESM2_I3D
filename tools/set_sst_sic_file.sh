#!/usr/bin/env sh
# Change a CESM case to use provided SSTs
# specific to particular file.
# #arguments
# #1 start_year
# #2 end_year
# #2 file name
start_year=$1 ; shift
end_year=$1 ; shift
file=$1 ; shift
# first check file exists:.
DIR=$(./xmlquery DIN_LOC_ROOT | cut -f2 -d":" | awk '{$1=$1};1') # get value, split at colon and remove leading/trailing whitespace.
path=$DIR"/atm/cam/sst/"$file
if [[ ! -f  "$path" ]] ; then
    echo "path: $path does not exist."
    exit 1
fi
./xmlchange --id SSTICE_YEAR_ALIGN --val $start_year
./xmlchange --id SSTICE_YEAR_START --val $start_year
./xmlchange --id SSTICE_YEAR_END --val $end_year
./xmlchange --id SSTICE_DATA_FILENAME --val '$DIN_LOC_ROOT'/atm/cam/sst/$file
# NB use of ' so shell does not expand $DIN_LOC_ROOT
# show what we have changed
./xmlquery SSTICE_YEAR_START,SSTICE_YEAR_ALIGN,SSTICE_YEAR_END,SSTICE_DATA_FILENAME
