

## Install Miniconda Python

Get the windows installer here:  
https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe

## Open a conda terminal  

## Create a new conda environment for this project  
`$conda create --name miniMonitor pandas`

## Activating it  
`$source activate miniMonitor`

## Run the monitor to test  
`$python miniMonitor.py`

## Afterwards, figure out how to run it continuously on windows.

On linux, this could be achieved with:  
`$nohup python miniMonitor.py &`
