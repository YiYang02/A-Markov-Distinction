# Markov Kaleidoscope
## Description
This code creates Kaleidoscope art using pre-defined Markov Chains to determine visual elements such as shape, color, and pattern transitions. For shapes, the program at any state can either draw an arc or an ellipse. There are many colors that the Kaleidoscope can pick from, ranging from Violet to Pink! For patterns, the number of sides ranges from 5 - 30. 
## How to Set Up and Run the Code:
1. Open the terminal
2. Install the Python PIL library
```
$ pip install Pillow
```
3. Download this project from Github
```
$ git clone https://github.com/YiYang02/A-Markov-Distinction.git
```
4. Change your directory to this project
5. Run the program!
```
$ python3 markov_code.py
```
## Reflection:
**Describe how the system is personally meaningful to you**
<br />
This system is personally meaningful to me because I've always wanted to create a computational art system without heavily leaning on the use of AI. In recent months, I've been fascinated by the leaps in advances within Generative AI Art and have been playing around with several AI image generation models such as Dall-E Mini, Stable Diffusion, and Midjourney. Moreover, when it came time for me to try and create my own AI image generation model, I felt very intimidated by all the machine learning techniques and jargon I had to learn. Given that Markov Chains is a  fairly simple probabilistic model that I've learned in AI previously, I'm really happy with my program! 

Besides my system being intellectually meaningful to me, my system also showcases my "creative" aspect in a new way. Traditional forms of creativity have always been in the form of art, something that I'm not particularly good at (I can only draw stick figures). However, I am good at coding! Through code, I've learned to be able to express my own take on Kaleidoscopes without having to pick up a colored pencil!
<br />

**Explain how working on it genuinely challenged you as a computer scientist**
<br />
Working on this system genuinely challenged me as a computer scientist in many aspects. For example, I had to take an open-ended technical problem and find an appropriate "solution" that used Markov Chains and could produce unique "creative" art outputs. What does it mean for a system to be "creative"? These were the first questions asked in the first week of class and something that I still struggle to understand given that all creative outputs must be computationally generated in this class. Thus, I looked for something that was both artistic but also had enough patterns/structure to the art form so that I could mathematically represent it. Consequently, I stumbled upon the art form of cubism and later kaleidoscopes. Once I had my art form down, I had to mathematically represent it and understand how to use Markov Chain transitions to guide my program to create a proper kaleidoscope. Thus, I had to research several math formulas within the Pillow library so that I could draw circles, arcs, and ellipses for my kaleidoscope. This involved deep diving into the Pillow library documentation, something that I normally don't do for a computer science class. Lastly, I had to play around with the Markov Chain state transition probabilities, so that the probabilities best represent something similar to how you would normally create a kaleidoscope. I pushed myself outside of my comfort zone by not only tackling the project prompt but also going above and beyond by continuing to tweak my "formula" for representing kaleidoscope shapes, colors, and patterns via trial and error. It was certainly not easy.

This was an important challenge for me because it taught me the importance of perseverance. Much like real-world industry projects, you are normally given a final outlook of what the product should look like. This brings much ambiguity and puts a lot of responsibility on the developer to ideate and deliver an appropriate solution. I think this project has sufficiently taught me and prepared me for how to work as a developer at a company! 

My next steps going forward are to introduce more shapes that the kaleidoscope system can use to create. Moreover, I hope to talk to kaleidoscope experts and get their opinions about my system's art pieces!
<br />

**Include a discussion of whether you believe your system is creative**
<br />
Based on the class’s definition of creativity... I believe my system fulfills the novel requirement of creativity as each time it is able to create a new kaleidoscope output with different colors, shapes, and sides. However, it lacks the inherent intentionality that many attribute to genuine creativity. For example, my system represents a static representation of my creative understanding of kaleidoscopes. At this point in writing, my basic understanding of kaleidoscope and how I choose to represent it via code/mathematical structure and Markov Chains has translated to my system. However, through time my understanding of what a kaleidoscope is and how to construct one will certainly change. But my system will not change. I feel my system is creative to a certain extent, but not genuinely creative in the sense that it will grow with my creative understanding of kaleidoscopes.

<br />

**Sources**
<br />
- https://www.datacamp.com/tutorial/markov-chains-python-tutorial
- https://docs.python.org/3/library/random.html
- https://pillow.readthedocs.io/en/stable/
- https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
- https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/
