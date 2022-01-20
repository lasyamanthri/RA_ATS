from jiwer import wer
import re
f = open('meeting_saved_closed_caption.txt','r')
g = open('gt.txt','r')
#reading the file
b1=g.read()
b2=f.read()
#WER without pre-processing the data
error = wer(b1,b2)
print(error)
#Step1: From the orginal transcript I removed time stamps, audience reactions (Applause/laughter) and the braces for the same;
b3= re.sub('\d*:\d*|([lL]aughter)|([aA]pplause)|[()]','',b1)
#Step2: As zoom did not record the audiences' reaction, I only had to remove the time stamps.
b4=re.sub('\d*:\d*','',b2)
#Step3: I calculated WER using wer from module jiwer. It was very simple.
error = wer(b3,b4)
print(error)
b6=g.read()
b7=f.read()
#WER without removing audiences' reaction
b6= re.sub('\d|:','',b6)
error = wer(b1,b4)
print(error)
