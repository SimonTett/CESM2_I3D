#!/bin/csh -f
# Modified by SFBT to have stream#1 be saved annually (rather than monthly) and
# stream#2 to be saved monthly rather than daily. All in attempt to reduce data volume
if ( $OCN_GRID =~ gx* ) then
#shut off time-invariant stream until vertical grid issues are resolved
cat >! $CASEBUILD/popconf/base.tavg.nml << EOF
tavg_freq_opt           = 'nyear'   'nmonth'   'once' 
tavg_freq               =     1         1       1   
tavg_stream_filestrings = 'nyear1'  'nmonth1'  'once' 
tavg_file_freq_opt      = 'nyear'   'nmonth' 'once' 
tavg_file_freq          =     1         1       1    
tavg_start_opt          = 'nstep'    'nstep'  'nstep'
tavg_start              =     0         0       0    
tavg_fmt_in             = 'nc'       'nc'      'nc' 
tavg_fmt_out            = 'nc'       'nc'      'nc' 
ltavg_has_offset_date   = .false.    .false.  .false.
tavg_offset_years       =     1         1       1    
tavg_offset_months      =     1         1       1    
tavg_offset_days        =     2         2       2    
ltavg_one_time_header   = .false.    .false.  .false.
EOF
endif

if ( $OCN_GRID =~ tx* ) then
cat >! $CASEBUILD/popconf/base.tavg.nml << EOF
tavg_freq_opt           = 'nmonth'     'nday'   
tavg_freq               =     1          1      
tavg_stream_filestrings = 'nmonth1'    'nday1'  
tavg_file_freq_opt      = 'nmonth'     'nmonth' 
tavg_file_freq          =     1          1       
tavg_start_opt          = 'nstep'      'nstep' 
tavg_start              =     0          0       
tavg_fmt_in             =   'nc'        'nc'    
tavg_fmt_out            =   'nc'        'nc'    
ltavg_has_offset_date   = .false.      .false.  
tavg_offset_years       =     1          1       
tavg_offset_months      =     1          1       
tavg_offset_days        =     2          2       
ltavg_one_time_header   = .false.      .false.  
EOF
endif

