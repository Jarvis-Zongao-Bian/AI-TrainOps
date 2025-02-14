#!/bin/bash

mkdir -p logs

# Training Log
echo "$(date) 🚀 Starting Training..." | tee logs/train.log
python3 src/train.py 2>&1 | tee -a logs/train.log
echo "$(date) ✅ Training Complete!" | tee -a logs/train.log

# Testing Log
echo "$(date) 🚀 Starting Testing..." | tee logs/test.log
python3 src/test.py 2>&1 | tee -a logs/test.log
echo "$(date) 🎉 Testing Complete!" | tee -a logs/test.log
