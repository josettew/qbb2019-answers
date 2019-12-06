
conda create -n hifive -c bioconda -c anaconda -c conda-forge hifive
conda activate hifive

download 4 data sets

create a a genome partition:
hifive fends -B chr10_frags.bed fends_out

load interaction data:
hifive hic-data -M chr10_data.mat fends_out data_fname_output

create our project file:
python -c "import hifive; hic=hifive.HiC('project_file', 'w'); hic.load_data('data_fname_output'); hic.filter_fends(10); hic.save()"

normalize the Hi-C data:
hifive hic-normalize express -w cis -f 10 project_file

generating heatmaps:
hifive hic-heatmap -b 500000 -d raw -F npz -i heatmap1.png project_file heatmap1_output.npz

hifive hic-interval -c chr10 -s 5000000 -e 50000000 -b 50000 -d fend -M -i heatmap2.png project_file heatmap2_output

load the data from the two bed files, filtering them down to only interactions within our region of interest:
