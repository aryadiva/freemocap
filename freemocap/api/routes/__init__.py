from .camera.cam_data_ws import cam_ws_router
from .camera.camera_route import camera_router
from .health.health_check_route import healthcheck_router
from .home.home import home_router
from .processing.core_process_routes import core_process_router
from .session.session_router import session_router
from .startup.startup import startup_router

# REGISTER NEW ROUTES HERE
enabled_routers = [
    healthcheck_router,
    core_process_router,
    camera_router,
    cam_ws_router,
    startup_router,
    home_router,
    session_router,
]