import os
import json
import ast

import matplotlib.pyplot as plt


path = "log.txt"

def extract_from_parenthesis(line):
    return ast.literal_eval(line[line.find("{"):line.find("}")+1])

def parse_lines(path):
    train_dics = []
    val_dics = []
    with open(path, "r") as f:
        for line in f:
            if "breakdown" in line:
                if "Train" in line:
                    train_dics.append(extract_from_parenthesis(line))
                elif "Val" in line:
                    val_dics.append(extract_from_parenthesis(line))
    return train_dics, val_dics
    
def plot_key(train, val, key, y_label, y_lim, title, save_path):
    x = list(range(len(train)))
    y_train = [dic[key] for dic in train]
    y_val = [dic[key] for dic in val]
    plt.figure()
    plt.plot(x, y_train, label="Train")
    plt.plot(x, y_val, label="Val")
    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel(y_label)
    plt.ylim(0, y_lim)
    plt.legend()
    plt.savefig(save_path)
    
    
if __name__ == "__main__":
    train_dics, val_dics = parse_lines(path)
    plot_key(train_dics, val_dics, key="perf", y_label="Cycle count", y_lim=12.74, title="Normalized Cycle Count vs Epoch", save_path="perf.png")
    plot_key(train_dics, val_dics, key="util-LUT", y_label="LUT", y_lim=2.23, title="LUT vs Epoch", save_path="lut.png")
    plot_key(train_dics, val_dics, key="util-FF", y_label="FF", y_lim=1.66, title="FF vs Epoch", save_path="ff.png")
    plot_key(train_dics, val_dics, key="util-DSP", y_label="DSP", y_lim=4.19, title="DSP vs Epoch", save_path="dsp.png")
    plot_key(train_dics, val_dics, key="util-BRAM", y_label="BRAM", y_lim=1.72, title="BRAM vs Epoch", save_path="bram.png")