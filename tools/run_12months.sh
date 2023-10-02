#!/usr/bin/env sh
# modify a std CESM case to run for 12 months.
# std cases are 5 day runs in the short Q
# Changes STOP_N, STOP_OPTION, CONTINUE_RUN, JOB_WALLCLOCK_TIME and JOB_QUEUE
./xmlchange --id STOP_N --val 12
./xmlchange --id STOP_OPTION --val nmonths
./xmlchange --id CONTINUE_RUN --val TRUE
./xmlchange --subgroup case.run --id JOB_WALLCLOCK_TIME  --val 09:00:00
./xmlchange --subgroup case.run --id JOB_QUEUE --val standard
# show what we have changed.
./xmlquery STOP_N,STOP_OPTION,CONTINUE_RUN,JOB_WALLCLOCK_TIME,JOB_QUEUE
