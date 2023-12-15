# Use in DNA nexus terminal or the app ttyd

for sample in {10..60}; do dx run app-swiss-army-knife --instance-type mem1_ssd1_v2_x36 --priority low --cost-limit 10 -y -icmd="bash /mnt/project/your_folder_path/bash_gcgr.sh ${sample}" ; done 


#final csv tables with genotypes of 469,914 individuals for the all variants are located under project-xxxxxxxxxxxxxxxx:/your_folder_path/results/
These were generated running bash_gcgr.sh (--auth-token accordingly)
