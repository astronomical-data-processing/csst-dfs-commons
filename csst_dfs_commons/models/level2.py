import dataclasses
from .common import BaseModel

@dataclasses.dataclass
class Level2Record(BaseModel):
    id: int = 0
    level0_id: str = ''
    level1_id: int = 0
    brick_id: int = 0
    module_id: str = ''
    object_name : str=""
    data_type: str=""
    filename : str=""
    file_path: str=""
    qc2_status: int = 0
    qc2_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    update_time: str=""
    pipeline_id: str=""
    import_status: int = 0

@dataclasses.dataclass
class Level2TypeRecord(BaseModel):
    data_type: str=""
    module_id: str = ''
    key_column : str=""
    hdu_index: int=0
    demo_filename : str=""
    demo_file_path: str=""
    ra_column: str=""
    dec_column: str=""
    update_time: str=""
    create_time: str=""
    import_status: int = 0

def filter_table_name(data_type):
    return '_'.join(data_type.split('-'))

