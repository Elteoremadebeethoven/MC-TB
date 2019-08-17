from manimlib.imports import *

"""
Author:         Elteoremadebeethoven
Date:           August 17/2019
Last update:    August 17/2019
Contact*:       
OS:             Linux ArchLabs
Files*:         
Results:        https://imgur.com/WOBQ7o9
"""

t_offset = 0

class OrbitAnimation(Scene):
    def construct(self):
        orbit = Ellipse(color=GREEN).scale(2.5)
        planet = Dot()
        text = TextMobject("Orbit animation")
        planet.move_to(orbit.point_from_proportion(0))

        def update_planet(mob, dt):
            global t_offset
            rate = dt * 0.2
            mob.move_to(orbit.point_from_proportion(((t_offset + rate))%1))
            t_offset += rate

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        self.wait(3)
        self.play(Write(text))
        self.wait(3)