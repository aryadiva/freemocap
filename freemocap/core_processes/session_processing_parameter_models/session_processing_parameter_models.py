import logging
from pathlib import Path
from typing import Union

from pydantic import BaseModel

from freemocap.configuration.paths_and_files_names import (
    get_last_successful_calibration_toml_path,
    get_most_recent_recording_path,
    OUTPUT_DATA_FOLDER_NAME,
    SYNCHRONIZED_VIDEOS_FOLDER_NAME,
)
from freemocap.core_processes.session_processing_parameter_models.session_info_model import (
    SessionInfoModel,
)

logger = logging.getLogger(__name__)


class MediapipeParametersModel(BaseModel):
    model_complexity: int = 2
    min_detection_confidence: float = 0.5
    min_tracking_confidence: float = 0.5
    static_image_mode: bool = False


class AniposeTriangulate3DParametersModel(BaseModel):
    confidence_threshold_cutoff: float = 0.7
    use_triangulate_ransac_method: bool = False


class ButterworthFilterParametersModel(BaseModel):
    sampling_rate: float = 30
    cutoff_frequency: float = 7
    order: int = 4


class PostProcessingParametersModel(BaseModel):
    framerate: float = 30.0
    butterworth_filter_parameters = ButterworthFilterParametersModel()


class SessionProcessingParameterModel(BaseModel):
    session_info_model: SessionInfoModel = SessionInfoModel()
    mediapipe_parameters_model: MediapipeParametersModel = MediapipeParametersModel()
    anipose_triangulate_3d_parameters_model: AniposeTriangulate3DParametersModel = (
        AniposeTriangulate3DParametersModel()
    )
    post_processing_parameters_model: PostProcessingParametersModel = (
        PostProcessingParametersModel()
    )

    class Config:
        arbitrary_types_allowed = True