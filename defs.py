import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
import shutil
from matplotlib_venn import venn2, venn3
from venn import venn

def heatmap(df,path):
    figy = len(df.index) * 0.9
    figx = len(df.index) * 0.6
    col = len(df.columns)
    heatmapdf = df.iloc[:, 1:col]
    sns.set(font_scale=15)
    plt.figure(figsize=(figx, figy), frameon=True)
    sns.heatmap(heatmapdf, annot=False, cmap="vlag", center=0)
    name = input("Name your heat map file (no spaces please):")
    HMpath = os.path.join(path, name)
    plt.savefig(HMpath)
    print(HMpath)
    plt.clf()
    print("Saved heat map\n")


def findPath():
    # Finding paths, creating paths, saving heatmap
    downloads_path = str(Path.home() / "Downloads")
    directory = "ProteinAnalysis"
    path = os.path.join(downloads_path, directory)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    return path


def twoVenn(dfvd,path,list1):

    comparison_column = np.where((dfvd[list1[0]] > 0) & (dfvd[list1[1]] > 0), dfvd.index, False)
    overlap = np.count_nonzero(comparison_column)
    comparison_column = np.delete(comparison_column, np.argwhere(comparison_column == False))

    total0col = np.where((dfvd[list1[0]] > 0), True, False)
    total0colb = np.where((dfvd[list1[0]] > 0), dfvd.index, False)
    total0colb = np.delete(total0colb, np.argwhere(total0col == False))

    total1col = np.where((dfvd[list1[1]] > 0), True, False)
    total1colb = np.where((dfvd[list1[1]] > 0), dfvd.index, False)
    total1colb = np.delete(total1colb, np.argwhere(total1col == False))

    total0 = len(dfvd[total0col].value_counts())
    total1 = len(dfvd[total1col].value_counts())

    outside0 = total0 - overlap
    outside1 = total1 - overlap

    venn2(subsets=(outside0, outside1, overlap), set_labels=(list1[0], list1[1]))

    VDpath = os.path.join(path, list1[0]+"-"+ list1[1]+ "-increase")
    plt.savefig(VDpath)
    VDpath2 = (VDpath + "-Data.xlsx")

    total0colc = pd.DataFrame({list1[0]: total0colb})
    total1colc = pd.DataFrame({list1[1]: total1colb})
    comparison_columnc = pd.DataFrame({'Overlap': comparison_column})

    output1 = pd.concat([total0colc, total1colc, comparison_columnc], axis=1)
    output1.to_excel(VDpath2, index=False)
    plt.clf()
    plt.close()

    comparison_column = np.where((dfvd[list1[0]] < 0) & (dfvd[list1[1]] < 0), dfvd.index, False)
    overlap = np.count_nonzero(comparison_column)
    comparison_column = np.delete(comparison_column, np.argwhere(comparison_column == False))

    total0col = np.where((dfvd[list1[0]] < 0), True, False)
    total0colb = np.where((dfvd[list1[0]] < 0), dfvd.index, False)
    total0colb = np.delete(total0colb, np.argwhere(total0col == False))

    total1col = np.where((dfvd[list1[1]] < 0), True, False)
    total1colb = np.where((dfvd[list1[1]] < 0), dfvd.index, False)
    total1colb = np.delete(total1colb, np.argwhere(total1col == False))

    total0 = len(dfvd[total0col].value_counts())
    total1 = len(dfvd[total1col].value_counts())

    outside0 = total0 - overlap
    outside1 = total1 - overlap

    venn2(subsets=(outside0, outside1, overlap), set_labels=(list1[0], list1[1]))

    VDpath = os.path.join(path, list1[0] + "-" + list1[1]+"-decrease")
    plt.savefig(VDpath)
    VDpath2 = (VDpath + "-Data.xlsx")

    total0colc = pd.DataFrame({list1[0]: total0colb})
    total1colc = pd.DataFrame({list1[1]: total1colb})
    comparison_columnc = pd.DataFrame({'Overlap': comparison_column})

    output1 = pd.concat([total0colc, total1colc, comparison_columnc], axis=1)
    output1.to_excel(VDpath2, index=False)
    plt.clf()
    plt.close()


