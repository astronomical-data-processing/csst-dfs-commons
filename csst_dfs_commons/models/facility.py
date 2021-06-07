
import dataclasses
from typing import List
from .common import BaseModel

@dataclasses.dataclass
class Observation(BaseModel):
    id: int = 0
    obs_time: str = ""
    exp_time : float = 0
    module_id: str=""
    obs_type: str=""
    facility_status_id: int = 0
    module_status_id: int = 0
    qc0_status: int = 0
    qc0_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    import_status: int = 0

@dataclasses.dataclass
class Level0PrcRecord(BaseModel):
    id: int = 0
    level0_id: int = 0
    pipeline_id: str = ""
    prc_module: str = ""
    params_id: str=""
    prc_status: int = 0
    prc_time: str=""
    file_path: str=""

@dataclasses.dataclass
class Level0Record(BaseModel):
    id: int = 0
    obs_id: int = 0
    detector_no: str = ""
    obs_type: str = ""
    obs_time: str=""
    exp_time: float = 0
    detector_status_id: int = 0
    filename: str=""
    file_path: str=""
    qc0_status: int = 0
    qc0_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""

@dataclasses.dataclass
class CalMergeRecord(BaseModel):
    id: int = 0
    detector_no: str = ""
    ref_type: str = ""
    obs_time: str=""
    exp_time: float = 0
    filename: str=""
    file_path: str=""
    qc1_status: int = 0
    qc1_time: str=""
    prc_status: int = 0
    prc_time: str=""
    prc_time: str=""
    create_time: str=""
    level0_ids: list = dataclasses.field(default_factory=list)

@dataclasses.dataclass
class Detector(BaseModel):
    no: str = ""
    detector_name: str = ""
    module_id: str=""
    filter_id: float = 0
    create_time: str=""
    update_time: str=""


@dataclasses.dataclass
class DetectorStatus(BaseModel):
    id: int = 0
    detector_no: str = ""
    status: str=""
    create_time: str=""
    status_time: str=""