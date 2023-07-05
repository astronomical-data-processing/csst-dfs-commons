import dataclasses
from .common import BaseModel

@dataclasses.dataclass
class Level2Spectra(BaseModel):
    id: int = 0
    level0_id: str = ''
    level1_id: int=0
    file_type: str=""
    filename : str=""
    file_path: str=""
    qc2_status: int = 0
    qc2_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""    
