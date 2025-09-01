from manim import *
from manim import ManimColor
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
        titre = Tex(title_msg, font_size=35, color=BLUE).scale(0.75)
        self.play(Write(titre))
        self.wait(1.5)
        self.play(titre.animate.to_edge(UP))
        self.wait(1.5)
        
        complex_plane = ComplexPlane()
        self.play(
            ReplacementTransform(titre, complex_plane)
        )
        self.wait(1.5)

        # Initial square
        d1 = Dot(complex_plane.n2p(-2 -2j), color=YELLOW)
        d2 = Dot(complex_plane.n2p(2 - 2j), color=YELLOW)
        d3 = Dot(complex_plane.n2p(2 + 2j), color=YELLOW)
        d4 = Dot(complex_plane.n2p(-2 + 2j), color=YELLOW)
        dots = [d1, d2, d3, d4]
        self.play(
            *[Create(d) for d in dots]
        )
        self.wait(2)

        l12 = Line(d1, d2, color=YELLOW)
        l23 = Line(d2, d3, color=YELLOW)
        l34 = Line(d3, d4, color=YELLOW)
        l41 = Line(d4, d1, color=YELLOW)
        lines = [l12, l23, l34, l41]
        self.play(
            *[Create(l) for l in lines]
        )
        self.wait(2)

        brace_x = Brace(l12, color=BLUE)
        x_text = brace_x.get_tex("x")
        brace_y = Brace(l41, color=BLUE)
        y_text = brace_y.get_tex("y")
        diag = Line(d1, d3, color=RED)
        









class Holder1GeometricYoungStepByStep(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        # Titre rapide
        txt_title = "Inégalité de Young (géométrique)"
        titre = Tex(txt_title, font_size=40, color=BLUE)
        self.play(Write(titre))
        self.wait(1)
        self.play(FadeOut(titre))

        # -------------------------------------------------
        # 1) Petit carré bleu O(0,0) A(1,0) B(1,1) C(0,1)
        # -------------------------------------------------
        O, A, B, C = (0,0,0), (1,0,0), (1,1,0), (0,1,0)
        small_square = Polygon(O, A, B, C,
                               color=BLUE,
                               fill_color=BLUE,
                               fill_opacity=0.4,
                               stroke_width=2)

        diag_small = Line(O, B, color=YELLOW, stroke_width=2)

        label_small = MathTex(
            "xy=x^{2}=\\frac{x^{2}}{2}+\\frac{x^{2}}{2}",
            font_size=36
        ).to_edge(UP)

        self.play(Create(small_square))
        self.play(Create(diag_small), Write(label_small))
        self.wait(2)

        # -------------------------------------------------
        # 2) Rectangle orange O D(2,0) E(2,1) C(0,1)
        # -------------------------------------------------
        D, E = (2,0,0), (2,1,0)
        rectangle = Polygon(O, D, E, C,
                            color=ORANGE,
                            fill_color=ORANGE,
                            fill_opacity=0.4,
                            stroke_width=2)

        self.play(ReplacementTransform(small_square, rectangle))
        self.wait(1)

        # -------------------------------------------------
        # 3) Grand carré rose O(0,0) D(2,0) F(2,2) G(0,2)
        # -------------------------------------------------
        F, G = (2,2,0), (0,2,0)
        big_square = Polygon(O, D, F, G,
                             color=PINK,
                             fill_color=PINK,
                             fill_opacity=0.2,
                             stroke_width=2)

        diag_big = Line(O, F, color=YELLOW, stroke_width=2)

        # -------------------------------------------------
        # 4) Triangle BEF (identique à OAB translaté)
        # -------------------------------------------------
        B_shift = (1,1,0)   # B original
        E_point  = E
        F_point  = F
        triangle_BEF = Polygon(B_shift, E_point, F_point,
                               color=BLUE,
                               fill_color=BLUE,
                               fill_opacity=0.7,
                               stroke_width=2)

        # -------------------------------------------------
        # 5) Formules finales
        # -------------------------------------------------
        xy_formula   = MathTex(
            "xy = 2\\times 1 = 2",
            font_size=36,
            color=ORANGE
        ).to_edge(UP)
        sum_formula  = MathTex(
            "\\frac{x^{2}}{2}+\\frac{y^{2}}{2}=2+1=3",
            font_size=36,
            color=PINK
        ).next_to(xy_formula, DOWN, buff=0.3)
        inequality   = MathTex(
            "2 < 3",
            font_size=40,
            color=YELLOW
        ).next_to(sum_formula, DOWN, buff=0.3)

        txt_voice = "Élargissons x à 2 et conservons y à 1. "
        txt_voice += "Le rectangle orange a une aire de 2. "
        txt_voice += "Le carré rose totalise 4, soit 2 + 2, "
        txt_voice += "mais seule la moitié de chaque demi-carré "
        txt_voice += "est nécessaire : 2 + 1 = 3. Colorons le "
        txt_voice += "triangle BEF : il a la même aire que le "
        txt_voice += "triangle OAB du petit carré, prouvant "
        txt_voice += "ainsi que 2 < 3."
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                Create(big_square),
                ReplacementTransform(diag_small, diag_big),
                run_time=tracker.duration/2
            )
            self.play(
                FadeIn(triangle_BEF),
                ReplacementTransform(label_small, xy_formula),
                Write(sum_formula),
                Write(inequality),
                run_time=tracker.duration/2
            )

        # Encadrage final
        box = SurroundingRectangle(inequality, color=WHITE, buff=0.2)
        self.play(Create(box))
        self.wait(4)



