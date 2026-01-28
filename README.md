# Matematika Seru 🎓

Daily educational math videos for Indonesian students, created with Manim and AI voiceover.

## About

Short, engaging math explainers that make mathematics accessible and fun for Indonesian students. Each video tackles a real-world math concept with:
- Clickbait-worthy hooks (because engagement matters!)
- Step-by-step visual explanations
- Indonesian context and examples
- AI-generated voiceover (MLX Audio / Kokoro)

## Tech Stack

- **Animation:** [Manim Community Edition](https://www.manim.community/)
- **Voiceover:** MLX Audio (Kokoro TTS) — local, fast, free
- **Posting:** Twitter/X via @ainunnajib

## Video Structure

Each video follows this format:
```
videos/
└── YYYY-MM-DD-topic-name/
    ├── script.md          # Narration script (Indonesian)
    ├── scene.py            # Manim animation code
    ├── voiceover.wav       # Generated audio
    └── final.mp4           # Rendered video
```

## Topics Covered

- [x] 2026-01-28: Persentase & Diskon Bertumpuk
- [ ] Probabilitas dalam permainan
- [ ] Geometri dalam arsitektur
- [ ] Statistik dalam olahraga
- [ ] Bunga majemuk (compound interest)
- [ ] Rasio dalam resep masakan
- [ ] Teorema Pythagoras sehari-hari
- [ ] ...and more!

## Workflow

1. Write script in `script.md`
2. Create Manim scene in `scene.py`
3. Generate voiceover: `~/clawd/scripts/mlx-tts.sh "$(cat script.md)" voiceover.wav`
4. Render video: `manim render -qh scene.py`
5. Combine audio + video with ffmpeg
6. Commit & push
7. Post to Twitter

## License

Educational content — feel free to use for learning!

---

Created by AI-Noon 🌞 for @ainunnajib
