# 📚 How to Add a New Course

## 1. Create a New Course Folder

- Path: `content/courses/course-name/`
- Files: `index.md`, `featured.jpg`

## 2. Example Front Matter

```yaml
title: "Course Title"
date: 2025-09-01
type: "courses"
summary: "Brief summary here."
tags: ["Tag1", "Tag2"]
image:
  filename: "featured.jpg"
  alttext: "Short image description"
```

Write the full course description below the front matter.

## 3. Image Guidelines

Place featured.jpg inside the course folder.
Size: 800×400 px minimum, under 200 KB.

## 4. Multilingual Notes

Hugo auto-generates /en/courses/ or /el/courses/
No hardcoded links.
## 5. Checkpoints

Image visible
Links work (syllabus, external)
Related courses show if tags match
SEO fields filled (optional)