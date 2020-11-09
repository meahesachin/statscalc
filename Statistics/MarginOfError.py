
from Statistics.StandardDeviation import stddev

def margin_of_error(sample,z,N):
    stddeviation = float(stddev(sample))
    rootN = (N ** .5)
    return round(z*(stddeviation/rootN), 5)
