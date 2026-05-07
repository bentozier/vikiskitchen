#!/usr/bin/env python3
"""
Download all 238 gallery images from Viki's Kitchen.
No login or cookies required — images are publicly accessible.

Run from the vikiskitchen/ folder:
    python3 download_gallery.py
"""

import os, time, json, urllib.request, pathlib

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Referer": "https://vikiskitchen.com/gallery",
}

json_path = pathlib.Path(__file__).parent / "gallery_urls.json"
with open(json_path) as f:
    IMAGES = [(item["url"], item["local"]) for item in json.load(f)]

print(f"Downloading {len(IMAGES)} gallery images into gallery/...\n")
os.makedirs("gallery", exist_ok=True)

ok = fail = 0
for i, (url, path) in enumerate(IMAGES):
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        print(f"  ✓ already have {path}")
        ok += 1
        continue
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 1000:
            raise ValueError(f"Response too small ({len(data)} bytes)")
        with open(path, 'wb') as f:
            f.write(data)
        print(f"  ↓ {path} ({len(data)//1024} KB)")
        ok += 1
    except Exception as e:
        print(f"  ✗ {path} — {e}")
        fail += 1
    time.sleep(0.15 if (i % 10 != 9) else 2.0)

print(f"\n{'='*40}")
print(f"✅ Done: {ok} saved, {fail} failed")
if fail:
    print("   Re-run the script to retry any failed images.")