class Holder1GeometricYoung2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())
        
        # Titre éphémère
        txt_title = "Inégalité de Young (géométrique)"
        titre = Tex(txt_title, font_size=40, color=BLUE)
        self.play(Write(titre))
        self.wait(1)
        self.play(FadeOut(titre))
        
        # Configuration centrale
        center_point = ORIGIN
        
        # === ÉTAPE 1 : CARRÉ INITIAL ===
        side_length = 3
        square = Square(
            side_length=side_length,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(center_point)
        
        # Labels
        x_label = MathTex("x", font_size=36, color=GREEN).next_to(square.get_edge_center(DOWN), DOWN)
        y_label = MathTex("x", font_size=36, color=RED).next_to(square.get_edge_center(LEFT), LEFT)
        
        # Diagonale pour le carré
        diagonal = Line(
            square.get_corner(DL), 
            square.get_corner(UR), 
            color=YELLOW, 
            stroke_width=3
        )
        
        # Triangles formés par la diagonale
        triangle1 = Polygon(
            square.get_corner(DL),
            square.get_corner(DR),
            square.get_corner(UR),
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.4
        )
        triangle2 = Polygon(
            square.get_corner(DL),
            square.get_corner(UR),
            square.get_corner(UL),
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=0.4
        )
        
        # Formule condensée
        formula = MathTex("A = x^2 = \\frac{x^2}{2} + \\frac{x^2}{2}", 
                         font_size=36, color=WHITE).to_edge(UP)

        txt_voice = "Commençons avec un carré de côté x"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(Create(square), Write(x_label), Write(y_label))

        txt_voice = "L'aire est x carré, exactement égale à la somme "
        txt_voice += "des deux demi-carrés formés par la diagonale"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                Create(diagonal),
                FadeIn(triangle1),
                FadeIn(triangle2),
                Write(formula),
                run_time=tracker.duration
            )
        
        self.wait(2)
        
        # === ÉTAPE 2 : MOUVEMENT PROGRESSIF ===
        # Créer le rectangle avec des paramètres variables
        x_new = 4
        y_new = 2
        
        # Animation séquentielle : d'abord x, puis y
        txt_voice = "Maintenant, écartons d'abord la dimension horizontale"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                square.animate.stretch_about_point(
                    x_new/side_length, 0, center_point
                ),
                x_label.animate.next_to(
                    square.get_edge_center(DOWN), DOWN).shift(RIGHT*0.5),
                run_time=tracker.duration
            )
        
        # Mise à jour de x_label
        x_label_new = MathTex(
            "x'",
            font_size=36,
            color=GREEN
        ).next_to(square.get_edge_center(DOWN), DOWN)

        txt_voice = "Puis la dimension verticale"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                square.animate.stretch_about_point(
                    y_new/side_length, 1, center_point
                ),
                Transform(x_label, x_label_new),
                y_label.animate.next_to(
                    square.get_edge_center(LEFT), LEFT).shift(UP*0.3),
                run_time=tracker.duration
            )
        
        # Mise à jour finale des labels
        x_final = MathTex(
            "x",
            font_size=36,
            color=GREEN
        ).next_to(square.get_edge_center(DOWN), DOWN)
        y_final = MathTex(
            "y",
            font_size=36,
            color=RED
        ).next_to(square.get_edge_center(LEFT), LEFT)
        
        self.play(
            Transform(
                x_label,
                x_final
            ),
            Transform(
                y_label,
                MathTex(
                    "y",
                    font_size=36,
                    color=RED
                ).next_to(
                    square.get_edge_center(LEFT), LEFT)
            )
        )
        
        # === ÉTAPE 3 : NOUVEAU RECTANGLE ET INÉGALITÉ ===
        # Rectangle final (le même objet square transformé)
        rectangle = square
        
        # Supprimer l'ancienne diagonale et créer la nouvelle
        new_diagonal = Line(
            rectangle.get_corner(DL), 
            rectangle.get_corner(UR), 
            color=YELLOW, 
            stroke_width=3
        )
        
        # Nouveaux triangles adaptés
        new_triangle1 = Polygon(
            rectangle.get_corner(DL),
            rectangle.get_corner(DR),
            rectangle.get_corner(UR),
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3
        )
        new_triangle2 = Polygon(
            rectangle.get_corner(DL),
            rectangle.get_corner(UR),
            rectangle.get_corner(UL),
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=0.3
        )

        txt_voice = "La diagonale s'adapte au nouveau rectangle"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                ReplacementTransform(diagonal, new_diagonal),
                Transform(triangle1, new_triangle1),
                Transform(triangle2, new_triangle2),
                run_time=tracker.duration
            )
        
        # Formules finales
        formula_rect = MathTex(
            "A = xy",
            font_size=36,
            color=BLUE
        ).to_edge(UP)
        inequality = MathTex(
            "xy \\leq \\frac{x^2 + y^2}{2}",
            font_size=36,
            color=YELLOW
        )
        inequality.next_to(formula_rect, DOWN)

        txt_voice = "L'aire devient xy et l'inégalité de Young "
        txt_voice += "apparaît dès que x et y sont différents"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                ReplacementTransform(formula, formula_rect),
                Write(inequality),
                run_time=tracker.duration
            )
        
        # Encadrer l'inégalité
        box = SurroundingRectangle(inequality, color=WHITE, buff=0.2)
        self.play(Create(box))
        
        # Animation finale : montrer l'écart
        gap_indicator = Arrow(
            rectangle.get_corner(UR),
            rectangle.get_corner(UR) + UP*0.5 + RIGHT*0.5,
            color=RED,
            buff=0.1
        )
        
        gap_text = MathTex("\\text{Écart}", font_size=24, color=RED)
        gap_text.next_to(gap_indicator, UR)

        txt_voice = "L'écart entre les deux aires représente l'inégalité"
        with self.voiceover(text=txt_voice) as tracker:
            self.play(
                GrowArrow(gap_indicator),
                Write(gap_text),
                run_time=tracker.duration
            )
        
        self.wait(4)        


