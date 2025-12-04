import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

st.title("📌 MediaPipe 얼굴 검출 데모")
st.write("미디어파이프 얼굴검출 (model_selection=1) Streamlit 데모입니다.")

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# 1) 이미지 업로드
uploaded_file = st.file_uploader("이미지를 업로드하세요.", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Streamlit → OpenCV 이미지 변환
    image = Image.open(uploaded_file)
    img_np = np.array(image)

    st.image(img_np, caption="업로드된 이미지", use_container_width=True)

    # 2) MediaPipe 얼굴 검출
    with mp_face_detection.FaceDetection(
        model_selection=1,     # 5m 이내 촬영 사진/전신
        min_detection_confidence=0.5
    ) as face_detection:

        results = face_detection.process(cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR))

        if not results.detections:
            st.error("얼굴이 검출되지 않았습니다.")
        else:
            st.success(f"검출된 얼굴 수: {len(results.detections)}")

            # 3) 검출 결과 출력
            st.write("📌 **검출된 Detections**")
            st.write(results.detections)

            # 4) 얼굴 박스 그리기
            annotated_image = img_np.copy()
            for detection in results.detections:
                mp_drawing.draw_detection(annotated_image, detection)

            st.image(annotated_image, caption="검출 결과 이미지", use_container_width=True)
