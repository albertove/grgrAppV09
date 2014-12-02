#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      BMGFOU
#
# Created:     10-11-2014
# Copyright:   (c) BMGFOU 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf

#vinfile = open_workbook('vinnova.xls')

def thicknessSubbaseLayer(terras,traffic,subbase):
    calfile = open_workbook('grgrSite/grgrApp/grgrSIte/grgrApp/calculationgrgr.xlsx')
    sheet = calfile.sheet_by_index(0)
    cell = sheet.cell(18+terras,7+(2*traffic))
    try:
        sublayer = cell.value.replace('*','')
    except:
        sublayer = cell.value
    if subbase == 2:
        porc = sheet.cell(18+terras,17)
        sublayer = float(sublayer)*(1.0 + float(porc.value)/100.0)
    return sublayer

def thicknessBaseLayer(val):
    calfile = open_workbook('grgrSite/grgrApp/grgrSIte/grgrApp/calculationgrgr.xlsx')
    sheet = calfile.sheet_by_index(0)
    cell = sheet.cell(10+val,3)
    return cell.value

def totalThickness(thicksubbase,thickbase,climatic,frost):
    calfile = open_workbook('grgrSite/grgrApp/grgrSIte/grgrApp/calculationgrgr.xlsx')
    sheet = calfile.sheet_by_index(0)
    cell = sheet.cell(13+frost,17+climatic)

    if cell.value == '':
        thickcontrol = 0
    else:
        thickcontrol = float(cell.value)

    thicktotal = thicksubbase + thickbase

    if thicktotal < thickcontrol:
        thicksubbase = thicksubbase + (thickcontrol - thicktotal)
    if thicksubbase < 200:
        fraction_subbase = '0/90'
    else:
        fraction_subbase = '0/32'
    return thicktotal,thicksubbase,fraction_subbase

def DData(variables):
    vinnovafile = open_workbook('grgrSite/grgrApp/grgrSIte/grgrApp/vinnova.xls')
    r_sheet = vinnovafile.sheet_by_index(0)
    #celltype = sheet.cell(11,3)
    wb = copy(vinnovafile)
    w_sheet = wb.get_sheet(0)

    for k in range(len(variables)):
        if k == 9:
            w_sheet.write(37,3,variables[k])
        elif k>9:
            w_sheet.write(2+k,17,variables[k])
        else:
            w_sheet.write(10+k,3,variables[k])

    wb.save('grgrSite/grgrApp/grgrSIte/grgrApp/vinnovatemp.xls')
    vinnovafile = open_workbook('grgrSite/grgrApp/grgrSIte/grgrApp/vinnovatemp.xls')
    r_sheet = vinnovafile.sheet_by_index(0)
    design_duration_rain = r_sheet.cell(105,3).value #D106
    available_volume = r_sheet.cell(107,3).value #D108
    required_volume = r_sheet.cell(106,3).value #D107
    D101 = r_sheet.cell(100,3).value
    D109 = r_sheet.cell(108,3).value
    design_duration_rain_ditch = r_sheet.cell(104,17).value #R105
    available_volume_ditch = r_sheet.cell(109,17).value #R110
    required_volume_ditch = r_sheet.cell(98,17).value #R99
    R102 = r_sheet.cell(101,17).value

    DRespons = [design_duration_rain,available_volume,required_volume,D101,D109,design_duration_rain_ditch,available_volume_ditch,required_volume_ditch,R102]
    #print DRespons
    return DRespons

def valueCell(calfile,row,col):
    """
    Read value from Sheet=sheet at Row = row and Column = col.
    Return this value.
    """
    sheet = calfile.sheet_by_index(0)
    cell = sheet.cell(row,col)
    return cell.value

if __name__ == '__main__':
    main()