#===============================================================================
# EXTRACTION SCRIPT jan_cocktail_x1_microbone only.py
#===============================================================================
'''
modifier: 03
eqtime: 12
'''
def main():
    info("Jan Cocktail Pipette x1")
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    open(name="T", description="Microbone to CO2 Laser")
    gosub('jan:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('jan:PrepareForAirShotExpansion')  
    gosub('common:ExpandPipette1')
    sleep(duration=3.0)
    close(name="T", description="Microbone to CO2 Laser")
    close(name="L", description="Microbone to Minibone")
    sleep(duration=2.0)
#===============================================================================
# POST EQUILIBRATION SCRIPT jan_pump_extraction_line.py
#===============================================================================
def main():
    info('Pump after analysis')

    if extract_device=="FusionsDiode":
        info('Pump after Jan diode analysis')
        gosub('jan:PumpMicroBoneAfterDiodeAnalysis')
        gosub('jan:PumpMiniboneAfterDiodeAnalysis')
    else:
        gosub('jan:PumpMicrobone')
        v=get_resource_value(name='JanMiniboneFlag')
        info('get resource value {}'.format(v))
        if v:
            info('Pumping Minibone')
            gosub('jan:PumpMinibone')
        else:
            info('Not Pumping Minibone')

#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O', cancel_on_failed_actuation=False)
    
