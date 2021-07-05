import ROOT
from array import array

var = 'pt'

def OneEmptyBins(h):
  # if a bin of h1 is equal to 0 ir negative then remove it
  # also remove non zero bins with > 100% errors
  for i in range(1,h.GetNbinsX()+1):
    if h.GetBinContent(i) == 0 and h.GetBinError(i) == 0:
      h.SetBinContent(i,1)
      h.SetBinError(i,0)
  return h

weight = "eventWeight"

bins = array('f', map(float,[0,100,200,300,400,500,600,700,800,900,1000,1150,1300,1500,1800,2000,2250,2500,2750,3000]))
hout = ROOT.TH1D('hout','',len(bins)-1, bins)

f1 = ROOT.TFile('betaRd33_0_mU2_gU1.root')
t1 = f1.Get('ntuple')
pt1 = hout.Clone()
pt1.SetName('pt1')
t1.Draw(var+'>>pt1',weight+'*(1)','goff')
pt1 = t1.GetHistogram()
pt1.GetXaxis().SetLabelSize(0)
pt1.Print("all")

f2 = ROOT.TFile('betaRd33_0_mU4_gU1.root')
t2 = f2.Get('ntuple')
pt2 = hout.Clone()
pt2.SetName('pt2')
t2.Draw(var+'>>pt2',weight+'*(1)','goff')
pt2 = t2.GetHistogram()
pt2.Print("all")

pt1_over_pt1 = pt1.Clone()
pt1_over_pt1.Divide(pt1)
pt1_over_pt1 = OneEmptyBins(pt1_over_pt1)
pt2_over_pt1 = pt2.Clone()
pt2_over_pt1.Divide(pt1)
pt2_over_pt1 = OneEmptyBins(pt2_over_pt1)


c = ROOT.TCanvas('c','c',700,700)
pad1 = ROOT.TPad("pad1","pad1",0,0.3,1,1)
pad1.SetBottomMargin(0.03)
pad1.Draw()
pad1.cd()

pt1.Draw("HIST")
pt1.SetStats(0)
pt2.Draw("HIST same")
pt2.SetLineColor(2)

l = ROOT.TLegend(0.65,0.75,0.9,0.9);
l.AddEntry(pt1,"2 TeV","l")
l.AddEntry(pt2,"4 TeV","l");
l.Draw()

c.cd()
pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.28)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.2)
pad2.Draw()
pad2.cd()

pt2_over_pt1.Draw("HIST")
pt2_over_pt1.SetAxisRange(0,2,'Y')
pt2_over_pt1.GetXaxis().SetLabelSize(0.08)
pt2_over_pt1.GetYaxis().SetLabelSize(0.08)
pt2_over_pt1.GetYaxis().SetTitleSize(0.1)
pt2_over_pt1.GetYaxis().SetTitleOffset(0.2)
pt2_over_pt1.GetXaxis().SetTitleSize(0.1)
pt2_over_pt1.GetXaxis().SetTitleOffset(0.9)
pt2_over_pt1.GetXaxis().SetTitle(var)
pt2_over_pt1.SetLineColor(2)
pt2_over_pt1.SetStats(0)

pt1_over_pt1.Draw("HIST same")


c.Print("mass_comparison.pdf")
