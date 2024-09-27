import math as m

#Basic Inputs
Chr = str(input(" Input the character name: "))
Chr_lvl = str(input(" Input the character level: "))
Chr_skl = str(input(" Input the character skills: "))

#BDMG Parameters 基础伤害参数
#攻击力
BAP = float(input(" Input the Basic_Attack_Power: "))
#额外攻击力（绿）
ExAP = float(input(" Input the Extra_Attack_Power: "))
#技能倍率
SP = float(input(" Input the Skill_Percentage: "))

#Calculations 计算公式
#基础伤害
BDMG = (BAP + ExAP)*SP
print(BDMG)
