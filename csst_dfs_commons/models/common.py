import copy
from dataclasses import dataclass, field
import json

def from_proto_model_list(clazz, records):
    return [clazz().from_proto_model(r) for r in records]

def from_dict_list(clazz, records):
    return [clazz().from_dict(r) for r in records]

def to_proto_model_list(protoObjClazz, records):
    return [r.to_proto_model(protoObjClazz) for r in records]

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__    
    def __init__(self, **args):
        super(Dict, self).__init__()
        self.update(args)

def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst=Dict()
    for k,v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

@dataclass
class BaseModel:
    def from_dict(self, data = {}):
        for k in self.__dataclass_fields__.keys():
            self.__setattr__(k, data.get(k, None))
        return self

    def from_proto_model(self, record):
        if record is None:
            return None
        for k in self.__dataclass_fields__.keys():
            if k == 'header':
                if record.__getattribute__(k):
                    self.__setattr__(k, json.loads(record.__getattribute__(k)))
            else:
                self.__setattr__(k, record.__getattribute__(k))
        return self
    
    def to_proto_model(self, protoObjClazz):
        obj = protoObjClazz()
        for k in self.__dataclass_fields__.keys():
            v = self.__getattribute__(k)
            if v is not None:
                if isinstance(v, list) or isinstance(v, tuple):
                    obj.__getattribute__(k).extend(v)
                elif isinstance(v, dict):
                    if k == 'header':
                        obj.__setattr__(k, json.dumps(v))
                    else:
                        obj.__getattribute__(k).update(v)                    
                else:
                    obj.__setattr__(k, v)
        return obj

