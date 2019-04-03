# coding:utf-8
import xlrd

class ExcelUtil:
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            mylist = []
            j = 1
            for i in range(self.rowNum - 1):
                datadict = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    datadict[self.keys[x]] = values[x]
                mylist.append(datadict)
                j += 1
            return mylist

if __name__ == "__main__":
    filePath = "F:\my_test\datas\Ganzhou_datas.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filePath, sheetName)
    datalist = data.dict_data()
    print(datalist)