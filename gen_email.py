from PIL import Image, ImageDraw, ImageFont

# --- CONFIGURATION ---
email = "ypapadopoulos@mail.ntua.gr"
output_file = "email.png"
font_size = 24
padding = 0

# Adjust for your system:
# macOS: /System/Library/Fonts/Supplemental/Arial.ttf
# Linux: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
# Windows: C:/Windows/Fonts/Arial.ttf
font_path = "/Users/Lato.ttf"
font_path = "/Users/yannis/Library/Fonts/Lato-Regular.ttf"

# --- FONT & TEXT BOUNDS ---
font = ImageFont.truetype(font_path, font_size)
dummy_img = Image.new("RGB", (1, 1))
draw = ImageDraw.Draw(dummy_img)
bbox = draw.textbbox((0, 0), email, font=font)

width = bbox[2] - bbox[0] + 2 * padding
height = bbox[3] - bbox[1] + 2 * padding

# --- DRAW FINAL IMAGE ---
img = Image.new("RGBA", (int(width), int(height)), (255, 255, 255, 0))  # transparent background
draw = ImageDraw.Draw(img)
draw.text((padding, padding), email, font=font, fill=(0, 0, 0))

img.save(output_file)
print(f"Saved: {output_file}")
