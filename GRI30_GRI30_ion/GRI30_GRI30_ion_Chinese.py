#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @Time    : 2026/9/5 17:19
# @Author  : https://github.com/Skixkk
# @Email   : skixkk7@gmail.com
# @File    : GRI30_GRI30_ion_Chinese.py
# @Version : 0.0.1 (SemVer规范：主版本.次版本.修订号)
# @Project : cantera_thermodynamic
# @IDE     : PyCharm 
# ----------------------------------------------------------------------------
# 协作规范区
# @Dependencies: 
#     - requests>=2.25.1 (通过`requirements.txt`管理)
#     - package<version (版本冲突规避说明将在此写明，如无则通过`requirements.txt`配置)
# @finish      : 
#     - [高优先级] 示例：实现多线程优化 (负责人: @Skixkk)
#     - [待评审] 示例：重构数据验证逻辑XXX (截止日期: 2026-0X-XX)
# ----------------------------------------------------------------------------
# 法律声明区
# @License     : MIT
# @SPDX-License-Identifier: MIT
# @Copyright   : Copyright (c) 2026 by Skixkk , All Rights Reserved
# @Description : [Functional description of the file]
#     [功能描述] 
#     [技术架构] 
# ----------------------------------------------------------------------------
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def calc_adiabatic_temp(phi, mechanism, T0=300.0, P=ct.one_atm):
    gas = ct.Solution(mechanism)
    gas.set_equivalence_ratio(phi, fuel="CH4", oxidizer={"O2": 1, "N2": 3.76})
    gas.TP = T0, P
    gas.equilibrate("HP")
    return gas.T


# 自动创建输出文件夹
out_dir = Path("./dist")
out_dir.mkdir(exist_ok=True)

phi_array = np.linspace(0.6, 1.4, 60)

mech_list = [
    {"name": "GRI‑3.0",      "file": "gri30.yaml",     "color": "#000000"},
    {"name": "GRI‑30‑ion",   "file": "gri30_ion.yaml", "color": "#d62728"}
]

results = []
for mech in mech_list:
    print(f"正在计算机理: {mech['name']}")
    temp_data = [calc_adiabatic_temp(phi, mech["file"]) for phi in phi_array]
    results.append({"label": mech["name"], "T": temp_data, "color": mech["color"]})


# ===================== 中文绘图配置 =====================
plt.rcParams.update({
    "font.sans-serif": ["SimHei"],
    "axes.unicode_minus": False,
    "axes.linewidth": 1.0,
    "figure.dpi": 300
})

fig, ax = plt.subplots(figsize=(8, 5))

for res in results:
    ax.plot(phi_array, res["T"], color=res["color"], linewidth=1.8, label=res["label"])

ax.axvline(x=1.0, color="#666666", linestyle="--", linewidth=1.2, label=r"$\phi=1$（化学计量比）")

ax.set_xlabel(r"当量比 $\phi$", fontsize=12)
ax.set_ylabel(r"绝热火焰温度 $T_{\rm ad}$ / K", fontsize=12)
ax.set_title("不同反应机理下甲烷‑空气绝热火焰温度对比", fontsize=13)

ax.grid(False)
ax.legend(loc="best", frameon=False)

plt.tight_layout()

# 导出矢量图
plt.savefig(out_dir / "gri30_vs_gri30ion_Tad_中文.pdf", format="pdf", bbox_inches="tight")
plt.savefig(out_dir / "gri30_vs_gri30ion_Tad_中文.svg", format="svg", bbox_inches="tight")
plt.savefig(out_dir / "gri30_vs_gri30ion_Tad_中文.png", format="png", dpi=300, bbox_inches="tight")

plt.show()

# 峰值打印
for res in results:
    t_max = max(res["T"])
    phi_max = phi_array[np.argmax(res["T"])]
    print(f"\n{res['label']}:")
    print(f"    峰值温度 = {t_max:.2f} K, 对应 phi = {phi_max:.2f}")
