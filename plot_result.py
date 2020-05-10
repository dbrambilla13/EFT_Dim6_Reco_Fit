import ROOT 


# apro il file csv
f = open('less_nuisances/results.csv','r')

# leggo una riga come stringa


read_file = []

line = f.readline()
while ( line != ""):
    line = line.replace('\n','')
    temp = line.split(',')
    read_file.append(temp)
    line = f.readline()
     
# ordino, divido, ecc ecc
records = read_file[1:]

histo1SigmaSx = ROOT.TH1F()
# histo1SigmaDx
# histo2SigmaSx
# histo2SigmaDx

for aux in records:
    print('a')

# creo 4 istogrammi istogrammi con root

# creo il plot degli intervalli di confidenza sovrapponendoli

