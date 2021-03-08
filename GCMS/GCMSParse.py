# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

def parse_GCMS(directory):
    #input: directory containing .txt GC-MS raw data files
    #output: pandas dataframe with GC-MS peak areas
    # dataframe columns: filename/index, 1-C6, C6isomers, 1-C8, C8isomers, PhCl, nonane, 
    import os
    print("parsing GC-MS directory: " + directory)
    data =pd.DataFrame(columns=retentionTimes.keys())
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print('parsing ' + filename)
            files.append(filename[:-4])
    data['file'] = files
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):            
            file = open(directory + "/" + filename,'r')
            for line in file:
                #find the relevant peaks in the file, transfer to df
                time = line.split()[2] # find retention time in GC-MS file
                for r in retentionTimes:
                    t = r[1]
                    analyte = r[0]
                    if abs(time - t) < 0.02:
                        #record area in dataframe
                        break
                if (time > retentionTimes["1-C8"] + offset and time < retentionTimes["PhCl"] - offset)
                #sum up the unknown peaks to count for totC8, totC10, totC12, totC14, and C16+
                continue
        else:
            continue
    return data

def GCMSarea_to_mass(areas,nonane_mg):
    #input: pandas df with GC-MS peak areas; mg of nonane in reactor (float)
    #output: pandas df with relative product masses, averaged among duplicate/triplicate injections      
    print("GCMS area to concentrations")
          
def write_output(df):
    #input: a pandas dataframe for GC-MS peak areas, calculated masses, and relative concentrations
    #output: Excel workbook with worksheets for (a) raw GC-MS peak areas (b) calculated mass yields (c) activities and wt% selectivities (requiring user input in the Excel table of Cr amount, nonane amount, reaction time, PE masses)
    from openpyxl import Workbook
    from openpyxl.utils.dataframe import dataframe_to_rows
    print("writing output Excel: data = " + str(data))
    wb = Workbook()
    ws0 = wb.active
    ws0.title = "exp_parameters"
    #create ws0 to enter Cr amt, nonane amt, Cr:L ratio, reaction time, PE masses
    ws1 = wb.create_sheet()
    ws1.title = "GCMS_areas"
    
    for r in dataframe_to_rows(df, index=True, header=True):
        ws1.append(r)
    
    ws2 = wb.create_sheet()
    ws2.title = "yields_avg"
    #write Excel equations to ws2, using pre-defined linear response factors, areas from ws1, and nonane amt
    
    ws3 = wb.create_sheet()
    ws3.title = "output"
    #write Excel equations to ws3, calculating activities and selecitivites from ws2, and input from ws: Cr amt, PE mass, reaction time
    
    ws4 = wb.create()
    ws4.title = "polished"
    #reformat useful data from ws3 into pretty form
    
    #for cell in ws['A'] + ws[1]:
    #    cell.style='Pandas'
        
    wb.save("output.xlsx")
    
experiments=["AOT-SL-130-1","AOT-SL-130-2","AOT-SL-130-3","AOT-SL-130-4"]
columns=["experiment","1-C6","H3C5a","H2C5e","1-C8", "C8", "PhCl", "C9", "1-C10","1-C12_mg","1-C14_mg","1-C16+_mg","PE_mg","TotalProducts_mg","Activity_g/gCr/h",
         "1-C6_wt%","H3C5a_wt%","H2C5e_wt%","1-C8_wt%","1-C10_wt%","1-C12_wt%","1-C14_wt%","1-C16+_wt%","PE_mg"]
retentionTimes={
    "1-C6":1.1,
    "methylcyclopentane":1.1,
    "methylenecyclopentane":1.3,
    "1-C8":1.4,
    "PhCl":1.5,
    "C9":1.6,
    "1-C10":1.7,
    "1-C12":1.8,
    "1-C14":1.9
    } #seconds(?) these may change with column aging

offset=0.5 #fudge time to account for a peak


linearResponseFactors={
    "1-C6":1.1,
    "methylcyclopentane":1.1,
    "methylenecyclopentane":1.3,
    "1-C8":1.4,
    "PhCl":1.5,
    "C9":1.6,
    "1-C10":1.7,
    "1-C12":1.8,
    "1-C14":1.9
    } #these may change as MS ages or is retuned


data = pd.DataFrame(index=experiments, columns=retentionTimes.keys())
data = data.fillna(0)

write_output(data)
