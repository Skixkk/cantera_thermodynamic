#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# @Time    : 2026/9/5 16:52
# @Author  : https://github.com/Skixkk
# @Email   : skixkk7@gmail.com
# @File    : Constant_P_adiabatic_flame_T.py
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
#     [功能描述] 甲烷‑空气 定压绝热火焰温度（Constant‑pressure adiabatic flame temperature）
#     [技术架构] Cantera
# ----------------------------------------------------------------------------
import cantera as ct

"""
原理：定压绝热，反应前后焓相等 \(H_{reactants}=H_{products}\)，
Cantera equilibrate('HP') 就是固定焓 H、压力 P 求平衡态，自动算出绝热火焰温度。

1. `equilibrate('HP')` —— **定压绝热火焰温度（最常用）**
   - H：焓不变（绝热无热损失）
   - P：压力不变（定压燃烧）
2. `equilibrate('UV')` —— **定容绝热火焰温度**（密闭容器）
3. `set_equivalence_ratio(phi, fuel, oxidizer)`：自动生成燃料‑氧化剂组分，比手写 `CH4:1,O2:2...` 更方便，不容易配平出错。

"""

# ---------------------- 1. 初始化混合气 ----------------------
gas = ct.Solution('gri30.yaml')

# 初始状态：300 K，1 atm，化学计量比甲烷‑空气
# 化学计量反应 CH4 + 2 O2 + 2*3.76 N2  → CH4:1, O2:2, N2:7.52
T_in = 300.0
P_in = ct.one_atm
gas.TPX = T_in, P_in, "CH4:1, O2:2, N2:7.52"

# 保存反应物总焓（定压绝热：反应物焓 = 产物焓）
h_react = gas.h

print("=== 反应物初始状态 ===")
print(f"T_react = {gas.T:.2f} K")
print(f"P = {gas.P:.2f} Pa")
print(f"Enthalpy (molar) = {gas.h:.2f} J/mol")

# ---------------------- 2. HP平衡计算绝热火焰温度 ----------------------
# equilibrate('HP'): 保持焓H、压力P不变，达到化学平衡 → 绝热火焰温度
# 定压绝热火焰温度（最常用）
gas.equilibrate('HP')

print("\n=== 定压绝热燃烧产物（平衡态） ===")
print(f"Adiabatic Flame Temperature = {gas.T:.2f} K")
print(f"P = {gas.P:.2f} Pa")
print(f"Enthalpy (molar) = {gas.h:.2f} J/mol")
print("\n产物组分摩尔分数：")
gas()
