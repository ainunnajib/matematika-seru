from manim import *

class DiskonBertumpuk(Scene):
    def construct(self):
        # Colors
        ACCENT = "#FF6B6B"
        SUCCESS = "#4ECDC4"
        WARNING = "#FFE66D"
        
        # Hook
        hook = Text("97% ORANG SALAH!", font_size=64, color=ACCENT)
        hook2 = Text("Hitung Diskon", font_size=48).next_to(hook, DOWN)
        self.play(Write(hook), run_time=1)
        self.play(FadeIn(hook2), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(hook), FadeOut(hook2))
        
        # Problem setup - using simple text instead of emoji
        shoe = Text("SEPATU", font_size=48, weight=BOLD)
        price = Text("Rp 500.000", font_size=56, color=SUCCESS).next_to(shoe, DOWN)
        discount = Text("Diskon 50% + 20%", font_size=40, color=WARNING).next_to(price, DOWN)
        
        problem = VGroup(shoe, price, discount)
        self.play(FadeIn(problem))
        self.wait(2)
        
        # Wrong answer
        question = Text("Berapa harga akhir?", font_size=40).to_edge(UP)
        self.play(Write(question))
        
        wrong = Text("500rb - 70% = 150rb?", font_size=48).next_to(problem, DOWN, buff=1)
        self.play(Write(wrong))
        self.wait(1)
        
        # X mark - using text instead of emoji
        x_mark = Text("SALAH!", font_size=72, color=ACCENT)
        self.play(
            FadeOut(problem),
            FadeOut(wrong),
            FadeOut(question),
            FadeIn(x_mark, scale=1.5)
        )
        self.wait(1)
        self.play(FadeOut(x_mark))
        
        # Step by step calculation
        title = Text("Cara yang BENAR:", font_size=40, color=SUCCESS).to_edge(UP)
        self.play(Write(title))
        
        # Step 1 - using Text instead of MathTex
        step1_label = Text("Step 1: Diskon 50%", font_size=36).shift(UP*2)
        step1_calc = Text("500.000 × 50% = 250.000", font_size=40).next_to(step1_label, DOWN)
        self.play(Write(step1_label))
        self.play(Write(step1_calc))
        self.wait(1.5)
        
        # Step 2
        step2_label = Text("Step 2: Diskon 20%", font_size=36).next_to(step1_calc, DOWN, buff=0.8)
        step2_calc = Text("250.000 × 20% = 50.000", font_size=40).next_to(step2_label, DOWN)
        self.play(Write(step2_label))
        self.play(Write(step2_calc))
        self.wait(1.5)
        
        # Result
        result_label = Text("Harga Akhir:", font_size=36).next_to(step2_calc, DOWN, buff=0.8)
        result = Text("250.000 - 50.000 = 200.000", font_size=48, color=SUCCESS).next_to(result_label, DOWN)
        self.play(Write(result_label))
        self.play(Write(result))
        self.wait(2)
        
        # Clear and show comparison
        self.play(
            FadeOut(title), FadeOut(step1_label), FadeOut(step1_calc),
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(result_label), FadeOut(result)
        )
        
        # Comparison
        compare_title = Text("Perbandingan:", font_size=40).to_edge(UP)
        wrong_box = VGroup(
            Text("Cara Salah", font_size=32, color=ACCENT),
            Text("Rp 150.000", font_size=48, color=ACCENT)
        ).arrange(DOWN).shift(LEFT*3)
        
        right_box = VGroup(
            Text("Cara Benar", font_size=32, color=SUCCESS),
            Text("Rp 200.000", font_size=48, color=SUCCESS)
        ).arrange(DOWN).shift(RIGHT*3)
        
        diff = Text("Selisih: Rp 50.000!", font_size=36, color=WARNING).to_edge(DOWN, buff=1)
        
        self.play(Write(compare_title))
        self.play(FadeIn(wrong_box), FadeIn(right_box))
        self.play(Write(diff))
        self.wait(2)
        
        # Formula
        self.play(FadeOut(compare_title), FadeOut(wrong_box), FadeOut(right_box), FadeOut(diff))
        
        formula_title = Text("RUMUS:", font_size=48, color=WARNING).to_edge(UP)
        formula = Text(
            "Harga Akhir = Harga Awal × (1-d1) × (1-d2)",
            font_size=32
        )
        self.play(Write(formula_title))
        self.play(Write(formula))
        self.wait(2)
        
        # CTA
        self.play(FadeOut(formula_title), FadeOut(formula))
        cta = Text("Follow untuk tips matematika!", font_size=44, color=SUCCESS)
        self.play(Write(cta))
        self.wait(2)
        self.play(FadeOut(cta))
