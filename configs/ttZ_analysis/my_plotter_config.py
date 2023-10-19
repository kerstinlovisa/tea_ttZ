import ROOT
from Sample import Sample, SampleType
from Legend import Legend
from Histogram import Histogram
from HistogramNormalizer import NormalizationType

samples = (
  Sample(
    name="DY",
    file_path="../samples/histograms/background_dy.root",
    type=SampleType.background,
    cross_section=0.4,
    line_alpha=0.0,
    fill_color=ROOT.kRed-2,
    fill_alpha=0.7,
    marker_size=0.0,
    legend_description="DY"
  ),
)
output_path = "../plots"

histograms = (
#           name            title logy    norm_type                  rebin xmin xmax ymin ymax  xlabel         ylabel
  Histogram("Electron_pt" , "",   True,   NormalizationType.to_lumi, 5,   0  , 150,  1,   1e3 , "Electron p_{T} [GeV]", "# events (2018)"),
  Histogram("Electron_eta", "",   False,  NormalizationType.to_lumi, 5,  -2.4, 2.4,  0,   70  , "Electron #eta"       , "# events (2018)"),
)
luminosity = 63670. # pb^-1 (2018)

legends = {
  SampleType.background: Legend(0.7, 0.8, 0.85, 0.85, "f"),
}

canvas_size = (800, 600)
show_ratio_plots = False