def threeVenn(dfvd,path,list1):

    comparison_column = np.where((dfvd[list1[0]] > 0) & (dfvd[list1[1]] > 0) & (dfvd[list1[2]] > 0), dfvd.index, False)
    comparison_column0 = np.where((dfvd[list1[0]] > 0) & (dfvd[list1[1]] > 0), dfvd.index, False)
    comparison_column1 = np.where((dfvd[list1[1]] > 0) & (dfvd[list1[2]] > 0), dfvd.index, False)
    comparison_column2 = np.where((dfvd[list1[2]] > 0) & (dfvd[list1[0]] > 0), dfvd.index, False)

    overlap = np.count_nonzero(comparison_column)
    overlap0 = np.count_nonzero(comparison_column0) - overlap
    overlap1 = np.count_nonzero(comparison_column1) - overlap
    overlap2 = np.count_nonzero(comparison_column2) - overlap

    comparison_column = np.delete(comparison_column, np.argwhere(comparison_column == False))
    comparison_column0 = np.delete(comparison_column0, np.argwhere(comparison_column0 == False))
    comparison_column1 = np.delete(comparison_column1, np.argwhere(comparison_column1 == False))
    comparison_column2 = np.delete(comparison_column2, np.argwhere(comparison_column2 == False))

    total0col = np.where((dfvd[list1[0]] > 0), True, False)
    total0colb = np.where((dfvd[list1[0]] > 0), dfvd.index, False)
    total0colb = np.delete(total0colb, np.argwhere(total0col == False))

    total1col = np.where((dfvd[list1[1]] > 0), True, False)
    total1colb = np.where((dfvd[list1[1]] > 0), dfvd.index, False)
    total1colb = np.delete(total1colb, np.argwhere(total1col == False))

    total2col = np.where((dfvd[list1[2]] > 0), True, False)
    total2colb = np.where((dfvd[list1[2]] > 0), dfvd.index, False)
    total2colb = np.delete(total2colb, np.argwhere(total2col == False))

    total0 = np.count_nonzero(total0col)
    total1 = np.count_nonzero(total1col)
    total2 = np.count_nonzero(total2col)

    outside0 = total0 - overlap0 - overlap2 - overlap
    outside1 = total1 - overlap0 - overlap1 - overlap
    outside2 = total2 - overlap1 - overlap2 - overlap

    venn3(subsets=(outside0, outside1, overlap0, outside2, overlap2, overlap1, overlap), set_labels=(list1[0], list1[1], list1[2]))
    VDpath = os.path.join(path, list1[0]+"-"+list1[1]+"-"+list1[2] + "-increase")
    plt.savefig(VDpath)
    VDpath2 = (VDpath + "-Data.xlsx")
    plt.clf()
    plt.close()

    total0colc = pd.DataFrame({list1[0]: total0colb})
    total1colc = pd.DataFrame({list1[1]: total1colb})
    total2colc = pd.DataFrame({list1[2]: total2colb})

    comparison_columnc_name = list1[0] + "-" + list1[1] + "-" + list1[2] + "-Overlap"
    comparison_columnc = pd.DataFrame({comparison_columnc_name: comparison_column})

    comparison_column0_name = list1[0] + "-" + list1[1] + "-" + "-Overlap"
    comparison_column0c = pd.DataFrame({comparison_column0_name: comparison_column0})

    comparison_column1_name = list1[1] + "-" + list1[2] + "-" + "-Overlap"
    comparison_column1c = pd.DataFrame({comparison_column1_name: comparison_column1})

    comparison_column2_name = list1[2] + "-" + list1[0] + "-" + "-Overlap"
    comparison_column2c = pd.DataFrame({comparison_column2_name: comparison_column2})

    output1 = pd.concat([total0colc, total1colc, total2colc, comparison_columnc, comparison_column0c, comparison_column1c, comparison_column2c], axis=1)
    output1.to_excel(VDpath2, index=False)

    comparison_column = np.where((dfvd[list1[0]] < 0) & (dfvd[list1[1]] < 0) & (dfvd[list1[2]] < 0), dfvd.index,
                                 False)
    comparison_column0 = np.where((dfvd[list1[0]] < 0) & (dfvd[list1[1]] < 0), dfvd.index, False)
    comparison_column1 = np.where((dfvd[list1[1]] < 0) & (dfvd[list1[2]] < 0), dfvd.index, False)
    comparison_column2 = np.where((dfvd[list1[2]] < 0) & (dfvd[list1[0]] < 0), dfvd.index, False)

    overlap = np.count_nonzero(comparison_column)
    overlap0 = np.count_nonzero(comparison_column0) - overlap
    overlap1 = np.count_nonzero(comparison_column1) - overlap
    overlap2 = np.count_nonzero(comparison_column2) - overlap

    comparison_column = np.delete(comparison_column, np.argwhere(comparison_column == False))
    comparison_column0 = np.delete(comparison_column0, np.argwhere(comparison_column0 == False))
    comparison_column1 = np.delete(comparison_column1, np.argwhere(comparison_column1 == False))
    comparison_column2 = np.delete(comparison_column2, np.argwhere(comparison_column2 == False))

    total0col = np.where((dfvd[list1[0]] < 0), True, False)
    total0colb = np.where((dfvd[list1[0]] < 0), dfvd.index, False)
    total0colb = np.delete(total0colb, np.argwhere(total0col == False))

    total1col = np.where((dfvd[list1[1]] < 0), True, False)
    total1colb = np.where((dfvd[list1[1]] < 0), dfvd.index, False)
    total1colb = np.delete(total1colb, np.argwhere(total1col == False))

    total2col = np.where((dfvd[list1[2]] < 0), True, False)
    total2colb = np.where((dfvd[list1[2]] < 0), dfvd.index, False)
    total2colb = np.delete(total2colb, np.argwhere(total2col == False))

    total0 = np.count_nonzero(total0col)
    total1 = np.count_nonzero(total1col)
    total2 = np.count_nonzero(total2col)

    outside0 = total0 - overlap0 - overlap2 - overlap
    outside1 = total1 - overlap0 - overlap1 - overlap
    outside2 = total2 - overlap1 - overlap2 - overlap

    venn3(subsets=(outside0, outside1, overlap0, outside2, overlap2, overlap1, overlap),
          set_labels=(list1[0], list1[1], list1[2]))
    VDpath3 = os.path.join(path, list1[0]+"-"+list1[1]+"-"+list1[2]+ "-decrease")
    plt.savefig(VDpath3)
    VDpath4 = (VDpath3 + "-Data.xlsx")
    plt.clf()
    plt.close()

    total0colc = pd.DataFrame({list1[0]: total0colb})
    total1colc = pd.DataFrame({list1[1]: total1colb})
    total2colc = pd.DataFrame({list1[2]: total2colb})

    comparison_columnc_name = list1[0] + "-" + list1[1] + "-" + list1[2] + "-Overlap"
    comparison_columnc = pd.DataFrame({comparison_columnc_name: comparison_column})

    comparison_column0_name = list1[0] + "-" + list1[1] + "-" + "-Overlap"
    comparison_column0c = pd.DataFrame({comparison_column0_name: comparison_column0})

    comparison_column1_name = list1[1] + "-" + list1[2] + "-" + "-Overlap"
    comparison_column1c = pd.DataFrame({comparison_column1_name: comparison_column1})

    comparison_column2_name = list1[2] + "-" + list1[0] + "-" + "-Overlap"
    comparison_column2c = pd.DataFrame({comparison_column2_name: comparison_column2})

    output1 = pd.concat(
        [total0colc, total1colc, total2colc, comparison_columnc, comparison_column0c, comparison_column1c,
         comparison_column2c], axis=1)
    output1.to_excel(VDpath4, index=False)


