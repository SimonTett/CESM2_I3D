#!/usr/bin/env sh
# modify a std CESM case to run for N months.
# std cases are 5 day runs in the short Q
# Changes STOP_N, STOP_OPTION,CONTINUE_RUN, JOB_WALLCLOCK_TIME and JOB_QUEUE
# Takes the following arguments:
# #1 the number of months to run for.
# sets Q limit to 12 hours so do not go over about 1.5 years x no of nodes.
nMonths=$1 ; shift
./xmlchange --id STOP_N --val $nMonths
./xmlchange --id STOP_OPTION --val nmonths
./xmlchange --id CONTINUE_RUN --val TRUE
./xmlchange --subgroup case.run --id JOB_WALLCLOCK_TIME  --val 12:00:00
./xmlchange --subgroup case.run --id JOB_QUEUE --val standard
# show what we have changed.
./xmlquery STOP_N,STOP_OPTION,CONTINUE_RUN,JOB_WALLCLOCK_TIME,JOB_QUEUE
echo "Set CONTINUE_RUN if you want to run on"
