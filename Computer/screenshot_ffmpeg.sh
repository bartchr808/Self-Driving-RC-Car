#!/bin/bash
ffmpeg -i tcp://192.168.1.31:2222 -start_number 0 -s 640x480 -vf fps=2 "image-%02d.png"
