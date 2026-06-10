import math

angle = int(input('Enter any angle: '))

sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print('The angle {}° has:'.format(angle))
print('Sine: {:.2f}'.format(sine))
print('Cosine: {:.2f}'.format(cosine))
print('Tangent: {:.2f}'.format(tangent))
