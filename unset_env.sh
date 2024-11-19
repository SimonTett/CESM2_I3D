# Script to un  environment
if [[ ! -z "${CESM_EXTRAS}" ]]
then
    deactivate # decative the env first
    modules="cray-python tk tcl cdo ncview"
    for module in $modules ; do
	module unload $module
    done
    unset CESM_EXTRAS
    echo "Env all removed"
else
        echo "Nothing to unload as CESM_EXTRAS not set"
fi

