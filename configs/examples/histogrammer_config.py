from skimmer_config import extraEventCollections

nEvents = -1
printEveryNevents = 1000

inputFilePath = "../samples/background_dy.root"
histogramsOutputFilePath = "../samples/histograms/background_dy.root"

defaultHistParams = (
#  collection      variable          bins    xmin     xmax     dir
  ("Event"       , "nMuon"         , 50,     0,       50,      ""  ),
  ("Muon"        , "pt"            , 400,    0,       200,     ""  ),
  ("Muon"        , "eta"           , 100,    -2.5,    2.5,     ""  ),
  ("Event"       , "nGoodLeptons"  , 50,     0,       50,      ""  ),
  ("GoodLeptons" , "pt"            , 400,    0,       200,     ""  ),
  ("GoodLeptons" , "eta"           , 100,    -2.5,    2.5,     ""  ),
)

weightsBranchName = "genWeight"
