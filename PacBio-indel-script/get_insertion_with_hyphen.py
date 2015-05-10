import re
def main():
    
    sourcefile = open('Wt_single_hit_with_query_and_hyphen.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    
    insert_file=open('Wt_insert.fasta_with_hyphen','w')
    remaining_file=open('Wt_remaining_with_hyphen.fasta','w')	
    other_file=open('Wt_other_with_hyphen.fasta','w') 
    block_name=['']*len(data_blocks) 
   
    left_pattern=re.compile('C-*C-*A-*C-*T-*G-*C-*A')
    right_pattern=re.compile('C-*C-*T-*G-*G-*G-*G-*A')
   
    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]

        m=re.search(left_pattern,lines[2])
        if m!=None:
            upstram_position=re.search(left_pattern,lines[2]).start()
            shift=(len(m.group()))-1
            left_end = upstram_position + shift

        n=re.search(right_pattern,lines[2])
        if n!=None:
            downstram_position=re.search(right_pattern,lines[2]).start()

        distance=downstram_position-left_end-1

        between_string =lines[2][left_end+1:downstram_position]
        hyphen_count= between_string.count('-')
        print(hyphen_count)
        
        if hyphen_count >=1:
	    insert_file.write('>'+ block_name[i]+'\n')
            insert_file.write('The upstream ends at : '+ str(left_end+1) +'\n')
            insert_file.write('The downstream  begins at : '+ str(downstram_position+1)+'\n')
            insert_file.write('The insert length is :\n')
            insert_file.write(str(hyphen_count) +'\n')
            insert_file.write('The whole sequence is : \n'+ lines[4]+'\n\n')
        
	elif hyphen_count==0:
            remaining_file.write('>'+ paragraph)
	else:
            other_file.write('>'+ paragraph)
		
    insert_file.close()
    remaining_file.close()	
    other_file.close() 
           
if __name__ == "__main__": main()
