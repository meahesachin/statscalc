from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling
from Statistics.SampleMean import mean
from Statistics.StandardDeviation import stddev
from Calculator.squareroot import squareroot

def confidence_interval_95Upper(data,N):


    sample = simple_rand_sampling(data, N)

    z = float(1.960)
    sample_mean = float(mean(sample))
    stddeviation = float(stddev(sample))
    rootN = float(squareroot(N))
    return round(sample_mean + (z*(stddeviation/rootN)), 5)

def confidence_interval_95Lower(data,N):


    sample = simple_rand_sampling(data, N)

    z = float(1.960)
    sample_mean = float(mean(sample))
    stddeviation = float(stddev(sample))
    rootN = float(squareroot(N))
    return round(sample_mean - (z*(stddeviation/rootN)), 5)
