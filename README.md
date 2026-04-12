# Log Analyzer

A Log Analyzer is made with python 

## How to run (2 options in terminal)
python log_analyzer.py auth.log
- This method will show results in terminal

python log_analyzer.py auth.log --output file
- This method will show results in a file called reports.txt. If `--output file` is not given then it will run in default mode (option 1)

## About the tool
This tool reads auth log file and looks for suspicious and multiple failed attempts from same user or IP address. It flags the failed attempts and shows in terminal with user names and IP address, or writes it in a file.


## Built with
- Python 3
- re module
- collections.Counter module
- argparse module

## Purpose
In cybersecurity, there's always risk of brute force attempts and multiple failed logins, so to avoid such risk, this tool use to block such users or IP addresses