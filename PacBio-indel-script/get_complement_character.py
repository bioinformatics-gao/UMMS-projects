import re
def main():
    
    sourcefile = open('Wt_remaining_with_hyphen.fasta') # source file 
    data=sourcefile.read()
    sourcefile.close()
    data_blocks=data.split('>')
    block_name=['']*len(data_blocks)    
    del_count_file=open('Wt_del_count_file.fasta','w')

    re_pattern=re.compile('C-*C-*A-*C-*T-*G-*C-*A-*T-*C-*C-*T-*G-*G-*G-*G-*A')

    for i in range(1,len(data_blocks)):
        paragraph=data_blocks[i]
        lines=paragraph.split('\n')
        block_name[i]=lines[0]

        m= re.search(re_pattern, lines[2])
        if m!=None:
            target=m.group()
            sub1= re.search( 'T-*C-*C-*T',  target)
            sub2= re.search( 'C-*C-*T-*G',  target)
            sub3= re.search( 'C-*T-*G-*G',  target)
            sub4= re.search( 'T-*G-*G-*G',  target)
            sub5= re.search( 'G-*G-*G-*G',  target)
            sub6= re.search( 'G-*G-*G-*A',  target)
            core_positions=[]
            core_positions.append(m.start()+sub1.start())
            core_positions.append(m.start()+sub2.start())
            core_positions.append(m.start()+sub3.start())
            core_positions.append(m.start()+sub4.start())
            core_positions.append(m.start()+sub5.start())
            core_positions.append(m.start()+sub6.start())
            length_core_positions=len(core_positions)
            deletion_length=[0]*length_core_positions
            start_position=['']*length_core_positions

	    for j in range(length_core_positions):
                position=core_positions[j]  
                if lines[4][position]=='-':
	            print('There is an delection========================')
                    deletion_length[j] += 1
            	    start_position[j]=position
                    for k in range(position-1,0,-1):
                        if lines[4][k]!='-':
                            break
                        deletion_length[j] += 1
            	        start_position[j] -= 1
                    for m in range(position+1,len(lines[4])):
                        if lines[4][m]!='-':
                            break
                        deletion_length[j] += 1
            start_keys = start_position
            length_values = deletion_length
            start_length_dictionary = dict(zip(start_keys, length_values))
            if '' in  start_length_dictionary:
                del(start_length_dictionary[''])
            print(start_length_dictionary)
            total_del_length=str(sum(start_length_dictionary.values()))
            print('The total indel length is : ' + total_del_length)
            
            del_count_file.write('>'+ block_name[i]+'\n')
            del_count_file.write('The total delection length is : \n' + total_del_length + '\n')
            del_count_file.write('The sequence is : \n'+lines[4]+'\n\n')
            
    del_count_file.close()    	

if __name__ == "__main__": main()
