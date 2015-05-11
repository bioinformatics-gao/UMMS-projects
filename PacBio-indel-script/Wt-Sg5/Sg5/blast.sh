#blastn -query wt_ref_corrected_by_reads.fa -out outputSg2.blast.txt -db Sg2dbBLAST
#blastn -query wt_ref_corrected_by_reads.fa -out outputSg5.blast.txt -db Sg5dbBLAST

#tblastn -query protein.fasta -db nucl.blastdb -out results.tblastnout -evalue 1 -outfmt 7 -num\_descriptions 100000 -num\_alignments 100000
#blastn -query wt_ref_corrected_by_reads.fa -db Sg2dbBLAST -out outputSg2_blast_max_num.txt -evalue 1 -outfmt 6 -num\_descriptions 100000 -num\_alignments 100000
blastn -query wt_ref_corrected_by_reads.fa -db Sg5dbBLAST -out outputSg5_blast_max_num.txt -evalue 1 -num\_descriptions 100000 -num\_alignments 100000
