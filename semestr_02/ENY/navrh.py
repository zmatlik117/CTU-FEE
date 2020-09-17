# pylint: disable=invalid-name
import math
from engineering_notation import EngNumber
# parametry siti
v_nom_1 = 400000  # [V]  # not used
v_nom_2 = 110000  # [V]  # not used
s_nom_1 = 10.5e9  # [W]
s_nom_2 = 6.5e9  # [W]

# predpokladany export
export = 200e6

# zaskokove TRF
trz_uk = 0.10
trz_s = 25e6
# trz_p = 110 / 10

# odbockove TRF
tro_uk = 0.10
tro_s = 25e6
# tro_p = 13.75 / 10

# blokove TRF
trb_uk = 0.10
trb_s = 250e6
# trb_p = 400 / 13.75

# generator
gen_xd = 0.155
gen_s = 235e6

# parametry vlastni spotreby
vs = 10e6  # [MVA]
iz = 4.5
v_vs_nom = 10e3  # [V]
# nejvetsi motor ve VS
vs_mot_nejvetsi = 4e6

# maximalni pripustne hodnoty rozvodny, motoru, etc
mot_nejvetsi_min_v = 0.85 * v_vs_nom
mot_vsechny_min_v = 0.65 * v_vs_nom
mot_prov_max_v = 1.05 * v_vs_nom
mot_prov_min_v = 0.95 * v_vs_nom
rozv_max_ik0 = 25e3
rozv_max_ikm = 80e3

# koeficienty
koef_zkrat_vn = 1.1
koef_naraz_vn = 1.7
koef_zkrat_mot = 0.95

koef_zkrat_vvn = 1.1
koef_naraz_vvn = 1.7


def eval_result(a, b, val, unit, req=True):
    if a > b and req:
        print("OK %s %s%s > %s%s" % (val, EngNumber(a), unit, EngNumber(b), unit))
    else:
        print("ERR %s %s%s > %s%s" % (val, EngNumber(a), unit, EngNumber(b), unit))


def vypocet_zaskokove_vetve():
    print("zkratovy proud a vykon v zaskokove vetvi")
    sv = 20e6
    uv = 10e3
    xs = sv / s_nom_2
    xt = trz_uk * sv / trz_s
    x = xs + xt
    iv = sv / (math.sqrt(3) * uv)
    # razovy proud
    ik0 = koef_zkrat_vn * iv / x
    eval_result(rozv_max_ik0, ik0, "Ikm", "A")
    ikm = ik0 * math.sqrt(2) * koef_naraz_vn
    eval_result(rozv_max_ikm, ikm, "Ikm", "A")
    sk0 = math.sqrt(3) * uv * ik0
    print("sk0 = %sVA" % EngNumber(sk0))
    print("\nNajizdeni vsech motoru ze zaskokove vetve")
    xmot = sv / (iz * vs)
    xtot = xs + xt + xmot
    v_naj = v_vs_nom * xmot / xtot
    eval_result(v_naj, mot_vsechny_min_v, "Vnaj", "V")
    i_zb = iv / xtot
    print("Zaberny proud Iz = %sA" % EngNumber(i_zb))
    print("Pokles napeti dany nejvetsim motorem ve VS")
    xmot = sv / (iz * vs_mot_nejvetsi)
    xtot = xs + xt + xmot
    v_naj = v_vs_nom * xmot / xtot
    eval_result(v_naj, mot_nejvetsi_min_v, "Vnaj", "V")
    print("Kontrola napeti na motorech za behu")
    xmot = sv / vs
    xtot = xs + xt + xmot
    v_prov = v_vs_nom * xmot / xtot
    eval_result(v_prov, mot_prov_min_v, "V_prov", "V")
    eval_result(mot_prov_max_v, v_prov, "V_prov", "V")


def vypocet_hlavni_vetve():
    print("zkratovy proud a vykon v hlavni vetvi")
    sv = 20e6
    uv = 10e3
    xs = sv / s_nom_1
    xto = tro_uk * sv / tro_s
    xtb = trb_uk * sv / trb_s
    x_gen = gen_xd * sv / gen_s
    x_gen_tb = 1 / ((1 / x_gen) + (1 / xtb))
    x = xs + x_gen_tb + xto
    iv = sv / (math.sqrt(3) * uv)
    ik0 = koef_zkrat_vvn * iv / x
    eval_result(rozv_max_ik0, ik0, "Ikm", "A")
    ikm = ik0 * math.sqrt(2) * koef_naraz_vvn
    eval_result(rozv_max_ikm, ikm, "Ikm", "A")
    sk0 = math.sqrt(3) * uv * ik0
    print("sk0 = %sVA" % EngNumber(sk0))
    print("\nNajizdeni vsech motoru z hlavni vetve")
    xmot = sv / (iz * vs)
    xtot = xs + x_gen_tb + xto + xmot
    v_naj = v_vs_nom * xmot / xtot
    eval_result(v_naj, mot_vsechny_min_v, "Vnaj", "V")
    i_zb = iv / xtot
    print("Zaberny proud Iz = %sA" % EngNumber(i_zb))
    print("Pokles napeti dany nejvetsim motorem ve VS")
    xmot = sv / (iz * vs_mot_nejvetsi)
    xtot = xs + xto + xtb + xmot
    v_naj = v_vs_nom * xmot / xtot
    eval_result(v_naj, mot_nejvetsi_min_v, "Vnaj", "V")
    xmot = sv / vs
    print("Kontrola napeti na motorech za behu s nepripojenym generatorem")
    xmot = sv / vs
    xtot = xs + xto + xtb + xmot
    v_prov = v_vs_nom * xmot / xtot
    eval_result(v_prov, mot_prov_min_v, "V_prov", "V")
    eval_result(mot_prov_max_v, v_prov, "V_prov", "V")
    print("Kontrola napeti na motorech za behu se zatizenym generatorem")
    xmot = sv / vs
    xtot = xs + x_gen_tb + xtb + xmot
    v_prov = v_vs_nom * xmot / xtot
    eval_result(v_prov, mot_prov_min_v, "V_prov", "V")
    eval_result(mot_prov_max_v, v_prov, "V_prov", "V")


