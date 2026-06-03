import os
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from google import genai
from google.genai import types
from google.genai.errors import APIError
from dotenv import load_dotenv

# Path configuration
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "business_agent" / ".env"
PRODUCTS_JSON_PATH = BASE_DIR / "business_agent" / "src" / "business_agent" / "data" / "products.json"
IMAGES_DIR = BASE_DIR / "business_agent" / "src" / "business_agent" / "data" / "images"

# Load environment variables
load_dotenv(ENV_PATH)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in environment or .env file.")
    exit(1)

# Initialize the Gemini Gen AI SDK client
client = genai.Client(api_key=api_key)

def generate_image_for_product(product, retries=5):
    sku = product["sku"]
    name = product["name"]
    desc = product["description"]
    
    prompt = f"A clean, high-quality professional e-commerce product photograph of '{name}'. Details: {desc}. Isolated on a simple, neutral studio background."
    output_filename = f"{sku}.png"
    output_path = IMAGES_DIR / output_filename
    
    print(f"[{sku}] Starting image generation for '{name}'...")
    
    delay = 5
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-image",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE"],
                    image_config=types.ImageConfig(
                        aspect_ratio="1:1",
                    ),
                ),
            )
            
            image_data = None
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    image_data = part.inline_data.data
                    break
            
            if image_data:
                with open(output_path, "wb") as img_file:
                    img_file.write(image_data)
                print(f"[{sku}] Successfully generated and saved to {output_filename}")
                return sku, f"http://localhost:10999/images/{output_filename}"
            else:
                raise ValueError("No image data returned from model response.")
                
        except APIError as e:
            if e.code == 429:
                print(f"[{sku}] Rate limited (429). Retrying in {delay}s... (Attempt {attempt+1}/{retries})")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"[{sku}] API Error: {e}")
                raise e
        except Exception as e:
            print(f"[{sku}] Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
            delay *= 2
            
    raise Exception(f"[{sku}] Failed to generate image after {retries} attempts.")

def main():
    if not PRODUCTS_JSON_PATH.exists():
        print(f"Products file not found at: {PRODUCTS_JSON_PATH}")
        return
        
    with open(PRODUCTS_JSON_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)
        
    # Filter products that have unsplash URLs
    targets = []
    for product in products:
        images = product.get("image", [])
        if images and any(img.startswith("https://images.unsplash.com") for img in images):
            targets.append(product)
            
    total_targets = len(targets)
    print(f"Found {total_targets} products with Unsplash image URLs to regenerate.")
    
    if total_targets == 0:
        print("No products need image regeneration.")
        return
        
    cpu_count = os.cpu_count() or 4
    print(f"Running ThreadPoolExecutor with {cpu_count} workers...")
    
    results_map = {}
    
    with ThreadPoolExecutor(max_workers=cpu_count) as executor:
        futures = {executor.submit(generate_image_for_product, prod): prod for prod in targets}
        
        completed = 0
        for future in as_completed(futures):
            prod = futures[future]
            try:
                sku, local_url = future.result()
                results_map[sku] = local_url
            except Exception as e:
                print(f"Failed to generate image for SKU {prod['sku']}: {e}")
            finally:
                completed += 1
                print(f"Progress: {completed}/{total_targets} completed.")
                
    # Update products list in memory
    updated_count = 0
    for product in products:
        sku = product["sku"]
        if sku in results_map:
            product["image"] = [results_map[sku]]
            updated_count += 1
            
    # Save back to database
    with open(PRODUCTS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully updated {updated_count} products in products.json with local image links.")

if __name__ == "__main__":
    main()
