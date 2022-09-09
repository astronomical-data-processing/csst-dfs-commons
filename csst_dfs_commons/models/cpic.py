import dataclasses
from typing import Dict
from .common import BaseModel, default_field

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
class Level0Record(BaseModel):
    id: int = 0
    level0_id: str = ""
    obs_id: str = ""
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
    cal_id: str = ""
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
class Level1Record(BaseModel):
    id: int = 0
    level0_id : str = ""
    data_type: str=""
    prc_params: str=""
    filename : str=""
    file_path: str=""
    qc1_status: int = 0
    qc1_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""
    refs: Dict[str,int] = default_field({})

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
