---
# Leave the homepage title empty to use the site title
title: []
date: 2022-10-24
type: landing


sections:
  - block: hero
    content:
      title: |
        Ερευνητική ομάδα Βιοφωτονικής
      image:
        filename: hand_nature.jpg
        caption: "test"
      text: |
        <br>
        
        Η ερευνητική ομάδα **Βιοφωτονικής** επικεντρώνεται στην έρευνα στον τομέα της βιοϊατρικής απεικόνισης, των μέσων σκέδασης και της μικροσκοπικής βιοανίχνευσης με έμφαση στις συσκευές ηλεκτρονικών ειδών ευρείας κατανάλωσης.

  - block: slider
    content:
      slides:
        - title: Καλώς ήρθατε στην ομάδα Βιοφωτονικής
          content: Ρίξτε μια ματιά στο τι δουλεύουμε...
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: beautiful-optical-fiber-detail.jpg
              filters:
                brightness: 0.4
            position: right
            color: '#666'
          link:
            icon: flask
            icon_pack: fas
            text: About Us
            url: ../about/
        - title: Lunch & Learn ☕️
          content: 'Share your knowledge with the group and explore exciting new topics together!'
          align: left
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: beautiful-optical-fiber-detail.jpg
              filters:
                brightness: 0.4
            position: center
            color: '#555'
        - title: World-Class Semiconductor Lab
          content: 'Just opened last month!'
          align: right
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: beautiful-optical-fiber-detail.jpg
              filters:
                brightness: 0.4
            position: center
            color: '#333'
          link:
            icon: graduation-cap
            icon_pack: fas
            text: Join Us
            url: ../contact/
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
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '2'
---
