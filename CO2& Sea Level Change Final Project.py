import matplotlib.pyplot as plt
import csv
plt.clf()
csvFile1 = open("Average_CO2.csv","r")
csvReader1 = csv.reader(csvFile1, delimiter = ',')
next(csvReader1)
csvFile2 = open("Average_sea_level_change.csv","r")
csvReader2 = csv.reader(csvFile2, delimiter = ',')
next(csvReader2)

CO2data= []
CO2Years = []
TempCO2Year = []
TempCO2= []


for row in csvReader1:
    if len(TempCO2Year) == 0:
        TempCO2Year.append(float(row[0]))
        TempCO2.append(float(row[2]))
    else:
        if float(row[0]) in TempCO2Year:
            TempCO2.append(float(row[2]))
        else:
            CO2data.append(sum(TempCO2)/len(TempCO2))
            CO2Years.append(float(row[0])-1)
            TempCO2Year = [float(row[0])]
            TempCO2 = [float(row[2])]
SeaLevYears= [] 
SeaLevdata=[]   
TempSeaLev= []  
TempSeaLevYear= []      
for row in csvReader2:
    if len(TempSeaLevYear) == 0:
        TempSeaLevYear.append(float(row[0]))
        TempSeaLev.append(float(row[1]))
    else:
        if float(row[0]) in TempSeaLevYear:
            TempSeaLev.append(float(row[1]))
        else:
            SeaLevdata.append(sum(TempSeaLev)/len(TempSeaLev))
            SeaLevYears.append(float(row[0])-1)
            TempSeaLevYear = [float(row[0])]
            TempSeaLev = [float(row[1])]
   
#print(SeaLevYears)
#print (CO2Years)
#print(CO2data)
#print (SeaLevdata)

plt.plot(SeaLevYears, SeaLevdata, label = "Sea Level Change", color = "CornflowerBlue")
plt.xlabel("Year")
plt.ylabel("Sea Level Change (mm)")
plt.legend(bbox_to_anchor=(0.4,0.9))
plt.twinx()

plt.plot(CO2Years, CO2data, label = "CO2 (ppm)", color = "MediumSeaGreen")
plt.ylabel("CO2 (ppm)")
plt.title("CO2 and Sea Level Change Over Time")
plt.legend(bbox_to_anchor=(0.3,1))
plt.show()

