# hsr_af_fangame

## mechanics.py

# changeSkillPoints(change)

takes change as a variable, where change is the amount of skill points added/removed after action.
change should be 1 in case of normal attack, or -1 in case of skill, etc.
if skill points get increased, they cannot surpass MAX_SP, if decreased, cannot go below 0
