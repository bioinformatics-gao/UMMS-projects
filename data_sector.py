#!/bin/python
import re
import numpy

def main():
    
    sourcefile = open('pacbio.filtered_subreads.fastq') # source file containing all fastq data 
    lines=sourcefile.readlines()
    sourcefile.close()
    total_lines=len(lines)
    total_reads=total_lines//4
    selected_reads_list=open('selected_out_reads_list_CCS_18K_26K_38.5'+'.fastq','w')
	
    for i in range(0,total_reads):
        seq_read=lines[4*i+1].strip()
	seq_length=len(seq_read)
		
	if  seq_length>=1800 and seq_length<= 2600:
	   	quality_read=lines[4*i+3].strip()
		total_score=0
		for j in range(seq_length):
	            character_score = ord(quality_read[j])
		    if character_score>=40:
			character_score=40
		    total_score=total_score + character_score
                    
	 	ave_score=total_score/len(quality_read)
#                print (ave_score)
			
		if ave_score>=38.5:
                    selected_reads_list.writelines(lines[4*i:4*i+4])
    
    selected_reads_list.close()

if __name__ == "__main__": main()

