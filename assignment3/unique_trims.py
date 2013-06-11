import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    id = record[0]
    tide = record[1]
    new_tide = tide[:-10]
    mr.emit_intermediate(new_tide, new_tide)
    
def reducer(key, list_of_values):
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
