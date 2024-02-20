from .models import VisionModel

def process_form(prompt_path, img_paths, out_path):
    try:
        vision_model = VisionModel()
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        response = vision_model.complete(prompt, img_paths)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(response)
    except Exception as e:
        print(f"An error occurred: {e}")