def vypocet_export_proudu():
    print("Export proud pri maximalnim Pout")
    for nom in (v_nom_1, v_nom_2):
        i_exp = export / (math.sqrt(3) * nom)
        print("Iexp pro %sV nominal = %sA" % (EngNumber(nom), EngNumber(i_exp)))


def vypocet_import_vs():
    print("Import na VS pres ZS")
    for nom in (v_nom_1, v_nom_2):
        i_imp = trz_s / (math.sqrt(3) * nom)
        print("I vs pro %sV nominal = %sA" % (EngNumber(nom), EngNumber(i_imp)))


def zkrat_na_gen():
    print("Zkrat na generatoru")
    sv = 25e6
    uv1 = 13.75e3
    uv2 = 10e3
    xs = sv / s_nom_1
    xto = tro_uk * sv / tro_s
    xtb = trb_uk * sv / trb_s
    x_gen = gen_xd * sv / gen_s
    xmot = sv / (iz * vs)
    x_sit = xs + xtb + x_gen
    iv1 = sv / (math.sqrt(3) * uv1)
    i_sit = iv1 / x_sit
    iv2 = sv / (math.sqrt(3) * uv2 * koef_zkrat_mot)
    i_ot = iv2 / xto + xmot
    ik0 = i_sit + i_ot
    print("Ik0s = %sA, Ik0OT = %sA, Ik0 = %sA" % (EngNumber(i_sit), EngNumber(i_ot), EngNumber(ik0)))
    sk0 = math.sqrt(3) * uv1 * ik0
    print("Zkratovy vykon Sk0 = %sVA" % EngNumber(sk0))


def prepojeni_vyvod_zaskok():
    sv = 25e6
    uv = 10e3
    xot = 0.1
    xzt = 0.1
    xg = gen_xd * sv / gen_s
    xs = vs / s_nom_2
    x_mot = vs / (iz * vs)
    u_mot = uv * x_mot / (xg + xot + x_mot)
    print("Napeti na motorech kdyz gen vykryva VS Umot = %sV" % EngNumber(u_mot))
    eval_result(u_mot, mot_vsechny_min_v, "Vmot", "V")

    xtot = 1 / ((1 / (xg + xot)) + (1 / (xs + xzt))) + x_mot
    iv = sv / ((uv) * math.sqrt(3))
    i_prep = iv / xtot
    print("Proud pri prepnuti vyvod -> zaskok Iprep = %sA" % EngNumber(i_prep))
    s_prep = i_prep * uv * math.sqrt(3)
    print("Vykon pri prepnuti vyvod -> zaskok Sprep = %sVA" % EngNumber(s_prep))


def prepojeni_zaskok_vyvod():
    sv = 25e6
    uv = 10e3
    xot = 0.1
    xbt = 0.01
    xg = gen_xd * sv / gen_s
    xs = vs / s_nom_1
    x_mot = vs / (iz * vs)
    u_mot = uv * x_mot / (xg + xot + x_mot)
    print("Napeti na motorech kdyz gen vykryva VS Umot = %sV" % EngNumber(u_mot))
    eval_result(u_mot, mot_vsechny_min_v, "Vmot", "V")

    xtot = 1 / ((1 / (xg + xot)) + (1 / (xs + xbt))) + x_mot
    iv = sv / ((uv) * math.sqrt(3))
    i_prep = iv / xtot
    print("Proud pri prepnuti zaskok -> vyvod Iprep = %sA" % EngNumber(i_prep))
    s_prep = i_prep * uv * math.sqrt(3)
    print("Vykon pri prepnuti zaskok -> vyvod Sprep = %sVA" % EngNumber(s_prep))


vypocet_export_proudu()
print()
vypocet_import_vs()
print()
vypocet_zaskokove_vetve()
print()
vypocet_hlavni_vetve()
print()
zkrat_na_gen()
print()
prepojeni_vyvod_zaskok()
print()
prepojeni_zaskok_vyvod()