@dataclass
class Gaia3Record(BaseModel):
    SolutionId: int = -1
    Designation: str = ''
    SourceId: int = -1
    RandomIndex: int = -1
    RefEpoch: float = -1
    Ra: float = -1
    RaError: float = -1
    Dec: float = -1
    DecError: float = -1
    Parallax: float = -1
    ParallaxError: float = -1
    ParallaxOverError: float = -1
    Pm: float = -1
    Pmra: float = -1
    PmraError: float = -1
    Pmdec: float = -1
    PmdecError: float = -1
    RaDecCorr: float = -1
    RaParallaxCorr: float = -1
    RaPmraCorr: float = -1
    RaPmdecCorr: float = -1
    DecParallaxCorr: float = -1
    DecPmraCorr: float = -1
    DecPmdecCorr: float = -1
    ParallaxPmraCorr: float = -1
    ParallaxPmdecCorr: float = -1
    PmraPmdecCorr: float = -1
    AstrometricNObsAl: int = -1
    AstrometricNObsAc: int = -1
    AstrometricNGoodObsAl: int = -1
    AstrometricNBadObsAl: int = -1
    AstrometricGofAl: float = -1
    AstrometricChi2Al: float = -1
    AstrometricExcessNoise: float = -1
    AstrometricExcessNoiseSig: float = -1
    AstrometricParamsSolved: int = -1
    AstrometricPrimaryFlag: int = 0
    NuEffUsedInAstrometry: float = -1
    Pseudocolour: float = -1
    PseudocolourError: float = -1
    RaPseudocolourCorr: float = -1
    DecPseudocolourCorr: float = -1
    ParallaxPseudocolourCorr: float = -1
    PmraPseudocolourCorr: float = -1
    PmdecPseudocolourCorr: float = -1
    AstrometricMatchedTransits: int = -1
    VisibilityPeriodsUsed: int = -1
    AstrometricSigma5dMax: float = -1
    MatchedTransits: int = -1
    NewMatchedTransits: int = -1
    MatchedTransitsRemoved: int = -1
    IpdGofHarmonicAmplitude: float = -1
    IpdGofHarmonicPhase: float = -1
    IpdFracMultiPeak: int = -1
    IpdFracOddWin: int = -1
    Ruwe: float = -1
    ScanDirectionStrengthK1: float = -1
    ScanDirectionStrengthK2: float = -1
    ScanDirectionStrengthK3: float = -1
    ScanDirectionStrengthK4: float = -1
    ScanDirectionMeanK1: float = -1
    ScanDirectionMeanK2: float = -1
    ScanDirectionMeanK3: float = -1
    ScanDirectionMeanK4: float = -1
    DuplicatedSource: int = 0
    PhotGNObs: int = -1
    PhotGMeanFlux: float = -1
    PhotGMeanFluxError: float = -1
    PhotGMeanFluxOverError: float = -1
    PhotGMeanMag: float = -1
    PhotBpNObs: int = -1
    PhotBpMeanFlux: float = -1
    PhotBpMeanFluxError: float = -1
    PhotBpMeanFluxOverError: float = -1
    PhotBpMeanMag: float = -1
    PhotRpNObs: int = -1
    PhotRpMeanFlux: float = -1
    PhotRpMeanFluxError: float = -1
    PhotRpMeanFluxOverError: float = -1
    PhotRpMeanMag: float = -1
    PhotBpRpExcessFactor: float = -1
    PhotBpNContaminatedTransits: float = -1
    PhotBpNBlendedTransits: float = -1
    PhotRpNContaminatedTransits: float = -1
    PhotRpNBlendedTransits: float = -1
    PhotProcMode: float = -1
    BpRp: float = -1
    BpG: float = -1
    GRp: float = -1
    RadialVelocity: float = -1
    RadialVelocityError: float = -1
    RvMethodUsed: float = -1
    RvNbTransits: float = -1
    RvNbDeblendedTransits: float = -1
    RvVisibilityPeriodsUsed: float = -1
    RvExpectedSigToNoise: float = -1
    RvRenormalisedGof: float = -1
    RvChisqPvalue: float = -1
    RvTimeDuration: float = -1
    RvAmplitudeRobust: float = -1
    RvTemplateTeff: float = -1
    RvTemplateLogg: float = -1
    RvTemplateFeH: float = -1
    RvAtmParamOrigin: float = -1
    Vbroad: float = -1
    VbroadError: float = -1
    VbroadNbTransits: float = -1
    GrvsMag: float = -1
    GrvsMagError: float = -1
    GrvsMagNbTransits: float = -1
    RvsSpecSigToNoise: float = -1
    PhotVariableFlag: str = ''
    L: float = -1
    B: float = -1
    EclLon: float = -1
    EclLat: float = -1
    InQsoCandidates: int = 0
    InGalaxyCandidates: int = 0
    NonSingleStar: int = -1
    HasXpContinuous: int = 0
    HasXpSampled: int = 0
    HasRvs: int = 0
    HasEpochPhotometry: int = 0
    HasEpochRv: int = 0
    HasMcmcGspphot: int = 0
    HasMcmcMsc: int = 0
    InAndromedaSurvey: int = 0
    ClassprobDscCombmodQuasar: float = -1
    ClassprobDscCombmodGalaxy: float = -1
    ClassprobDscCombmodStar: float = -1
    TeffGspphot: float = -1
    TeffGspphotLower: float = -1
    TeffGspphotUpper: float = -1
    LoggGspphot: float = -1
    LoggGspphotLower: float = -1
    LoggGspphotUpper: float = -1
    MhGspphot: float = -1
    MhGspphotLower: float = -1
    MhGspphotUpper: float = -1
    DistanceGspphot: float = -1
    DistanceGspphotLower: float = -1
    DistanceGspphotUpper: float = -1
    AzeroGspphot: float = -1
    AzeroGspphotLower: float = -1
    AzeroGspphotUpper: float = -1
    AgGspphot: float = -1
    AgGspphotLower: float = -1
    AgGspphotUpper: float = -1
    EbpminrpGspphot: float = -1
    EbpminrpGspphotLower: float = -1
    EbpminrpGspphotUpper: float = -1
    LibnameGspphot: str = ''
    NS8HIdx: int = -1
    NS16HIdx: int = -1
    NS32HIdx: int = -1
    NS64HIdx: int = -1
    FileIdx: int = -1
    
    def __init__(self):
        self.AstrometricNObsAc = 0
