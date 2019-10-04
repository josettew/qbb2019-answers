
get and install stuff

wget https://www.taylorlab.org/cmdb-lab/week5_query.fa
conda install blast emboss mafft

BLAST Search:
blastn -remote -db nr -query week5_query.fa -evalue 0.0001 -max_target_seqs 1000 -outfmt "6 sseqid sseq" -out query.out

Convert to fasta:
sed "s/-//g" query.out > newquery.out
sed "s/^/>/" newquery.out > nextquery.out
awk "{print $1"\n"$2}" < nextquery.out > finalquery.out

Multiple Alignment:
transeq -sequence finalquery.out -outseq sequence.out
mafft sequence.out > aligned.out