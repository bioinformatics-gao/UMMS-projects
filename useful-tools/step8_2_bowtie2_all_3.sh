##bowtie2-build  lambda_virus.fa  lambda_virus
#bowtie2 --threads 4 --very-sensitive-local -x ../ref_genome/wt_ref_corrected_by_reads -U Sg2.fastq | samtools view -bS -q 1 - >  Sg2.bt2.bam  2>  Sg2.bt2.log 
#samtools view  Sg2.bt2.bam |wc -l
#samtools sort  Sg2.bt2.bam Sg2_sorted.bt2
#samtools index Sg2_sorted.bt2.bam 

###bowtie2 --threads 4 --very-sensitive-local -x ../ref_genome/wt_ref_corrected_by_reads -U Sg5.fastq | samtools view -bS -q 1 - >  Sg5.bt2.bam  2>  Sg5.bt2.log 
###samtools view  Sg5.bt2.bam |wc -l
###samtools sort  Sg5.bt2.bam Sg5_sorted.bt2
###samtools index Sg5_sorted.bt2.bam 

#samtools mpileup -uf ../ref_genome/wt_ref.fa  X_sorted.bt2.bam | bcftools view -cg - | vcfutils.pl vcf2fq > cns.fq
#samtools mpileup -uf ref.fa aln.bam | bcftools view -cg - | vcfutils.pl vcf2fq > cns.fq

#samtools mpileup -uf ref.fa aln.bam | bcftools view -cg - | vcfutils.pl vcf2fq > cns.
#bowtie2 -f --threads 4 --very-sensitive-local -x ../ref_genome/wt_ref -U X.fa |samtools view -bS -q 1 - > X.bt2.bam  2>  X.bt2.log 


#bowtie2 --threads 4  --very-sensitive-local -x ../Fishing_regin/IntronP -U 1227.fastq | samtools view -bS -q 1 - > 1227_IntronP.fastq.bt2.bam  2>  1227_IntronP.fastq.bt2.log 

#bowtie2 -f --threads 4 --very-sensitive-local -x /home/gao/Dan_lk/ref_genome/wt_ref_corrected_by_reads -U Sg2_possible_deletion_format.fasta | samtools view -bS -q 1 - >  Sg2_possible_deletion.bt2.bam  2>  Sg2_possible_deletion.bt2.log 
bowtie2 -f --threads 4 --very-sensitive-local -x wt_ref_corrected_by_reads -U Wt_no_repeat.fasta | samtools view -bS -q 1 - >  Wt_no_repeat.bt2.bam  2>  Wt_no_repeat.bt2.log 
samtools view  Wt_no_repeat.bt2.bam |wc -l
samtools sort  Wt_no_repeat.bt2.bam Wt_no_repeat_sorted.bt2
samtools index Wt_no_repeat_sorted.bt2.bam 
