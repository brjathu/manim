from manimlib.imports import *
import numpy as np
import sys
import os.path
import cv2



# ITAML. An incremental task aganostic meta learing approch

# Generalization is a key factor for contialal learing
# however, meta leariing algorithms do not fit well into an incremyal learing setting
# they struglle with out of order distibutions
# and support set is required for fine tuning at the end
# the data dirstibution is skwed due to  examplar replay.
# Additionally, the state of the art incremenal learnibg algorthms, lacks generaligaization.





# INPUT_PATH=. OUTPUT_PATH=. docker-compose run manim slides.py Slide_1 -pl
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
print(sys.path)
from nn.network import *
from nn.part1 import *



def add_title(self):
    title = TextMobject("\\small \\textbf{iTAML : An Incremental Task-Agnostic Meta-learning}")
    title.to_corner(UL)
    self.add(title)


class Slide_0(Scene):
    def construct(self):
        title = TextMobject("\\huge \\textbf{iTAML}")
        title2 = TextMobject("\\small \\textbf{iTAML : An Incremental Task-Agnostic Meta-learning}")

        self.play(Write(title) , run_time=1)
        # self.wait(1)
        self.play(Transform(title, title2), run_time=1)
        self.wait(0.5)

        self.play(ApplyMethod(title.to_corner, UL, run_time=1))
        self.wait(0.5)


        text = TextMobject("\\small Jathushan Rajasegaran$^1$ \\ \\ \\ \\ \\ Salman Khan$^1$ \\ \\ \\ \\ \\ Munawar Hayat$^1$")
        text2 = TextMobject("\\small Fahad Shahbaz Khan$^{1,2}$ \\ \\ \\ \\ \\ Mubarak Shah$^3$")
        # text.to_corner(LEFT)
        text2.shift(DOWN)
        self.play(FadeIn(text) , run_time=1)
        # self.wait(0.5)
        self.play(FadeIn(text2) , run_time=1)
        self.wait(0.5)




        text = TextMobject("\\tiny $^1$Inception Institute of Artificial Intelligence \\ \\ $^2$CVL, Linköping University")
        text.shift(DOWN*3)

        text2 = TextMobject("\\tiny $^3$University of Central Florida")
        text2.shift(DOWN*3.5)

        # text.to_corner(LEFT)
        self.play(FadeIn(text) , run_time=1)
        self.play(FadeIn(text2) , run_time=1)
        self.wait(2)


