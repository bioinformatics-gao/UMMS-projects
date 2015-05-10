import re


def main():
    
    barcodelist=['gacttcag', 'gcttcaga', 'attcaggc', 'tggactca', 'agactctg', 'gactctag']
    reverse_complementary_barcodelist=['tgagtcca', 'cagagtct', 'ctagagtc', 'ctgaagtc', 'tctgaagc', 'gcctgaat']
    sourcefile = open('reads_of_insert.fastq') # source file containing all fastq data 
    barcode_Num=len(barcodelist) 
    lines=sourcefile.readlines()
    total_lines=len(lines)
    remainlines=lines[:]
    sourcefile.close()
    remain_reads_file = open('remain_reads.fastq', 'w') # source file containing all fastq data 
    name=['']*len(barcodelist)
    num_bar_code=['']*len(barcodelist)
    num_RC_bar_code_without_bar_code=['']*len(barcodelist)
 
    
    for k in range(0,barcode_Num):
        name[k] = open(barcodelist[k]+'_'+'.fa','w') # the output file containing fastq data with certain barcode 
        num_bar_code[k]=0
        num_RC_bar_code_without_bar_code[k]=0
    
    for i in range(0,total_lines):
        line=lines[i]
#	lines=remainlines[:]
        ends=line[-9:-1]
	for k in range(0,barcode_Num):
            if re.match(barcodelist[k], line, re.IGNORECASE):
                name[k].writelines(lines[i-1:i+3])
                num_bar_code[k]=num_bar_code[k]+1
		remainlines[i-1:i+3]=["\n","\n","\n","\n"]
            elif re.search(reverse_complementary_barcodelist[k], ends, re.IGNORECASE):
                name[k].writelines(lines[i-1:i+3])
		remainlines[i-1:i+3]=["\n","\n","\n","\n"]
                num_RC_bar_code_without_bar_code[k]=num_RC_bar_code_without_bar_code[k]+1
    for k in range(0,barcode_Num):
	 name[k].close() 
	 
    remain_reads_file.writelines(remainlines)
    remain_reads_file.close()
	
	
    for k in range(0,barcode_Num):
        print("The barcode----" + barcodelist[k] +" has total begin matching times: "+ str(num_bar_code[k]))	
	print("The reverse complementary barcode----" + barcodelist[k] +" has total end matching times (without begin matching) : "+ str(num_RC_bar_code_without_bar_code[k]))	
 
if __name__ == "__main__": main()
