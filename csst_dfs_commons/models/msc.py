import dataclasses
from typing import Dict
from .common import BaseModel, default_field

@dataclasses.dataclass
class Level1Record(BaseModel):
    id: int = 0
    level0_id : str = ""
    data_type: str=""
    cor_sci_id: int = 0
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

@dataclasses.dataclass
class Level2Record(BaseModel):
    id: int = 0
    level0_id: str = ''
    level1_id : int = 0
    data_type: str=""
    filename : str=""
    file_path: str=""
    obs_time: str=""
    qc2_status: int = 0
    qc2_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""
    import_status: int = 0

@dataclasses.dataclass
class Level2CoRecord(BaseModel):
    id: int = 0
    data_type: str=""
    filename : str=""
    file_path: str=""
    qc2_status: int = 0
    qc2_time: str=""
    prc_status: int = 0
    prc_time: str=""
    create_time: str=""
    pipeline_id: str=""
    import_status: int = 0

@dataclasses.dataclass
class Level2CatalogRecord(BaseModel):
    level2_id: int = 0
    seq: int = 0
    flux_aper: list = dataclasses.field(default_factory=list)
    fluxerr_aper: list = dataclasses.field(default_factory=list)
    mag_aper: list = dataclasses.field(default_factory=list)
    magerr_aper: list = dataclasses.field(default_factory=list)
    flux_auto: float = -1
    fluxerr_auto: float = -1
    mag_auto: float = -1
    magerr_auto: float = -1
    kron_radius: float = -1
    background: float = -1
    x_image: float = -1
    y_image: float = -1
    alpha_j2000: float = -1
    delta_j2000: float = -1
    a_image: float = -1
    b_image: float = -1
    theta_image: float = -1
    a_world: float = -1
    b_world: float = -1
    theta_world: float = -1
    theta_j2000: float = -1
    errx2_image: float = -1
    erry2_image: float = -1
    erra_image: float = -1
    errb_image: float = -1
    errtheta_image: float = -1
    erra_world: float = -1
    errb_world: float = -1
    errtheta_world: float = -1
    errtheta_j2000: float = -1
    xwin_image: float = -1
    ywin_image: float = -1
    alphawin_j2000: float = -1
    deltawin_j2000: float = -1
    errx2win_image: float = -1
    erry2win_image: float = -1
    flags: int = 0
    flags_weight: int = 0
    imaflags_iso: float = -1
    nimaflags_iso: float = -1
    fwhm_image: float = -1
    fwhm_world: float = -1
    elongation: float = -1
    ellipticity: float = -1
    class_star: float = -1
    flux_radius: float = -1
    fwhmpsf_image: float = -1
    fwhmpsf_world: float = -1
    xpsf_image: float = -1
    ypsf_image: float = -1
    alphapsf_j2000: float = -1
    deltapsf_j2000: float = -1
    flux_psf: float = -1
    fluxerr_psf: float = -1
    mag_psf: float = -1
    magerr_psf: float = -1
    niter_psf: int = 0
    chi2_psf: float = -1
    errx2psf_image: float = -1
    erry2psf_image: float = -1
    chi2_model: float = -1
    flags_model: int = 0
    niter_model: int = 0
    flux_model: float = -1
    fluxerr_model: float = -1
    mag_model: float = -1
    magerr_model: float = -1
    flux_hybrid: float = -1
    fluxerr_hybrid: float = -1
    mag_hybrid: float = -1
    magerr_hybrid: float = -1
    flux_max_model: float = -1
    mu_max_model: float = -1
    flux_eff_model: float = -1
    mu_eff_model: float = -1
    flux_mean_model: float = -1
    mu_mean_model: float = -1
    xmodel_image: float = -1
    ymodel_image: float = -1
    alphamodel_j2000: float = -1
    deltamodel_j2000: float = -1
    erry2model_image: float = -1
    erramodel_image: float = -1
    errbmodel_image: float = -1
    errthetamodel_image: float = -1
    erramodel_world: float = -1
    errbmodel_world: float = -1
    errthetamodel_world: float = -1
    errthetamodel_j2000: float = -1
    amodel_image: float = -1
    bmodel_image: float = -1
    thetamodel_image: float = -1
    amodel_world: float = -1
    bmodel_world: float = -1
    thetamodel_world: float = -1
    thetamodel_j2000: float = -1
    spread_model: float = -1
    spreaderr_model: float = -1
    noisearea_model: float = -1
    flux_spheroid: float = -1
    fluxerr_spheroid: float = -1
    mag_spheroid: float = -1
    magerr_spheroid: float = -1
    flux_max_spheroid: float = -1
    mu_max_spheroid: float = -1
    flux_eff_spheroid: float = -1
    mu_eff_spheroid: float = -1
    flux_mean_spheroid: float = -1
    mu_mean_spheroid: float = -1
    fluxratio_spheroid: float = -1
    fluxratioerr_spheroid: float = -1
    spheroid_reff_image: float = -1
    spheroid_refferr_image: float = -1
    spheroid_reff_world: float = -1
    spheroid_refferr_world: float = -1
    spheroid_aspect_image: float = -1
    spheroid_aspecterr_image: float = -1
    spheroid_aspect_world: float = -1
    spheroid_aspecterr_world: float = -1
    spheroid_theta_image: float = -1
    spheroid_thetaerr_image: float = -1
    spheroid_theta_world: float = -1
    spheroid_thetaerr_world: float = -1
    spheroid_theta_j2000: float = -1
    spheroid_sersicn: float = -1
    spheroid_sersicnerr: float = -1
    flux_disk: float = -1
    fluxerr_disk: float = -1
    mag_disk: float = -1
    magerr_disk: float = -1
    flux_max_disk: float = -1
    mu_max_disk: float = -1
    flux_eff_disk: float = -1
    mu_eff_disk: float = -1
    flux_mean_disk: float = -1
    mu_mean_disk: float = -1
    fluxratio_disk: float = -1
    fluxratioerr_disk: float = -1
    disk_scale_image: float = -1
    disk_scaleerr_image: float = -1
    disk_scale_world: float = -1
    disk_scaleerr_world: float = -1
    disk_aspect_image: float = -1
    disk_aspecterr_image: float = -1
    disk_aspect_world: float = -1
    disk_aspecterr_world: float = -1
    disk_inclination: float = -1
    disk_inclinationerr: float = -1
    disk_theta_image: float = -1
    disk_thetaerr_image: float = -1
    disk_theta_world: float = -1
    disk_thetaerr_world: float = -1
    disk_theta_j2000: float = -1    
    NS8HIdx: int = 0
    NS16HIdx: int = 0
    NS32HIdx: int = 0
    NS64HIdx: int = 0
    create_time: str = ''

