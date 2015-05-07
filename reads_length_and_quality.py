#!/bin/python
import re
import numpy

def main():
    
    sourcefile = open('1227.fastq') # source file containing all fastq data 
    lines=sourcefile.readlines()
    sourcefile.close()
    total_lines=len(lines)
    total_reads=total_lines//4
    accumulated_for_each_lenth={}
    quality_for_each_lenth={}
    ave_quality_for_each_lenth={}
    ave_score_list=[]
    
    for i in range(0,total_reads):
        seq_read=lines[4*i+1].strip()
	lenth_of_seq_read=str(len(seq_read))
	if lenth_of_seq_read not in accumulated_for_each_lenth:
	    accumulated_for_each_lenth[lenth_of_seq_read]=1
	else:
	    accumulated_for_each_lenth[lenth_of_seq_read]=accumulated_for_each_lenth[lenth_of_seq_read]+1
        
        quality_read=lines[4*i+3].strip()
        total_score=0
        for j in range(len(quality_read)):
            character_score = ord(quality_read[j])
            if character_score>=40:
                character_score=40
            total_score=total_score + character_score
        ave_score=total_score/len(quality_read)
	ave_score_list.append(ave_score)

        if lenth_of_seq_read not in quality_for_each_lenth:
            quality_for_each_lenth[lenth_of_seq_read]=[]
            ave_quality_for_each_lenth[lenth_of_seq_read]=None
	    quality_for_each_lenth[lenth_of_seq_read].append(ave_score)
	else:
	    quality_for_each_lenth[lenth_of_seq_read].append(ave_score)

    print(numpy.mean(ave_score_list))
    print(numpy.median(ave_score_list))

    for key in ave_quality_for_each_lenth:
        ave_quality_for_each_lenth[key]=numpy.mean(quality_for_each_lenth[key])

    result = {}
    for key in (accumulated_for_each_lenth.viewkeys() | ave_quality_for_each_lenth.keys()):
        if key in accumulated_for_each_lenth: result.setdefault(key, []).append(accumulated_for_each_lenth[key])
        if key in ave_quality_for_each_lenth: result.setdefault(key, []).append(ave_quality_for_each_lenth[key])
   
    outfile = open( 'dict_length_and_score_.txt', 'w' )
    for key, value in  result.items():
          outfile.write( str(key) + '\t' + str(value[0]) + '\t' + str(value[1]) +'\n' )

if __name__ == "__main__": main()

