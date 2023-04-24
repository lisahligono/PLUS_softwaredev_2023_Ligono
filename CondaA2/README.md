# Ligono A2 Conda assignment
Step 1:Cloning the GitHub repository to my local repository
Created a folder 'geo-software-dev' in my OS
git clone https://github.com/augustinh22/geo-software-dev.git
set the path to the 'geo-software-dev' folder

Step 2:Recreate both environments with conda
I recreated the 2 environments as follows:
conda env create -f software_dev_v1.yml
conda env create -f software_dev_v2.yml

# software_dev_v1 environment was not created

Step 3:Modify one of the environments
Since software_dev_v2 was the only one created, I modified it as follows: 
Listed all packages in the environment: conda list -n software_dev_v2

# Installed a new package 'earthpy' into that environment using the conda-forge channel:
(software_dev_v2) lisahligono@Lisahs-Air A2 % conda install -c conda-forge earthpy

Step 4:Export the modified environment file
# First I renamed the environment to software_ligono_version
conda rename -n software_dev_v2 software_ligono_version
#Exporting
conda env export --from-history>software_ligono_version.yml

Step 5:Commit the modified env file to your personal PLUS_softwaredev_2023_Ligono  GitHub repository 
Folder: CondaA2