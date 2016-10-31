#===============================================================================
# EXTRACTION SCRIPT jan_co2.py
#===============================================================================
'''
eqtime: 12
'''
def main():
    info('Jan CO2 laser analysis')
    gosub('jan:WaitForCO2Access')
    gosub('jan:PrepareForCO2Analysis')

    set_motor('beam',beam_diameter)

    if analysis_type=='blank':
        info('is blank. not heating')
        '''
        sleep cumulative time to account for blank
        during a multiple position analysis
        '''
        close(description='Microbone to Turbo')
        numPositions=len(position)

        sleep(duration*max(1,numPositions))
    else:

        '''
        this is the most generic what to move and fire the laser
        position is always a list even if only one hole is specified
        '''

        for i,pi in enumerate(position):
            '''
            position the laser at pi, pi can be an holenumber or (x,y)
            '''
            move_to_position(pi, autocenter=True)
            if i==0:
                sleep(5)
                close(description='Microbone to Turbo')

            do_extraction()
            if disable_between_positions:
                end_extract()
        end_extract()
        disable()

    sleep(cleanup)


def do_extraction():
    info('enable laser')
    enable()
    if ramp_duration>0:
        '''
        style 1.
        '''
#               begin_interval(duration)
#               info('ramping to {} at {} {}/s'.format(extract_value, ramp_rate, extract_units)
#               ramp(setpoint=extract_value, duration=ramp_duration)
#               complete_interval()
        '''
        style 2.
        '''
        elapsed=ramp(setpoint=extract_value, duration=ramp_duration)
        pelapsed=execute_pattern(pattern)
        sleep(max(0, duration-elapsed-pelapsed))

    else:

        info('begin interval')
        begin_interval(duration)

        info('set extract to {}'.format(extract_value))
        extract(extract_value)
        #sleep(2)

        if pattern:
            info('executing pattern {}'.format(pattern))
            execute_pattern(pattern)

        complete_interval()

#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O')
    