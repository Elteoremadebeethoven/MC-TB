from manimlib.imports import *

"""
Author:         Elteoremadebeethoven
Date:           August 17/2019
Last update:    August 17/2019
OS:             Linux ArchLabs
Files:          Put keyboard/ in sounds directory (assets/sounds/)
Results:        https://imgur.com/sra73bD
"""

class KeyboardScene(Scene):
    CONFIG = {
        "lag": 0.1,
        "rate_factor": 0.05,
        "time_factor": 0.13,
        "lag_spaces": 0.2,
        "range_random": 3
    }
    def keyboard(self, text, position=ORIGIN, scale=1,**text_config):
        text = TextMobject(text, **text_config)[0]
        text.move_to(position)
        text.scale(scale)
        def return_random():
            return random.randint(1, self.range_random)
        for i in range(len(text)):
            self.add_sound("keyboard/key%s"%return_random())
            text[i].set_fill(None, 1)
            self.play(LaggedStartMap(FadeIn, 
                        text[i], run_time=self.rate_factor*len(text[i]),
                        lag_ratio=self.lag/len(text[i])))
            self.wait(0.3*return_random()*self.time_factor)
            if i < len(text) - 1:
                pre_ty = text[i].get_center()[1]
                pre_tx = text[i].get_center()[0]
                pos_ty = text[i+1].get_center()[1]
                pos_tx = text[i+1].get_center()[0]
                pre_width = text[i].get_width() / 2
                pos_width = text[i+1].get_width() / 2
                pre_height = text[i].get_height() / 2
                pos_height = text[i+1].get_height() / 2
                dist_min_x = (pre_width + pos_width) * 1.6
                dist_min_y = (pre_height + pos_height) * 1.2
                if i == 0 or dist_max_x < dist_min_x:
                    dist_max_x = dist_min_x
                if i == 0 or dist_max_y < dist_min_y:
                    dist_max_y = dist_min_y
                if abs(pre_ty - pos_ty) > dist_max_y:
                    self.add_sound("keyboard/enter")
                    self.wait(self.time_factor)
                elif abs(pre_tx - pos_tx) > dist_max_x and abs(pre_ty - pos_ty) < dist_max_y:
                    self.add_sound("keyboard/space")
                    self.wait(self.time_factor)
            if i == len(text) - 1:
                self.add_sound("keyboard/enter")
                self.wait(self.time_factor)

class KeyboardExample(KeyboardScene):
    def construct(self):
        self.keyboard(
            "\\tt <hello world!>",
            color=BLUE,
            position=UP*2,
            scale=3
            )
        self.wait()