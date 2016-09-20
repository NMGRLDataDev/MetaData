#===============================================================================
# EXTRACTION SCRIPT jan_MS_Dynamic.py
#===============================================================================
'''
modifier: 01

'''
def main():
    info('Jan MS dynamic blank')
    gosub('jan:PrepareForMSdynamicAnalysis')
 
#===============================================================================
# POST MEASUREMENT SCRIPT jan_pump_ms.py
#===============================================================================
def main():
    info('Pumping spectrometer')
    open(name='O')
    