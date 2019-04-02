# coding:utf-8
import xlrd

filePath = "F:\my_test\datas\Hunan_datas.xlsx"
sheetName = "Sheet1"

data = xlrd.open_workbook(filename=filePath)
sheet = data.sheet_by_name(sheetName)
ncols = sheet.ncols
nrows = sheet.nrows
L1 =[]
L2 = []
for i in range(nrows-1):
    i += 1
    parameters_keys = sheet.row_values(0)
    parameters = sheet.row_values(i)
    num = sheet.col_values(1)
    para = dict(zip(parameters_keys, parameters))
    print(para)
    L1.append(para)
for i in range(len(L1)):
    i+=1
    L2.append(i)

print(L2)
paras= dict(zip(L2,L1))
print(paras)

print(paras[1]["username"])