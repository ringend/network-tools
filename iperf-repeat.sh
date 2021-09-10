#!/bin/bash
#Script to run iperf a n number of time with the option to
#pause between each run

echo "What is IP or hostname of iperf server?"
read server
echo "What TCP port do you want to use?"
read port
echo "How many times do you want iperf to run?"
read counter
echo "How many seconds do you want to pause between each run?"
read timer

run=0
total=$counter
while [ $counter -gt 0 ]
do
   run=$(( $run + 1 ))
   echo "Performing run $run of $total"
   iperf3 -c $server -p $port
   echo " "
   counter=$(( $counter - 1 ))
   # Skip sleep command on last run
   if [ $counter -gt 0 ]
   then
      echo "Pausing for $timer seconds..."
      sleep $timer
      echo " "
   fi
Done
