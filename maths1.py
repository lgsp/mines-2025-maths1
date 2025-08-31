from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService


class Holder1AlgebraicYoung(VoiceoverScene):
    def construct(self):
        # Set the lang argument to another language code.
        # self.set_speech_service(GTTSService(lang="fr"))
        self.set_speech_service(RecorderService())
        
        # Titre
        title_msg = r"Concours Mines-Télécom 2025 Maths 1 : "
        title_msg += r"inégalité de Young (cas particuliers)"
        titre = Tex(title_msg, font_size=48, color=BLUE).scale(0.75)
        self.play(Write(titre))
        self.wait(1)
        self.play(titre.animate.to_edge(UP))

        texts = [
            "Montrons que pour tout couple de réels positifs x et y on a",
            "xy inférieur ou égal à x puissance p sur p plus y puissance q sur q",
            "avec p et q deux réels strictement plus grand que 1 qui sont conjugués",
            "Si x égale zéro ou y égale zéro alors c'est gagné.",
            "Si p égale q alors deux sur p égale un et donc p vaut 2",
            "c'est-à-dire que l'inégalité à montrer devient x carré sur deux plus y carré sur deux supérieur ou égal à xy",
            "soit x carré plus y carré supérieur ou égal à deux xy",
            "qui revient à x carré plus y carré moins deux xy positif",
        ]

        phrases = [
            r"Montrons que \((x, y)\in (\mathbb{R}_{+})^2,\quad xy\leqslant \dfrac{x^p}{p} + \dfrac{y^q}{q}\)",
            r"avec \((p, q)\in (]1 ; +\infty [)^2,\quad \dfrac{1}{p} + \dfrac{1}{q} = 1\)",
            r"Si \(x = 0\) ou \(y = 0\) alors c'est gagné.",
            r"Si \(p = q\) alors \(\dfrac{2}{p} = 1\) et donc \(p = 2\)",
            r"l'inégalité à montrer devient \(\dfrac{x^2}{2}+\dfrac{y^2}{2}\geqslant xy\)",
            r"soit \(x^2 + y^2 \geqslant 2xy\)",
            r"qui revient à \(x^2 + y^2 - 2xy \geqslant 0\)",
        ]

        text_objects = []  # Stocker les objets texte

        for i, phrase in enumerate(phrases):
            with self.voiceover(text=texts[i]) as tracker:
                text_obj = Tex(
                    phrase,
                    font_size=42,
                    color=GREEN if i == 7 else WHITE
                )

                # Position verticale
                vertical_positions = [
                    2.25, 1.25, 0.5, -0.25, -1, -1.75, -2.5
                ]
                text_obj.shift(UP * vertical_positions[i])
                
                text_objects.append(text_obj)  # Stocker l'objet
                self.play(Write(text_obj), run_time=tracker.duration)

            self.wait(0.5)

        # Pour la dernière phrase - séparer complètement
        text_final = Tex(r"\text{finalement }", font_size=42, color=WHITE)
        formula = Tex(r"\((x - y)^2\geqslant 0\)", font_size=42, color=GREEN)

        final_group = VGroup(text_final, formula).arrange(RIGHT, buff=0.25)
        final_group.shift(DOWN * 3.25)

        final_voice = "finalement x moins y le tout au carré positif "
        final_voice += "ce qui est toujours vrai"
        with self.voiceover(text=final_voice) as tracker:
            self.play(
                Write(text_final),
                run_time=tracker.duration/2
            )
            self.play(
                Write(formula),
                run_time=tracker.duration/2
            )
            
        # Fonction optimisée pour les effets
        def apply_highlight_sequence(mob, effects=None, wait_time=0.3):
            """Applique une séquence d'effets sur un mob avec des pauses."""
            if effects is None:
                effects = [ApplyWave, Circumscribe, Indicate]
            
            for effect_class in effects:
                self.play(effect_class(mob), run_time=0.6)
                self.wait(wait_time)
        
        # Utilisation simple
        apply_highlight_sequence(formula, wait_time=0.5)

        # Encadrer la dernière formule avec style
        framebox = SurroundingRectangle(
            formula, 
            buff=0.15,
            color=YELLOW,
            stroke_width=2.5,
            corner_radius=0.1
        )
        self.play(
            Create(framebox)
        )
        
        self.wait(2)
        
        # Optionnel : faire disparaître ensemble
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )



        
class Holder1GeometricYoung(VoiceoverScene):
    def construct(self):
        # Set the lang argument to another language code.
        # self.set_speech_service(GTTSService(lang="fr"))
        self.set_speech_service(RecorderService())
        
        # Titre
        title_msg = r"Concours Mines-Télécom 2025 Maths 1 : "
        title_msg += r"inégalité de Young (approche géométrique)"
        titre = Tex(title_msg, font_size=45, color=BLUE).scale(0.75)
        self.play(Write(titre))
        self.wait(1)
        self.play(titre.animate.to_edge(UP))
        
        complex_plane = ComplexPlane()
        self.play(Create(complex_plane))
        self.wait()

        # Initial square
        d1 = Dot(complex_plane.n2p(0 + 0j), color=YELLOW)
        d2 = Dot(complex_plane.n2p(2 + 0j), color=YELLOW)
        d3 = Dot(complex_plane.n2p(2 + 2j), color=YELLOW)
        d4 = Dot(complex_plane.n2p(0 + 2j), color=YELLOW)
        dots = [d1, d2, d3, d4]
        self.play(
            *[Create(d) for d in dots]
        )
        self.wait(2)
                  
