#===============================================================================
# EXTRACTION SCRIPT jan_sniffair_x1_split_with_getter.py
#===============================================================================
'''
modifier: 01
eqtime: 8
'''
def main():
    info("Jan Air Sniff Pipette x1")
    gosub('jan:WaitForMiniboneAccess')
    gosub('jan:PrepareForAirShot')
    open(name="Q", description="Quad Inlet")
    gosub('jan:EvacPipette2')
    gosub('common:FillPipette2')
    gosub('jan:PrepareForAirShotExpansion')
    gosub('common:SniffPipette2')
    open(name="S", description="Microbone to Inlet Pipette")
    sleep(duration=2.0)
    close(name="M", description="Microbone to Getter NP-10")
    sleep(duration=2.0)
    open(name="U", description="Microbone to Turbo")
    close(name="L", description="Microbone to Minibone")
    sleep(duration=20.0)
    close(name="U", description="Microbone to Turbo")
    sleep(duration=3.0)
    open(name="M", description="Microbone to Getter NP-10")
    sleep(duration=10.0)
    close(name="S", description="Microbone to Inlet Pipette")
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
    open(name='O')
    