@dataclasses.dataclass
class Level2CatalogRecordV2(BaseModel):
    level2_id: int = 0
    ID: str = ''
    CCDNO: int = 0
    objID: int = 0
    X: float = -1
    XErr: float = -1
    Y: float = -1
    YErr: float = -1
    RA: float = -1
    RAErr: float = -1
    DEC: float = -1
    DECErr: float = -1
    A: float = -1
    AErr: float = -1
    B: float = -1
    BErr: float = -1
    PA: float = -1
    PAErr: float = -1
    Flag: int = 0
    Flag_ISO: int = 0
    Flag_ISO_Num: int = 0
    FWHM: float = -1
    AB: float = -1
    E: float = -1
    Flux_Kron: float = -1
    FluxErr_Kron: float = -1
    Mag_Kron: float = -1
    MagErr_Kron: float = -1
    Radius_Kron: float = -1
    Sky: float = -1
    Flux_Aper1: float = -1
    FluxErr_Aper1: float = -1
    Mag_Aper1: float = -1
    MagErr_Aper1: float = -1
    Flux_Aper2: float = -1
    FluxErr_Aper2: float = -1
    Mag_Aper2: float = -1
    MagErr_Aper2: float = -1
    Flux_Aper3: float = -1
    FluxErr_Aper3: float = -1
    Mag_Aper3: float = -1
    MagErr_Aper3: float = -1
    Flux_Aper4: float = -1
    FluxErr_Aper4: float = -1
    Mag_Aper4: float = -1
    MagErr_Aper4: float = -1
    Flux_Aper5: float = -1
    FluxErr_Aper5: float = -1
    Mag_Aper5: float = -1
    MagErr_Aper5: float = -1
    Flux_Aper6: float = -1
    FluxErr_Aper6: float = -1
    Mag_Aper6: float = -1
    MagErr_Aper6: float = -1
    Flux_Aper7: float = -1
    FluxErr_Aper7: float = -1
    Mag_Aper7: float = -1
    MagErr_Aper7: float = -1
    Flux_Aper8: float = -1
    FluxErr_Aper8: float = -1
    Mag_Aper8: float = -1
    MagErr_Aper8: float = -1
    Flux_Aper9: float = -1
    FluxErr_Aper9: float = -1
    Mag_Aper9: float = -1
    MagErr_Aper9: float = -1
    Flux_Aper10: float = -1
    FluxErr_Aper10: float = -1
    Mag_Aper10: float = -1
    MagErr_Aper10: float = -1
    Flux_Aper11: float = -1
    FluxErr_Aper11: float = -1
    Mag_Aper11: float = -1
    MagErr_Aper11: float = -1
    Flux_Aper12: float = -1
    FluxErr_Aper12: float = -1
    Mag_Aper12: float = -1
    MagErr_Aper12: float = -1
    Type: int = 0
    R20: float = -1
    R50: float = -1
    R90: float = -1
    X_PSF: float = -1
    Y_PSF: float = -1
    RA_PSF: float = -1
    DEC_PSF: float = -1
    Chi2_PSF: float = -1
    Flux_PSF: float = -1
    FluxErr_PSF: float = -1
    Mag_PSF: float = -1
    MagErr_PSF: float = -1
    X_Model: float = -1
    Y_Model: float = -1
    RA_Model: float = -1
    DEC_Model: float = -1
    Chi2_Model: float = -1
    Flag_Model: int = 0
    Flux_Model: float = -1
    FluxErr_Model: float = -1
    Mag_Model: float = -1
    MagErr_Model: float = -1
    Flux_Bulge: float = -1
    FluxErr_Bulge: float = -1
    Mag_Bulge: float = -1
    MagErr_Bulge: float = -1
    Re_Bulge: float = -1
    ReErr_Bulge: float = -1
    E_Bulge: float = -1
    EErr_Bulge: float = -1
    PA_Bulge: float = -1
    PAErr_Bulge: float = -1
    Flux_Disk: float = -1
    FluxErr_Disk: float = -1
    Mag_Disk: float = -1
    MagErr_Disk: float = -1
    Re_Disk: float = -1
    ReErr_Disk: float = -1
    E_Disk: float = -1
    EErr_Disk: float = -1
    PA_Disk: float = -1
    PAErr_Disk: float = -1
    Ratio_Disk: float = -1
    RatioErr_Disk: float = -1
    Spread_Model: float = -1
    SpreadErr_Model: float = -1
    NS8HIdx: int = 0
    NS16HIdx: int = 0
    NS32HIdx: int = 0
    NS64HIdx: int = 0
    
