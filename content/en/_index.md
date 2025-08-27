---
# Leave the homepage title empty to use the site title
title: []
date: 2022-10-24
type: landing


sections:
  # - block: hero
  #   content:
  #     title: |
  #       Biophotonics Research Group
  #     image:
  #       filename: hand_nature.jpg
  #       caption: "Psaltis, D. & Papadopoulos, I. N. Imaging: The fog clears. Nature 491, 197–198 (2012)"
  #       captionwidth: '400px'
  #     text: |
  #       We explore how light behaves in biological media to push the limits of biomedical imaging and sensing. Our research spans wavefront shaping, multiphoton microscopy, and **miniature biosensing technologies** designed for integration into everyday consumer devices.

  - block: fullscreen-hero
    content:
      image: 
        filename: hand_nature.jpg       # Path relative to `static/`
      title: Welcome to the Department
      text: Advancing knowledge through education and research.
      cta:
        label: Learn More
        url: /el/department/


  - block: slider
    content:
      slides:
        - title: Welcome to the Biophotonics group
          content: Take a look at what we're working on...
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: beautiful-optical-fiber-detail.jpg
              filters:
                brightness: 0.4
            position: right
            color: '#46616e'
          link:
            icon: flask
            icon_pack: fas
            text: About Us
            url: ./about-us/
        - title: Teaching activities
          content: 'Explore our courses and available thesis projects'
          align: left
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: psf-preview.png
              filters:
                brightness: 0.4
            position: center
            color: '#555'
          link:
            # icon: flask
            # icon_pack: fas
            text: Thesis projects
            url: ./thesis-projects/
        - title: We are hiring
          content: 'We are looking for motivated researchers at the PhD or PostDoc level'
          align: right
          link:
            text: Hiring!
            url: ./post/2025-5-29-job-openings
          background:
            image:
              filename: gradient-ntua.png
              filters:
                brightness: 0.7
            position: right
            color: '#666'
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: 400px
      # Make the slides full screen within the browser window?
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000
  
  # - block: collection
  #   content:
  #     title: Latest News
  #     subtitle:
  #     text:
  #     count: 5
  #     filters:
  #       author: ''
  #       category: ''
  #       exclude_featured: false
  #       publication_type: ''
  #       tag: ''
  #     offset: 0
  #     order: desc
  #     page_type: post
  #   design:
  #     # background:
  #     # # Choose a color such as from https://html-color-codes.info
  #     #   color: 'navy'
  #     #   # Text color (true=light, false=dark, or remove for the dynamic theme color).
  #     #   text_color_light: true
  #     view: card
  #     columns: '1'

  # - block: collection
  #   id: Thesis Projects
  #   content:
  #     title: Available thesis projects
  #     subtitle: ''
  #     text: 'Undergrad and postgrad thesis projects'
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 0
  #     # Filter on criteria
  #     filters:
  #       # The folders to display content from
  #       folders:
  #         - thesis-projects
  #       author: ""
  #       category: ""
  #       tag: ""
  #       publication_type: ""
  #       featured_only: false
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #     # Choose how many pages you would like to offset by
  #     # Useful if you wish to show the first item in the Featured widget
  #     offset: 0
  #     # Field to sort by, such as Date or Title
  #     sort_by: 'Date'
  #     sort_ascending: false
  #   design:
  #     # Choose a listing view
  #     view: card
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  # - block: collection
  #   content:
  #     title: Latest Preprints
  #     text: ""
  #     count: 5
  #     filters:
  #       folders:
  #         - publication
  #       publication_type: 'article'
  #   design:
  #     view: citation
  #     columns: '1'


  - block: markdown
    content:
      title: Meet Our Team
      subtitle: |
        <span class="fs-5 d-block">Learn more about the people behind the research</span>
      text: |
        <a href="./people/" 
          class="btn btn-dark btn-lg px-5 py-3 mt-4" 
          style="color: white !important; transition: all 0.3s ease;">
          Explore our group →
        </a>
    design:
      columns: '1'
      background:
        color: "#f8f9fa"  # Adjust if needed (e.g., "#e9ecef" or your gray tone)
        text_color_light: false
      spacing:
        padding: ["3rem", "0", "3rem", "0"]
      css_class: text-center shadow-sm border-top
      animation:
        entrance: fadeInUp


---
