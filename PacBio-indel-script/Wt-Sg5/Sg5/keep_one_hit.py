import re
def main():
    
    sourcefile = open('Sg5_blast_pure.blast') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    
    single_hit_file=open('Sg5_single_hit.blast','w') 
    block_name=['']*len(data_blocks)    

    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[1]
        for k in range(5,len(lines)):
            m= re.search('Identities', lines[k])
            if m is not None:
                subparagraph='\n'.join(lines[0:k-1])
                single_hit_file.write('>'+subparagraph)
		break
        else:
             single_hit_file.write('>'+ paragraph)

    single_hit_file.close()

if __name__ == "__main__": main()
