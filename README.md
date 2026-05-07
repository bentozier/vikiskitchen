# Viki's Kitchen 🍳

A static memorial recipe website for Viki, hosted on GitHub Pages.

## Structure

```
vikiskitchen/
├── index.html          ← The entire website (single file)
├── images/             ← Recipe card images (download with script below)
│   ├── korean-noodle-salad.png
│   └── ... (49 total)
├── download_images.sh  ← Script to pull all images from Squarespace CDN
└── README.md
```

## Setup Steps

### 1. Download recipe images (do this BEFORE canceling Squarespace!)

```bash
chmod +x download_images.sh
./download_images.sh
```

This saves all 49 recipe images locally so they're preserved forever.

### 2. Push to GitHub

```bash
git init
git add .
git commit -m "Launch Viki's Kitchen"
git branch -M main
git remote add origin https://github.com/bentozier/vikiskitchen.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repo on GitHub → **Settings → Pages**
2. Under "Source", select **main** branch, **/ (root)** folder
3. Click **Save**
4. Your site will be live at `https://bentozier.github.io/vikiskitchen` within a minute

### 4. Connect your custom domain (vikiskitchen.com)

In GitHub Pages settings, add your custom domain: `vikiskitchen.com`

Then update your DNS with your domain registrar:
- Add an **A record** pointing to `185.199.108.153`
- Add an **A record** pointing to `185.199.109.153`
- Add an **A record** pointing to `185.199.110.153`
- Add an **A record** pointing to `185.199.111.153`
- Add a **CNAME record**: `www` → `bentozier.github.io`

DNS changes take 10–60 minutes to propagate.

### 5. Cancel Squarespace

Once your site is live at vikiskitchen.com on GitHub Pages, you're safe to cancel Squarespace.

## Maintenance

To update the site in the future, just edit `index.html` and push:
```bash
git add index.html
git commit -m "Update about section"
git push
```

Changes go live within 1–2 minutes.
