import cv2
import numpy as np
import toml

from pathlib import Path
from matplotlib import pyplot as plt


def camera_dict_from_toml(path_to_toml: str | Path) -> dict:
    camera_dict = {}
    calibration_dict = toml.load(Path(path_to_toml))

    for key, value in calibration_dict.items():
        if key == "metadata":
            continue
        camera_dict[key] = {"rotation": value["rotation"], "translation": value["translation"]}

    return camera_dict

def rotation_matrix_to_direction(rvec: np.ndarray) -> np.ndarray:
    rotation_matrix, _ = cv2.Rodrigues(rvec)
    direction = rotation_matrix[:, 2]

    return direction

def plot_points(camera_dict: dict, skeleton: np.ndarray, line_length: float = 300) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for camera_name, camera_data in camera_dict.items():
        rotation = camera_data["rotation"]
        translation = camera_data["translation"]
        direction = rotation_matrix_to_direction(np.asarray(rotation))

        ax.scatter(translation[0], translation[1], translation[2], label=f"{camera_name}")

        ax.quiver(translation[0], translation[1], translation[2], 
                  direction[0], direction[1], direction[2], 
                  length=line_length, normalize=True)
        
    skeleton_scatter = ax.scatter(skeleton[:, 0], skeleton[:, 1], skeleton[:, 2], label='Original Points')
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    toml_path = "/Users/philipqueen/freemocap_data/recording_sessions/freemocap_sample_data/2022-09-19_16_16_50_in_class_jsm_camera_calibration.toml"

    raw_skeleton_data = np.load("/Users/philipqueen/freemocap_data/recording_sessions/freemocap_sample_data/output_data/raw_data/mediapipe3dData_numFrames_numTrackedPoints_spatialXYZ.npy")

    good_frame = 450

    good_frame_skeleton_data = raw_skeleton_data[good_frame, :, :]
    print(good_frame_skeleton_data)
    print(good_frame_skeleton_data.shape)

    camera_dict = camera_dict_from_toml(toml_path)

    plot_points(camera_dict, good_frame_skeleton_data)