from manimlib.imports import *

"""
Author:         Elteoremadebeethoven
Date:           August 17/2019
Last update:    August 17/2019
OS:             Linux ArchLabs
Results:        ./
"""

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class GetIntersections:
    def get_coord_from_proportion(self,vmob,proportion):
        return vmob.point_from_proportion(proportion)

    def get_points_from_curve(self, vmob, dx=0.005):
        coords = []
        for point in Range(0, 1, dx):
            dot = Dot(self.get_coord_from_proportion(vmob,point))
            coords.append(dot.get_center())
        return coords

    def get_intersections_between_two_vmobs(self, vmob1, vmob2,
                                            tolerance=0.05,
                                            radius_error=0.2,
                                            use_average=True,
                                            use_first_vmob_reference=False):
        coords_1 = self.get_points_from_curve(vmob1)
        coords_2 = self.get_points_from_curve(vmob2)
        intersections = []
        for coord_1 in coords_1:
            for coord_2 in coords_2:
                distance_between_points = get_norm(coord_1 - coord_2)
                if use_average:
                    coord_3 = (coord_2 - coord_1) / 2
                    average_point = coord_1 + coord_3
                else:
                    if use_first_vmob_reference:
                        average_point = coord_1
                    else:
                        average_point = coord_2
                if len(intersections) > 0 and distance_between_points < tolerance:
                    last_intersection=intersections[-1]
                    distance_between_previus_point = get_norm(average_point - last_intersection)
                    if distance_between_previus_point > radius_error:
                        intersections.append(average_point)
                if len(intersections) == 0 and distance_between_points < tolerance:
                    intersections.append(average_point)
        return intersections


class IntersectionScene(Scene,GetIntersections):
    def construct(self):
        square=Square(color=BLUE).scale(2.7)
        circle=Circle(color=BLUE).scale(3)

        self.add(square,circle)
        intersections = self.get_intersections_between_two_vmobs(circle, square)

        for point in intersections:
            self.add(Dot(radius=0.05, color=YELLOW).move_to(point))