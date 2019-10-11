Getting data:
conda create -n macs2 macs2
source activate macs2
wget http://67.207.142.119/outgoing/g1e.tar.xz
wget http://hgdownload.soe.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz
conda install bowtie2
tar xvzf g1e.tar.xz 
gunzip chr19.fa.gz 

Mapping reads:
bowtie2-build chr19.fa refchr19
bowtie2 -x refchr19 -U CTCF_ER4.fastq -S CER4.sam
bowtie2 -x refchr19 -U CTCF_G1E.fastq -S CG1E.sam
bowtie2 -x refchr19 -U input_ER4.fastq -S inER4.sam
bowtie2 -x refchr19 -U input_G1E.fastq -S inG1E.sam

Calling Peaks:
conda install samtools
conda install bedtools
samtools view -Sb CER4.sam > CER4.bam
samtools view -Sb CG1E.sam > CG1E.bam
samtools view -Sb inER4.sam > inER4.bam
samtools view -Sb inG1E.sam > inG1E.bam

samtools sort CER4.bam > CER4_sorted.bam
samtools sort CG1E.bam > CG1E_sorted.bam
samtools sort inER4.bam > inER4_sorted.bam
samtools sort inG1E.bam > inG1E_sorted.bam

macs2 callpeak -f BAM -t CER4_sorted.bam -c inER4_sorted.bam -g 62309240 --outdir callpeaks_output_CER4
macs2 callpeak -f BAM -t CG1E_sorted.bam -c inG1E_sorted.bam -g 62309240 --outdir callpeaks_output_G1E

cut -f 1,2,3,4,5,6 ./callpeaks_output_CER4/NA_peaks.narrowPeak > simpleER4.BED
cut -f 1,2,3,4,5,6 ./callpeaks_output_G1E/NA_peaks.narrowPeak > simpleG1E.BED

Differential Binding:
bedtools intersect -v -a simpleER4.BED -b simpleG1E.BED > ER4_G1E
bedtools intersect -v -a simpleG1E.BED -b simpleER4.BED > G1E_ER4

Feature Overlapping:
wget https://www.taylorlab.org/cmdb-lab/Mus_musculus.GRCm38.94_features.bed
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b simpleER4.BED > featureER4
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b simpleG1E.BED > featureG1E

