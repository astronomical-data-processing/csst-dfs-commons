UPLOAD_CHUNK_SIZE = 1024*1000*4

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
MODULE_IFS = "IFS"
MODULE_MCI = "MCI"
MODULE_CPIC = "CPIC"
MODULE_THZ = "HSTDM"

MODULES = (MODULE_MSC, MODULE_IFS, MODULE_MCI, MODULE_CPIC, MODULE_THZ)


PRC_MODULE_QC0 = "QC0"
PRC_MODULE_QC1 = "QC1"

PRC_MODULE_MSC_INSTRUMENT_EFFECT = "MSC-IE"

