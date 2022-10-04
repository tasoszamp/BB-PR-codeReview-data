import json
import numpy as np

def trim_outliers_mean(data, m):
    d = np.abs(data - np.mean(data))
    mdev = np.mean(d)
    s = d/mdev
    return data[s<m]

def trim_outliers_median(data, m):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev
    return data[s<m]

UNIQ_USERS = []
TOTAL_TIME_APPR = 0
TOTAL_TIME_MERGE = 0
appr_time = []
merge_time = []

with open('last1000.json') as f:
   data = json.load(f)

for d in data:
    #TOTAL_TIME_APPR = TOTAL_TIME_APPR + d["Approved"]
    #TOTAL_TIME_MERGE = TOTAL_TIME_MERGE + d["Merged"]
    
    appr_time.append(d["Approved"])
    merge_time.append(d["Merged"])
    if d["Creator"] not in UNIQ_USERS:
        UNIQ_USERS.append(d["Creator"])

### for raw data    
AVG_TIME_APPR = np.mean(appr_time)
AVG_TIME_MERGE = np.mean(merge_time)
MIN_RAW = np.min(appr_time)
MAX_RAW = np.max(appr_time)

appr_time.sort()
np_time_data = np.array(appr_time)
print (appr_time)

print ('On the raw data, average approval time is {}, average merge time is {}, minimum time to approve is {} and maximum is {} from {} unique users'.format(AVG_TIME_APPR, AVG_TIME_MERGE, MIN_RAW, MAX_RAW, len(UNIQ_USERS)))

### for mean trim
trimmed_time_data_mean = trim_outliers_mean(np_time_data, 2.)
AVG_TIME_APPR_MEAN = np.mean(trimmed_time_data_mean)
MIN_MEAN = np.min(trimmed_time_data_mean)
MAX_MEAN = np.max(trimmed_time_data_mean)
TRIMMED_MEAN = 1000 - len(trimmed_time_data_mean)
MIN_TRIMMED_MEAN  = appr_time[len(trimmed_time_data_mean)]

print ('On the mean trimmed, trimmed {} PRs with min outlier {}, average is {}, min {}, max {}'.format(TRIMMED_MEAN, MIN_TRIMMED_MEAN, AVG_TIME_APPR_MEAN, MIN_MEAN, MAX_MEAN))

### for median trim
trimmed_time_data_median = trim_outliers_median(np_time_data, 2.)
AVG_TIME_APPR_MEDIAN = np.mean(trimmed_time_data_median)
MIN_MEDIAN = np.min(trimmed_time_data_median)
MAX_MEDIAN = np.max(trimmed_time_data_median)
TRIMMED_MEDIAN = 1000 - len(trimmed_time_data_median)
MIN_TRIMMED_MEDIAN  = appr_time[len(trimmed_time_data_median)]

print ('On the median trimmed, trimmed {} PRs with min outlier {}, average is {}, min {}, max {}'.format(TRIMMED_MEDIAN, MIN_TRIMMED_MEDIAN, AVG_TIME_APPR_MEDIAN, MIN_MEDIAN, MAX_MEDIAN))