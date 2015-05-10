import re
def main():
    
    sourcefile = open('Wt_remaining_with_hyphen.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    
    fasta_file=open('Wt_remaining.fasta','w') 
    block_name=['']*len(data_blocks)    

    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]
        print('>'+ block_name[i]+'\n')
	
        lines[4]=lines[4].replace('-','') 
        fasta_file.write('>'+ block_name[i]+'\n')
        fasta_file.write(lines[4]+'\n\n')
	
    fasta_file.close()

if __name__ == "__main__": main()