def fourVenn(dfvd,path,list1):
    #increased
    total0colV = np.where((dfvd[list1[0]] > 0), dfvd.index, False)
    total1colV = np.where((dfvd[list1[1]] > 0), dfvd.index, False)
    total2colV = np.where((dfvd[list1[2]] > 0), dfvd.index, False)
    total3colV = np.where((dfvd[list1[3]] > 0), dfvd.index, False)

    total0colV = np.delete(total0colV, np.argwhere(total0colV == False))
    total1colV = np.delete(total1colV, np.argwhere(total1colV == False))
    total2colV = np.delete(total2colV, np.argwhere(total2colV == False))
    total3colV = np.delete(total3colV, np.argwhere(total3colV == False))

    dict = {}
    dict[list1[0]] = set(total0colV.flatten())
    dict[list1[1]] = set(total1colV.flatten())
    dict[list1[2]] = set(total2colV.flatten())
    dict[list1[3]] = set(total3colV.flatten())

    venn(dict)

    VDpath5 = os.path.join(path, list1[0] + "-" + list1[1] + "-" + list1[2] + "-" + list1[3] + "-increase")
    plt.savefig(VDpath5)
    plt.clf()
    plt.close()

    #decreased
    total0col = np.where((dfvd[list1[0]] < 0), dfvd.index, False)
    total1col = np.where((dfvd[list1[1]] < 0), dfvd.index, False)
    total2col = np.where((dfvd[list1[2]] < 0), dfvd.index, False)
    total3col = np.where((dfvd[list1[3]] < 0), dfvd.index, False)

    total0col = np.delete(total0col, np.argwhere(total0col == False))
    total1col = np.delete(total1col, np.argwhere(total1col == False))
    total2col = np.delete(total2col, np.argwhere(total2col == False))
    total3col = np.delete(total3col, np.argwhere(total3col == False))

    dict = {}
    dict[list1[0]] = set(total0col.flatten())
    dict[list1[1]] = set(total1col.flatten())
    dict[list1[2]] = set(total2col.flatten())
    dict[list1[3]] = set(total3col.flatten())

    venn(dict)

    VDpath6 = os.path.join(path, list1[0] + "-" + list1[1] + "-" + list1[2] + "-" + list1[3] + "-decrease")
    plt.savefig(VDpath6)
    plt.clf()
    plt.close()