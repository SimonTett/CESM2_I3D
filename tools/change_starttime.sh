#!/usr/bin/env sh
# Change a CESM case to have a different starttime.
# This does nothing else than set the start time and ref time

date=$1 ; shift
./xmlchange --id RUN_TYPE --val startup
./xmlchange --id RUN_REFDATE --val $date
./xmlchange --id RUN_STARTDATE --val $date
# show what we have changed
./xmlquery RUN_TYPE,RUN_REFDATE,RUN_STARTDATE
