#!/bin/bash
ps -ef | grep "Algo_Backend" | grep -v grep | awk '{print $2}' | xargs kill -9 
