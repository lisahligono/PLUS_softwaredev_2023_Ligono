# Ligono A2 Conda assignment
# Step 1:Cloning the GitHub repository to my local repository
Created a folder 'geo-software-dev' in my OS
git clone https://github.com/augustinh22/geo-software-dev.git
set the path to the 'geo-software-dev' folder

# Step 2:Recreated both environments with conda
I recreated the 2 environments as follows:
conda env create -f software_dev_v1.yml
conda env create -f software_dev_v2.yml

**software_dev_v1 environment was not created

<img width="417" alt="image" src="https://user-images.githubusercontent.com/72496335/234009684-773c08c1-f5a2-4fe0-98c4-2d68c00c903b.png">


software_dev_v2 environment

<img width="462" alt="image" src="https://user-images.githubusercontent.com/72496335/234009021-9196bbf7-7ee8-43a6-b5fb-3c91a1329b77.png">


# Step 3:Modified v2 environment
Since software_dev_v2 was the only one created, I modified it as follows: 
Listed all packages in the environment: conda list -n software_dev_v2

**Installed a new package 'earthpy' into that environment using the conda-forge channel:
(software_dev_v2) lisahligono@Lisahs-Air A2 % conda install -c conda-forge earthpy

<img width="350" alt="image" src="https://user-images.githubusercontent.com/72496335/234010195-2091116f-ae4f-49ba-81a2-6019939070fc.png">


# Step 4:Exported the modified environment file
**First I renamed the environment to software_ligono_version
conda rename -n software_dev_v2 software_ligono_version
#Exporting
conda env export --from-history>software_ligono_version.yml

# Step 5:Commit the modified env file to PLUS_softwaredev_2023_Ligono
Folder: CondaA2
Contains the modified yml (software_ligono_vesion) and README file
