import dataclasses
from typing import List,Dict
from .common import BaseModel, default_field

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

@dataclasses.dataclass
class Level0Record(BaseModel):
    id: int = 0
    level0_id: str = ""
    obs_id: str = ""
    detector_no: str = ""
    module_id: str = ""
    filter: str=""
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
    header: Dict[str,object] = default_field({})

@dataclasses.dataclass
class Level0PrcRecord(BaseModel):
    id: int = 0
    level0_id: str = ""
    pipeline_id: str = ""
    prc_module: str = ""
    params_file_path: str=""
    prc_status: int = 0
    prc_time: str=""
    result_file_path: str=""

@dataclasses.dataclass
class Level1Record(BaseModel):
    id: int = 0
    level0_id : str = ""
    data_type: str=""
    cor_sci_id: int = 0
    module_id: str = ""
    prc_params: str=""
    filter: str=""
    filename : str=""
    file_path: str=""
    qc1_status: int = 0
    qc1_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""
    detector_no: str=""
    header: Dict[str,object] = default_field({})
    refs: Dict[str,str] = default_field({})

@dataclasses.dataclass
class Level1PrcRecord(BaseModel):
    id: int = 0
    level1_id: int = 0
    pipeline_id: str = ""
    prc_module: str = ""
    params_file_path: str=""
    prc_status: int = 0
    prc_time: str=""
    result_file_path: str="" 

@dataclasses.dataclass
class OtherDataRecord(BaseModel):
    id: int = 0
    obs_id : str = ""
    detector_no: str=""
    module_id: str = ""
    file_type: str=""
    filename : str=""
    file_path: str=""
    create_time: str=""
    pipeline_id: str=""