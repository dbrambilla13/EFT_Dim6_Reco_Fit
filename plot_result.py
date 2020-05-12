import ROOT 

import config 

# apro il file csv
f = open(config.tag + '/results.csv','r')

# leggo una riga come stringa

read_file = []

line = f.readline()
while ( line != ""):
    line = line.replace('\n','')
    temp = line.split(',')
    read_file.append(temp)
    line = f.readline()
     
# ordino, divido, ecc ecc
records = []

# select best variables
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
print(nbins)

histo1Sigma = ROOT.TH1F("histo1Sigma","histo1Sigma",nbins,0,10)
histo2Sigma = ROOT.TH1F("histo2Sigma","histo2Sigma",nbins,0,10)


for i in range(nbins):
    histo1Sigma.SetBinContent(i+1,float(records[i][3])-float(records[i][2]))
    histo1Sigma.GetXaxis().SetBinLabel(i+1,records[i][0] + ' (' + records[i][1] + ')')
    histo1Sigma.GetXaxis().ChangeLabel(i+1,45)
    histo2Sigma.SetBinContent(i+1,float(records[i][5])-float(records[i][4]))
    histo2Sigma.GetXaxis().SetBinLabel(i+1,records[i][0] + ' (' + records[i][1] + ')')
    histo2Sigma.GetXaxis().ChangeLabel(i+1,45)

c1 = ROOT.TCanvas()

histo2Sigma.Draw()
histo2Sigma.SetFillColor(ROOT.kCyan)
histo1Sigma.Draw("same")
histo1Sigma.SetFillColor(ROOT.kOrange)

ROOT.gStyle.SetOptStat(0)

# printout
c1.Print(config.tag + "/results.png",".png")
histo2Sigma.GetYaxis().SetRangeUser(0,5)
histo1Sigma.GetYaxis().SetRangeUser(0,5)
c1.Print(config.tag + "/results_zoom.png",".png")

# c1.SetLogy()
# c1.Print(config.tag + "/results_log.png",".png")

