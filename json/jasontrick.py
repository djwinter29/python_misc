
from decimal import Decimal
from datetime import datetime
from fractions import Fraction
from numpy import arange
from json_tricks import dump, dumps, load, loads, strip_comments

class MyTestCls:
        def __init__(self, **kwargs):
                for k, v in kwargs.items():
                        setattr(self, k, v)
                        
myclas=loads(open(".//json//test.json",mode='r').read())
                        
json2 = dumps(myclas, indent=4)                      
                                                
print(json2)
