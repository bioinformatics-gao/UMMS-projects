import re
def main():
    
    sourcefile = open('Wt_single_hit.blast') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    single_hit_fasta_file=open('Wt_single_hit_with_query_and_hyphen.fasta','w') 
    block_name=['']*len(data_blocks)    

    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]
        print('>'+ block_name[i]+'\n')
	
        queryparagraph=''
        re_pattern1=re.compile('C-*C-*A-*C-*T-*G-*C-*A-*T-*C-*C-*T-*G-*G-*G-*G-*A')
        re_pattern2=re.compile('G-*A-*C-*G-*A-*T-*G-*C-*C-*A-*T-*T-*G-*G-*G-*C[ATCG-]*A-*G-*A-*C-*A-*A-*C-*T-*A-*A-*A-*C-*T-*A-*A')
        for k in range(5,len(lines)):
            if  re.search('Query', lines[k]):
                lines[k]=lines[k].strip('Query') 
                lines[k]= ''.join(m for m in lines[k] if not m.isdigit())
                lines[k]=lines[k].strip() 
                queryparagraph+=(lines[k])
        m= re.search(re_pattern1, queryparagraph)
        n= re.search(re_pattern2, queryparagraph)
        if m==None or n==None:
 	    continue

        subparagraph=''
        for j in range(5,len(lines)):
            if  re.search('Sbjct', lines[j]):
                lines[j]=lines[j].strip('Sbjct') 
                lines[j]= ''.join(m for m in lines[j] if not m.isdigit())
                lines[j]=lines[j].strip() 
                subparagraph+=(lines[j])
        print(subparagraph)
        print(len(subparagraph))
        single_hit_fasta_file.write('>'+ block_name[i]+'\n')
        single_hit_fasta_file.write('Query Sequence \n')
        single_hit_fasta_file.write(queryparagraph+'\n')
        single_hit_fasta_file.write('Reads Sequencen \n')
        single_hit_fasta_file.write(subparagraph+'\n\n')
	
    single_hit_fasta_file.close()

if __name__ == "__main__": main()