@dataclasses.dataclass
class Level2CoCatalogRecord(BaseModel):
    level2_id: int = 0
    seq: int = 0
    flux_aper: list = dataclasses.field(default_factory=list)
    fluxerr_aper: list = dataclasses.field(default_factory=list)
    mag_aper: list = dataclasses.field(default_factory=list)
    magerr_aper: list = dataclasses.field(default_factory=list)
    flux_auto: float = -1
    fluxerr_auto: float = -1
    mag_auto: float = -1
    magerr_auto: float = -1
    kron_radius: float = -1
    background: float = -1
    x_image: float = -1
    y_image: float = -1
    alpha_j2000: float = -1
    delta_j2000: float = -1
    a_image: float = -1
    b_image: float = -1
    theta_image: float = -1
    a_world: float = -1
    b_world: float = -1
    theta_world: float = -1
    theta_j2000: float = -1
    errx2_image: float = -1
    erry2_image: float = -1
    erra_image: float = -1
    errb_image: float = -1
    errtheta_image: float = -1
    erra_world: float = -1
    errb_world: float = -1
    errtheta_world: float = -1
    errtheta_j2000: float = -1
    xwin_image: float = -1
    ywin_image: float = -1
    alphawin_j2000: float = -1
    deltawin_j2000: float = -1
    errx2win_image: float = -1
    erry2win_image: float = -1
    flags: int = 0
    flags_weight: int = 0
    imaflags_iso: float = -1
    nimaflags_iso: float = -1
    fwhm_image: float = -1
    fwhm_world: float = -1
    elongation: float = -1
    ellipticity: float = -1
    class_star: float = -1
    flux_radius: float = -1
    fwhmpsf_image: float = -1
    fwhmpsf_world: float = -1
    xpsf_image: float = -1
    ypsf_image: float = -1
    alphapsf_j2000: float = -1
    deltapsf_j2000: float = -1
    flux_psf: float = -1
    fluxerr_psf: float = -1
    mag_psf: float = -1
    magerr_psf: float = -1
    niter_psf: int = 0
    chi2_psf: float = -1
    errx2psf_image: float = -1
    erry2psf_image: float = -1
    chi2_model: float = -1
    flags_model: int = 0
    niter_model: int = 0
    flux_model: float = -1
    fluxerr_model: float = -1
    mag_model: float = -1
    magerr_model: float = -1
    flux_hybrid: float = -1
    fluxerr_hybrid: float = -1
    mag_hybrid: float = -1
    magerr_hybrid: float = -1
    flux_max_model: float = -1
    mu_max_model: float = -1
    flux_eff_model: float = -1
    mu_eff_model: float = -1
    flux_mean_model: float = -1
    mu_mean_model: float = -1
    xmodel_image: float = -1
    ymodel_image: float = -1
    alphamodel_j2000: float = -1
    deltamodel_j2000: float = -1
    erry2model_image: float = -1
    erramodel_image: float = -1
    errbmodel_image: float = -1
    errthetamodel_image: float = -1
    erramodel_world: float = -1
    errbmodel_world: float = -1
    errthetamodel_world: float = -1
    errthetamodel_j2000: float = -1
    amodel_image: float = -1
    bmodel_image: float = -1
    thetamodel_image: float = -1
    amodel_world: float = -1
    bmodel_world: float = -1
    thetamodel_world: float = -1
    thetamodel_j2000: float = -1
    spread_model: float = -1
    spreaderr_model: float = -1
    noisearea_model: float = -1
    flux_spheroid: float = -1
    fluxerr_spheroid: float = -1
    mag_spheroid: float = -1
    magerr_spheroid: float = -1
    flux_max_spheroid: float = -1
    mu_max_spheroid: float = -1
    flux_eff_spheroid: float = -1
    mu_eff_spheroid: float = -1
    flux_mean_spheroid: float = -1
    mu_mean_spheroid: float = -1
    fluxratio_spheroid: float = -1
    fluxratioerr_spheroid: float = -1
    spheroid_reff_image: float = -1
    spheroid_refferr_image: float = -1
    spheroid_reff_world: float = -1
    spheroid_refferr_world: float = -1
    spheroid_aspect_image: float = -1
    spheroid_aspecterr_image: float = -1
    spheroid_aspect_world: float = -1
    spheroid_aspecterr_world: float = -1
    spheroid_theta_image: float = -1
    spheroid_thetaerr_image: float = -1
    spheroid_theta_world: float = -1
    spheroid_thetaerr_world: float = -1
    spheroid_theta_j2000: float = -1
    spheroid_sersicn: float = -1
    spheroid_sersicnerr: float = -1
    flux_disk: float = -1
    fluxerr_disk: float = -1
    mag_disk: float = -1
    magerr_disk: float = -1
    flux_max_disk: float = -1
    mu_max_disk: float = -1
    flux_eff_disk: float = -1
    mu_eff_disk: float = -1
    flux_mean_disk: float = -1
    mu_mean_disk: float = -1
    fluxratio_disk: float = -1
    fluxratioerr_disk: float = -1
    disk_scale_image: float = -1
    disk_scaleerr_image: float = -1
    disk_scale_world: float = -1
    disk_scaleerr_world: float = -1
    disk_aspect_image: float = -1
    disk_aspecterr_image: float = -1
    disk_aspect_world: float = -1
    disk_aspecterr_world: float = -1
    disk_inclination: float = -1
    disk_inclinationerr: float = -1
    disk_theta_image: float = -1
    disk_thetaerr_image: float = -1
    disk_theta_world: float = -1
    disk_thetaerr_world: float = -1
    disk_theta_j2000: float = -1    
    NS8HIdx: int = 0
    NS16HIdx: int = 0
    NS32HIdx: int = 0
    NS64HIdx: int = 0
    create_time: str = ''
