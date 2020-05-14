# run with python plot_result.py -b
# -b is for batch mode

import ROOT 
import sys

# my modules
# importing modules
config_module_name = str(sys.argv[1])[:-3]
print ("importing module" + config_module_name)
cf = __import__(config_module_name)

operator_module_name = str(sys.argv[2])[:-3]
print ("importing module" + operator_module_name)
ops = __import__(operator_module_name)

# apro il file csv
f = open(cf.tag + '/results.csv','r')

# leggo una riga come stringa

read_file = []

line = f.readline()
while ( line != ""):
    line = line.replace('\n','')
    temp = line.split(',')
    read_file.append(temp)
    line = f.readline()

f.close()     

# select best variables
records = []
record_index = 0
records.append(read_file[1])
width = float(records[0][3])-float(records[0][2])
prev_ele_name = records[0][0]

for element in read_file[2:]:
    if element[0] == prev_ele_name:
        new_width = float(element[3])-float(element[2])
        if  new_width < width:
            records[record_index] = element
            width = new_width
    if element[0] != prev_ele_name:
        prev_ele_name = element[0]
        record_index += 1        
        records.append(element)
        width = float(element[3])-float(element[2])

# sorting by 1 sigma interval width
records.sort(key = lambda a : float(a[3]) - float(a[2]))

# produce histogram
nbins = len(records)
# print(nbins)

histo1Sigma = ROOT.TH1F("histo1Sigma","histo1Sigma",nbins,0,nbins)
histo2Sigma = ROOT.TH1F("histo2Sigma","histo2Sigma",nbins,0,nbins)


for i in range(nbins):
    histo1Sigma.SetBinContent(i+1,float(records[i][3])-float(records[i][2]))
    histo1Sigma.GetXaxis().SetBinLabel(i+1,records[i][0] + ' (' + records[i][1] + ')')
    histo1Sigma.GetXaxis().ChangeLabel(i+1,45)
    histo2Sigma.SetBinContent(i+1,float(records[i][5])-float(records[i][4]))
    histo2Sigma.GetXaxis().SetBinLabel(i+1,records[i][0] + ' (' + records[i][1] + ')')
    histo2Sigma.GetXaxis().ChangeLabel(i+1,45)

c1 = ROOT.TCanvas()

histo2Sigma.Draw()
histo2Sigma.SetFillColor(ROOT.kOrange)
histo1Sigma.Draw("same")
histo1Sigma.SetFillColor(ROOT.kRed)


leg = ROOT.TLegend(0.1,0.7,0.4,0.9)
leg.SetHeader("Legend","C")
leg.AddEntry(histo1Sigma,"1 Sigma Width","f")
leg.AddEntry(histo2Sigma,"2 Sigma Width","f")
leg.Draw()

ROOT.gStyle.SetOptStat(0)
ROOT.gPad.SetGrid()
# printout
c1.Print(cf.tag + "/results_all.png",".png")
histo2Sigma.GetYaxis().SetRangeUser(0,5)
histo1Sigma.GetYaxis().SetRangeUser(0,5)
c1.Print(cf.tag + "/results_all_zoom.png",".png")

# c1.SetLogy()
# c1.Print(cf.tag + "/results_log.png",".png")


# make variable comparison prints for every operator

for op in ops.operator:

    elements = [ x for x in read_file[1:] if x[0]== "k_"+op]

    # sorting by width
    elements.sort(key = lambda el : float(el[3]) - float(el[2]))

    nbins = len(elements)
    name1 = "h_1S_Var_{}".format(op)
    name2 = "h_2S_Var_{}".format(op)
    h_1S_Var = ROOT.TH1F(name1,name1,nbins,0,nbins)
    h_2S_Var = ROOT.TH1F(name2,name2,nbins,0,nbins)

    for i in range(nbins):
        h_1S_Var.SetBinContent(i+1,float(elements[i][3])-float(elements[i][2]))
        h_1S_Var.GetXaxis().SetBinLabel(i+1, elements[i][1] )
        h_1S_Var.GetXaxis().ChangeLabel(i+1,45)
        h_2S_Var.SetBinContent(i+1,float(elements[i][5])-float(elements[i][4]))
        h_2S_Var.GetXaxis().SetBinLabel(i+1, elements[i][1] )
        h_2S_Var.GetXaxis().ChangeLabel(i+1,45)

    c1 = ROOT.TCanvas()

    h_2S_Var.Draw()
    h_2S_Var.SetMinimum(0)
    h_2S_Var.SetMinimum(h_2S_Var.GetMaximum()*1.1)
    h_2S_Var.SetFillColor(ROOT.kCyan)
    h_2S_Var.SetTitle("")
    h_1S_Var.Draw("same")
    h_1S_Var.SetFillColor(ROOT.kBlue)
    h_1S_Var.SetTitle("")

    leg = ROOT.TLegend(0.6,0.7,0.9,0.9)
    leg.SetHeader("Legend","C")
    leg.AddEntry(h_1S_Var,"1 Sigma Width","f")
    leg.AddEntry(h_2S_Var,"2 Sigma Width","f")
    leg.Draw()

    ROOT.gStyle.SetOptStat(0)
    ROOT.gPad.SetGrid()
    # printout
    c1.Print(cf.tag + "/results_{}.png".format(op),".png")