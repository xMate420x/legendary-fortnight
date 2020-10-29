import random;

def rng(sentencenum):
    prefixes = ["refactored","reimagined","stunning","sturdy","solid","cuddly","literate","animated","silver","psychic","congenital","crispy","special","legendary","expert","friendly","shiny","curly","bug-free","didactic","cautious","laughing","redesigned","fictional","improved","glowing","bookish","probable","upgraded"]
    suffixes = ["pancake","guide","succotash","lamp","happiness","computing-machine","carnival","umbrella","system","waddle","potato","palm-tree","parakeet","guacamole","eureka","fortnight","chainsaw","garbanzo","winner","goggles","memory","carnival","pancake","robot","doodle","funicular","giggle","fiesta","disco","waffle","bassoon","couscous","broccoli","succotash"]
    infixes = ["octo"]

    if(sentencenum == 3): print(random.choice(prefixes)+"-"+random.choice(infixes)+"-"+random.choice(suffixes))
    else: print(random.choice(prefixes)+"-"+random.choice(suffixes))

if(random.randint(0, 10) == 10): rng(3);
else: rng(2);
