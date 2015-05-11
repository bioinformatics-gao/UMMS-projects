#!/bin/python

import re

def main():
    
    sourcefile = open('Wt_Specific_del_file.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    block_name=['']*len(data_blocks) 

    accumulated_for_each_lenth={}
     
    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]
        gap_length=int(lines[2].strip())
        print(gap_length)
        #    Specific_del_file.write('>'+ data_blocks[i])    
	if gap_length not in accumulated_for_each_lenth:
	    accumulated_for_each_lenth[gap_length]=1
	else:
	    accumulated_for_each_lenth[gap_length]+=1
    print(accumulated_for_each_lenth)    
    outfile = open('Wt_specific_gap_length_and_count.txt', 'w' )
    for key, value in  accumulated_for_each_lenth.items():
        outfile.write( str(key) + '\t' + str(value) +'\n' )
    outfile.close()

if __name__ == "__main__": main()

