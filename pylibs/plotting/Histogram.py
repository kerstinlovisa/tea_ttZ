from dataclasses import dataclass
from ROOT import TObject

@dataclass
class Histogram:
  name: str = ""
  title: str = ""
  log_y: bool = False
  norm_type: str = "norm1"
  rebin: int = 1
  x_min: float = 0.0
  x_max: float = 0.0
  y_min: float = 0.0
  y_max: float = 0.0
  x_label: str = ""
  y_label: str = ""
  
  def load(self, input_file):
    self.hist = input_file.Get(self.name)
  
  def isGood(self):
    if self.hist is None or type(self.hist) is TObject:
      print(f"Could not find histogram: {self.name}")
      return False
    if self.hist.GetEntries() == 0:
      print(f"Histogram is empty: {self.name}")
      return False
    
    return True
    
  def setup(self, sample):
    self.hist.SetLineStyle(sample.line_style)
    self.hist.SetLineColor(sample.line_color)
    self.hist.SetMarkerStyle(sample.marker_style)
    self.hist.SetMarkerSize(sample.marker_size)
    self.hist.SetMarkerColor(sample.marker_color)
    self.hist.SetLineColorAlpha(sample.line_color, sample.line_alpha)
    self.hist.SetFillColorAlpha(sample.fill_color, sample.fill_alpha)
    self.hist.Rebin(self.rebin)
    self.hist.Scale(1./self.rebin)
    self.hist.Sumw2(False)

@dataclass
class Histogram2D:
  name: str = ""
  title: str = ""
  x_rebin: int = 1
  y_rebin: int = 1
  x_min: float = 0.0
  x_max: float = 0.0
  y_min: float = 0.0
  y_max: float = 0.0
  z_min: float = 0.0
  z_max: float = 0.0
  x_label: str = ""
  y_label: str = ""
  z_label: str = ""
  
  def load(self, input_file):
    self.hist = input_file.Get(self.name)
    
  def isGood(self):
    if self.hist is None or type(self.hist) is TObject:
      print(f"Could not find histogram: {self.name}")
      return False
    if self.hist.GetEntries() == 0:
      print(f"Histogram is empty: {self.name}")
      return False
    
    return True
    
  def setup(self):
    self.hist.Rebin2D(self.x_rebin, self.y_rebin)
