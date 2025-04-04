def solution(routes):
    # 진출 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    cameras = 0
    last_camera = -30001  # 카메라의 마지막 설치 위치 (제한 범위 바깥)

    for route in routes:
        # 카메라가 현재 차량의 진입 지점보다 이전에 설치되어 있으면
        # 해당 차량을 감지할 수 없음 → 새 카메라 설치 필요
        if last_camera < route[0]:
            cameras += 1
            last_camera = route[1]  # 현재 차량의 진출 지점에 카메라 설치

    return cameras
