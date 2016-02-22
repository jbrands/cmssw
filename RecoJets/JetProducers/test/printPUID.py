import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()
 
from DataFormats.FWLite import Handle, Events
from PhysicsTools.HeppyCore.utils.deltar import deltaR

jets, jetLabel = Handle("std::vector<pat::Jet>"), "patJetsAK4PFCHS"
puid, puidLabel = Handle("edm::ValueMap<StoredPileupJetIdentifier>"), "pileupJetIdCalculator"                                                                                                      
genjets, genjetLabel = Handle("std::vector<reco::GenJet>"), "patJetsAK4PFCHS"        
events = Events("file://testJetTools_0220.root")

f = open('training76X.txt','w')
for iev,event in enumerate(events):
    #if iev >= 10: break 
    event.getByLabel(jetLabel, jets)
    event.getByLabel(puidLabel, puid)               
    #event.getByLabel(genjetLabel, genjets)

    print "\nEvent %d: run %6d, lumi %4d, event %12d" % (iev,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event()) 
    # Jets (standard AK4)
    for i,j in enumerate(jets.product()):
        if j.pt() < 20: continue
        try: pdgId=j.genParton().pdgId()
        except: pdgId=0
        #try: genJetMatch=j.genJet().pt()>30
        try: genJetMatch=deltaR(j.genJet().eta(),j.genJet().phi(),j.eta(),j.phi())<0.2
        except: genJetMatch=0
        try: genPuJetMatch=deltaR(j.genJet().eta(),j.genJet().phi(),j.eta(),j.phi())<0.5 #and deltaR(j.genJet().eta(),j.genJet().phi(),j.eta(),j.phi())>0.2
        except: genPuJetMatch=0
        #print dir(puid.product().get(i))
        #print "jet %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, parton pdgID %3d, genjet match %3d, genPujetmatch %3d, pileup mva disc %+.2f, jetEta %+.2f, jetPt %+.2f, rho %+.2f, nParticles %+.2f, nCharged %+.2f, majW %+.2f, minW %+.2f, frac01 %+.2f, frac02 %+.2f, frac03 %+.2f, frac04 %+.2f, ptD %+.2f, beta %+.2f, betaStar %+.2f, pull %+.6f, jetR %+.2f, jetRchg %+.2f"  % (
         #   i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.eta(), pdgId, genJetMatch, genPuJetMatch, j.userFloat("pileupJetIdEvaluator:fullDiscriminant"), puid.product().get(i).jetEta(), puid.product().get(i).jetPt(), puid.product().get(i).rho(), puid.product().get(i).nParticles(), puid.product().get(i).nCharged(), puid.product().get(i).majW(), puid.product().get(i).minW(), puid.product().get(i).frac01(), puid.product().get(i).frac02(), puid.product().get(i).frac03(), puid.product().get(i).frac04(), puid.product().get(i).ptD(), puid.product().get(i).beta(), puid.product().get(i).betaStar(), puid.product().get(i).pull(), puid.product().get(i).jetR(), puid.product().get(i).jetRchg())
        f.write( "%.5f %.5f matchJet: %3d and matchPuJet: %3d %.5f"  % (
            j.pt(), j.userFloat("pileupJetIdEvaluator:fullDiscriminant"), genJetMatch, genPuJetMatch, j.eta() ) )
        f.write("\n")

f.close()

# std::cout << "jetPt " << internalId_.jetPt_ << std::endl;
#           std::cout << "jetEta " << internalId_.jetEta_ << std::endl;
#           std::cout << "DR_weightd " << internalId_.DR_weighted_ << std::endl;
#           std::cout << "rho " << internalId_.rho_ << std::endl;
#           std::cout << "nParticles " << internalId_.nParticles_ << std::endl;
#           std::cout << "nCharged " << internalId_.nCharged_ << std::endl;
#           std::cout << "majW " << internalId_.majW_ << std::endl;
#           std::cout << "minW " << internalId_.minW_ << std::endl;
#           std::cout << "frac01 " << internalId_.frac01_ << std::endl;
#           std::cout << "frac02 " << internalId_.frac02_ << std::endl;
#           std::cout << "frac03 " << internalId_.frac03_ << std::endl;
#           std::cout << "frac04 " << internalId_.frac04_ << std::endl;
#           std::cout << "ptD " << internalId_.ptD_ << std::endl;
#           std::cout << "beta " << internalId_.beta_ << std::endl;
#           std::cout << "betaStar " << internalId_.betaStar_ << std::endl;
#           std::cout << "pull " << internalId_.pull_ << std::endl;
