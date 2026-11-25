# fionahoang.dev

Source for my personal site at [fionahoang.dev](https://fionahoang.dev). It's set up like a dictionary entry, with a sense for each part of my life.

The site is one static page. It uses plain HTML, CSS and JavaScript, with no frameworks and nothing to install. GitHub Pages serves it straight from `main`.

## Layout

```
src/
  content.py   all the copy: experience, papers, languages, contact
  build.py     layout, styles and scripts; writes index.html
index.html     generated; don't edit by hand
img/ audio/ video/
resume.pdf
```

## Editing

To change a word, edit `src/content.py`. To change how something looks or behaves, edit `src/build.py`. Then rebuild:

```
python3 src/build.py
```

The build needs Python 3.8 or later and only the standard library. Commit the regenerated `index.html` along with the source, and Pages deploys it on push.

## Notes

- Photos are resized and have their EXIF data stripped before they go in `img/`.
- The video is compressed with no audio track.
- Motion respects `prefers-reduced-motion`, and the custom cursor only appears on mouse and trackpad.
- Both colour palettes were checked against WCAG contrast.
