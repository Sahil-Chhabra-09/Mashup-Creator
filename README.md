# Mashup-Creator
Creates an audio mashup using python script

Required libraries:
  * moviepy - `pip install moviepy`
  * pytube - `pip install pytube`
  * os
  * sys
  
Takes 4 inputs through the standard input through command line in the following format:
  1. Name of the singer
  2. Number of songs to mix
  3. Duration each song should run in the created mashup
  4. Name of the final audio file with a ".mp3" extension

Sample code executions:
  * `python mashup.py "Halsey" 5 25 "Out.mp3"`
  * `python mashup.py "Drake" 10 30 "Out.mp3"`
  * `python mashup.py "Alan Walker" 15 15 "Out.mp3"`
