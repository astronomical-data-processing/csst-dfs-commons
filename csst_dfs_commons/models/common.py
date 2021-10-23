import copy
from dataclasses import dataclass, field

def from_proto_model_list(clazz, records):
    return [clazz().from_proto_model(r) for r in records]

def from_dict_list(clazz, records):
    return [clazz().from_dict(r) for r in records]

def to_proto_model_list(protoObjClazz, records):
    return [r.to_proto_model(protoObjClazz) for r in records]

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))    
@dataclass
class BaseModel:

    def from_dict(self, data = {}):
        for k in self.__dataclass_fields__.keys():
            self.__setattr__(k, data.get(k, None))
        return self

    def from_proto_model(self, record):
        for k in self.__dataclass_fields__.keys():
            self.__setattr__(k, record.__getattribute__(k))
        return self
    
    def to_proto_model(self, protoObjClazz):
        obj = protoObjClazz()
        for k in self.__dataclass_fields__.keys():
            v = self.__getattribute__(k)
            if v is not None:
                if isinstance(v, list) or isinstance(v, tuple):
                    obj.__getattribute__(k).extend(v)
                if isinstance(v, dict):
                    obj.__getattribute__(k).update(v)                    
                else:
                    obj.__setattr__(k, v)
        return obj

@dataclass
class Gaia3Record(BaseModel):
    SourceId: int  = -1
    RandomIndex: int  = -1
    RefEpoch: float = -1
    Ra: float = -1
    RaError: float = -1
    Dec : float = -1
    DecError: float = -1
    Parallax: float = -1
    ParallaxError: float = -1
    ParallaxOverError: float = -1
    Pm: float = -1
    Pmra: float = -1
    PmraError: float = -1
    Pmdec: float = -1
    PmdecError: float = -1
    RaDecCorr : float = -1
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
    AstrometricPrimaryFlag: int = -1
    NuEffUsedInAstrometry: float = -1
    Pseudocolour: float = -1
    PseudocolourError: float = -1
    RaPseudocolourCorr: float = -1
    DecPseudocolourCorr: float = -1
    ParallaxPseudocolourCorr: float = -1
    PmraPseudocolourCorr : float = -1
    PmdecPseudocolourCorr: float = -1
    AstrometricMatchedTransits: int = -1
    VisibilityPeriodsUsed: int = -1
    AstrometricSigma5dMax : float = -1
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
    DuplicatedSource: int = -1
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
    PhotBpNContaminatedTransits: float = -1
    PhotBpNBlendedTransits: float = -1
    PhotRpNContaminatedTransits: float = -1
    PhotRpNBlendedTransits: float = -1
    PhotProcMode : float = -1
    PhotBpRpExcessFactor: float = -1
    BpRp: float = -1
    BpG : float = -1
    GRp : float = -1
    Dr2RadialVelocity: float = -1
    Dr2RadialVelocityError: float = -1
    Dr2RvNbTransits: int = -1
    Dr2RvTemplateTeff: float = -1
    Dr2RvTemplateLogg: float = -1
    Dr2RvTemplateFeH : float = -1
    L: float = -1
    B: float = -1
    EclLon: float = -1
    EclLat: float = -1
    NS8HIdx: int = -1
    NS16HIdx: int = -1
    NS32HIdx: int = -1
    NS64HIdx: int = -1

    def __init__(self):
        self.AstrometricNObsAc = 0
