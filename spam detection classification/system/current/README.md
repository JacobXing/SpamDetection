## 1.0 Malicious Twitter User Classification
A series of python programs designed to facilitate the classification of malicious twitter users utilizing the honeypot dataset.

The programs can be conceputualized as a pipeline of operations, with each operation occupying it's own discrete script. This design is reflected to a high degree within the "scripts" and "python_notebooks" subdirectories. Each operation within the pipeline exists as a standalone script capable of executing independantly of it's sibling scripts, and bar the preprocessing script, is coupled with it's own configuration file allowing for parameter control over a given scripts relevant operations.

The preprocessing script seeks to import the raw data sets, preprocess the static and dynamic feature sets and ensure these feature sets correspond accurately to one another. The feature engineering script seeks to generate the finalized, dynamic features. The clustering script seeks to consolidate the static and dynamic features into a master dataframe, perform clustering using a selection of features and segment the master dataframe based upon this clustering outcome. The classification script seeks to train and test a variety of classification methods upon each of the previously segmented, clustered datasets. Finally, a wrapper script is capable of executing combinations and subsets of these scripts as desired to improve the iterative capacity of the system (eg. perform classification exclusively, multiple times, once a suitable set of features has been generated).

It's useful to know that at each stage of the pipeline, the data is saved in intermediate forms. These forms are also reflected to a high degree within the parralel "data" directory. Raw, preprocessed and final forms of the data set exist, changing based upon the appropriate user input (eg. the number of cluster frames is determined by the number of clusters specified within the clustering script config).
## 1.1 Project Structure Notes
The project has been segmented based upon code and data concerns. Within the code subdirectory exists an output folder, which serves as the final destination of the classification script, as well as directories containing each of the scripts as a standalone python scripts (scripts) as well as jupyter notebook variations of these scripts (python_notebooks). This has been done to provide flexibility during the development and experiment phase of system use. A suggested workflow is to utilize the jupyter notebooks to quickly prototype changes, before formalizing these changes within the pure python scripts (ensuring portability and reducing dependencies between machines). Though of course, feel free to chop/change utilize components as necessary.

Within the data_sets subdirectory exists folders for both the honeypot and 14 million tweets datasets and their intermediate processing variations. The honey pot dataset comprised the main focus of this project, though it would be desireable to preprocess the 14 million tweets dataset into a similar format to the honeypot dataset to allow the rest of the pipeline scripts to be applied to this alternative dataset.
## 2.0 Getting Started
There are a variety of ways to get started with the software, these approaches are detailed below. Whilst virtual environment configuration is recommended methods 2.1 and 2.2, they are not entirely necessary, however the specified dependencies will take effect within the global environment, perhaps altering existing module configurations.
## 2.1 Standard Env
Create a new virtual environment to contain the projects dependencies. Activate the environment and ensure pip3 and python 3.6 is installed for use. Run the following script within the top-level directory of the project to install dependant libraries:
```
pip3 install -r requirements.txt
```
Once complete, install NLTK dependency requirements via:
```
python3 -m nltk.downloader all
```
This approach provides the user flexibility to run the vanilla scripts, and to also utilize jupyter notebooks (provided Jupyter notebooks is installed, additional steps required for this).
## 2.2 Anaconda Env
Create a new conda virtual environment to contain the projects dependencies. Ensure python 3.6 is installed and the environment has been activated. Retrieve relevant dependencies using following syntax:
```
conda install -n <env_name> <package>
```
Required packages listed within requirements.txt dependency file, be sure to include the specific build version within the <package> specification as it is contained within this requirements file. Install the NLTK dependency requirements in the same way as specified by the standard env installation.

This approach is the most straight forward and guaranteed way as Anaconda packages Jupyter notebooks as well as Spyder (Python IDE) within each installation/virtual installation, allowing the user to run the vanilla scripts as well as to utilize Jupyter notebooks and the Spyder IDE. Highly Recommended as a "one stop shop" for data needs.
## 2.2 Docker Env
Build and run the provided docker image (Ubuntu 16.04 base) in the usual fashion. Execution of the scripts and combinations of them can be run within the container in the usual way:
```
python3 <script_name>
```
Docker file locates to within the code/scripts subdirectory. This approach does not currently allow for the use of Jupyter notebooks.
## 3.0 Built With
Generally; Anaconda 4.3.24, Python 3.6.0, Jupyter 4.2.1.
Specifically; scipy 0.19.1, numpy 1.13.1, pandas 0.20.3, sklearn 0.19.0, nltk 3.2.2.
## 4.0 Authors
Sam Hardy - Implementation.
## 4.1 Acknowledgments ##
Yue Xu (QUT professor), for her superverision and technical guidance during the VRES project period.
## 4.2 Relevant Resources ##
| Title  | Link  |
| ------------- | ----- |
|Creating new conda virtual environment| https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/ |
|Creating virtual environments outside of Conda | https://docs.python.org/3/tutorial/venv.html |

