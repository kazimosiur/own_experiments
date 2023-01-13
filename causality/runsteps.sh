#!/bin/bash

#install jupyter and dependents
conda install jupyter -y
pip install --upgrade jupyter
conda install -c conda-forge jupyter_contrib_nbextensions -y

# to handle the 500:INTERNAL SERVER ERROR PROBLEM
conda install nbconvert==5.4.1 -y

#install causal elements
conda install networkx -y
conda install -c conda-forge dowhy -y
conda install matplotlib -y
conda install tqdm -y
conda install pygraphviz - y
pip3 install pygraphviz

