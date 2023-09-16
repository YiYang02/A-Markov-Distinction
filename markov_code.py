"""
Markov Kaleidoscope
Mission 3: A Markov Distinction
Yi Yang
14 Sept, 2023

Class to generate a kaleidoscope pattern using Markov Chains.
"""

import math
import random
from PIL import Image, ImageDraw

class Kaleidoscope:
    """
    Initializes the kaleidoscope settings and properties.
    """
    def __init__(self, width, height):
        
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND_COLOR = (255, 255, 255)

        # Color definitions and transitions
        self.COLORS = {
            "Violet": (148, 0, 211),
            "Indigo": (75, 0, 130),
            "Blue": (0, 0, 255),
            "Green": (0, 255, 0),
            "Yellow": (255, 255, 0),
            "Orange": (255, 127, 0),
            "Red": (255, 0, 0),
            "Brown": (139, 69, 19),
            "Pink": (255, 20, 147),
        }

        self.COLOR_TRANSITIONS = {
            "Violet": {"Violet": 0.2, "Indigo": 0.4, "Blue": 0.2, "Green": 0.1, "Red": 0.1},
            "Indigo": {"Violet": 0.3, "Indigo": 0.3, "Blue": 0.2, "Green": 0.1, "Yellow": 0.1},
            "Blue": {"Violet": 0.1, "Indigo": 0.3, "Blue": 0.3, "Green": 0.2, "Pink": 0.1},
            "Green": {"Blue": 0.3, "Green": 0.3, "Yellow": 0.2, "Orange": 0.2},
            "Yellow": {"Green": 0.3, "Yellow": 0.2, "Orange": 0.3, "Red": 0.2},
            "Orange": {"Yellow": 0.3, "Orange": 0.3, "Red": 0.2, "Brown": 0.2},
            "Red": {"Orange": 0.2, "Red": 0.4, "Pink": 0.2, "Violet": 0.2},
            "Brown": {"Red": 0.3, "Brown": 0.3, "Orange": 0.2, "Green": 0.2},
            "Pink": {"Red": 0.2, "Pink": 0.4, "Violet": 0.3, "Indigo": 0.1},
        }

        # Shape definitions and transitions
        self.SHAPE_ARC = 'arc'
        self.SHAPE_ELLIPSE = 'ellipse'
        self.SHAPE_TRANSITIONS = {
            'arc': {'arc': 0.2, 'ellipse': 0.8},
            'ellipse': {'arc': 0.8, 'ellipse': 0.2}
        }

        # Sides definitions and transitions
        self.SIDES = [10, 12, 15, 20, 25, 30]
        self.SIDES_TRANSITIONS = {
            10: {10: 0.1, 12: 0.3, 15: 0.3, 20: 0.2, 25: 0.1},
            12: {10: 0.1, 12: 0.3, 15: 0.3, 20: 0.2, 25: 0.1},
            15: {10: 0.2, 12: 0.2, 15: 0.2, 20: 0.2, 25: 0.1, 30: 0.1},
            20: {10: 0.1, 15: 0.2, 20: 0.3, 25: 0.2, 30: 0.2},
            25: {15: 0.1, 20: 0.3, 25: 0.3, 30: 0.3},
            30: {20: 0.1, 25: 0.4, 30: 0.5}
        }

    """"
    Return the next value based on the current value and its defined transitions.
    """
    def get_next(self, current_value, transition_dict):
        
        possibilities = list(transition_dict[current_value].keys())
        probabilities = list(transition_dict[current_value].values())
        return random.choices(possibilities, probabilities)[0]

    """
    Draws a segment of the kaleidoscope pattern based on the provided parameters.
    """
    def draw_kaleidoscope_pattern(self, draw, cx, cy, max_radius, current_sides, current_shape, current_color_name):
        next_sides = self.get_next(current_sides, self.SIDES_TRANSITIONS)
        
        # Draw arcs based on the given parameters
        if current_shape == self.SHAPE_ARC:
            angle = 2 * math.pi / next_sides
            for i in range(next_sides):
                radius = random.uniform(5, max_radius)
                start_angle = 0
                end_angle = 360
                next_color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
                x1, y1 = cx - radius, cy - radius
                x2, y2 = cx + radius, cy + radius
                draw.arc([x1, y1, x2, y2], math.degrees(start_angle), math.degrees(end_angle), fill=self.COLORS[current_color_name], width=random.randint(1, 5))
                start_angle, end_angle = start_angle + angle, end_angle + angle
        # Draw ellipses based on the given parameters
        elif current_shape == self.SHAPE_ELLIPSE:
            next_color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
            radius = random.uniform(5, max_radius)
            draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=self.COLORS[current_color_name], width=random.randint(1, 5))

        next_shape = self.get_next(current_shape, self.SHAPE_TRANSITIONS)

        # return the next states to draw for the kaleidoscope
        return next_sides, next_shape, next_color_name

    """
    Fills the center of the image with concentric circles.
    """
    def fill_center(self, draw, cx, cy, max_radius, current_color_name):
        # Create circles starting from the middle of the image and then ripple outwards
        for r in range(5, int(max_radius), 1):
            current_color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
            current_color = self.COLORS[current_color_name]
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=current_color, width=1)

    """
    Creates the kaleidoscope image and saves it to the given filename.
    """
    def create(self, filename, patterns):
        img = Image.new('RGB', (self.WIDTH, self.HEIGHT), self.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Center of the image
        cx, cy = self.WIDTH // 2, self.HEIGHT // 2

        # Initial values for color, shape, and sides. These values are random
        current_color_name = random.choice(list(self.COLORS.keys()))
        current_shape = random.choice([self.SHAPE_ARC, self.SHAPE_ELLIPSE])
        current_sides = random.choice(self.SIDES)

        # Fill the center with circles starting from small circles all the way to large circles
        self.fill_center(draw, cx, cy, self.WIDTH, current_color_name)
        # Create kaleidoscope patterns throughout the image such as ellipses and arcs
        for i in range(patterns):
            current_sides, current_shape, current_color_name = self.draw_kaleidoscope_pattern(
                draw, cx, cy, random.uniform(self.WIDTH/6, self.WIDTH), current_sides, current_shape, current_color_name)
            # Fuzzify the drawing so that it represents more of looking through a kaleidoscope
            img = img.rotate(random.choice([-10, 10]))

        # Save and display the image
        img.save(filename)
        img.show()

if __name__ == "__main__":
    kaleidoscope = Kaleidoscope(800, 800)
    kaleidoscope.create(filename="examples/kaleidoscope7.png", patterns=500)
