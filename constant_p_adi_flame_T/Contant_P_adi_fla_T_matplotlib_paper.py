#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @Time    : 2026/9/5 17:00
# @Author  : https://github.com/Skixkk
# @Email   : skixkk7@gmail.com
# @File    : Contant_P_adi_fla_T_matplotlib_paper.py
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
#     [功能描述] 计算 + 绘图 + 导出论文级 PDF / SVG 矢量图
#      > 矢量图无限放大无锯齿，**PDF 最适合 SCI、毕业论文；SVG 适合 Word、PPT**。
#      > 关闭 markers 圆点，学术论文曲线更干净；字体采用 Times New Roman（英文期刊标准字体）。
#     [技术架构] 
# ----------------------------------------------------------------------------
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt


def adiabatic_flame_temp(phi, T0=300, P=ct.one_atm):
    gas = ct.Solution("gri30.yaml")
    gas.set_equivalence_ratio(phi, fuel="CH4", oxidizer={"O2": 1, "N2": 3.76})
    gas.TP = T0, P
    gas.equilibrate("HP")
    return gas.T


# ---------------------- 1. 计算数据 ----------------------
phi_range = np.linspace(0.6, 1.4, 60)
T_adiab_list = [adiabatic_flame_temp(phi) for phi in phi_range]

# ---------------------- 2. 学术绘图配置（论文标准） ----------------------
# Chinese:
# plt.rcParams.update({
#     "font.sans-serif": ["SimHei"],
#     "axes.unicode_minus": False
# })
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "axes.unicode_minus": False,
    "axes.linewidth": 1.0,
    "figure.dpi": 300,
})

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(phi_range, T_adiab_list, color="#000000", linewidth=1.8)
ax.axvline(x=1.0, color="#666666", linestyle="--", linewidth=1.2, label=r"$\phi=1$ (Stoichiometric)")

ax.set_xlabel(r"Equivalence ratio $\phi$", fontsize=12)
ax.set_ylabel(r"Adiabatic flame temperature $T_{\rm ad}$ / K", fontsize=12)
# Chinese：ax.set_title("甲烷‑空气定压绝热火焰温度随当量比变化曲线", fontsize=13)
ax.set_title("Adiabatic flame temperature of methane‑air mixture", fontsize=13)
ax.grid(False)    # 期刊一般去掉网格线，如需网格改为 ax.grid(alpha=0.3)
ax.legend(loc="best", frameon=False)

plt.tight_layout()

# ---------------------- 3. 导出矢量文件 ----------------------
# PDF (优先推荐，毕业论文/期刊投稿)
plt.savefig("./dist/adiabatic_flame_temp.pdf", format="pdf", bbox_inches="tight")
# SVG (适合 Word、PPT、Visio二次编辑)
plt.savefig("./dist/adiabatic_flame_temp.svg", format="svg", bbox_inches="tight")
# 同时导出一张高清png预览图
plt.savefig("./dist/adiabatic_flame_temp.png", format="png", dpi=300, bbox_inches="tight")

plt.show()

# 输出峰值结果
max_temp = max(T_adiab_list)
max_phi = phi_range[np.argmax(T_adiab_list)]
print(f"峰值绝热火焰温度 = {max_temp:.2f} K, 对应当量比 = {max_phi:.2f}")
