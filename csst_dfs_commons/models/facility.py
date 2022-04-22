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

@dataclasses.dataclass
class Brick(BaseModel):
    id: int = -1
    ra: float = 0.0
    dec: float = 0.0
    boundingbox: str=""

@dataclasses.dataclass
class BrickObsStatus(BaseModel):
    brick_id: int = -1
    band: str=""
    cover_num: int = 0
    update_time: str=""

@dataclasses.dataclass
class BrickLevel1(BaseModel):
    brick_id: int = -1
    level1_id: int = 0
    obs_id: str=""
    module: str=""
    obs_time: str=""

@dataclasses.dataclass
class Level2Producer(BaseModel):
    id: int = 0
    name: str=""
    priority: int = 0
    gitlink: str=""
    paramfiles: str=""
    pre_producers: list = dataclasses.field(default_factory=list)
    create_time: str=""
    update_time: str=""      

@dataclasses.dataclass
class Level2Job(BaseModel):
    id: int = 0
    dag: str=""
    status: int = 0
    create_time: str=""
    update_time: str=""     

@dataclasses.dataclass
class Level2ProducerRuning(BaseModel):
    id: int = 0
    job_id: int = 0
    producer_id: int = 0
    brick_id: int = -1
    start_time: str=""
    end_time: str=""
    prc_status: int = 0
    prc_result: str=""
    create_time: str=""
    update_time: str=""        
