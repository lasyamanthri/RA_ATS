import jiwer
import re
f = open('meeting_saved_closed_caption.txt','r')
g = open('gt.txt','r')
#reading the file
b1=g.read()
b2=f.read()
#print(b1)
transformation = jiwer.Compose([
    jiwer.ToLowerCase(),
    jiwer.RemoveWhiteSpace(replace_by_space=True),
    jiwer.RemoveMultipleSpaces(),
    jiwer.ReduceToListOfListOfWords(word_delimiter=" "),

]) 
b1=jiwer.RemoveKaldiNonWords()(b1)
b2=jiwer.RemoveKaldiNonWords()(b2)

b1=jiwer.ExpandCommonEnglishContractions()(b1)
b2=jiwer.ExpandCommonEnglishContractions()(b2)
b1=jiwer.RemovePunctuation()(b1)
b2=jiwer.RemovePunctuation()(b2)

b1= re.sub('\d|[lL]aughter|[aA]pplause','',b1)
b2= re.sub('\d|[lL]aughter|[aA]pplause','',b2)
b1=jiwer.RemoveEmptyStrings()(b1)
b2=jiwer.RemoveEmptyStrings()(b2)
print(b1,b2)
error=jiwer.wer(
    
    b1, 
    b2, 
    truth_transform=transformation, 
    hypothesis_transform=transformation
)
"""
error = jiwer.wer(b1,b2)"""
print(error)