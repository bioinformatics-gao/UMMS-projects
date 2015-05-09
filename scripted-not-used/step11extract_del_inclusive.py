import re
def main():
    
    sourcefile = open('Wt_del_count_file.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    block_name=['']*len(data_blocks)    
    Specific_del_file=open('Wt_Specific_del_file.fasta','w')

    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]
        gap_count=int(lines[2].strip())
        if gap_count>=1:
            print(lines[2])
            Specific_del_file.write('>'+ data_blocks[i])

    Specific_del_file.close()    	
if __name__ == "__main__": main()
