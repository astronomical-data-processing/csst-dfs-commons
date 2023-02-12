PI = 3.14159265358979323846

UPLOAD_CHUNK_SIZE = 16*1024

STATUS_SUCESS = 0

REF_TYPE_BIAS = "bias"
REF_TYPE_DARK = "dark"
REF_TYPE_FlAT = "flat"
REF_TYPE_ARC = "arc"
REF_TYPE_LAMP = "lamp"
REF_TYPE_SKY = "sky"

REF_TYPES = (REF_TYPE_BIAS, REF_TYPE_DARK, REF_TYPE_FlAT, REF_TYPE_ARC, REF_TYPE_LAMP, REF_TYPE_SKY)

OBS_TYPE_SCI = "sci"
OBS_TYPE_CAL = "cal"
OBS_TYPE_TEST = "test"
OBS_TYPE_JOIN = "join" # joint observation fo IFS and MCI
OBS_TYPES = (OBS_TYPE_SCI, OBS_TYPE_CAL, OBS_TYPE_TEST, OBS_TYPE_JOIN)

MODULE_MSC = "MSC"
MODULE_MBI = "MBI"
MODULE_SLS = "SLS"
MODULE_IFS = "IFS"
MODULE_MCI = "MCI"
MODULE_CPIC = "CPIC"
MODULE_THZ = "HSTDM"

MODULES = (MODULE_MSC, MODULE_IFS, MODULE_MCI, MODULE_CPIC, MODULE_THZ)

PRC_MODULE_QC0 = "QC0"
PRC_MODULE_QC1 = "QC1"

PRC_MODULE_MSC_INSTRUMENT_EFFECT = "MSC-IE"

MBI_DECTECTORS = [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25]
MBI_FILTERS = ['N', 'u', 'g', 'r', 'i', 'z', 'y']
MBI_DECTECTORS2FILTER = {
    6: "y",
    7: "i",
    8: "g",
    9: "r",
    11: "z",
    12: "nuv",
    13: "nuv",
    14: "u",
    15: "y",
    16: "y",
    17: "u",
    18: "nuv",
    19: "nuv",
    20: "z",
    22: "r",
    23: "g",
    24: "i",
    25: "y"
}
SLS_DECTECTORS = [1, 2, 3, 4, 5, 10, 21, 26, 27, 28, 29, 30]
SLS_FILTERS = ['N', 'u', 'g', 'r', 'i', 'z', 'y']
SLS_DECTECTORS2FILTER = {
    1: "GI",
    2: "GV",
    3: "GU",
    4: "GU",
    5: "GV",
    10: "GI",
    21: "GI",
    26: "GV",
    27: "GU",
    28: "GU",
    29: "GV",
    30: "GI"
}