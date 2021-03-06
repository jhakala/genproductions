import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'SoftQCD:singleDiffractive = on',
            'SoftQCD:doubleDiffractive = on',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tauMax = 10',
            'Tune:pp 5',
            'Tune:ee 3',
            'ContactInteractions:QCffbar2eebar = on',
            'PhaseSpace:mHatMin = 800'
            'ContactInteractions:Lambda = 22000',
            'ContactInteractions:etaLL = 0',
            'ContactInteractions:etaRR = -1',
            'ContactInteractions:etaLR = 0',
       ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
    )
)
