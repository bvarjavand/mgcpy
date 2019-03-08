import numpy as np
import pytest

from mgcpy.independence_tests.mgc import MGC


def test_mgc_sample_linear():
    X = np.array([0.07487683, -0.18073412, 0.37266440, 0.06074847, 0.76899045,
                  0.51862516, -0.13480764, -0.54368083, -0.73812644, 0.54910974]).reshape(-1, 1)
    Y = np.array([-1.31741173, -0.41634224, 2.24021815, 0.88317196, 2.00149312,
                  1.35857623, -0.06729464, 0.16168344, -0.61048226, 0.41711113]).reshape(-1, 1)

    mgc_statistic = 0.4389398
    optimal_scale = [10, 10]

    mgc = MGC()
    mgc_statistic_res, independence_test_metadata = mgc.test_statistic(X, Y)

    assert mgc.get_name() == 'mgc'
    assert np.allclose(mgc_statistic, mgc_statistic_res)
    assert np.allclose(optimal_scale, independence_test_metadata["optimal_scale"])


def test_mgc_sample_non_linear():
    mgc = MGC()

    # spiral data
    X1 = np.array([1.19076532, -4.89949601, -1.04671781, -0.78870398, -4.96541929, -3.47913731, 0.61608779, -1.04636872, 0.01792450, -2.99958358, 1.99093892, 2.02476848, -1.00291164, 3.84247195, -0.97867784, 0.06643890, -2.04553564, 3.95870375, -2.60045257, -1.04668339, -0.92919140, -2.94754180, -0.48332416, 1.26781216, 0.13068389,
                   0.17426063, 1.51532887, -0.65853037, 1.83957953, -2.47333005, 0.13855163, -3.51847437, -4.94476873, -0.99116531, 0.94505361, 0.02117659, -0.98862767, -1.04662608, -0.47863973, -4.95602679, -2.44573834, -0.57811752, 3.35735796, -2.77334193, -2.66310047, 0.12282333, 1.84287144, 3.17489424, 1.69930914, 3.24924651]).reshape(-1, 1)
    Y1 = np.array([-1.40947688, 1.04194197, 0.40771759, -3.16609585, 0.62368044, 3.77762740, 4.09967197, -0.45247854, 0.21346485, -1.51231169, 0.01814165, 0.63590620, -0.17373739, 0.88791421, 0.29489715, -0.25420314, 1.60145057, 0.70182757, -2.24325328, -0.52412790, 3.37903326, -1.25394361, -2.56437048, -1.63174998, 0.40462931,
                   1.49760321, 1.42923722, 0.23255328, 1.35751771, -2.10603089, 2.85151995, 3.03632266, 0.48248123, 0.54841016, 2.22176329, 0.77264609, 0.41259043, -0.50495140, -1.44860013, 1.20476810, -1.94893291, -1.52795955, -2.06691591, -1.83411979, 1.07099382, 0.24942774, 1.43385633, 2.94960357, -3.34529118, 3.16868061]).reshape(-1, 1)

    mgc_statistic_1 = 0.1991505
    optimal_scale_1 = [2, 6]

    mgc_statistic_res_1, independence_test_metadata_1 = mgc.test_statistic(X1, Y1)

    assert np.allclose(mgc_statistic_1, mgc_statistic_res_1)
    assert np.allclose(optimal_scale_1, independence_test_metadata_1["optimal_scale"])

    X2 = np.array([0.01421334, -2.74656298,  0.77314408,  1.16537193, -2.90519144, -4.22264528, -0.89891050,  3.84718386, -1.56702656,  0.96299667, -4.04908889,  1.23211283,  0.16186615, -2.80339400, -4.52963579,  1.50649684, -2.19419173, -0.17158617, -4.99565629,  4.00691706, -2.84808717,  2.21568866, -0.42059251, -2.72486898,  1.93019558,
                   0.17617120,  3.81677009, -0.22529392,  1.26280821,  3.86391161,  2.02327480,  1.99630927,  1.82478940, -4.44260943, -0.98931338, -2.94800338, -3.01352134, -2.25180778, -0.92833990, -0.76114888, -0.62939441, -0.98264787, -3.82053926,  1.04258668, -2.15039133, -1.03893152,  1.93208834,  1.82361258,  0.99874067,  0.24155370]).reshape(-1, 1)
    Y2 = np.array([0.038971270,  0.833857761, -1.521444608,  4.304165019, -1.020602336,  2.312007878,  0.155703456,  1.380484921,  4.254963435, -1.278597445,  2.701115622,  2.021871587,  0.456433211,  0.829949638,  1.885978521, -0.945712267, -2.407083726, -3.454198852, -0.014086007,  0.145404797,  0.670799013,  3.672285741,  0.602226433,  3.785518506, -0.350152540, -
                   1.588788123,  1.520267990, -1.409208061, -1.398139886,  1.131541762,  0.356061760,  0.002080002,  1.017373457,  2.080078016, -0.042361065, -0.973710472, -0.228119833,  1.550782393,  0.203302174, -3.383666925,  0.576408069,  0.209023397,  2.955761299, -1.346304143,  4.215744704, -0.540418117,  0.931602249, -0.445806493,  2.179037240, -1.662197212]).reshape(-1, 1)

    mgc_statistic_2 = 0.2313806
    optimal_scale_2 = [3, 4]

    mgc_statistic_res_2, independence_test_metadata_2 = mgc.test_statistic(X2, Y2)

    assert np.allclose(mgc_statistic_2, mgc_statistic_res_2)
    assert np.allclose(optimal_scale_2, independence_test_metadata_2["optimal_scale"])
