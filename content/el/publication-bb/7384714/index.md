---
title: Optical Tomographic Image Reconstruction Based on Beam Propagation and Sparse
  Regularization

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Ulugbek S. Kamilov
- Yannis Papadopoulos
- Morteza H. Shoreh
- Alexandre Goy
- Cedric Vonesch
- Michael Unser
- Demetri Psaltis

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2016-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2025-05-07T10:20:14.028218Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*IEEE Transactions on Computational Imaging*'
publication_short: ''

doi: 10.1109/tci.2016.2519261

abstract: Optical tomographic imaging requires an accurate forward model as well as
  regularization to mitigate missing-data artifacts and to suppress noise. Nonlinear
  forward models can provide more accurate interpretation of the measured data than
  their linear counterparts, but they generally result in computationally prohibitive
  reconstruction algorithms. Although sparsity-driven regularizers significantly improve
  the quality of reconstructed image, they further increase the computational burden
  of imaging. In this paper, we present a novel iterative imaging method for optical
  tomography that combines a nonlinear forward model based on the beam propagation
  method (BPM) with an edge-preserving three-dimensional (3-D) total variation (TV)
  regularizer. The central element of our approach is a time-reversal scheme, which
  allows for an efficient computation of the derivative of the transmitted wave-field
  with respect to the distribution of the refractive index. This time-reversal scheme
  together with our stochastic proximal-gradient algorithm makes it possible to optimize
  under a nonlinear forward model in a computationally tractable way, thus enabling
  a high-quality imaging of the refractive index throughout the object. We demonstrate
  the effectiveness of our method through several experiments on simulated and experimentally
  measured data.

# Summary. An optional shortened abstract.
summary: ''

tags: []

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
volume: '*2*'
pages: 59-70
---

