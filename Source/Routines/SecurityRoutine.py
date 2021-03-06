import cv2
import numpy as np
from tomlkit import parse
from Tasks.face_tasks import FaceCascadeDetector, dnnFaceDetector, svmFace
import os
import time

# class SecurityRoutine(Routine, faceTask):
#    def __init__(self,):
#        Routine.__init__(self, gray=True)


def load_config(toml_path, table):
    with open(toml_path, "r") as f:
        data = f.read()
        config = parse(data)
        print(config)
    return config[table]


if __name__ == "__main__":
    # initilize the feed
    # TODO add CaptureManager or similar class to handle multiple feeds
    feed = cv2.VideoCapture(0)
    time.sleep(3)
    ret, frame = feed.read()
    print("yak")
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # load necessary configs from argos.toml
    argos_home = os.getenv("ARGOS_HOME")

    face_data = load_config(argos_home + "/Storage/config/argos.toml", "face_data")
    # set up tasks

    # TODO have constraints passed as cmdline argument in order to choose
    # between different implementations based on performance and accuracy
    print(face_data)
    """
    faceDetector = faceCascadeDetector(
        argos_home + face_data["faceCascadePath"],
        argos_home + face_data["eyeCascadePath"],
    )
    """
    faceDetector = dnnFaceDetector(
        argos_home + face_data["dnn_detector_path"],
        argos_home + face_data["dnn_weights_path"],
        minimumConfidence=0.5,
    )
    faceRecognizer = svmFace(
        argos_home + face_data["face_embedding_model"],
        argos_home + face_data["svm_recognizer_path"],
        argos_home + face_data["svm_labels_path"],
    )
    cv2.namedWindow("feed")
    key = ord("a")
    while key != ord("q"):
        ret, frame = feed.read()
        faceRegions = faceDetector.getFaceRegions(frame)
        # only executes if at least 1 face is found
        for region in faceRegions:
            frame = faceRecognizer.labelFrame(frame, region)
        cv2.imshow("feed", frame)
        key = cv2.waitKey(10)
