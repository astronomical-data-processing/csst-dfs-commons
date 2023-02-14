import dataclasses
from typing import Dict
from .common import BaseModel, default_field

@dataclasses.dataclass
class Level2Spectra(BaseModel):
    id: int = 0
    level0_id: str = ''
    spectra_id : str = ""
    level1_id: int=0
    region: str=""
    filename : str=""
    file_path: str=""
    qc1_status: int = 0
    qc1_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""    
