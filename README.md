# apscheduler_benchmark
This repository contains POC about APScheduler and how it can serve in a high scalability system which can serve critical mission.

https://github.com/agronholm/apscheduler/

# How to benchmark APScheduler.

We would schedule a million jobs and send it to kafka. 


# Running with redis

## First run:

LIMIT = 1000
max_instances = 3
thread_pool = 20

can only successfully run 383 jobs in one second.
misfired 617 jobs 



Increased max_instances to 15 and thread_pool to 100 
The job to be executed only 375. Misfired 625

Guessing: Maybe it's the limitation of Redis server


## Try to run without sending anything
simple print

LIMIT 100
max_instances = 15
thread_pool = 100


Ran 403 jobs - Misfired 597

## Try to run with jobstore in memory

Without any database and use only memory as job scheduling. The system seem running fine. 


## Job just failed without running

Increase it to 1.000.000 job in memory but it failed.

## Job with Redis target and  Memory 

Try with 10.000 job

4.000 job executed in time. Misfired 6000 by 2.3 seconds

## Job with Print target and memory

Try with 10.000 job

4.500 job executed in time. Misfired 5500 by 2.3 seconds


## Best result

100.000 jobs
misfire_grace_time=60
- send_to_redis 
- memory storage
- 100.000 job finished in 27 seconds
