#===============================================================================
# EXTRACTION SCRIPT jan_cocktail_x1.py
#===============================================================================
'''
modifier: 02
eqtime: 15
'''
def main():
    info("Jan Cocktail Pipette x1")
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    gosub('jan:EvacPipette1')
    gosub('common:FillPipette1')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette1')

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
        if get_resource_value(name='JanMiniboneFlag'):
            gosub('jan:PumpMinibone')