from libraries import *
from parser import parcing,prices_normal,prices_discount
from writer import file_writer


parcing()
print(f"Normal: {prices_normal}")
print(f"Discount: {prices_discount}")
file_writer()