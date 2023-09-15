import math
import random
from PIL import Image, ImageDraw

class Kaleidoscope:
    """Class to create and manage the kaleidoscope image."""

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.COLORS = [
            (148, 0, 211), (75, 0, 130), (0, 0, 255),
            (0, 255, 0), (255, 255, 0), (255, 127, 0),
            (255, 0, 0), (139, 69, 19), (255, 20, 147),
            (255, 105, 180), (176, 224, 230), (70, 130, 180),
            (240, 230, 140), (152, 251, 152), (0, 255, 127),
            (255, 99, 71), (0, 206, 209), (100, 149, 237),
            (138, 43, 226), (127, 255, 212), (218, 165, 32),
            (222, 184, 135), (95, 158, 160), (85, 107, 47)
        ]

    def draw_kaleidoscope_pattern(self, draw, cx, cy, max_radius, sides):
        """Draw a segment of the kaleidoscope pattern.
        
        Args:
        - draw: The ImageDraw.Draw instance.
        - cx, cy: Coordinates for the center of the pattern.
        - max_radius: The maximum radius for the patterns.
        - sides: Number of sides for the kaleidoscope pattern.
        """
        angle = 2 * math.pi / sides
        for i in range(sides):
            # Randomly decide pattern parameters
            radius = random.uniform(5, max_radius)
            start_angle = random.uniform(0, 2 * math.pi)
            end_angle = start_angle + random.uniform(angle/2, angle)
            color = random.choice(self.COLORS)

            # Define the arc boundary
            x1, y1 = cx - radius, cy - radius
            x2, y2 = cx + radius, cy + radius

            # Draw the arc segment
            draw.arc([x1, y1, x2, y2], math.degrees(start_angle), math.degrees(end_angle), fill=color, width=random.randint(1, 5))

            # Prepare for the next segment
            start_angle, end_angle = start_angle + angle, end_angle + angle

    def fill_center(self, draw, cx, cy, max_radius):
        """Fill the center with concentric circles.

        Args:
        - draw: The ImageDraw.Draw instance.
        - cx, cy: Center coordinates of the image.
        - max_radius: Maximum radius for the center pattern.
        """
        for r in range(5, int(max_radius), 1):
            color = random.choice(self.COLORS)
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color, width=1)

    def create(self, filename, patterns):
        """Create the kaleidoscope image and save to file."""
        img = Image.new('RGB', (self.WIDTH, self.HEIGHT), self.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Define the center
        cx, cy = self.WIDTH // 2, self.HEIGHT // 2

        # Fill the central area
        self.fill_center(draw, cx, cy, self.WIDTH)

        # Add multiple kaleidoscope patterns
        for i in range(patterns):  # default is 50 patterns
            self.draw_kaleidoscope_pattern(draw, cx, cy, random.uniform(10, self.WIDTH/6), sides=random.choice([5, 10, 15, 20]))
            img = img.rotate(random.uniform(-5, 5))  # Add some rotation for diversity

        img.save(filename)
        img.show()

if __name__ == "__main__":
    # Create an instance of the Kaleidoscope and generate the image
    kaleidoscope = Kaleidoscope(800, 800)
    kaleidoscope.create(filename="kaleidoscope4.png", patterns=50)