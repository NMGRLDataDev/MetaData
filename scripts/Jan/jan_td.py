#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 2
  detector: H1
  mass: 39.59
default_fits: nominal
equilibration:
  eqtime: 3
  inlet: R
  inlet_delay: 1
  outlet: S
  use_extraction_eqtime: false
multicollect:
  counts: 2
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  isotope: Ar40
peakhop:
  hops_name: hop
  use_peak_hop: true

'''
ACTIVE_DETECTORS=('H2','H1','AX','L1','L2', 'CDD')

def main():
    #this is a comment
    '''
        this is a multiline
        comment aka docstring
    '''

    # #open a plot panel for this detectors
    # activate_detectors(*ACTIVE_DETECTORS)
    #
    # #position mass spectrometer
    # position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)
    #
    # #gas is staged behind inlet
    #
    # #post equilibration script triggered after eqtime elapsed
    # #equilibrate is non blocking
    # #so use either a sniff of sleep as a placeholder until eq finished
    # if mx.equilibration.use_extraction_eqtime:
    #     e = ex.eqtime
    # else:
    #     e = mx.equilibration.eqtime
    #
    # equilibrate(eqtime=e, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet)
    #
    # #equilibrate returns immediately after the inlet opens
    # set_time_zero()
    #
    # sniff(e)
    # #measurement_delay(100)
    # #set default regression
    # set_fits()
    # set_baseline_fits()
    #
    # multicollect(ncounts=mx.multicollect.counts, integration_time=1)
    #
    # if mx.baseline.after:
    #     baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector)
    #
    # info('peak center after {}'.format(mx.peakcenter.after))
    # if mx.peakcenter.after:
    #     peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    info('finished measure script')

#========================EOF==============================================================
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)
    #baselines(counts=50,mass=0.5, detector='CDD')s

#isolate sniffer volume
    # close('S')
#     sleep(1)
#
#     #open to mass spec
#     open('R')
#
#     set_time_zero()
#     #display pressure wave
#     sniff(5)
#
#     #define sniff/split threshold
#     sniff_threshold=100
#
#     #test condition
#     #if get_intensity('H1')>sniff_threshold:
#     if True:
#         gosub('splits:jan_split', klass='ExtractionLinePyScript')
#
