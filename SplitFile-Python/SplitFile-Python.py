import ffmpeg
import argparse

parser=argparse.ArgumentParser(description='''Split a media file into to chunks''')         #– Creăm un parser care știe să citească argumentele date când rulezi scriptul.

parser.add_argument('inputfile',help="Input filename")
parser.add_argument('starttime',type=float,help="Start time in seconds")
parser.add_argument('endtime',type=float,help="End time in second")
parser.add_argument('outputfile1',help="Output file")
parser.add_argument('outputfile2',help="Output file")

"""
– Definim ce argumente așteptăm de la utilizator:
inputfile → fișierul video/audio pe care îl tai.
starttime → timpul de început al primei bucăți (în secunde).
endtime → timpul de sfârșit al primei bucăți și începutul celei de-a doua.
outputfile1 → numele fișierului pentru prima bucată.
outputfile2 → numele fișierului pentru a doua bucată.
"""

args= parser.parse_args()                                                         #– Citește efectiv argumentele din linia de comandă și le pune în obiectul args.
                                                                                  #python SplitFile-Python.py video.mp4 5 10 part1.mp4 part2.mp4

in1 = ffmpeg.input(args.inputfile)                                                #– Creează un „input stream” pentru fișierul sursă

v1 = in1.filter('trim', start=float(args.starttime), end=(args.endtime))          #– Aplică filtrul trim din ffmpeg pe in1.– Asta taie fișierul între starttime și endtime.– Rezultatul este prima bucată (v1).
v2 = in1.filter('trim',start=float(args.endtime))                                 #– Aplică tot filtrul trim, dar începe de la endtime până la sfârșitul fișierului.– Asta este a doua bucată (v2).



#Definim două output-uri:
out1=ffmpeg.output(v1,args.outputfile1)         #out1 scrie v1 (prima bucată) în outputfile1.
out2=ffmpeg.output(v2,args.outputfile2)         #out2 scrie v2 (a doua bucată) în outputfile2.



out1.run()
out2.run()
#– Rulează comenzile ffmpeg → efectiv scrie fișierele pe disc.
#– După execuție, vei avea cele două fișiere tăiate.


