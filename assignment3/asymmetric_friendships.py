import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    friender = record[0]
    friendee = record[1]
    mr.emit_intermediate(friender, friendee)
    mr.emit_intermediate(friendee, friender)
    
def reducer(key, list_of_values):
    names = {}
    for i in list_of_values:
        if i not in names:
            names[i] = 1
        else:
            del names[i]   
    for i in names:
        mr.emit((key, i))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
