from dataclasses import dataclass
from typing import Dict
from .common import BaseModel, default_field
@dataclass
class Level1Record(BaseModel):
    id: int = 0
    level0_id : str = ""
    data_type: str=""
    cor_sci_id: int = 0
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









