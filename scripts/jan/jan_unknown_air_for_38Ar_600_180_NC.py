#!Measurement
'''
baseline:
  after: true
  before: false
  counts: 180
  detector: H1
  mass: 34.2
  settling_time: 20.0
default_fits: nominal
equilibration:
  eqtime: 1.0
  inlet: R
  inlet_delay: 3
  outlet: O
  use_extraction_eqtime: true
  post_equilibration_delay: 5
multicollect:
  counts: 600
  detector: H1
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H1
  detectors:
  - H1
  - AX
  - L2
  - CDD
  integration_time: 0.262144
  isotope: Ar40
peakhop:
  generate_ic_table: false
  hops_name: ''
  ncycles: 0
  use_peak_hop: false
'''
ACTIVE_DETECTORS=('H2','H1','AX','L1','L2','CDD')
    
def main():
    info('unknown measurement script')
    set_deflection('CDD', 400)
    activate_detectors(*ACTIVE_DETECTORS)
   
    
    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    
    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)
    
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #sniff the gas during equilibration
    if mx.equilibration.use_extraction_eqtime:
        eqt = eqtime
    else:
        eqt = mx.equilibration.eqtime
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''

    equilibrate(eqtime=eqt, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet, 
               delay=mx.equilibration.inlet_delay)

    set_time_zero()
    
    sniff(eqt)    
    set_fits()
    set_baseline_fits()

    # delay to migitate 39Ar spike from inlet valve close
    sleep(mx.equilibration.post_equilibration_delay)

    #multicollect on active detectors
    multicollect(ncounts=mx.multicollect.counts, integration_time=1)
    
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector, 
                  settling_time=mx.baseline.settling_time)
    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope,
        integration_time=mx.peakcenter.integration_time)

    if use_cdd_warming:
       gosub('warm_cdd', argv=(mx.equilibration.outlet,))    
    set_deflection('CDD', 50)  
    info('finished measure script')
    