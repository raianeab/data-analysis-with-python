import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1) Import the data from medical_examination.csv
df = pd.read_csv("medical_examination.csv")

# 2) Add a column to determine if a person is overweight (BMI > 25 → 1, else 0)
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3) Normalize cholesterol and gluc (1 → good, >1 → bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4) Draw the Categorical Plot
def draw_cat_plot():
    # 5) Create melted DataFrame with cardio as id_vars and categorical features as value_vars
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6) Draw categorical plot (countplot split by cardio)
    catplot = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',
        hue='value',
        col='cardio'
    )

    # 7) Customize labels, legend, and titles
    catplot.set_axis_labels("variable", "total")
    catplot._legend.set_title("value")
    catplot.set_titles("cardio = {col_name}")

    # 8) Return figure
    fig = catplot.fig
    return fig


# 9) Draw the Heat Map
def draw_heat_map():
    # 10) Clean data with filtering rules
    height_low = df['height'].quantile(0.025)
    height_high = df['height'].quantile(0.975)
    weight_low = df['weight'].quantile(0.025)
    weight_high = df['weight'].quantile(0.975)

    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= height_low) &
        (df['height'] <= height_high) &
        (df['weight'] >= weight_low) &
        (df['weight'] <= weight_high)
    ].copy()

    # 11) Calculate correlation matrix
    corr = df_heat.corr()

    # 12) Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13) Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 14) Draw seaborn heatmap with annotations
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        linewidths=.5,
        square=True,
        cbar_kws={"shrink": .5},
        ax=ax,
        center=0
    )

    # 15) Return figure
    return fig


# 16) Allow direct execution to save plots
if __name__ == "__main__":
    # Draw and save Cat Plot
    fig1 = draw_cat_plot()
    fig1.savefig("catplot.png")
    print("catplot.png salvo.")

    # Draw and save Heat Map
    fig2 = draw_heat_map()
    fig2.savefig("heatmap.png")
    print("heatmap.png salvo.")