class Slide_1(Scene):
    def construct(self):

        add_title(self)
        self.wait(1)


        text = TextMobject("\\small $\\bullet$ Generalization is a key for continual learning algorithms.")
        text.to_corner(LEFT)
        text.shift(UP)
        self.play(Write(text) , run_time=1)
        self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ Meta-learning achieve generalization by", "`learning to learn'",".")
        text2.to_corner(LEFT)
        # text2.shift(UP)
        self.play(Write(text2) , run_time=1)
        self.wait(1)

        # text2[1].set_color(GREEN)
        self.play(FadeToColor(text2[1], GREEN), run_time=0.5)
        self.wait(0.5)

        temp1 = []
        self.play(FadeOut(text), run_time=0)
        self.play(FadeOut(text2[0]), run_time=0)
        self.play(FadeOut(text2[2]), run_time=0)
        self.play(ApplyMethod(text2[1].move_to, [0,0,0]), run_time=0.2)
        self.play(ApplyMethod(text2[1].scale, 2), run_time=0.2)
        # self.play(ApplyMethod(text2[1].scale, 2, run_time=1))
        self.wait(1)


class Slide_2(Scene):
    def construct(self):

        add_title(self)
        self.wait(1)


        text = TextMobject("\\small $\\bullet$ ","\\small Model Agnostic Meta Learning")
        text.to_corner(LEFT)
        text.shift(2*UP)
        self.play(Write(text) , run_time=1)
        self.wait(2)


        text2 = TextMobject("\\footnotesize $\\bullet$ A popular tool for meta-learning.")
        text2.to_corner(LEFT)
        text2.shift(UP+0.5*RIGHT)
        self.play(Write(text2) , run_time=1)
        self.wait(2)

        text3 = TextMobject("\\footnotesize $\\bullet$ Gradient based approch to find better initialization.")
        text3.to_corner(LEFT)
        text3.shift(0.5*RIGHT)
        self.play(Write(text3) , run_time=1)
        self.wait(2)


        text4 = text[1].copy()
        text5 = TextMobject("\\small MAML")
        text5.to_corner(LEFT)
        text5.shift(2*DOWN+1.5*RIGHT)
        self.play(ApplyMethod(text4.shift, 4*DOWN, run_time=1))
        self.play(Transform(text4, text5), run_time=1)


        text6 = TextMobject("\\small gradient")
        text6.next_to(text5, RIGHT, buff=.5)
        text7 = TexMobject("=", "\\nabla_{\\theta} \\sum \\mathcal{L}_{\\theta_i}(\\mathcal{D}_{i}^{val})")
        text7.next_to(text6, RIGHT, buff=.5)
        self.play(Write(text6), run_time=1)
        self.play(Write(text7), run_time=1)

        self.wait(3)

        self.play(FadeOut(text), run_time=0.01)
        self.play(FadeOut(text2), run_time=0.01)
        self.play(FadeOut(text3), run_time=0.01)
        self.play(FadeOut(text4), run_time=0.01)
        self.play(FadeOut(text5), run_time=0.01)
        self.play(FadeOut(text6), run_time=0.01)
        self.play(FadeOut(text7[0]), run_time=0.01)
        self.play(ApplyMethod(text7[1].move_to, [0,2,0], run_time=1))
        # self.play(ApplyMethod(text7[1].shift, UP, run_time=1))

        self.wait(1)




class Slide_3(Scene):
    def construct(self):

        add_title(self)


        eq = TexMobject("\\nabla","_{\\theta}","\\sum \\mathcal{L}","_{\\theta_i}","(\\mathcal{D}_{i}^{val})")
        eq.shift([0,2,0])
        self.add(eq)

        self.wait(3)

        # dot = Dot()
        # line = Line((0,0,0), (3,0,0))
        # self.play(ShowCreation(dot))
        # self.play(Transform(dot, line))
        # self.dither()


        x = -4
        y = -1
        g = 0.3
        theta = Dot([x, y, 0], radius=0.1, color=BLUE)
        text1 = TextMobject("$\\theta$")
        text1.shift([x-g, y+g, 0])
        self.play(ShowCreation(theta))
        self.add(text1)

        framebox1 = SurroundingRectangle(eq[1], buff = .1)
        framebox2 = SurroundingRectangle(text1, buff = .1)
        self.play(ShowCreation(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(1)
        self.play(FadeOut(framebox1, run_time=0))
        self.play(FadeOut(framebox2, run_time=0))


        theta11 = Dot([-2, 0, 0], radius=0.1, color=RED)
        arrow11 = Arrow(theta.get_bottom(),theta11.get_bottom(),buff=0.1)
        arrow11.set_color(ORANGE)
        arrow11b = Arrow(theta11.get_center(),theta.get_center(),buff=0.1)
        arrow11b.set_color(GREEN)
        self.play(GrowArrow(arrow11))
        self.play(ShowCreation(theta11))


        theta12 = Dot([-0.5, -0.5, 0], radius=0.1, color=RED)
        arrow12 = Arrow(theta11.get_bottom(),theta12.get_bottom(),buff=0.1)
        arrow12.set_color(ORANGE)
        arrow12b = Arrow(theta12.get_center(),theta11.get_center(),buff=0.1)
        arrow12b.set_color(GREEN)
        self.play(GrowArrow(arrow12))
        self.play(ShowCreation(theta12))


        theta13 = Dot([2, 1, 0], radius=0.1, color=RED)
        text1 = TextMobject("$\\theta_{i}$")
        text1.shift([2+g, 1+g, 0])
        arrow13 = Arrow(theta12.get_bottom(),theta13.get_bottom(),buff=0.1)
        arrow13.set_color(ORANGE)
        arrow13b = Arrow(theta13.get_center(),theta12.get_center(),buff=0.1)
        arrow13b.set_color(GREEN)
        self.play(GrowArrow(arrow13))
        self.play(ShowCreation(theta13))
        self.add(text1)


        framebox1 = SurroundingRectangle(eq[3], buff = .1)
        framebox2 = SurroundingRectangle(text1, buff = .1)
        self.play(ShowCreation(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(1)
        self.play(FadeOut(framebox1, run_time=0))
        self.play(FadeOut(framebox2, run_time=0))
        





        theta21 = Dot([-2.5, -2, 0], radius=0.1, color=RED)
        arrow21 = Arrow(theta.get_bottom(),theta21.get_bottom(),buff=0.1)
        arrow21.set_color(ORANGE)
        arrow21b = Arrow(theta21.get_center(),theta.get_center(),buff=0.1)
        arrow21b.set_color(GREEN)
        self.play(GrowArrow(arrow21))
        self.play(ShowCreation(theta21))


        theta22 = Dot([-1, -2, 0], radius=0.1, color=RED)
        arrow22 = Arrow(theta21.get_bottom(),theta22.get_bottom(),buff=0.1)
        arrow22.set_color(ORANGE)
        arrow22b = Arrow(theta22.get_center(),theta21.get_center(),buff=0.1)
        arrow22b.set_color(GREEN)
        self.play(GrowArrow(arrow22))
        self.play(ShowCreation(theta22))


        theta23 = Dot([3, -2.5, 0], radius=0.1, color=RED)
        text2 = TextMobject("$\\theta_{i+1}$")
        text2.shift([3+g, -2.5+g, 0])
        arrow23 = Arrow(theta22.get_bottom(),theta23.get_bottom(),buff=0.1)
        arrow23.set_color(ORANGE)
        arrow23b = Arrow(theta23.get_center(),theta22.get_center(),buff=0.1)
        arrow23b.set_color(GREEN)
        self.play(GrowArrow(arrow23))
        self.play(ShowCreation(theta23))
        self.add(text2)



        self.play(GrowArrow(arrow13b))
        self.play(GrowArrow(arrow12b))
        self.play(GrowArrow(arrow11b))

        self.play(GrowArrow(arrow23b))
        self.play(GrowArrow(arrow22b))
        self.play(GrowArrow(arrow21b))


        self.play(FadeOut(arrow13, run_time=0))
        self.play(FadeOut(arrow12, run_time=0))
        self.play(FadeOut(arrow11, run_time=0))

        self.play(FadeOut(arrow23, run_time=0))
        self.play(FadeOut(arrow22, run_time=0))
        self.play(FadeOut(arrow21, run_time=0))


        # self.play(FadeOut(arrow13b, run_time=0))
        # self.play(FadeOut(arrow12b, run_time=0))
        # self.play(FadeOut(arrow11b, run_time=0))

        # self.play(FadeOut(arrow23b, run_time=0))
        # self.play(FadeOut(arrow22b, run_time=0))
        # self.play(FadeOut(arrow21b, run_time=0))


        self.wait(3)


        theta_new = Dot([-1, -1, 0], radius=0.1, color=YELLOW)
        text_new = TextMobject("$\\theta_{new}$")
        text_new.shift([-1+g, -1+g, 0])

        text_meta = TextMobject("\\tiny Meta update")
        text_meta.shift([-2.5, -1+g/2, 0])

        arrow_meta = Arrow(theta.get_bottom(),theta_new.get_bottom(),buff=0.1)
        arrow_meta.set_color(GREEN)
        self.play(GrowArrow(arrow_meta))
        self.play(ShowCreation(theta_new))
        self.add(text_new)
        self.play(Write(text_meta))


        self.wait(3)



class Slide_4(Scene):
    def construct(self):

        add_title(self)
        self.wait(1)

        start_x = -6
        start_y = 2
        tab = 1

        text1 = TextMobject("\\small $\\bullet$ However, MAML requires $2^{nd}$ order gradients.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(2)

        text2 = TextMobject("\\small $\\bullet$ ", "Reptile", ", which is a first-order approximation of MAML.")
        text2.move_to([start_x, start_y-1, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(2)


        text3 = text2[1].copy()
        self.play(ApplyMethod(text3.move_to, [start_x+2, start_y-3, 0]))
        self.wait(2)

        text4 = TextMobject("\\small gradient")
        text4.next_to(text3, RIGHT, buff=.2)
        text5 = TexMobject(" = ", "\\sum {{\\theta_i-\\theta}\\over \\alpha}")
        text5.next_to(text4, RIGHT, buff=.5)
        self.play(Write(text4), run_time=1)
        self.play(Write(text5), run_time=1)

        self.wait(3)

        self.play(FadeOut(text1), run_time=0.01)
        self.play(FadeOut(text2), run_time=0.01)
        self.play(FadeOut(text3), run_time=0.01)
        self.play(FadeOut(text4), run_time=0.01)
        self.play(FadeOut(text5[0]), run_time=0.01)
        self.play(ApplyMethod(text5[1].move_to, [0,2,0], run_time=1))

        
class Slide_5(Scene):
    def construct(self):
        add_title(self)
        
        eq = TexMobject("\\sum ", "{", "{\\theta_i", "-", "\\theta}" , "\\over \\alpha}")
        eq.move_to([0,2,0])
        self.add(eq)
        self.wait(2)




        start_x = -6
        start_y = 2
        tab = 1



        x = -4
        y = -1
        g = 0.3
        theta = Dot([x, y, 0], radius=0.1, color=BLUE)
        text1 = TextMobject("$\\theta$")
        text1.shift([x-g, y+g, 0])
        self.play(ShowCreation(theta))
        self.add(text1)

        framebox1 = SurroundingRectangle(eq[4], buff = .1)
        framebox2 = SurroundingRectangle(text1, buff = .1)
        self.play(ShowCreation(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(1)
        self.play(FadeOut(framebox1, run_time=0))
        self.play(FadeOut(framebox2, run_time=0))


        theta11 = Dot([-2, 0, 0], radius=0.1, color=RED)
        arrow11 = Arrow(theta.get_center(),theta11.get_center(),buff=0.1)
        arrow11.set_color(ORANGE)
        self.play(GrowArrow(arrow11))
        self.play(ShowCreation(theta11))


        theta12 = Dot([-0.5, -0.5, 0], radius=0.1, color=RED)
        arrow12 = Arrow(theta11.get_center(),theta12.get_center(),buff=0.1)
        arrow12.set_color(ORANGE)
        self.play(GrowArrow(arrow12))
        self.play(ShowCreation(theta12))


        theta13 = Dot([2, 1, 0], radius=0.1, color=RED)
        text1 = TextMobject("$\\theta_{i}$")
        text1.shift([2+g, 1+g, 0])
        arrow13 = Arrow(theta12.get_center(),theta13.get_center(),buff=0.1)
        arrow13.set_color(ORANGE)
        self.play(GrowArrow(arrow13))
        self.play(ShowCreation(theta13))
        self.add(text1)


        framebox1 = SurroundingRectangle(eq[2], buff = .1)
        framebox2 = SurroundingRectangle(text1, buff = .1)
        self.play(ShowCreation(framebox1))
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait(1)
        self.play(FadeOut(framebox1, run_time=0))
        self.play(FadeOut(framebox2, run_time=0))
        





        theta21 = Dot([-2.5, -2, 0], radius=0.1, color=RED)
        arrow21 = Arrow(theta.get_center(),theta21.get_center(),buff=0.1)
        arrow21.set_color(ORANGE)
        self.play(GrowArrow(arrow21))
        self.play(ShowCreation(theta21))


        theta22 = Dot([-1, -2, 0], radius=0.1, color=RED)
        arrow22 = Arrow(theta21.get_center(),theta22.get_center(),buff=0.1)
        arrow22.set_color(ORANGE)
        self.play(GrowArrow(arrow22))
        self.play(ShowCreation(theta22))



        theta23 = Dot([3, -2.5, 0], radius=0.1, color=RED)
        text2 = TextMobject("$\\theta_{i+1}$")
        text2.shift([3+g, -2.5+g, 0])
        arrow23 = Arrow(theta22.get_center(),theta23.get_center(),buff=0.1)
        arrow23.set_color(ORANGE)
        self.play(GrowArrow(arrow23))
        self.play(ShowCreation(theta23))
        self.add(text2)


        arrow1b = Arrow(theta.get_center(),theta13.get_center(),buff=0.1)
        arrow1b.set_color(GREEN)
        arrow2b = Arrow(theta.get_center(),theta23.get_center(),buff=0.1)
        arrow2b.set_color(GREEN)
        self.play(GrowArrow(arrow1b))
        self.play(GrowArrow(arrow2b))
        

        self.play(FadeOut(theta11, run_time=0))
        self.play(FadeOut(theta12, run_time=0))
        self.play(FadeOut(theta21, run_time=0))
        self.play(FadeOut(theta22, run_time=0))


        self.play(FadeOut(arrow13, run_time=0))
        self.play(FadeOut(arrow12, run_time=0))
        self.play(FadeOut(arrow11, run_time=0))

        self.play(FadeOut(arrow23, run_time=0))
        self.play(FadeOut(arrow22, run_time=0))
        self.play(FadeOut(arrow21, run_time=0))


        # self.play(FadeOut(arrow13b, run_time=0))
        # self.play(FadeOut(arrow12b, run_time=0))
        # self.play(FadeOut(arrow11b, run_time=0))

        # self.play(FadeOut(arrow23b, run_time=0))
        # self.play(FadeOut(arrow22b, run_time=0))
        # self.play(FadeOut(arrow21b, run_time=0))


        self.wait(3)


        theta_new = Dot([-0.75, -0.875, 0], radius=0.1, color=BLUE)
        text_new = TextMobject("$\\theta_{new}$")
        text_new.shift([-0.75+g, -0.875+g, 0])

        text_meta = TextMobject("\\tiny Meta update")
        text_meta.shift([-2.3, -1+g/1.4, 0])
        text_meta.rotate(3*np.pi/180)

        arrow_meta = Arrow(theta.get_center(),theta_new.get_center(),buff=0.1)
        arrow_meta.set_color(GREEN)
        self.play(GrowArrow(arrow_meta))
        self.play(ShowCreation(theta_new))
        self.add(text_new)
        self.play(Write(text_meta))


        self.wait(3)



class Slide_6(Scene):
    def construct(self):
        add_title(self)
        self.wait(1)


        start_x = -6
        start_y = 2.4
        tab = 1

        text1 = TextMobject("\\small $\\bullet$ Generalization is a key factor for continual learning.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(3)

        # text1 = TextMobject("\\small $\\bullet$ Meta learning algorithms learns a better generalization.")
        # text1.move_to([start_x, start_y-1, 0], UL)
        # self.play(Write(text1) , run_time=1)
        # self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ ", "Meta learning algorithms don't fit on incremental setting.")
        text2.move_to([start_x, start_y-1, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)

        text2 = TextMobject("\\small $\\bullet$ ", "Out of Order Distribution (OOD).")
        text2.move_to([start_x+tab, start_y-2, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)

        text2 = TextMobject("\\small $\\bullet$ ", "Fine-tuning on support set is required at the end.")
        text2.move_to([start_x+tab, start_y-3, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)

        text2 = TextMobject("\\small $\\bullet$ ", "Skewed data distribution with memory.")
        text2.move_to([start_x+tab, start_y-4, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)


        text2 = TextMobject("\\small $\\bullet$ ", "Additionally, STOA incremental learning algorithms", "lack generalization.")
        text2.move_to([start_x, start_y-5, 0], UL)
        text2[-1].move_to([start_x+0.4, start_y-5.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(5)



class Slide_7(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6
        start_y = 2
        tab = 1

        text1 = TextMobject("\\small $\\bullet$ iTAML tries to bridge the gap between meta learning and","incremental learning.")
        text1.move_to([start_x, start_y, 0], UL)
        text1[-1].move_to([start_x+0.4, start_y-0.6, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(4)
        start_y -= 0.6



        text2 = TextMobject("\\small $\\bullet$ ", "Disentangle the network into a generic feature extractor", "and task specific ","classification weights.")
        text2.move_to([start_x+tab, start_y-1, 0], UL)
        text2[-2].move_to([start_x+tab+2, start_y-1.6, 0])
        text2[-1].move_to([start_x+tab+6, start_y-1.6, 0])
        self.play(Write(text2) , run_time=1)
        self.wait(5)


        start_y -= 0.6
        text2 = TextMobject("\\small $\\bullet$ ", "Task agnostic prediction, with two stage classification.")
        text2.move_to([start_x+tab, start_y-2, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)

        text2 = TextMobject("\\small $\\bullet$ ", "A momentum based meta update to avoid forgetting.")
        text2.move_to([start_x+tab, start_y-3, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(3)

        text2 = TextMobject("\\small $\\bullet$ ", "A sampling rate selection approach for data continuum.")
        text2.move_to([start_x+tab, start_y-4, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(5)




class Slide_8(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6
        start_y = 2.4
        tab = 1


        text1 = TextMobject("\\small $\\bullet$ Meta training of iTAML.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(1)


        svg = ImageMobject("./meta_train.png")
        svg.scale(2.5)
        svg.shift(DOWN)
        self.add(svg)

        self.wait(2)

class Slide_8_1(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6
        start_y = 2.4
        tab = 1


        text1 = TextMobject("\\small $\\bullet$ Meta training of iTAML.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ ", "Each mini batch is further broken into task specific","micro batches.")
        text2.move_to([start_x+tab, start_y-1, 0], UL)
        text2[-1].move_to([start_x+tab+0.4, start_y-1.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)
        start_y -= 0.6

        text2 = TextMobject("\\small $\\bullet$ ", "In the inner loop, task specific models are trained $\\Phi_{i}$.")
        text2.move_to([start_x+tab, start_y-2, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ ","In the outer loop a momentum controller","combines these task specific weights.")
        text2.move_to([start_x+tab, start_y-3, 0], UL)
        text2[2].move_to([start_x+tab+0.4, start_y-3.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)
        # start_y -= 0.6

        




class Slide_9(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6
        start_y = 2.4
        tab = 1

        text1 = TextMobject("\\small $\\bullet$ Inference of iTAML.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(1)


        svg = ImageMobject("./meta_test.png")
        svg.scale(2.5)
        svg.shift(DOWN)
        self.add(svg)

        self.wait(2)


class Slide_9_1(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6.5
        start_y = 2.6
        tab = 1


        text1 = TextMobject("\\small $\\bullet$ Inference of iTAML.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ ", "At inference, iTAML uses a two stage prediction.")
        text2.move_to([start_x+tab, start_y-1, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)

        text2 = TextMobject("\\small $\\bullet$ ", "First, given a data continuum $\\mathcal{C}(i,p)$ it will predict", "the task using average predictions.")
        text2.move_to([start_x+tab, start_y-2, 0], UL)
        text2[2].move_to([start_x+tab+0.4, start_y-2.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)
        start_y -= 0.6


        text2 = TextMobject("\\small $\\bullet$ ","Then, it uses exemplar data to adapt for the task","using a gradient update.")
        text2.move_to([start_x+tab, start_y-3, 0], UL)
        text2[2].move_to([start_x+tab+0.4, start_y-3.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)
        start_y -= 0.6

        text2 = TextMobject("\\small $\\bullet$ ","Finally, it will pass the continuum again and give", "class wise predictions.")
        text2.move_to([start_x+tab, start_y-4, 0], UL)
        text2[2].move_to([start_x+tab+0.4, start_y-4.6, 0], UL)
        self.play(Write(text2) , run_time=1)
        self.wait(1)



class Slide_10(Scene):
    def construct(self):
        add_title(self)
        
        start_x = -6
        start_y = 2.4
        tab = 1

        text1 = TextMobject("\\small $\\bullet$ Few experimental results.")
        text1.move_to([start_x, start_y, 0], UL)
        self.play(Write(text1) , run_time=1)
        self.wait(1)


        svg = ImageMobject("./results1.png")
        svg.scale(2.2)
        svg.shift(DOWN)
        self.add(svg)

        self.wait(3)



class ShowNet(Scene):
    CONFIG = {
        "layer_sizes" : [12, 8, 8, 8, 6],
        "network_mob_config" : {},
    }
    def setup(self):
        self.add_network()

    def add_network(self):
        self.network = Network(sizes = self.layer_sizes)
        self.network_mob = NetworkMobject(
            self.network,
            **self.network_mob_config
        )
        self.add(self.network_mob)


    def construct(self):

        self.add(self.network_mob.add_neurons)