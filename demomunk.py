import pygame
import pymunk
import pymunk.pygame_util
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)

draw_options = pymunk.pygame_util.DrawOptions(screen)

# ground plane
ground = pymunk.Segment(space.static_body, (50, 550), (75110, 550), 5)
ground.friction = 1.0
space.add(ground)

# little diagonal thing
diag = pymunk.Segment(space.static_body, (350,550),(450, 450), 5)
diag.friction = 1.0
space.add(diag)

# lil protrusion
protbody = space.static_body
protbody.position = (400,500)
protsize = (50,100)
prot = pymunk.Poly.create_box(protbody, protsize)
prot.friction = 1.0
space.add(prot)

# being in the same group = no collision with members of same group
creature_group = 1
creature_no_self_collision = pymunk.ShapeFilter(group=creature_group)

mass = 2
size = (120,30)

body1 = pymunk.Body(mass, pymunk.moment_for_box(mass, size))
body1.position = (400, 300)
shape1 = pymunk.Poly.create_box(body1, size)
shape1.friction = 0.8
shape1.filter = creature_no_self_collision

space.add(body1, shape1)

body2 = pymunk.Body(mass, pymunk.moment_for_box(mass, size))
body2.position = body1.position + (120,0)
shape2 = pymunk.Poly.create_box(body2, size)
shape2.friction = 0.8
shape2.filter = creature_no_self_collision

space.add(body2, shape2)

hinge_position = body1.position + (60,0)

joint = pymunk.PivotJoint(body1, body2, hinge_position)
space.add(joint)

body1.angular_damping = 0.9
body2.angular_damping = 0.9

limit = pymunk.RotaryLimitJoint(body1, body2,
                                math.radians(-90),
                                math.radians(90))
space.add(limit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    keys = pygame.key.get_pressed()

    TORQUE = 150000

    if keys[pygame.K_LEFT]:
        body2.torque = -TORQUE
    elif keys[pygame.K_RIGHT]:
        body2.torque = TORQUE

    if keys[pygame.K_a]:
        body1.torque = -TORQUE
    elif keys[pygame.K_d]:
        body1.torque = TORQUE

    space.step(1/60)

    creature_x = (body1.position.x + body2.position.x) / 2

    offset_x = WIDTH / 2 - creature_x

    draw_options.transform = pymunk.Transform(tx=offset_x, ty=0)

    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
