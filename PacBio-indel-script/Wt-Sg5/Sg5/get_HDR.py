import re
def main():
    
    sourcefile = open('Sg5_single_hit_with_query_and_hyphen.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    
    unchanged_file=open('Sg5_without_change.fasta','w')
    up_changed_file=open('Sg5_with_up_changed.fasta','w')	
    down_changed_file=open('Sg5_with_down_changed.fasta','w') 
    both_changed_file=open('Sg5_with_both_changed.fasta','w')
    unidentified_file=open('Sg5_unidentified.fasta','w')
    outfile = open('Sg5_HDR_count.txt', 'w+' )
	
    up_pattern  =re.compile('T-*G-*T-*A-*C-*C-*A-*T-*G-*T-*A')
    down_pattern=re.compile('G-*A-*A-*C-*G-*A-*G-*G-*C-*G-*G')
    
    block_name=['']*len(data_blocks) 
    up_accumulated_for_each_nt={}
    down_accumulated_for_each_nt={}
    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]

        m=re.search(up_pattern,lines[2])
	n=re.search(down_pattern,lines[2])
        if m!=None and n!=None:
            target1=m.group()
            sub1= re.search('C-*A-*T-*G',  target1)
	    up_core_position=m.start()+sub1.start()
            target2=n.group()
            sub2= re.search('A-*G-*G-*C',  target2)
	    down_core_position=n.start()+sub2.start()
			
            if lines[4][up_core_position]=='C' and lines[4][down_core_position]=='A':
		unchanged_file.write('>'+ paragraph)

	    elif lines[4][up_core_position]!='C' and lines[4][down_core_position]=='A':
		up_changed_file.write('>'+ paragraph)
                up_nt= lines[4][up_core_position]
                if up_nt not in up_accumulated_for_each_nt:
	            up_accumulated_for_each_nt[up_nt]=1
	        else:
	            up_accumulated_for_each_nt[up_nt]+=1
 
	    elif lines[4][up_core_position]=='C' and lines[4][down_core_position]!='A':
		down_changed_file.write('>'+ paragraph)
                down_nt= lines[4][down_core_position]
                if down_nt not in down_accumulated_for_each_nt:
                    down_accumulated_for_each_nt[down_nt]=1
                else:
                    down_accumulated_for_each_nt[down_nt]+=1
 
            elif lines[4][up_core_position]!='C' and lines[4][down_core_position]!='A':
		both_changed_file.write('>'+ paragraph)
                outfile.write(lines[4][up_core_position] + '\t' +lines[4][down_core_position] +'\n' )

	    else:
	        unidentified_file.write('>'+ paragraph) 

    outfile.write( 'The up_stream_changes:\n' )
    for key, value in up_accumulated_for_each_nt.items():
        outfile.write( str(key) + '\t' + str(value) +'\n' )
    outfile.write( 'The down_stream_changes:\n' )
    for key, value in down_accumulated_for_each_nt.items():
        outfile.write( str(key) + '\t' + str(value) +'\n' )

    outfile.close()
    unchanged_file.close()
    up_changed_file.close()	
    down_changed_file.close() 
    both_changed_file.close()
    unidentified_file.close()
	
if __name__ == "__main__": main()
