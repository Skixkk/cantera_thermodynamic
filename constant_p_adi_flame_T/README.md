# 中文 matplotlib

```
plt.rcParams.update({
    "font.sans-serif": ["SimHei"],
    "axes.unicode_minus": False,
    "axes.linewidth": 1.0,
    "figure.dpi": 300
})
ax.set_xlabel(r"当量比 $\phi$", fontsize=12)
ax.set_ylabel(r"绝热火焰温度 $T_{\rm ad}$ / K", fontsize=12)
ax.set_title("不同反应机理下甲烷‑空气绝热火焰温度对比", fontsize=13)

```