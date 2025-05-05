---
title: []
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Ερευνητική Ομάδα Βιοφωτονικής
      image:
        filename: hand_nature.jpg
        caption: "Psaltis, D. & Papadopoulos, I. N. Imaging: The fog clears. Nature 491, 197–198 (2012)"
      text: |
        Μελετάμε πώς συμπεριφέρεται το φως σε βιολογικά μέσα για να επεκτείνουμε τα όρια της απεικόνισης και της ανίχνευσης στη βιοϊατρική. Η έρευνά μας περιλαμβάνει διαμόρφωση μετώπου κύματος, μικροσκοπία πολλαπλών φωτονίων και **τεχνολογίες μικροαισθητήρων** σχεδιασμένες για ενσωμάτωση σε καθημερινές συσκευές.

  - block: slider
    content:
      slides:
        - title: Καλώς ήρθατε στην ομάδα Βιοφωτονικής
          content: Ρίξτε μια ματιά στην έρευνά μας...
          align: center
          background:
            image:
              filename: beautiful-optical-fiber-detail.jpg
              filters:
                brightness: 0.4
            position: right
            color: '#46616e'
          link:
            icon: flask
            icon_pack: fas
            text: Ποιοι είμαστε
            url: ./about-us/
        - title: Διδασκαλία
          content: Δείτε τα μαθήματα και τις διαθέσιμες διπλωματικές εργασίες
          align: left
          background:
            image:
              filename: psf-preview.png
              filters:
                brightness: 0.4
            position: center
            color: '#555'
          link:
            text: Διπλωματικές εργασίες
            url: ./thesis-projects/
    design:
      slide_height: 400px
      is_fullscreen: false
      loop: true
      interval: 2000

  - block: markdown
    content:
      title: Η Ομάδα Μας
      subtitle: |
        <span class="fs-5 d-block">Γνωρίστε τα άτομα πίσω από την έρευνα</span>
      text: |
        <a href="./people/" 
          class="btn btn-dark btn-lg px-5 py-3 mt-4" 
          style="color: white !important; transition: all 0.3s ease;">
          Γνωρίστε την ομάδα →
        </a>
    design:
      columns: '1'
      background:
        color: "#f8f9fa"
        text_color_light: false
      spacing:
        padding: ["3rem", "0", "3rem", "0"]
      css_class: text-center shadow-sm border-top
      animation:
        entrance: fadeInUp
---
