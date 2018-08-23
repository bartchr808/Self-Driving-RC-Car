#!/bin/bash
# Script to record a video from Raspberry pi
# Arguments:
#			#1: Number of file (example 30)
#			#2: Time in ms (example 17000 for 17 seconds)
raspivid -o basement_$1.h264 -vf -hf -t $2 -w 1280 -h 720
