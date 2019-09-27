/Users/cmdb/qbb2019-answers/20190927class

wget http://67.207.142.119/outgoing/BYxRM_segs_saccer3.bam.simplified.vcf.xz
wget http://67.207.142.119/outgoing/BYxRM_PhenoData.txt

create environment
conda create -n labweek4 python=3 PLINK
conda install matplotlib

conda install matplotlib

unzip the vcf files
unxz BYxRM_segs_saccer3.bam.simplified.vcf.xz 

PCA
plink --allow-extra-chr --mind --bfile plink --pca 2 --out components

Frequency
plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --freq --family --allow-extra-chr 

GWAS
get phenotypes in proper format
sed 's/_/ /1' BYxRM_PhenoData.txt > phenotypes.data

plink --allow-extra-chr --allow-no-sex --mind --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno phenotypes.data --all-pheno  --assoc --out phenoassoc
