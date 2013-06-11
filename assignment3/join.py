import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    order_id = record[1]
    other_elements = record[2:]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    final = []
    output = None
    for i in list_of_values:
        if i[0] == 'order':
            output = i
            break
    if output is not None:
        for i in list_of_values:
            if i[0] != 'order':    
                ret = output + i
                mr.emit((ret))
        return    
    else:
        for i in list_of_values:
            mr.emit((i[1], i))                    
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
