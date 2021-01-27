#a simple dictionary
alien_0 = {'colour': 'green' , 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

#working with dictionaries

#using get() to access values
phones = {'brand': 'LG', 'model': 'V60'}
varients = phones.get('model', 'thats not a model.')
print(varients)
varient = phones.get('SoC', 'no SoC information available')
print(varient)


