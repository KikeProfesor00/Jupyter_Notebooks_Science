from chempy import Substance
ferricyanide = Substance.from_formula('Fe(CN)6-3')
ferricyanide.composition == {0: -3, 26: 1, 6: 6, 7: 6}  # 0 for charge

print(ferricyanide.unicode_name)
# Fe(CN)₆³⁻

print(ferricyanide.latex_name + ", " + ferricyanide.html_name)
# Fe(CN)_{6}^{3-}, Fe(CN)<sub>6</sub><sup>3-</sup>

print('%.3f' % ferricyanide.mass)
#211.955