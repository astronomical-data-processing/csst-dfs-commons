import dataclasses
from typing import Dict
from .common import BaseModel, default_field
    
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
