Reveal.on("fragmentshown", event => {
  if (!event.fragment.classList.contains("video-trigger")) return;

  const slide = event.fragment.closest("section");
  const videos = [...slide.querySelectorAll("video")];

  videos.forEach(video => {
    video.pause();
    video.currentTime = 0;
  });

  videos.forEach(video => {
    video.play().catch(error => {
      console.error("Video playback failed:", error);
    });
  });
});

Reveal.on("fragmentshown", event => {
  if (!event.fragment.classList.contains("video-trigger-2")) return;

  const slide = event.fragment.closest("section");
  const first = slide.querySelector(".step-video-1");
  const second = slide.querySelector(".step-video-2");

  first?.pause();

  if (second) {
    second.currentTime = 0;
    second.play().catch(error => {
      console.error("Second video failed:", error);
    });
  }
});