from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class Holder1GeometricYoungGeneral(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        titre = Tex("Inégalité de Young (générale)", font_size=40, color=BLUE)
        self.play(Write(titre))
        self.wait(1)
        self.play(FadeOut(titre))

        # Paramètres généraux
        y = 1.5      # côté du petit carré
        x = 2.8      # côté du grand carré  (x > y pour voir l’inégalité)

        # Origine commune (bas-gauche)
        origin = ORIGIN

        # 1) Carré gauche : aire y²
        sq_y = Square(side_length=y, color=GREEN, fill_color=GREEN, fill_opacity=0.3)\
               .move_to(origin + y/2*UP + y/2*RIGHT)
        diag_y = Line(sq_y.get_corner(DL), sq_y.get_corner(UR), color=YELLOW, stroke_width=2)

        # 2) Rectangle central : aire x·y
        rect = Rectangle(width=x, height=y, color=ORANGE, fill_color=ORANGE, fill_opacity=0.3)\
               .move_to(origin + y/2*UP + (y + x/2)*RIGHT)

        # 3) Carré droit : aire x²
        sq_x = Square(side_length=x, color=BLUE, fill_color=BLUE, fill_opacity=0.3)\
               .move_to(origin + x/2*UP + (y + x + x/2)*RIGHT)
        diag_x = Line(sq_x.get_corner(DL), sq_x.get_corner(UR), color=YELLOW, stroke_width=2)

        # Labels
        label_y = MathTex("y^2", color=GREEN).next_to(sq_y, DOWN)
        label_xy = MathTex("xy", color=ORANGE).next_to(rect, DOWN)
        label_x = MathTex("x^2", color=BLUE).next_to(sq_x, DOWN)

        # Formule finale
        inequality = MathTex("xy \\leq \\frac{x^2 + y^2}{2}", font_size=44, color=WHITE).to_edge(UP)

        # Animation ordonnée
        with self.voiceover(text="Voici le carré de côté y, d'aire y carré") as tracker:
            self.play(Create(sq_y), Write(label_y), Create(diag_y))

        with self.voiceover(text="À côté, le rectangle d'aire x fois y") as tracker:
            self.play(Create(rect), Write(label_xy))

        with self.voiceover(text="Enfin le carré de côté x, d'aire x carré") as tracker:
            self.play(Create(sq_x), Write(label_x), Create(diag_x))

        with self.voiceover(text="L'inégalité de Young émerge visuellement") as tracker:
            self.play(Write(inequality))

        # Encadrage
        box = SurroundingRectangle(inequality, color=WHITE, buff=0.2)
        self.play(Create(box))

        self.wait(4)



class YoungTangram(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        # 1. Titre
        titre = Tex("Tangram de l'inégalité de Young", font_size=40, color=BLUE)
        self.play(Write(titre))
        self.wait(1)
        self.play(FadeOut(titre))

        # Paramètres
        x, y = 3, 1.8  # x > y pour voir l'espace restant
        center = ORIGIN

        # ------------------------------------------------------------
        # 1) DEMI-CARRÉS (x²/2 et y²/2)
        # ------------------------------------------------------------
        # Demi-carré droit (x²/2)
        half_x = Polygon(
            center + LEFT*x/2 + DOWN*y/2,
            center + RIGHT*x/2 + DOWN*y/2,
            center + RIGHT*x/2 + UP*(x-y/2),
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3
        )

        # Demi-carré gauche (y²/2)
        half_y = Polygon(
            center + LEFT*x/2 + DOWN*y/2,
            center + LEFT*x/2 + UP*(y/2),
            center + RIGHT*x/2 + UP*(y/2),
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.3
        )

        # ------------------------------------------------------------
        # 2) RECTANGLE xy À INSÉRER
        # ------------------------------------------------------------
        rectangle = Rectangle(width=x, height=y, color=ORANGE, fill_color=ORANGE, fill_opacity=0.6)\
                    .move_to(center + UP*y/4)  # Position intermédiaire

        # ------------------------------------------------------------
        # 3) PIÈCES DU TANGRAM (triangles et trapèzes)
        # ------------------------------------------------------------
        # Triangle 1 (coin inférieur droit)
        tri1 = Polygon(
            half_x.get_vertices()[0],
            half_x.get_vertices()[1],
            center + RIGHT*x/2 + UP*(y/2),
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.75
        )

        # Triangle 2 (coin supérieur gauche)
        tri2 = Polygon(
            half_y.get_vertices()[1],
            half_y.get_vertices()[2],
            center + LEFT*x/2 + UP*(y/2),
            color=RED, fill_color=RED, fill_opacity=0.75
        )

        # Trapèze central (forme adaptée)
        trapezoid = Polygon(
            center + LEFT*x/2 + UP*(y/2),
            center + RIGHT*x/2 + UP*(y/2),
            center + RIGHT*x/2 + UP*(x-y/2),
            center + LEFT*x/2 + UP*(y/2),
            color=PURPLE, fill_color=PURPLE, fill_opacity=0.5
        )

        # ------------------------------------------------------------
        # 4) ÉTIQUETTES
        # ------------------------------------------------------------
        label_xy = MathTex("xy", color=ORANGE).next_to(rectangle, DOWN)
        label_sum = MathTex(
            r"\dfrac{x^2}{2} + \dfrac{y^2}{2}",
            font_size=36,
            color=WHITE
        ).to_edge(UP)
        inequality = MathTex(
            r"xy < \dfrac{x^2}{2} + \dfrac{y^2}{2}",
            font_size=44,
            color=YELLOW
        ).next_to(label_sum, DOWN)

        # ------------------------------------------------------------
        # 5) ANIMATIONS
        # ------------------------------------------------------------
        # Affichage des demi-carrés
        with self.voiceover(text="Voici les deux demi-carrés x²/2 et y²/2") as tracker:
            self.play(Create(half_x), Create(half_y))

        # Construction visuelle du tangram
        with self.voiceover(text="En assemblant les pièces, on peut y loger exactement le rectangle d'aire xy") as tracker:
            self.play(
                Create(tri1),
                Create(tri2),
                Create(trapezoid),
                run_time=tracker.duration/2
            )
            self.play(
                FadeIn(rectangle),
                Write(label_xy),
                run_time=tracker.duration/2
            )

        # Mise en évidence de l'espace restant
        remaining_space = VGroup(
            Polygon(
                center + RIGHT*x/2 + UP*(y/2),
                center + RIGHT*x/2 + UP*(x-y/2),
                center + LEFT*x/2 + UP*(x-y/2),
                center + LEFT*x/2 + UP*(y/2),
                color=WHITE, fill_color=WHITE, fill_opacity=0.2
            ),
            Polygon(
                center + LEFT*x/2 + UP*(y/2),
                center + LEFT*x/2 + UP*y/2,
                center + RIGHT*x/2 + UP*y/2,
                center + RIGHT*x/2 + UP*(y/2),
                color=WHITE, fill_color=WHITE, fill_opacity=0.2
            )
        )

        with self.voiceover(text="Et il reste encore de la place !") as tracker:
            self.play(
                FadeIn(remaining_space),
                Write(label_sum),
                Write(inequality),
                run_time=tracker.duration
            )

        # Encadrage final
        box = SurroundingRectangle(inequality, color=WHITE, buff=0.2)
        self.play(Create(box))

        self.wait(4)        




class YoungGeoExact(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        # Fade-in title
        title = Tex("Inégalité de Young – construction géométrique", font_size=35, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # -------------------------------------------------
        # 1) Carré bleu OABC
        # -------------------------------------------------
        O, A, B, C = map(np.array, [(0,0,0), (1,0,0), (1,1,0), (0,1,0)])
        square_blue = Polygon(O, A, B, C, color=BLUE, fill_color=BLUE, fill_opacity=0.5)

        diag_OB = Line(O, B, color=YELLOW, stroke_width=2)

        # -------------------------------------------------
        # 2) Rectangle orange ODCE
        # -------------------------------------------------
        D, E = np.array([2,0,0]), np.array([2,1,0])
        rect_orange = Polygon(O, D, E, C, color=ORANGE, fill_color=ORANGE, fill_opacity=0.4)

        # -------------------------------------------------
        # 3) Carré rose ODFG
        # -------------------------------------------------
        F, G = np.array([2,2,0]), np.array([0,2,0])
        square_pink = Polygon(O, D, F, G, color=PINK, fill_color=PINK, fill_opacity=0.3)

        diag_OF = Line(O, F, color=YELLOW, stroke_width=2)

        # -------------------------------------------------
        # 4) Triangle BEF (blue)
        # -------------------------------------------------
        triangle_BEF = Polygon(B, E, F, color=WHITE, fill_color=BLUE, fill_opacity=0.7)

        # -------------------------------------------------
        # Labels
        # -------------------------------------------------
        label_sq1 = MathTex("1", font_size=28).move_to(square_blue.get_center())
        label_rect = MathTex("2\\times 1 = 2", font_size=28).move_to(rect_orange.get_center())
        label_sq2 = MathTex("2^2 = 4", font_size=28).move_to(square_pink.get_center())
        label_sum = MathTex("\\frac{2^2}{2} + \\frac{1^2}{2} = 2.5", font_size=32).to_edge(UP)
        label_ineq = MathTex("2 < 2.5", font_size=36, color=YELLOW).next_to(label_sum, DOWN)

        # -------------------------------------------------
        # Animate
        # -------------------------------------------------
        self.play(Create(square_blue), Write(label_sq1))
        self.play(Create(diag_OB))
        self.wait(0.5)

        self.play(Create(rect_orange), Write(label_rect))
        self.wait(0.5)

        self.play(Create(square_pink), Write(label_sq2))
        self.play(Create(diag_OF))
        self.wait(0.5)

        self.play(FadeIn(triangle_BEF))
        self.play(Write(label_sum), Write(label_ineq))

        # Encadrage final
        box = SurroundingRectangle(label_ineq, color=WHITE, buff=0.2)
        self.play(Create(box))

        self.wait(3)        





class YoungIntegralProof(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        # 1. Axes
        ax = Axes(
            x_range=[0, 3, 0.5], y_range=[0, 3, 0.5],
            axis_config={"include_numbers": True}
        ).scale(0.8).shift(DOWN*0.5)

        # 2. Parameters (general)
        p = 3
        q = p/(p-1)            # 1/p + 1/q = 1
        x = 2
        y = x**(p-1)           # inverse function gives y = f(x)

        # 3. Function and its inverse
        curve = ax.plot(lambda t: t**(p-1), x_range=[0, 3], color=BLUE_B)

        # 4. Areas
        area_under_f = ax.get_area(ax.plot(lambda t: t**(p-1), [0, x]),
                                     x_range=[0, x], color=RED, opacity=0.4)
        area_under_g = ax.get_area(ax.plot(lambda t: t**(q-1), [0, y]),
                                     x_range=[0, y], color=BLUE, opacity=0.4)
        rectangle_xy = Rectangle(width=x, height=y,
                                 fill_color=GREEN, fill_opacity=0.4, stroke_width=2)\
                        .move_to(ax.c2p(x/2, y/2))

        # 5. Labels
        labels = VGroup(
            MathTex("f(t)=t^{p-1}", color=BLUE).to_corner(UR),
            MathTex("\\int_{0}^{x} t^{p-1}\\,dt = \\frac{x^{p}}{p}", color=RED).next_to(area_under_f, RIGHT),
            MathTex("\\int_{0}^{y} t^{q-1}\\,dt = \\frac{y^{q}}{q}", color=BLUE).next_to(area_under_g, UP),
            MathTex("xy", color=GREEN).move_to(rectangle_xy)
        )

        # 6. Inequality
        inequality = MathTex("xy \\leq \\frac{x^{p}}{p}+\\frac{y^{q}}{q}", font_size=48).to_edge(UP)

        # 7. Animation
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(FadeIn(area_under_f), FadeIn(area_under_g), FadeIn(rectangle_xy))
        self.play(Write(labels), Write(inequality))

        # 8. Final box
        box = SurroundingRectangle(inequality, color=WHITE, buff=0.2)
        self.play(Create(box))
        self.wait(3)        




class YoungGeom2(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.camera.background_color = ManimColor("#606060")
        # gris foncé par exemple
        cyan_hex = ManimColor("#4FC3F7") # C-x C-t (transpose-lines)
        green = ManimColor("#4CAF50")
        navy = ManimColor("#003366")
        orange = ManimColor("#FF9800")
        yellow = ManimColor("#FFD54F")
        
        self.set_speech_service(RecorderService())

        # ---------- 1) Carré bleu ABCD + labels x=y et y=x ----------
        side = 2
        A = DL * 2.5
        B = A + RIGHT * side
        C = A + RIGHT * side + UP * side
        D = A + UP * side
        square = Polygon(
            A, B, C, D,
            color=navy,
            fill_color=navy, fill_opacity=0.25
        )

        label_x_eq_y = MathTex("x=y", color=navy).next_to(square, DOWN)
        label_y_eq_x = MathTex("y=x", color=navy).next_to(square, LEFT)

        self.play(Create(square), Write(label_x_eq_y), Write(label_y_eq_x))
        self.wait()
        # ---------- 2) Diagonale rouge ----------
        diag = Line(A, C, color=RED, stroke_width=5)
        self.play(Create(diag))
        self.wait()
        # ---------- 3) Disparition des labels ----------
        # self.play(FadeOut(label_x_eq_y), FadeOut(label_y_eq_x))

        # ---------- 4 & 5) Triangles + étiquettes 1/2 x² et 1/2 y² ----------
        tri_ACD = Polygon(
            A, C, D,
            color=yellow,
            fill_color=yellow,
            fill_opacity=0.75
        )
        tri_ABC = Polygon(
            A, B, C,
            color=cyan_hex,
            fill_color=cyan_hex,
            fill_opacity=0.75
        )

        label_half_y2 = MathTex(
            r"\dfrac{y^2}{2}=\dfrac{x^2}{2}",
            color=yellow
        ).next_to(square, LEFT)
        label_half_x2 = MathTex(
            r"\dfrac{x^2}{2}=\dfrac{y^2}{2}",
            color=cyan_hex
        ).next_to(square, DOWN)

        self.play(
            ReplacementTransform(label_y_eq_x, label_half_y2),
            ReplacementTransform(label_x_eq_y, label_half_x2),
            FadeIn(tri_ACD), FadeIn(tri_ABC), 
        )
        self.wait(2)

        # ---------- 6) Étiquette centrale xy ≤ 1/2(x²+y²) ----------
        label_ineq = MathTex(
            r"xy \leqslant \dfrac{x^2}{2}+\dfrac{y^2}{2}",
            color=WHITE
        ).scale(0.65).move_to(square.get_center())
        self.play(Write(label_ineq))
        self.wait()
        label_eq = MathTex(
                           r"xy = \dfrac{x^2}{2}+\dfrac{y^2}{2}",
                           color=navy
                           ).next_to(square, UP)
        self.play(
            ReplacementTransform(label_ineq, label_eq)
        )
        self.wait(2)
        
        # ---------- 7) Carré → rectangle horizontal (AEFD) ----------
        x_new = 2.5
        E, F = B + RIGHT * x_new, C + RIGHT * x_new
        rect_AEFD = Polygon(
            A, E, F, D,
            color=orange,
            fill_color=orange,
            fill_opacity=0.75
        )
        
        trap_AEFC = Polygon(
            A, E, F, C,
            color=cyan_hex,
            fill_color=cyan_hex,
            fill_opacity=0.75
        )

        x_sup_y = MathTex(r"x", color=cyan_hex)\
            .add(MathTex(r">", color=WHITE))\
            .add(MathTex(r"y", color=yellow))\
            .arrange(RIGHT)\
            .next_to(rect_AEFD, DOWN)
        
        y_inf_x = MathTex(r"y", color=yellow)\
            .add(MathTex(r"<", color=WHITE))\
            .add(MathTex(r"x", color=cyan_hex))\
            .arrange(RIGHT)\
            .next_to(rect_AEFD, LEFT)
        
        self.play(
            FadeOut(label_eq),
            ReplacementTransform(square, rect_AEFD),
            ReplacementTransform(
                label_half_x2,
                x_sup_y
            ),
            ReplacementTransform(
                label_half_y2,
                y_inf_x
            ),
            label_ineq.animate.next_to(rect_AEFD, UP)
        )
        self.wait(1.5)

        self.play(
            rect_AEFD.animate(fill_opacity=0.25),
            Create(trap_AEFC)
        )
        self.wait(1.5)
        
        # ---------- 9) Étiquette fractionnée ----------
        label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"=", color=WHITE))\
                      .add(MathTex(r"\dfrac{y^2}{2}", color=yellow))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Trapèze)}", color=cyan_hex))\
                      .arrange(RIGHT)\
                      .next_to(rect_AEFD, UP)
        self.play(ReplacementTransform(label_ineq, label_split))
        self.wait(1.5)
        
        # ---------- 10) Rectangle → grand carré AEGH vertical ----------
        G, H = F + UP * x_new, D + UP * x_new
        diag2 = Line(A, G, color=RED, stroke_width=5)
        big_square = Polygon(
            A, E, G, H,
            color=navy,
            fill_color=navy,
            fill_opacity=0.75
        )
        tri_AEG = Polygon(
            A, E, G,
            color=navy,
            fill_color=navy,
            fill_opacity=0.85
        )

        

        self.play(
            Create(diag2),
            ReplacementTransform(rect_AEFD, big_square),
            FadeIn(tri_AEG),
            label_split.animate.next_to(big_square, UP)
        )
        self.wait()
        
        # ---------- 11) Inégalité finale ----------
        final_label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"\leqslant", color=WHITE))\
                      .add(MathTex(r"\dfrac{x^2}{2}", color=navy))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\dfrac{y^2}{2}", color=yellow))\
                      .arrange(RIGHT)\
                      .next_to(big_square, UP)
        self.play(ReplacementTransform(label_split, final_label_split))
        self.wait(2)

        tri_ACD = Polygon(
            A, C, D,
            color=yellow,
            fill_color=yellow,
            fill_opacity=0.95
        )
        
        trap_AEFC = Polygon(
            A, E, F, C,
            color=cyan_hex,
            fill_color=cyan_hex,
            fill_opacity=0.95
        )

        trap_CGHD = Polygon(
            C, G, H, D,
            color=green,
            fill_color=green,
            fill_opacity=0.95
        )

        self.play(
            FadeIn(trap_AEFC), FadeIn(tri_ACD), FadeIn(trap_CGHD),
            ApplyWave(x_sup_y),
            ApplyWave(y_inf_x),
            Circumscribe(final_label_split)
        )
        self.wait(2)


        # ---------- Rotation 180° du triangle jaune ACD autour de C ----------
        # 1. Définir le triangle cible (CFG)
        Dp = C + RIGHT * side
        Ap = C + RIGHT * side + UP * side
        tri_CDpAp = Polygon(
            C, Dp, Ap,
            color=yellow,
            fill_color=yellow,
            fill_opacity=0.9
        )

        # 2. Rotation 180° autour de C
        self.play(
            Rotate(tri_ACD, angle=PI, about_point=C),
            run_time=1.5
        )
        self.wait(2)

        area_label = MathTex(
            r"\text{Triangle} + \text{Trapèze} \subseteq \text{Demi-carré}",
            color=WHITE
        ).to_corner(DL)
        
        self.play(
            Create(tri_CDpAp),
            Rotate(tri_ACD, angle=PI, about_point=C),
            Write(area_label),
            run_time=1.5,
        )
        self.wait(2)

        rect_AEFD = Polygon(
            A, E, F, D,
            color=orange,
            fill_color=orange,
            fill_opacity=0
        )

        rect_label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"=", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Triangle)}", color=yellow))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Trapèze)}", color=cyan_hex))\
                      .arrange(RIGHT)\
                      .next_to(big_square, UP)
        self.play(
            FadeOut(area_label),
            ReplacementTransform(final_label_split, rect_label_split),
            Create(rect_AEFD),
            Circumscribe(rect_label_split, color=orange)
        )
        self.wait(2)

        tri_AEG = Polygon(
            A, E, G,
            color=navy,
            fill_color=navy,
            fill_opacity=0
        )

        half_square_label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"=", color=WHITE))\
                      .add(MathTex(r"\dfrac{y^2}{2}", color=yellow))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Trapèze)}", color=cyan_hex))\
                      .add(MathTex(r"\leqslant", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Demi-carré)}", color=navy))\
                      .arrange(RIGHT)\
                      .next_to(big_square, UP)
        
        
        
        self.play(
            Create(tri_AEG),
            ReplacementTransform(rect_label_split, half_square_label_split),
            Circumscribe(half_square_label_split, color=navy),
        )
        self.wait(2)
        
        CA = A - C # vect CA
        self.play(
            tri_CDpAp.animate.shift(CA),
            run_time=1.5
        )
        self.wait(2)

        halves_squares_label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"\leqslant", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Demi-carré)}", color=navy))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\text{Aire(Demi-carré)}", color=yellow))\
                      .arrange(RIGHT)\
                      .next_to(big_square, UP)
        
        AC = C - A # vect AC
        self.play(
            tri_CDpAp.animate.shift(AC),
            ReplacementTransform(
                half_square_label_split,
                halves_squares_label_split
            ),
            Circumscribe(halves_squares_label_split, color=orange),
            run_time=1.5,
        )
        self.wait(2)

        final_label_split = MathTex(r"x", color=cyan_hex)\
                      .add(MathTex(r"y", color=yellow))\
                      .add(MathTex(r"\leqslant", color=WHITE))\
                      .add(MathTex(r"\dfrac{x^2}{2}", color=navy))\
                      .add(MathTex(r"+", color=WHITE))\
                      .add(MathTex(r"\dfrac{y^2}{2}", color=yellow))\
                      .arrange(RIGHT)\
                      .next_to(big_square, UP)
        
        self.play(
            ReplacementTransform(
                halves_squares_label_split,
                final_label_split),
            Circumscribe(final_label_split, color=green),
        )
        self.wait(2)

        self.camera.frame.animate.scale(0.6).move_to(final_label_split)
        self.wait(1.5)

        summary = MathTex(
            r"\boxed{xy \leq \frac{x^2}{2} + \frac{y^2}{2}}",
            font_size=48,
            color=WHITE
        ).to_edge(LEFT)
        self.play(Write(summary), Circumscribe(summary))
        self.wait()
        
