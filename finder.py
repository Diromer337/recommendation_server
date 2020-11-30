import os
import subprocess
from functools import lru_cache


class Finder:
    def __init__(self, file, delimiter=','):
        self.file = file
        # раскоментируйте для сортировки файла
        # os.system('LC_ALL=C sort -o {file} {file}'.format(file=self.file))
        self.n_byte = os.path.getsize(self.file)
        self.n_line = int(subprocess.check_output(['wc', file]).decode().split()[0])
        self.step = self.n_byte // self.n_line
        self.delimiter = delimiter
        print('--Finder init successful--')

    def find_product_seek(self, product):
        low = 0
        high = self.n_line - 1
        with open(self.file, 'r') as file:
            # binary search
            while low <= high:
                seek = self.step * ((low + high) // 2)
                file.seek(seek)
                sku = file.readline().split(self.delimiter)[0]
                if sku < product:
                    low = (seek // self.step) + 1
                elif sku > product:
                    high = (seek // self.step) - 1
                else:
                    return seek
            return -1

    def upper_rec(self, product, power, seek):
        rec_list = []
        shift = 1
        with open(self.file, 'r') as file:
            file.seek(seek - self.step * shift)
            sku, rec, power_ = file.readline().split(self.delimiter)
            while sku == product:
                if float(power_) >= power:
                    rec_list.append(rec)
                shift += 1
                if seek - self.step * shift >= 0:
                    file.seek(seek - self.step * shift)
                    sku, rec, power_ = file.readline().split(self.delimiter)
                else:
                    break
        return rec_list

    def lower_rec(self, product, power, seek):
        rec_list = []
        with open(self.file, 'r') as file:
            file.seek(seek)
            sku, rec, power_ = file.readline().split(self.delimiter)
            while sku == product:
                if float(power_) >= power:
                    rec_list.append(rec)
                row = file.readline()
                if row:
                    sku, rec, power_ = row.split(self.delimiter)
                else:
                    break
        return rec_list

    @lru_cache
    def find_rec(self, product, power=0):
        rec_list = []
        seek = self.find_product_seek(product)
        if seek == -1:
            return -1
        rec_list.extend(self.upper_rec(product, power, seek))
        rec_list.extend(self.lower_rec(product, power, seek))
        return rec_list
