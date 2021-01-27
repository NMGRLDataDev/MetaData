#===============================================================================
# EXTRACTION SCRIPT felix_air_x1_boneonly.py
#===============================================================================
'''
modifier: 02
eqtime: 30
'''

def main():
    info("Air Pipette x1-4 bone only")
    gosub('felix:WaitForMiniboneAccess')
    gosub('felix:PrepareForAirShot')
    
    #open(name='N')
    close(name='Q')
    close(name="D", description="Bone to CO2 Laser")
    close(name='B')
    
    gosub('common:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('felix:PrepareForAirShotExpansion')
    gosub('common:ExpandPipette2')
    
    #close(name='B')
    #close(name='Q')
    close(name='E')
    #close(name='D')
    #close(name='N')
    close(description='Outer Pipette 2')
    
    

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
	open(name='V', cancel_on_failed_actuation=False)
	