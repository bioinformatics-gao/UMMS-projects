import re
def main():
    
    sourcefile = open('Wt_single_hit_with_query_and_hyphen.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    
    unchanged_file=open('Wt_without_change.fasta','w')
    up_changed_file=open('Wt_with_up_changed.fasta','w')	
    down_changed_file=open('Wt_with_down_changed.fasta','w') 
    both_changed_file=open('Wt_with_both_changed.fasta','w')
    unidentified_file=open('Wt_unidentified.fasta','w')
	
    up_pattern  =re.compile('C-*C-*T-*G-*G-*G-*G-*A-*T-*C-*C')
    down_pattern=re.compile('G-*A-*A-*C-*G-*A-*G-*G-*C-*G-*G')
    
    block_name=['']*len(data_blocks) 
    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]

        m=re.search(up_pattern,lines[2])
	n=re.search(down_pattern,lines[2])
        if m!=None and n!=None:
            target1=m.group()
            sub1= re.search('G-*G-*G-*A',  target1)
	    up_core_position=m.start()+sub1.start()
            target2=n.group()
            sub2= re.search('A-*G-*G-*C',  target2)
	    down_core_position=n.start()+sub2.start()
			
            if lines[4][up_core_position]=='G' and lines[4][down_core_position]=='A':
		unchanged_file.write('>'+ paragraph)
	    elif lines[4][up_core_position]!='G' and lines[4][down_core_position]=='A':
		up_changed_file.write('>'+ paragraph)
	    elif lines[4][up_core_position]=='G' and lines[4][down_core_position]!='A':
		down_changed_file.write('>'+ paragraph)
            elif lines[4][up_core_position]!='G' and lines[4][down_core_position]!='A':
		both_changed_file.write('>'+ paragraph)
	    else:
	        unidentified_file.write('>'+ paragraph) 
		
    unchanged_file.close()
    up_changed_file.close()	
    down_changed_file.close() 
    both_changed_file.close()
    unidentified_file.close()
	
if __name__ == "__main__": main()