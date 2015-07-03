import FWCore.ParameterSet.Config as cms
from RecoJets.JetProducers.hltPUIdParams_cfi import *

####################################################################################################################  
full_74x = cms.PSet(
 impactParTkThreshold = cms.double(1.) ,
 cutBased = cms.bool(False),
 tmvaWeights = cms.string("RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_2var.xml"),
 #tmvaWeights = cms.string("RecoJets/JetProducers/data/MVAJetPuID.weights.xml"),
 #tmvaWeights = cms.string("RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights.xml"),
 tmvaMethod  = cms.string("JetID"),
 version = cms.int32(-1),
 tmvaVariables = cms.vstring(
    "DRweighted"     ,
    "rho"     ,
#    "nTot"     , 
#    "nCh" , 
#    "axisMajor" , 
#    "axisMinor",	
#    "fRing0",
#    "fRing1",
#    "fRing2",
#    "fRing3",		 
#    "ptD"      , 
#    "beta"   , 
#    "betaStar"   , 
#    "DR_weighted"   , 
#    "min(pull,0.1)"   , 
#    "jetR"   , 
#    "jetRchg"	
    ),
 tmvaSpectators = cms.vstring(
    "p4.fCoordinates.fPt",
    "p4.fCoordinates.fEta",
    "nTrueInt",
    "dRMatch",
    ),
 JetIdParams = full_74x_wp,
 label = cms.string("CATEv0")
 )

