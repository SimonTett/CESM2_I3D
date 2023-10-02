#!/usr/bin/env sh
# modify a CESM case to run for 5 days in the short Q
# std cases are 5 day runs in the short Q
# Changes STOP_N, STOP_OPTION, CONTINUE_RUN, JOB_WALLCLOCK_TIME and JOB_QUEUE
./xmlchange --id STOP_N --val 5
./xmlchange --id STOP_OPTION --val ndays
./xmlchange --id CONTINUE_RUN --val FALSE
./xmlchange --subgroup case.run --id JOB_WALLCLOCK_TIME  --val 00:20:00
./xmlchange --subgroup case.run --id JOB_QUEUE --val short
# show what we have changed.
./xmlquery STOP_N,STOP_OPTION,CONTINUE_RUN,JOB_WALLCLOCK_TIME,JOB_QUEUE
