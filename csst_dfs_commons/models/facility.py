import dataclasses
from typing import List
from .common import BaseModel

@dataclasses.dataclass
class Observation(BaseModel):
    id: int = 0
    obs_id: str = ""
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

