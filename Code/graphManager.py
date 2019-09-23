# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


class MrGraphManager:
    def __init__(self, dataframe):
        self.df = dataframe
    def GraphSimple(self,title):
        ax = sns.boxplot(x="snapshot", y="price",
            hue="bid|buyout", palette=["b", "g"],data =self.df)
        biddf = self.df['price'][]
        ax = sns.stripplot(x='snapshot', y='price', data=self.df, color="orange", jitter=0.2, size=2.5)
        plt.title(title, loc="left")
        fig = ax.get_figure()
        fig.savefig("output.png")