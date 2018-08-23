#!/bin/bash
# Script to convert a .h264 file to a .mp4 file
# Arguments:
#			#1: name of file (example "basement_30")
MP4Box -add basement_$1.h264 basement_$1.mp4
