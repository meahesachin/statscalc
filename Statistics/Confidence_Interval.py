from Statistics.ListofNumWithSeed import listofNumNoSeed
from Statistics.SimpleRandomSampling import simple_rand_sampling
from Statistics.SampleMean import mean
from Statistics.StandardDeviation import stddev
from Calculator.squareroot import squareroot

def confidence_intervalUpper(sample,z,N):


    #sample = simple_rand_sampling(data, N)

    #z = float(z)
    sample_mean = float(mean(sample))
    stddeviation = float(stddev(sample))
    rootN = (N**.5)
    return round(sample_mean + (z*(stddeviation/rootN)), 5)

def confidence_intervalLower(sample,z,N):


    #sample = simple_rand_sampling(data, N)

    #z= float(z)
    sample_mean = float(mean(sample))
    stddeviation = float(stddev(sample))
    rootN = (N**.5)
    return round(sample_mean - (z*(stddeviation/rootN)), 5)
