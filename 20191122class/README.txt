get data

fastq-dump –X 1000000 --split-files SRR1035454
fastq-dump -X 1000000 --split-files SRR1035452

bismark_genome_preparation . 


bismark --bowtie2 . -1 SRR1035452_1.fastq -2 SRR1035452_2.fastq
bismark --bowtie2 . -1 SRR1035454_1.fastq -2 SRR1035454_2.fastq


samtools sort -n SRR1035454_1_bismark_bt2_pe.bam -o sorted_SRR1035454_1_bismark_bt2_pe.bam
samtools sort -n SRR1035452_1_bismark_bt2_pe.bam -o sorted_SRR1035452_1_bismark_bt2_pe.bam

samtools index sorted_SRR1035454_1_bismark_bt2_pe.bam 
samtools index sorted_SRR1035452_1_bismark_bt2_pe.bam

bismark_methylation_extractor --bedgraph --comprehensive sorted_SRR1035454_1_bismark_bt2_pe.bam 
bismark_methylation_extractor --bedgraph --comprehensive sorted_SRR1035452_1_bismark_bt2_pe.bam 

gunzip sorted_SRR1035452_1_bismark_bt2_pe.bedGraph.gz
gunzip sorted_SRR1035454_1_bismark_bt2_pe.bedGraph.gz

