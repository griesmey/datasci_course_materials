import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if matrix == 'a':
        mr.emit_intermediate((i, j), val)
    else:
        mr.emit_intermediate((j, i), val)
    
def reducer(key, values):
    import pdb
    pdb.set_trace()
    if len(values) == 2:
        product = values[0] * values[1]
        mr.emit((key[0], key[1], product))
    else:
        mr.emit((key[0], key[1], sum(values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
