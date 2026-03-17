PI_Project/
├─ .venv/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ config/
│  ├─ vehicle.yaml
│  ├─ camera.yaml
│  └─ logging.yaml
├─ logs/
├─ data/
│  ├─ telemetry/
│  └─ recordings/
├─ scripts/
│  ├─ arm_test.py
│  ├─ telemetry_monitor.py
│  ├─ takeoff_test.py
│  └─ camera_test.py
├─ src/
│  └─ drone/
│     ├─ __init__.py
│     ├─ main.py
│     ├─ config.py
│     ├─ logger.py
│     ├─ state.py
│     ├─ safety.py
│     ├─ mavlink/
│     │  ├─ __init__.py
│     │  ├─ connection.py
│     │  ├─ telemetry.py
│     │  └─ commands.py
│     ├─ control/
│     │  ├─ __init__.py
│     │  ├─ pid.py
│     │  ├─ filters.py
│     │  └─ modes.py
│     ├─ sensors/
│     │  ├─ __init__.py
│     │  ├─ imu.py
│     │  ├─ gps.py
│     │  └─ power.py
│     ├─ vision/
│     │  ├─ __init__.py
│     │  ├─ camera.py
│     │  └─ detect.py
│     └─ utils/
│        ├─ __init__.py
│        ├─ math_utils.py
│        └─ time_utils.py
└─ tests/
   ├─ test_pid.py
   ├─ test_filters.py
   └─ test_connection.py