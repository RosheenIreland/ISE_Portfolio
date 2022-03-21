import random

Sentence_starter = ['How did I get here,' , 'A pure mad tale,' , 'Sure it went like this,']

character = [' said a gas lad.' , ' said yer one from down the road.' , ' said yer ma.' , 'said an ivisible man.']

time = [' On the night of satans birthday,' , ' One eventful morning,' , ' On a horrid night,']

story_plot = [' they were about to eat a poisoned egg,' , ' they almost won the lottery' , ' they spooned fed there nana']

place = [' on the magical toilet bowl.' , ' on the shitty mountains.' , ' on the garbage pile next door.']

second_chararcter = [' They gazed upon a goat' , ' They glared at Donald Trump,' , ' Bewildered, they saw a flirtatious ghost']

age = [' who was atleast 73,' , ' who had no disernable age,' , ' who looked older than the sea,']

work = [' holding up a giant gold encrusted kebab.' , ' sniffing a pair of old shoes.' , 'eating leftover turnips from last week.']

More = [' And as the story unfolds, so does the mayhem,' , 'And the further through this story we get the stranger you become,']

And_More = [ ' That is the tale of a goose and a pear' ' The rest is  horrible history']

print(random.choice(Sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(place)+random.choice(second_chararcter)+random.choice(age)+random.choice(work)+random.choice(More)+random.choice(And_More))

