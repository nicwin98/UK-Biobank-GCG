#!/bin/bash
cd /home/dnanexus
mkdir filtered_vcfs
sudo apt install parallel -y

ls /mnt/project/Bulk/'Exome sequences'/'Exome OQFE variant call files (VCFs)'/$1/*.vcf.gz | parallel -j+0 --eta bcftools view -H -R /mnt/project/your_folder_path/gcgr_region.txt {} ">" /home/dnanexus/filtered_vcfs/{/.}.filtered.csv

pip install pandas==1.5.2

python3 /mnt/project/your_folder_path/mergeVCF.py $1

wget \
  https://dnanexus-sdk.s3.amazonaws.com/dnanexus-upload-agent-1.5.33-linux.tar.gz -O - |\
  tar -xzf -

cd dnanexus-upload-agent-*-linux

./ua --auth-token your_token --project "project-xxxxxxxxxxxxxxxx" /home/dnanexus/UKB_VCFmerge* --folder /your_folder_path/results/