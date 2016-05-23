#===============================================================================
# EXTRACTION SCRIPT felix_furnace.py
#===============================================================================
'''
eqtime: 15
'''

OFFSET = 250

def main():
    start_response_recorder()
    info('Felix unknown furnace analysis')

    # prepare bone for furnace analysis
    close('F')
    open('D')
    
    # isolate furnace from bone
    close('J')
    close('FC')

    # open furnace to furnace stage
    open('FH')
    if analysis_type=='blank':
        info('Blank Analyis. Not heating Furnace')
        sleep(duration)
    else:
        info('Furnace enabled. Heating sample.')

        '''
        this is the most generic way to move and fire the laser
        position is always a list even if only one hole is specified
        '''
        enable()
        # for pi in position:
#             ''' 
#             position the laser at pi, pi can be an holenumber or (x,y)
#             '''
#             move_to_position(pi)
#             dump_sample()
        
        do_extraction()
        
        info("Furnace disabled.")
        
      
    #gosub('felix:EquilibrateThenIsolateDiodeColdfinger')    
    
    # furnace cool down before transfer
    sleep(60)
    
    # prepare bone for transfer
    close('B')
    close('E')
    close('C')
    
    sleep(2)
    
    # equilibrate furnace
    open('J')
    sleep(30)
    close('J')
    open('FC')
    
    sleep(cleanup)
    stop_response_recorder()

def do_extraction():
    
    set_pid_parameters(extract_value)
    
    if ramp_rate>0:
        '''
        style 1.
        '''
        #               begin_interval(duration)
        #               info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units)
        #               ramp(setpoint=extract_value, rate=ramp_rate)
        #               complete_interval()
        '''
        style 2.
        '''
        elapsed=ramp(setpoint=extract_value, rate=ramp_rate)
        pelapsed=execute_pattern(pattern)
        sleep(min(0, duration-elapsed-pelapsed))

    else:
        begin_interval(duration)
        
        info('set extract to {} ({})'.format(extract_value, extract_units))
        extract()
        sleep(2)
        complete_interval()
        
        if extract_value >= 1300:
            disable()
        else:
            extract(max(0, extract_value-OFFSET))

#===============================================================================
# POST EQUILIBRATION SCRIPT felix_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')
    gosub('felix:PumpBone')
    if get_resource_value(name='FelixMiniboneFlag'):
        gosub('felix:PumpMinibone')
#===============================================================================
# POST MEASUREMENT SCRIPT felix_pump_ms.py
#===============================================================================
def main():
	info('Pumping spectrometer')
	open(name='V')
	