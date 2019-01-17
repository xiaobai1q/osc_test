#encoding:utf-8

import xlrd

class ExcelUtils(object):
    def __init__(self,path,sheetName="Sheet1"):
        self.workbook = xlrd.open_workbook(path)
        self.table = self.workbook.sheet_by_name(sheetName)
        self.keys = list(map(lambda key:key.strip(),self.table.row_values(0)))
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols


    def get_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    if self.keys[x] == "userName":
                        s[self.keys[x]] = str(int(values[x]))
                    else:
                        s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == '__main__':
    utils = ExcelUtils("osc_test_data.xls","login_data")
    data = utils.get_data()
    print(data)

