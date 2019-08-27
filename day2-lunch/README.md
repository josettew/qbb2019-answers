Create da2-lunch/SRR072893.10k.fastq
	head -n 40000 SRR072893.fastq > SRR072893.10k.fastq

Generate a quality control report
	fastqu SRR072893.10k.fastq

Map reads to BDGP6
	hisat2 -p 4 -x BDGP6 -U SRR072893.10k.fastq
	
Convert .sam to .bam
	samtools sort -@ 4 SRR072893.10k.sam -o SRR072893.10k.bam
	samtools index -b -@ 4 SRR072893.10k.bam SRR072893.10k.bam.bai
	
Quantitate sorted .bam file 
	stringtie SRR072893.10k.bam -G BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf -p 4 -e -B


