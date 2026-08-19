# Personal Homepage
This repository contains the source code for my personal website, hosted at [https://hanbit-o.github.io/](https://hanbit-o.github.io/).

## Features
- Personal profile and background
- Research projects and publications
- Contact information
- Responsive design

## Local Development
To view or edit the website locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/hanbit-o/hanbit-o.github.io.git
   ```
2. Open the folder in your code editor.
3. Start a local web server from the repository root:
   ```bash
   python3 -m http.server
   ```
4. Open [http://localhost:8000](http://localhost:8000) in your browser.

## Asset Structure

All static assets live under a single `assets/` directory:

```text
assets/
├── home/       # Assets used by the main homepage
├── shared/     # CSS and JavaScript shared by research pages
└── projects/   # Images, videos, and documents owned by each project
```

Use paths relative to each HTML file so pages also work when opened directly
with a `file://` URL. Root pages use `assets/...`, while pages inside `research/`
or `blog/` use `../assets/...`:

```html
<link rel="stylesheet" href="../assets/shared/css/bulma.min.css">
<img src="../assets/projects/sart/images/overview-v2.png" alt="SART overview">
```

## Deployment
This site is automatically deployed via GitHub Pages. 

## License
License: TBD (To Be Determined)
