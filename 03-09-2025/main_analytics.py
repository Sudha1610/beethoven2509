from analytics.io.reader import read_data
from analytics.io.writer import write_data
from analytics.core.processor import process_data
from analytics.tools.formatter import formate_data

data = read_data()
data1 = process_data(data)
data2 = formate_data(data1)
print(write_data(data2))

