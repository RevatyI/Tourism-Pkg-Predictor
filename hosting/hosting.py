from huggingface_hub import HfApi, create_repo
import os
import time

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="deployment",     # the local folder containing your files
    repo_id="Revaty/Tourism-Pkg-Predictor",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
