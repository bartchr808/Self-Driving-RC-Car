#!/bin/bash
raspivid -fps 20 -w 1280 -h 720 -t 0 -l -hf -vf -o tcp://0.0.0.0:2222
