
import dataclasses
from .common import BaseModel

@dataclasses.dataclass
class Level1Record(BaseModel):
    id: int = 0
    level0_id : str = ""
    data_type: str=""
    cor_sci_id: int = 0
    prc_params: str=""
    flat_id: int = 0
    dark_id: int = 0
    bias_id: int = 0
    filename : str=""
    file_path: str=""
    qc1_status: int = 0
    qc1_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""









