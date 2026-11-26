"""Run the tests with the built-in demo accounts, whatever the environment says."""
import os

for _u in ("ADMIN", "SCIENTIST", "PARTNER", "EXPO"):
    os.environ.pop(f"CRYSTALSCOUT_PW_{_u}", None)
os.environ["CRYSTALSCOUT_NO_AUDIT"] = "1"
