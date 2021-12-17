# VennDiagramMaker
Makes heatmaps and venn diagrams of data across groups. Data with replicates should be averaged before using this program.

__________________
Command line usage:
python3 path/to/downloaded/main.py

When prompted, provide path to datafile. Example datafile is in this folder.
When prompted, select task. Results will populate in downloads folder in folder called “ProteinAnalysis”. When the program runs again, this will be written over unless it is renamed.

__________________
Intended use:
Data where values greater than 0 are "increased" and values less than 0 are "decreased". This program was created with log2(foldChange) in mind.

__________________
InputFile recommendations:
Do not use "/", in any group names. Consider replacing any "/"s with "-"s.
