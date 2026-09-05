#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @Time    : 2026/9/5 16:58
# @Author  : https://github.com/Skixkk
# @Email   : skixkk7@gmail.com
# @File    : Contant_P_adi_fla_T_matplotlib.py
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
#     [功能描述] 当量比‑绝热火焰温度 + Matplotlib 绘图
#     [技术架构] 
# ----------------------------------------------------------------------------
import cantera as ct
import numpy as np
import matplotlib.pyplot as plt


def adiabatic_flame_temp(phi, T0=300, P=ct.one_atm):
    """
    计算给定当量比下甲烷‑空气定压绝热火焰温度
    :param phi: 当量比
    :param T0: 反应物初始温度 K
    :param P: 压力 Pa
    :return: 绝热火焰温度 K
    """
    gas = ct.Solution("gri30.yaml")
    gas.set_equivalence_ratio(phi, fuel="CH4", oxidizer={"O2": 1, "N2": 3.76})
    gas.TP = T0, P
    gas.equilibrate("HP")   # 定焓定压 = 定压绝热燃烧
    return gas.T


# ---------------------- 1. 计算数据 ----------------------
phi_range = np.linspace(0.6, 1.4, 40)   # 当量比范围 0.6~1.4，取40个点
T_adiab_list = []

for phi in phi_range:
    Tad = adiabatic_flame_temp(phi)
    T_adiab_list.append(Tad)

# ---------------------- 2. 绘图 ----------------------
plt.rcParams["font.sans-serif"] = ["SimHei"]   # 显示中文
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(8, 5))
plt.plot(phi_range, T_adiab_list, color="#1f77b4", linewidth=2.2, marker="o", markersize=3)

plt.axvline(x=1.0, color="red", linestyle="--", label="化学计量比 $\\phi=1$")

plt.xlabel("当量比 $\\phi$", fontsize=12)
plt.ylabel("绝热火焰温度 $T_{ad}$ / K", fontsize=12)
plt.title("甲烷‑空气定压绝热火焰温度随当量比变化曲线", fontsize=13)
plt.grid(True, alpha=0.35)
plt.legend()
plt.tight_layout()
plt.show()

# 打印峰值温度
max_temp = max(T_adiab_list)
max_phi = phi_range[np.argmax(T_adiab_list)]
print(f"\n峰值绝热火焰温度 = {max_temp:.2f} K, 对应当量比 = {max_phi:.2f}")
