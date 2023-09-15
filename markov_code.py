import math
import random
from PIL import Image, ImageDraw

class Kaleidoscope:
    """Class to create and manage the kaleidoscope image."""

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND_COLOR = (255, 255, 255)
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

        self.SHAPE_TRANSITIONS = {
            'arc': {'arc': 0.5, 'ellipse': 0.5},
            'ellipse': {'arc': 0.6, 'ellipse': 0.4}
        }

        self.SIDES = [5, 10, 15, 20, 25, 30]

        self.SIDES_TRANSITIONS = {
            5: {5: 0.1, 10: 0.3, 15: 0.3, 20: 0.2, 25: 0.1},
            10: {5: 0.1, 10: 0.3, 15: 0.3, 20: 0.2, 25: 0.1},
            15: {5: 0.2, 10: 0.2, 15: 0.2, 20: 0.2, 25: 0.1, 30: 0.1},
            20: {10: 0.1, 15: 0.2, 20: 0.3, 25: 0.2, 30: 0.2},
            25: {15: 0.1, 20: 0.3, 25: 0.3, 30: 0.3},
            30: {20: 0.1, 25: 0.4, 30: 0.5}
        }
        self.SHAPE_ARC = 'arc'
        self.SHAPE_ELLIPSE = 'ellipse'

    def get_next(self, current_value, transition_dict):
        possibilities = list(transition_dict[current_value].keys())
        probabilities = list(transition_dict[current_value].values())
        return random.choices(possibilities, probabilities)[0]

    def draw_kaleidoscope_pattern(self, draw, cx, cy, max_radius, current_sides, current_shape, current_color_name):
        """Draw a segment of the kaleidoscope pattern."""
        sides = self.get_next(current_sides, self.SIDES_TRANSITIONS)
        current_color = self.COLORS[current_color_name]
        
        if current_shape == self.SHAPE_ARC:
            angle = 2 * math.pi / sides
            for i in range(sides):
                radius = random.uniform(5, max_radius)
                start_angle = random.uniform(0, 2 * math.pi)
                end_angle = start_angle + random.uniform(angle/2, angle)
                color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
                color = self.COLORS[color_name]
                x1, y1 = cx - radius, cy - radius
                x2, y2 = cx + radius, cy + radius
                draw.arc([x1, y1, x2, y2], math.degrees(start_angle), math.degrees(end_angle), fill=color, width=random.randint(1, 5))
                start_angle, end_angle = start_angle + angle, end_angle + angle

        elif current_shape == self.SHAPE_ELLIPSE:
            color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
            color = self.COLORS[color_name]
            radius = random.uniform(5, max_radius)
            draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=color, width=random.randint(1, 5))

        return sides, current_shape, color_name

    def fill_center(self, draw, cx, cy, max_radius, current_color_name):
        """Fill the center with concentric circles."""
        for r in range(5, int(max_radius), 1):
            color_name = self.get_next(current_color_name, self.COLOR_TRANSITIONS)
            color = self.COLORS[color_name]
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color, width=1)

    def create(self, filename, patterns):
        """Create the kaleidoscope image and save to file."""
        img = Image.new('RGB', (self.WIDTH, self.HEIGHT), self.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        cx, cy = self.WIDTH // 2, self.HEIGHT // 2
        current_color_name = random.choice(list(self.COLORS.keys()))
        self.fill_center(draw, cx, cy, self.WIDTH, current_color_name)

        current_shape = random.choice([self.SHAPE_ARC, self.SHAPE_ELLIPSE])
        current_sides = random.choice(self.SIDES)

        for i in range(patterns):
            current_sides, current_shape, current_color_name = self.draw_kaleidoscope_pattern(
                draw, cx, cy, random.uniform(10, self.WIDTH/6), current_sides, current_shape, current_color_name)
            current_shape = self.get_next(current_shape, self.SHAPE_TRANSITIONS)
            img = img.rotate(random.uniform(-5, 5))

        img.save(filename)
        img.show()

if __name__ == "__main__":
    kaleidoscope = Kaleidoscope(800, 800)
    kaleidoscope.create(filename="kaleidoscope5.png", patterns=5000)
