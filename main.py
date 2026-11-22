
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("train.csv")

# Data preprocessing
df["trip_duration_minutes"] = df["trip_duration"] / 60

data = df[
    (df["trip_duration_minutes"] > 0) &
    (df["trip_duration_minutes"] < 60)
]["trip_duration_minutes"].dropna()

# Statistical calculations
mean = data.mean()
median = data.median()
std = data.std()

print("\n🚕 NYC TAXI TRIP ANALYSIS")
print("=" * 35)
print(f"Total Trips       : {len(data):,}")
print(f"Mean Duration    : {mean:.2f} minutes")
print(f"Median Duration  : {median:.2f} minutes")
print(f"Std Deviation    : {std:.2f} minutes")
print(f"Skewness         : {data.skew():.2f}")
print("=" * 35)

# Dark theme
sns.set_theme(style="darkgrid", context="talk")

plt.rcParams.update({
    "figure.facecolor": "#0B1120",
    "axes.facecolor": "#111827",
    "axes.edgecolor": "#334155",
    "text.color": "#F8FAFC",
    "axes.labelcolor": "#CBD5E1",
    "xtick.color": "#94A3B8",
    "ytick.color": "#94A3B8",
    "grid.color": "#334155"
})

# Matplotlib visualization
fig, ax = plt.subplots(figsize=(13, 7))

sns.histplot(
    data,
    bins=60,
    kde=True,
    color="#00D4FF",
    edgecolor="#0B1120",
    alpha=0.8,
    line_kws={"color": "#A78BFA", "linewidth": 2.5},
    ax=ax
)

# Mean and median
ax.axvline(
    mean, color="#FF6B9A",
    linestyle="--", linewidth=2.5,
    label=f"Mean: {mean:.2f} min"
)

ax.axvline(
    median, color="#FFD166",
    linestyle="-.", linewidth=2.5,
    label=f"Median: {median:.2f} min"
)

# Statistics box
ax.text(
    0.97, 0.95,
    f"Total Trips: {len(data):,}\n"
    f"Mean: {mean:.2f} min\n"
    f"Median: {median:.2f} min\n"
    f"Std Dev: {std:.2f} min",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top",
    horizontalalignment="right",
    bbox=dict(
        boxstyle="round,pad=0.6",
        facecolor="#1E293B",
        edgecolor="#00D4FF",
        alpha=0.9
    )
)

ax.set_title(
    "NYC TAXI TRIP DURATION DISTRIBUTION",
    fontsize=19,
    fontweight="bold",
    color="#00D4FF",
    pad=20
)

ax.set_xlabel("Trip Duration (Minutes)")
ax.set_ylabel("Number of Trips")
ax.set_xlim(0, 60)

ax.legend(
    facecolor="#1E293B",
    edgecolor="#334155",
    labelcolor="white"
)

sns.despine()
plt.tight_layout()
plt.show()

# Interactive Plotly visualization
fig = px.histogram(
    data_frame=df[
        df["trip_duration_minutes"].between(0, 60, inclusive="neither")
    ],
    x="trip_duration_minutes",
    nbins=60,
    marginal="violin",
    opacity=0.85,
    title="NYC Taxi Trip Duration Analysis",
    labels={"trip_duration_minutes": "Trip Duration (Minutes)"},
    template="plotly_dark",
    color_discrete_sequence=["#00D4FF"],
    hover_data={"trip_duration_minutes": ":.2f"}
)

fig.add_vline(
    x=mean,
    line_dash="dash",
    line_color="#FF6B9A",
    annotation_text="Mean"
)

fig.add_vline(
    x=median,
    line_dash="dot",
    line_color="#FFD166",
    annotation_text="Median"
)

fig.update_layout(
    title_x=0.5,
    title_font_size=22,
    paper_bgcolor="#0B1120",
    plot_bgcolor="#111827",
    font_color="#F8FAFC",
    bargap=0.04,
    hoverlabel=dict(
        bgcolor="#1E293B",
        font_size=13
    )
)

fig.update_xaxes(
    showgrid=True,
    gridcolor="#334155",
    range=[0, 60]
)

fig.update_yaxes(
    showgrid=True,
    gridcolor="#334155"
)

fig.show()
